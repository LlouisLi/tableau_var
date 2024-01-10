"""
signvartable.py

Sign and variation Tables for latex

GNU Public License
http://www.gnu.org/licenses/
By Christopher Goyet; goyet.christopher@gmail.com

signvartable is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
It is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along.  If not, see <http://www.gnu.org/licenses/>.

Original version by Goyet Christopher

16 Avril 2020 - First working version

"""

from sympy import *
#from sympy.solvers.solveset import _solve_trig2

def get_fct_variable(fct):
    variables = fct.atoms(Symbol)
    if len(variables) > 1:
        raise Exception("One variable function only !")
    else:
        return variables.pop()

def _get_x_values(fct, departSet, continuous_domain=None):
    if departSet.is_empty:
        raise Exception("Set of departure empty !")
    if departSet.is_FiniteSet:
        raise Exception("Finite set of departure !")
    x = get_fct_variable(fct)
    if continuous_domain is None:
        D_f = calculus.util.continuous_domain(fct, x, departSet)
    else:
        D_f = continuous_domain.intersection(departSet)
    racines = solveset(fct, x, domain=departSet)
    #racines = _solve_trig2(fct, x, departSet)
    x_values = D_f.boundary
    x_values = x_values.union({D_f.inf, D_f.sup})
    x_values = x_values.union(racines)
    if not x_values.is_FiniteSet :
        raise Exception("Not finite set of x values : to much interesting values in this domain.")
    x_list = sorted(list(x_values))
    x_latex =",".join([latex(e, mode='inline', fold_short_frac=False) for e in x_list])
    x_latex = "{"+x_latex+"}"
    return x_list, x_latex

def _convert_sign_tab(fct, init_f, x, x_val, d_f, between):
    if x_val == -oo or x_val == oo:
        return ""
    if not d_f.contains(x_val):
        if between:
            return "h"
        return "d"
    ima = fct.subs(x, x_val)
    if ima == 0 :
        return "z"
    if not between:
        if init_f.subs(x, x_val) == 0:
            return "t"
        else:
            return ""
    if ima > 0 :
        return "+"
    if ima < 0 :
        return "-"
    raise Exception("Forgotten case ??? in convert_sign_tab")
    return ""

def _sign_tab(fct, x_list, departSet, fname=None, continuous_domain=None):
    x = get_fct_variable(fct)
    #first column :
    tkzTabInit_latex = "\\tkzTabInit{"+latex(x, mode='inline', fold_short_frac=False)+" / 1 "
    #Tableau de signes :
    tkzTabLines_latex = []
    if fct.func.is_Mul:
        sign_exprs = list(fct.args)
        sign_exprs.append(fct)
    else:
        sign_exprs = [fct]
    for fact in sign_exprs:
        if continuous_domain is None:
            d_fact = calculus.util.continuous_domain(fact, x, departSet)
        else:
            d_fact = continuous_domain.intersection(departSet)
        new_tkzTabLine = "\\tkzTabLine{"
        tkzTabInit_latex += ", "
        if fact == fct and fname :
            tkzTabInit_latex += "$"+fname+"("+latex(x)+")$"
        else:
            tkzTabInit_latex += latex(fact, mode='inline', fold_short_frac=False)
        tkzTabInit_latex += " / 1 "
        prev_val = x_list[0]
        for i, val in enumerate(x_list):
            if i: #not first
                new_tkzTabLine += ", "
                if prev_val ==-oo and val != oo:
                    inter_val = val-1
                elif prev_val ==-oo and val == oo:
                    inter_val = 0
                elif prev_val !=-oo and val == oo:
                    inter_val = prev_val+1
                else:
                    inter_val = (prev_val+val)/2 #mid
                new_tkzTabLine += _convert_sign_tab(fact, fct, x, inter_val, d_fact, True)
                new_tkzTabLine += ", "
            new_tkzTabLine += _convert_sign_tab(fact, fct, x, val, d_fact, False)
            prev_val = val
        new_tkzTabLine += "}"
        tkzTabLines_latex.append(new_tkzTabLine)
    return tkzTabInit_latex, tkzTabLines_latex


def _get_var_levels(fct, x, x_list, D_f):
    levels = []
    values = []
    groups = []
    cur_level = []
    niveau = 0
    for i in range(len(x_list)):
        if i==0:
            #print("First element")
            x1 = x_list[i]
            x2 = x_list[i+1] # necessarily exists
            if x1 != -oo and x2 != oo and not D_f.contains((x1+x2)/2):
                # x1 isolated -> H
                groups.append("H")
                levels.append([0])
                values.append(fct.subs(x, x1))
            else:
                cur_level.append(0)
                values.append(limit(fct, x, x1, '+'))
                groups.append("")
        elif i+1 == len(x_list):
            # print("Last element")
            x1 = x_list[i]
            if len(cur_level) == 0:
                # x1 isolated
                groups.append("")
                values.append(fct.subs(x, x1))
                cur_level.append(0)
            else:
                x0 = x_list[i-1] # necessarily exists
                f0r = limit(fct, x, x0, '+')
                f1l = limit(fct, x, x1, '-')
                if f0r<f1l:
                    niveau += 1
                if f0r>f1l:
                    niveau -= 1
                cur_level.append(niveau)
                if x1 != oo and not D_f.contains(x1):
                    groups.append("-D")
                    values.append(fct.subs(x, x1))
                else:
                    groups.append("")
                    values.append(f1l)
            # The End
            levels.append(cur_level)
        else:
            # In this order x0 < x1 < x2,
            # all exist because x1 neither the first nor the last
            x0 = x_list[i-1]
            x1 = x_list[i]
            x2 = x_list[i+1]
            f0r = limit(fct, x, x0, '+')
            f1l = limit(fct, x, x1, '-')
            f1r = limit(fct, x, x1, '+')
            if len(cur_level)==0:
                if x2!=oo and not D_f.contains((x1+x2)/2):
                    # not defined before and not after
                    # ---> x1 isolated
                    groups.append("H")
                    values.append(fct.subs(x, x1))
                    levels.append([0])
                else:
                    # not defined before but defined after
                    if D_f.contains(x1):
                        f1 = fct.subs(x, x1)
                        if f1 == f1r: # continuous
                            groups.append("")
                        else:
                            # discontinuous
                            groups.append("CD")
                            values.append(fct.subs(x, x1))
                            cur_level.append(niveau)
                    else:
                        # limits ?
                        groups.append("D-") #D- ou D+
                    cur_level.append(niveau)
                    values.append(f1r)


            else:
                # well defined before
                if f0r<f1l:
                    niveau += 1
                if f0r>f1l:
                    niveau -= 1
                cur_level.append(niveau)
                if x2!=oo and not D_f.contains((x1+x2)/2):
                    # defined before and not after
                    levels.append(cur_level)
                    cur_level = []
                    niveau = 0
                    if D_f.contains(x1):
                        f1 = fct.subs(x, x1)
                        if f1 == f1l: # continuous
                            groups.append("H")
                            values.append(f1)
                        else: # discontinuous
                            groups.append("CD")
                            values.append(f1l)
                            values.append(fct.subs(x, x1))
                    else:
                        #limits ?
                        groups.append("DH")
                        values.append(f1l)
                else:
                    # well defined before AND after
                    if f1r != f1l:
                        # valeur interdite
                        groups.append("-D-")
                        values.append(f1l)
                        values.append(f1r)
                        levels.append(cur_level)
                        niveau = 0
                        cur_level = [niveau]
                    else:
                        if D_f.contains(x1):
                            f1 = fct.subs(x, x1)
                            if f1 == f1r and f1 == f1l:
                                # continuous
                                groups.append("")
                                values.append(f1)
                            else:
                                # discontinuous
                                groups.append("-D-")
                                values.append(f1l)
                                values.append(f1r)
                                # can we disp f1 ???
                                levels.append(cur_level)
                                niveau = 0
                                cur_level = [niveau]
                        else:
                            #prolongement par continuité
                            groups.append("C")
                            values.append(f1l)

    for i, l in enumerate(levels):
        if min(l)<0:
            levels[i] = list(map(lambda x : x + 1, l))
        # placer en haut ou en bas les images isolées ?
        # if len(l) == 1:
        #     l[0] = 1
    return levels, values, groups


def _var_tab(fct, x_list, departSet, fname=None, continuous_domain=None):
    x = get_fct_variable(fct)
    tkzTabVar_latex = "\\tkzTabVar{"
    tkzTabInit_latex = ", $"
    if fname:
        tkzTabInit_latex += fname+"("+latex(x)+")"
    else:
        tkzTabInit_latex += latex(fct)
    tkzTabInit_latex += "$ /2"
    if continuous_domain is None:
        D_f = calculus.util.continuous_domain(fct, x, departSet)
    else:
        D_f = continuous_domain.intersection(departSet)
    levels, values, groups = _get_var_levels(fct, x, x_list, D_f)
    levels = [y for x in levels for y in x]
    j = 0 # index for levels
    for i, symb in enumerate(groups):
        if i:
            tkzTabVar_latex += ", "
        pos1 = levels[j]
        val1 = values[j]
        j += 1
        # only D- with sign after
        if symb == "D-":
            tkzTabVar_latex += "D"
            symb = ""
        # set position
        tkzTabVar_latex += "+" if pos1 else "-"
        # then letter
        if symb == "-D-":
            tkzTabVar_latex += "D"
        else:
            tkzTabVar_latex += symb
        # if 2 signs
        if symb in ["-D-", "CD", "DC"]:
            pos2 = levels[j]
            val2 = values[j]
            j += 1
            tkzTabVar_latex += "+" if pos2 else "-"
        tkzTabVar_latex += "/ "
        tkzTabVar_latex += latex(val1, mode='inline', fold_short_frac=False)
        # if 2 values
        if symb in ["-D-", "CD", "DC"]:
            tkzTabVar_latex += " / "
            tkzTabVar_latex += latex(val2, mode='inline', fold_short_frac=False)
    tkzTabVar_latex += "}"
    tkzTabVar_latex.replace("$\\infty$", "$+\\infty$")
    return tkzTabVar_latex, tkzTabInit_latex

def tab_sign(fct, departSet, fname="f", continuous_domain=None):
    x = get_fct_variable(fct)
    x_list, x_latex = _get_x_values(fct, departSet, continuous_domain=continuous_domain)
    tkzTabInit_latex, tkzTabLines_latex = _sign_tab(fct, x_list, departSet, fname=fname, continuous_domain=continuous_domain)
    tab = "\\begin{tikzpicture}"
    tab += tkzTabInit_latex+"}"
    tab += x_latex
    for line in tkzTabLines_latex:
        tab += line
    tab += "\\end{tikzpicture}"
    return tab

def tab_var(fct, departSet, fname="f", continuous_domain=None, derivability_domain=None):
    x = get_fct_variable(fct)
    fp = fct.diff()
    x_list, x_latex = _get_x_values(fp, departSet, continuous_domain=derivability_domain)
    tkzTabVar_latex, tkzTabInit_var = _var_tab(fct, x_list, departSet, fname=fname, continuous_domain=continuous_domain)
    tab = "\\begin{tikzpicture}"
    tab += "\\tkzTabInit{$"+latex(x)+"$ / 1 "
    tab += tkzTabInit_var+"}"
    tab += x_latex
    tab += tkzTabVar_latex
    tab += "\\end{tikzpicture}"
    return tab

def tabs_all(fct, departSet, fname="f", continuous_domain=None, derivability_domain=None):
    fp = fct.diff()
    x_list, x_latex = _get_x_values(fp, departSet, continuous_domain=derivability_domain)
    tkzTabInit_latex, tkzTabLines_latex = _sign_tab(fp, x_list, departSet, fname=fname+"\'", continuous_domain=derivability_domain)
    tkzTabVar_latex, tkzTabInit_var = _var_tab(fct, x_list, departSet, fname=fname, continuous_domain=continuous_domain)
    tab = "\\begin{tikzpicture}"
    tab += tkzTabInit_latex+tkzTabInit_var+"}"
    tab += x_latex
    for line in tkzTabLines_latex:
        tab += line
    tab += tkzTabVar_latex
    tab += "\\end{tikzpicture}"
    return tab

x = symbols('x')
f = -cos(5*x)
tabs_all(f, Interval(-pi/5, pi/5))
with open(r'C:\Users\Louis\Desktop\tableau variation\tableau.tex', 'w+') as file:
    file.write()