code_latex = r"""\documentclass{article}
    
\usepackage{tkz-tab}

\begin{document}
DONNER LES VARIATIONS DE f(x)\\

$f(x)=- x^{5} - x^{4} + x^{3} + x^{2}$\\
$f'(x)= - 5 x^{4} - 4 x^{3} + 3 x^{2} + 2 x$\\

    

\begin{tikzpicture}

   \tkzTabInit[espcl=2]{$x$ / 1 , $f'(x)$ / 1, variation de $f(x)$/1.5}
   {$+\infty$, $-1$,$-0.54$,$0$,$0.74$,$-\infty$}

   \tkzTabLine{,-,z,+,z,-,z,+,z,-,+\infty}
   \tkzTabVar{+/$+\infty$,-/$0$,+/$0.1$,-/$0$,+/$0.43$,-/$-\infty$}



\end{tikzpicture}


\end{document}"""
import sympy as sp
import tkinter as tk
from sympy import *
from tkinter import *
import random as rd
from tabulate import tabulate

# VARIABLES
couleur_bg = "#F0B27A"
font_frame = "Arial 12 bold"
font_cnv= "Times 14 bold"

# GRANDE FENETRE
nom = Tk()
nom.title('Générateur de afficher_tableau de variation')
nom.config(bg=couleur_bg)

# PREMIERE BOITE
frame = Frame(nom, bg=couleur_bg)

# DEUXIEME BOITE
cnv = Canvas(frame, width=1150, height=660, background=couleur_bg)
cnv.pack()

# INPUT
cnv.create_text(140, 70, text="Entrez une fonction :", font=font_frame)
cnv.create_text(538, 45, text="Borne 1", font=font_frame)
cnv.create_text(668, 45, text="Borne 2", font=font_frame)

default_function = "x**2-x**3"
default_borne1 = "-100"
default_borne2 = "100"
fonction_var = StringVar()
borne1_var = StringVar()
borne2_var = StringVar()
fonction_var.set(default_function)
borne1_var.set(default_borne1)
borne2_var.set(default_borne2)
entree_fonction = Entry(frame, width=20, font="Arial 12", bg="#F0B27A",text = fonction_var)
borne_1 = Entry(frame, width=8, font="Arial 12", bg="#F0B27A",text= borne1_var)
borne_2 = Entry(frame, width=8, font="Arial 12", bg="#F0B27A",text = borne2_var)

entree_fonction.place(x=225, y=60)
borne_1.place(x=500, y=60)
borne_2.place(x=630, y=60)
cnv1 = Canvas(cnv, width=900, height=400, background=couleur_bg)

def afficher_tableau():
    cnv1.place(x=100, y=130)
    cnv1.create_line(0, 60, 1000, 60, width=2, fill='black')
    cnv1.create_line(100, 0, 100, 300, width=2, fill='black')
    cnv1.create_line(0, 120, 1000, 120, width=2, fill='black')
    cnv1.update()
    cnv1.create_text(50, 35, text="x", font="Times 25 bold")
    cnv1.create_text(50, 90, text="f '(x)", font="Times 25 bold")
    cnv1.create_text(50, 180, text="f (x)", font="Times 25 bold")
    bbox = cnv1.bbox("all")
    cnv1.config(width=bbox[2] - bbox[0], height=bbox[3] - bbox[1])

def afficher_resultat():
    global Liste_fx  # Assurez-vous que Liste_fx soit global
    Liste_fx = []
    
    # def sp(expr):  
    #     expr1 = sympify(expr)
    #     expr2 = float(expr1)
    #     expr3 = '{:.2f}'.format(expr2)
    #     return expr3
    def arrondir(expr):
        expr_arrondie = '{:.2f}'.format(expr)
        
    #INTERVALLES
    cnv1.delete("derivative")
    borne_1_val, borne_2_val = borne_1.get(), borne_2.get()
    borne_1_val, borne_2_val = sympify(borne_1_val), sympify(borne_2_val) 
    if borne_2_val < borne_1_val:
        borne_1_val, borne_2_val = borne_2_val, borne_1_val
    borne_1_val = float(borne_1_val)
    borne_2_val = float(borne_2_val)
    cnv1.create_text(130, 35, text=borne_1_val, font= font_cnv, tags='derivative')
    cnv1.create_text(950, 35, text=borne_2_val, font=font_cnv, tags='derivative')
    
    #DERIVEE
    fonction = entree_fonction.get()  # Récupère la fonction depuis le champ de saisie
    x = symbols('x')
    f = sympify(fonction)
    f_prime = diff(f,x)
    f_prime_0 = solve(f_prime, x)
    f_prime_0 = sorted(f_prime_0)
    #f_prime_0 = [solution for solution in f_prime_0 if borne_1_val <= solution <= borne_2_val]

    
    # PRINT DERIVEE EN 0
    nb_solutions = len(f_prime_0)
    a = 1075  # Largeur totale 
    distance_entre_valeur = a / (nb_solutions + 1)  # Calcul de la distance entre les valeurs
    
    

    for i , solution in enumerate(f_prime_0):
        position = (i + 1) * distance_entre_valeur  # Calcul de la position horizontale
        solution = solution.evalf()
        position_y = 30
        solution_arrondie = '{:.2f}'.format(solution) #arrondie apres 3chiffres apres virgule 
        cnv1.create_text(position, position_y, text=solution_arrondie, font=font_cnv , tags= 'derivative')
        cnv1.create_text(position, position_y+60, text='0', font=font_cnv, tags = 'derivative')

        # LES SIGNES
        if i == 0:
            x_valeur = rd.uniform(borne_1_val, solution)
        else:
            x_valeur = rd.uniform(f_prime_0[i - 1], solution)
        if i == len(f_prime_0) - 1:
            x_value1 = rd.uniform(f_prime_0[i], borne_2_val)
            signe_1 = f_prime.subs(x, x_value1)
            if signe_1 > 0:
                signe = '+'
            else:
                signe = '-'  
            cnv1.create_text(position + 40, 90, text=signe, tags='derivative')
        signe_1 = f_prime.subs(x, x_valeur)
        if signe_1 > 0:
            signe = '+'
        else:
            signe = '-'        
        cnv1.create_text(position - 40, 90, text=signe, tags='derivative')


        #F(x)
        
        fx_borne_1 = f.subs(x, borne_1_val)
        fx_borne_2 = f.subs(x, borne_2_val)
        fx_borne_1 = arrondir(fx_borne_1)
        fx_borne_2 = arrondir(fx_borne_2)
        cnv1.create_text(130, position_y+110, text=fx_borne_1, font=font_cnv)
        cnv1.create_text(950, position_y+110, text=fx_borne_2, font=font_cnv)
        fx = f.subs(x, solution)
        fx = arrondir(fx)
        # if i == 0 :       
        #     if fx > fx_borne_1:
        #         cnv1.create_text(position, position_y+110, text=fx, font=font_cnv)
        #     else:
        #         cnv1.create_text(position, position_y+250, text=fx, font=font_cnv)
        # Liste_fx.append(fx)
        # print(Liste_fx)

        # if i>0:
        #     if fx > Liste_fx[i-1]:
        #         cnv1.create_text(position, position_y+110, text=fx, font=font_cnv)
        #     else:
    # ... (votre code pour la dérivée et le tableau de variation)


    # ... (le reste de votre code pour la dérivée et le tableau de variation)

    # Écrivez le tableau LaTeX avec les valeurs de x dans un fichier
    x_values =[borne_1_val]+f_prime_0+[borne_2_val]
    x_values_latex = ['$'+latex(x)+'$' for x in x_values]
    signes = []  # Créez une liste pour stocker les signes

    variations_fx = []

   
    for i, x_value in enumerate(x_values):
        if i == 0:
            signe = ''
            x_valeur = borne_1_val
        else:
            x_valeur = f_prime_0[i - 1]
            
        if i == len(x_values) - 1:
            x_value1 = borne_2_val
            signe_1 = f_prime.subs(x, x_value1)
            if signe_1 > 0:
                signe = '+'
            else:
                signe = '-'
        else:
            signe_1 = f_prime.subs(x, x_valeur)
            if signe_1 > 0:
                signe = '+'
            else:
                signe = '-'
        signes.append(signe)

        if i == 0:
            fx = f.subs(x, borne1_var.get())
        else:
            fx = f.subs(x, x_value)
        variations_fx.append('$'+str(fx)+'$')


    with open(r'C:\Users\Louis\Desktop\tableau variation\tableau_latex.tex', 'w') as file:
        file.write(r"""\documentclass{article}
\usepackage{tkz-tab}
\usepackage{amsmath} 
\begin{document}
DONNER LES VARIATIONS DE $f(x)$\\
$f(x)=""" + fonction + r"""$\\
$f'(x)=""" + latex(f_prime) + r"""$\\

\begin{tikzpicture}
\tkzTabInit{$x$ / 1 , $f'(x)$ / 1, variation de $f(x)$/1.5}
{""" +','.join(x_values_latex) + r"""$}
\tkzTabLine{""" ",".join(signes)+r"""}
\tkzTabVar{""" + ",".join(variations_fx) + r"""}
\end{tikzpicture}
\end{document}""")
    print (variations_fx)
    print(signe)

def tout_afficher():
    afficher_resultat()

    
bouton = Button(frame, text="Générer",font = "Times 11 bold", command=tout_afficher)
bouton.place(x=800, y=58)
frame.pack()
afficher_tableau()
nom.mainloop()
