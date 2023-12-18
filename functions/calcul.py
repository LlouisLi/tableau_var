import sympy as sp
import tkinter as tk
from sympy import *
from tkinter import *
import random as rd



def afficher_borne(borne_1, borne_2):

    valeur_borne_1, valeur_borne_2 = borne_1, borne_2
    valeur_borne_1, valeur_borne_2 = sympify(valeur_borne_1), sympify(valeur_borne_2) 
    valeur_borne_1 = float(valeur_borne_1)
    valeur_borne_2 = float(valeur_borne_2)

    return valeur_borne_1,valeur_borne_2

valeur_borne_1, valeur_borne_2 = afficher_borne(-100, 100)

def calculer_derivee(valeur_borne_1,valeur_borne_2,entree_fonction_initiale):
    fonction_initiale = entree_fonction_initiale  # Récupère la fonction_initiale depuis le champ de saisie
    x = symbols('x')
    fonction_initiale = sympify(fonction_initiale)
    derivee = diff(fonction_initiale,x)
    valeur_derivee_en_0 = solve(derivee, x)
    valeur_derivee_en_0 = sorted(valeur_derivee_en_0)
    valeur_de_x = [valeur_borne_1] + valeur_derivee_en_0 + [valeur_borne_2]
    valeur_de_x_latex = ['$' + latex(x) + '$' for x in valeur_de_x]
    signes = []
    variations_fx = []
    if not valeur_derivee_en_0:
        valeur_derivee_en_0 = [valeur_borne_1]

    return valeur_derivee_en_0
calculer_derivee(valeur_borne_1,valeur_borne_2,'x**2')

# def afficher_signes():

#      for element, solution in enumerate(valeur_derivee_en_0):
#         # LES SIGNES
#         if element== 0:
#             valeur_de_x = rd.uniform(valeur_borne_1, solution)
#             signe_1 = derivee.subs(x, valeur_de_x)
#         else:
#             valeur_de_x = rd.uniform(valeur_derivee_en_0[element- 1], solution)
#             signe_1 = derivee.subs(x, valeur_de_x)
#         if signe_1 > 0:
#             signe = '+'
#         else:
#             signe = '-'       
#         signes.append(str(signe))
#         if element== len(valeur_derivee_en_0) - 1:
#             valeur_de_x = rd.uniform(valeur_derivee_en_0[element], valeur_borne_2)
#             signe_1 = derivee.subs(x, valeur_de_x)
#             if signe_1 > 0:
#                 signe = '+'
#             else:
#                 signe = '-'
#             signes.append(str(signe))
#         print(signes)


# def stocker_valeur():

#     fx = fonction_initiale.subs(x, solution).evalf(3)
#     variations_fx.append(latex(fx))
#     image_de_borne_1 = fonction_initiale.subs(x, valeur_borne_1).evalf(2)
#     image_de_borne_2 = fonction_initiale.subs(x, valeur_borne_2).evalf(2)
#     variations_fonction_initiale = [image_de_borne_1] + variations_fx + [image_de_borne_2]
#     image_de_la_derniere_valeur = fonction_initiale.subs(x,valeur_derivee_en_0[-1]).evalf(2)
#     variations_fonction=[]


# def afficher_variation():

#     if not len(signes)==0:
#             if image_de_la_derniere_valeur >image_de_borne_2:
#                 derniere_variation = '-/$'+str(image_de_borne_2)+'$'
#             else:
#                 derniere_variation = '+/$'+str(image_de_borne_2)+'$'   
#             for element in range(len(signes)):
#                 if signes[element]=='+':
#                     variations_fonction.append('-/$'+str(variations_fonction_initiale[element])+'$,')
#                 if signes[element]=='-':
#                     variations_fonction.append('+/$'+str(variations_fonction_initiale[element])+'$,')



# afficher_signes()
# stocker_valeur()
# afficher_variation()

