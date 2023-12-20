from functions.interface import *
from functions.latex import *
from functions.calcul import *

afficher_borne(-10,10)
valeur_borne_1, valeur_borne_2 = afficher_borne(-5, 5 )

calculer_derivee(valeur_borne_1,valeur_borne_2,'(x-2)*(x-1)*(x+1)*(x+2)')
valeur_derivee_en_0, derivee, x , fonction_initiale , valeurs_de_x_latex = calculer_derivee(valeur_borne_1, valeur_borne_2, '(x-2)*(x-1)*(x+1)*(x+2)')


afficher_signes(valeur_derivee_en_0,valeur_borne_1,valeur_borne_2,derivee,x)
signes = afficher_signes(valeur_derivee_en_0,valeur_borne_1,valeur_borne_2,derivee,x)


stocker_valeur(valeur_borne_1, valeur_borne_2)
variations_fx, image_de_borne_1, image_de_borne_2, variations_fonction_initiale, image_de_la_derniere_valeur = stocker_valeur(valeur_borne_1, valeur_borne_2)


afficher_variation(image_de_borne_1 , image_de_borne_2 ,variations_fonction_initiale , image_de_la_derniere_valeur)

variations_fonction_latex, derniere_variation_latex = afficher_variation(image_de_borne_1 , image_de_borne_2 ,variations_fonction_initiale , image_de_la_derniere_valeur)

afficher_latex(fonction_initiale , derivee , valeurs_de_x_latex , signes , variations_fonction_latex , derniere_variation_latex)