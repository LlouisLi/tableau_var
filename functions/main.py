from calcul import *


valeur_borne_1, valeur_borne_2 = afficher_borne(-10, 10 )
print(valeur_borne_1, valeur_borne_2)

calculer_derivee(valeur_borne_1, valeur_borne_2,fonction )
valeur_derivee_en_0, derivee, x  , fonction_initiale , valeurs_de_x_latex , valeur_de_x = calculer_derivee(valeur_borne_1, valeur_borne_2, fonction)

signes = afficher_signes(valeur_derivee_en_0,valeur_borne_1,valeur_borne_2,derivee,x,valeur_de_x)
print(signes)

variations_fx, image_de_borne_1, image_de_borne_2, variations_fonction_initiale, image_de_la_derniere_valeur = variations_de_fx(valeur_borne_1, valeur_borne_2)
print(variations_fonction_initiale)
 
variations_fonction_latex, derniere_variation_latex = afficher_variation_latex(image_de_borne_2 ,variations_fonction_initiale , image_de_la_derniere_valeur,signes)
print(variations_fonction_latex, derniere_variation_latex)

afficher_latex(fonction_initiale , derivee , valeurs_de_x_latex , signes , variations_fonction_latex , derniere_variation_latex)
