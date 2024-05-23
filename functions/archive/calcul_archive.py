import sympy as sp
import tkinter as tk
from sympy import *
from tkinter import *
import random as rd
fonction = '(3*x+4)/x**2'

def afficher_borne(borne_1, borne_2):
    valeur_borne_1, valeur_borne_2 = borne_1, borne_2
    valeur_borne_1, valeur_borne_2 = sympify(valeur_borne_1), sympify(valeur_borne_2)
    
    return valeur_borne_1,valeur_borne_2

valeur_borne_1, valeur_borne_2 = afficher_borne(-10, 10 )
print(valeur_borne_1, valeur_borne_2)



def calculer_derivee(valeur_borne_1,valeur_borne_2,entree_fonction_initiale):
    fonction_initiale = sympify(entree_fonction_initiale)
    x = symbols('x')
    fonction_initiale = sympify(fonction_initiale)
    derivee = diff(fonction_initiale,x)
    valeur_derivee_en_0 = solve(derivee, x)
    valeur_derivee_en_0 = [val for val in valeur_derivee_en_0 if not val.is_imaginary]
    valeur_derivee_en_0 = sorted(valeur_derivee_en_0)
    valeur_de_x = [valeur_borne_1] + valeur_derivee_en_0 + [valeur_borne_2]
    print (valeur_derivee_en_0)
    if len(valeur_derivee_en_0) == 0:
        valeur_derivee_en_0 = [valeur_borne_1]
        valeur_de_x =  [valeur_borne_1] + [valeur_borne_2]   
    valeurs_de_x_latex = ['$' + latex(x) + '$' for x in valeur_de_x]

    return valeur_derivee_en_0 , derivee , x , fonction_initiale, valeurs_de_x_latex , valeur_de_x

calculer_derivee(valeur_borne_1, valeur_borne_2,fonction )
valeur_derivee_en_0, derivee, x , fonction_initiale , valeurs_de_x_latex , valeur_de_x = calculer_derivee(valeur_borne_1, valeur_borne_2, fonction)



def afficher_signes(valeur_derivee_en_0,valeur_borne_1,valeur_borne_2,derivee,x,valeur_de_x):
    signes = []
    for element, solution in enumerate(valeur_derivee_en_0):
        # LES SIGNES
        if len(valeur_de_x)>2:
            if element== 0:
                valeur_de_x_aleatoire = rd.uniform(valeur_de_x[0], solution)
                signe_1 = derivee.subs(x, valeur_de_x_aleatoire)
                print(valeur_de_x)
            else:
                valeur_de_x_aleatoire = rd.uniform(valeur_derivee_en_0[element- 1], solution)
                signe_1 = derivee.subs(x, valeur_de_x_aleatoire)
            if signe_1 > 0:
                signe = '+'
            else:
                signe = '-'       
            signes.append(str(signe))
            if element == len(valeur_derivee_en_0) - 1:
                valeur_de_x_aleatoire = rd.uniform(valeur_derivee_en_0[element], valeur_borne_2)
                signe_1 = derivee.subs(x, valeur_de_x_aleatoire)
                if signe_1 > 0:
                    signe = '+'
                else:
                    signe = '-'
                signes.append(str(signe))
        else : 
            valeur_de_x_aleatoire = rd.uniform(valeur_derivee_en_0[element], valeur_borne_2)
            signe_1 = derivee.subs(x, valeur_de_x_aleatoire)
            if signe_1 > 0:
                signe = '+'
            else:
                signe = '-'
            signes.append(str(signe))
    return signes

signes = afficher_signes(valeur_derivee_en_0,valeur_borne_1,valeur_borne_2,derivee,x,valeur_de_x)
print(signes)



def stocker_valeur(valeur_borne_1, valeur_borne_2):
    variations_fx = []
    for solution in valeur_derivee_en_0:
        fx = fonction_initiale.subs(x, solution)
        variations_fx.append(latex(fx))
    image_de_borne_1 = fonction_initiale.subs(x, valeur_borne_1)
    image_de_borne_2 = fonction_initiale.subs(x, valeur_borne_2)
    variations_fonction_initiale = [image_de_borne_1] + variations_fx + [image_de_borne_2]
    image_de_la_derniere_valeur = fonction_initiale.subs(x, valeur_de_x[-1])
    return variations_fx, image_de_borne_1, image_de_borne_2, variations_fonction_initiale, image_de_la_derniere_valeur

variations_fx, image_de_borne_1, image_de_borne_2, variations_fonction_initiale, image_de_la_derniere_valeur = stocker_valeur(valeur_borne_1, valeur_borne_2)
print(variations_fonction_initiale)



def afficher_variation( image_de_borne_2 ,variations_fonction_initiale , image_de_la_derniere_valeur):
    variations_fonction_latex = []
    if not len(signes)==0:
            if image_de_la_derniere_valeur >image_de_borne_2:
                derniere_variation_latex = '-/$'+str(image_de_borne_2)+'$'
            else:
                derniere_variation_latex = '+/$'+str(image_de_borne_2)+'$'   
            for element in range(len(signes)):
                if signes[element]== '+':
                    variations_fonction_latex.append('-/$'+str(variations_fonction_initiale[element])+'$,')
                else:
                    variations_fonction_latex.append('+/$'+str(variations_fonction_initiale[element])+'$,')
    return variations_fonction_latex, derniere_variation_latex

variations_fonction_latex, derniere_variation_latex = afficher_variation(image_de_borne_2 ,variations_fonction_initiale , image_de_la_derniere_valeur)
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
\tkzTabInit[espcl=3]{$x$ / 1 , $f'(x)$ / 1, variation de $f(x)$/1.2}
{""" + ','.join(valeurs_de_x_latex) + r"""}
\tkzTabLine{""" ','+ ",z,".join(signes) + r"""}
\tkzTabVar{""" + "".join(variations_fonction_latex) + derniere_variation_latex  + r"""}
\end{tikzpicture}
\end{document}""") 

afficher_latex(fonction_initiale , derivee , valeurs_de_x_latex , signes , variations_fonction_latex , derniere_variation_latex)
