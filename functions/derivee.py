import sympy as sp
from sympy import *

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