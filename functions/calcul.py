import sympy as sp
from sympy import *
import random as rd

fonction = 'ln(x)'


# print(rd.randint(-oo,0))

def afficher_borne(borne_1, borne_2):
    valeur_borne_1 = sympify(borne_1)
    valeur_borne_2 = sympify(borne_2)
    return valeur_borne_1,valeur_borne_2

valeur_borne_1, valeur_borne_2 = afficher_borne(0,+oo) 


def calculer_derivee(valeur_borne_1,valeur_borne_2,entree_fonction_initiale):
    fonction_initiale = sympify(entree_fonction_initiale)
    x = symbols('x')
    derivee = diff(fonction_initiale,x)
    valeur_derivee_en_0 = solve(derivee, x)
    valeur_derivee_en_0 = sorted([val for val in valeur_derivee_en_0 if  val.is_real and valeur_borne_1<val<valeur_borne_2])
    valeur_de_x = [valeur_borne_1] + valeur_derivee_en_0 + [valeur_borne_2]
    if len(valeur_derivee_en_0) == 0:
        valeur_derivee_en_0 = [valeur_borne_1]
        valeur_de_x =  [valeur_borne_1] + [valeur_borne_2]   
    return valeur_derivee_en_0 , derivee , x , fonction_initiale , valeur_de_x


calculer_derivee(valeur_borne_1, valeur_borne_2,fonction )
valeur_derivee_en_0, derivee, x , fonction_initiale  , valeur_de_x = calculer_derivee(valeur_borne_1, valeur_borne_2, fonction)
print (valeur_derivee_en_0)

# def discontinuité(entree_fonction_initiale):
#     discontinuité = sp.singularities(fonction_initiale, x)
#     print(discontinuité)
#     return discontinuité
# print(discontinuité(fonction))

def afficher_signes(derivee, x, valeur_de_x):
    signes = []
    for solution in range(len(valeur_de_x) - 1):
        if valeur_de_x[solution] == -oo:
            valeur_de_x_aleatoire = valeur_de_x[solution + 1] - 1
        elif valeur_de_x[solution + 1] == +oo:
            valeur_de_x_aleatoire = valeur_de_x[solution] + 1
        else:
            valeur_de_x_aleatoire = rd.uniform(valeur_de_x[solution], valeur_de_x[solution + 1])
        signe_1 = derivee.subs(x, valeur_de_x_aleatoire)
        if signe_1 > 0:
            signe = '+'
        elif signe_1 < 0:
            signe = '-'
        else:
            signe = '0'
        signes.append(signe)
    return signes

signes = afficher_signes(derivee,x,valeur_de_x)
print(signes)


def variations_de_fx(valeur_borne_1, valeur_borne_2,valeur_de_x):

    variations_fx = []
    
    for solution in valeur_de_x:
        fx = fonction_initiale.subs(x, solution)
        variations_fx.append(latex(fx))

    image_de_borne_1 = fonction_initiale.subs(x, valeur_borne_1)
    image_de_borne_2 = fonction_initiale.subs(x, valeur_borne_2)
    # variations_fonction_initiale = [image_de_borne_1] + variations_fx + [image_de_borne_2]
    image_de_la_derniere_valeur = fonction_initiale.subs(x, valeur_de_x[-2])

    for i in range(len(signes)-1):
        if signes[i]=='+' and signes[i+1]=='+':
            del(variations_fx[i+1])
            del(signes[i])
            del(valeur_de_x[i+1])

    return variations_fx, image_de_borne_1, image_de_borne_2, image_de_la_derniere_valeur

variations_fx, image_de_borne_1, image_de_borne_2, image_de_la_derniere_valeur = variations_de_fx(valeur_borne_1, valeur_borne_2,valeur_de_x)
print(variations_fx)


def afficher_variation_latex( image_de_borne_2 , image_de_la_derniere_valeur,signes):
    valeurs_de_x_latex = ['$' + latex(x) + '$' for x in valeur_de_x]
    variations_fonction_latex = []
    # if len(signes)==1:
    #     image_de_la_derniere_valeur = image_de_borne_1
    # if image_de_la_derniere_valeur < image_de_borne_2:
    #     derniere_variation_latex = '+/$'+latex(image_de_borne_2)+'$'
    # else:
    #     derniere_variation_latex = '-/$'+latex(image_de_borne_2)+'$'   

    for element in range(len(variations_fx)) :
        if element == len(variations_fx)-1:
            if variations_fx [element] >= variations_fx[element-1]:
                derniere_variation_latex = '+/$'+latex(image_de_borne_2)+'$'
            else:
                derniere_variation_latex = '-/$'+latex(image_de_borne_2)+'$'
            break

        if variations_fx[element] <= variations_fx[element+1]:
            variations_fonction_latex.append('-/$'+str(variations_fx[element])+'$,')
        else:
            print (valeur_de_x[element])
            variations_fonction_latex.append('+/$'+str(variations_fx[element])+'$,')      
    

    return variations_fonction_latex, derniere_variation_latex, valeurs_de_x_latex

variations_fonction_latex, derniere_variation_latex ,valeurs_de_x_latex = afficher_variation_latex(image_de_borne_2  , image_de_la_derniere_valeur,signes)
print(variations_fonction_latex, derniere_variation_latex)



def afficher_latex(fonction_initiale , derivee , valeurs_de_x_latex , signes , variations_fonction_latex , derniere_variation_latex):
    with open(r'C:\Users\Louis\Desktop\tableau variation\functions\tableau_variation.tex', 'w+') as file:
        file.write(r"""\documentclass{article}
\usepackage{tkz-tab}
\usepackage{amsmath} 
\usepackage{geometry}
\usepackage{indentfirst}
\setlength{\parindent}{0cm} % Retrait du paragraphe
\geometry{
    left=1cm }
\begin{document}
\underline{Tableau de variation de $f(x)$}\\
                   
$f(x)=""" + latex(fonction_initiale) + r"""$\\
$f'(x)=""" + latex(derivee) + r"""$\\

\begin{tikzpicture}
\tkzTabInit[espcl=3]{$x$ / 1 , $f'(x)$ / 1, $f(x)$/2.5}
{""" + ','.join(valeurs_de_x_latex) + r"""}
\tkzTabLine{""" ','+ ",z,".join(signes) + r"""}
\tkzTabVar{""" + "".join(variations_fonction_latex) + derniere_variation_latex  + r"""}

\end{tikzpicture}
\end{document}""") 

afficher_latex(fonction_initiale , derivee , valeurs_de_x_latex , signes , variations_fonction_latex , derniere_variation_latex)
