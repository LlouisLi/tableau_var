import sympy as sp
import tkinter as tk
from sympy import *
from tkinter import *
import random as rd
from tabulate import tabulate

# VARIABLES
couleur_fond = "gray"
police_ecriture = "Arial 12 bold"
canvas_police= "Times 14 bold"

# GRANDE FENETRE
nom = Tk()
nom.title('Générateur de afficher_tableau de variation')
nom.config(bg=couleur_fond)

# PREMIERE BOITE
frame = Frame(nom, bg=couleur_fond)

# DEUXIEME BOITE
canvas = Canvas(frame, width=1150, height=550, background=couleur_fond)
canvas.pack()

# INPUT
canvas.create_text(140, 70, text="Entrez une fonction_initiale :", font=police_ecriture)
canvas.create_text(538, 45, text="Borne 1", font=police_ecriture)
canvas.create_text(668, 45, text="Borne 2", font=police_ecriture)

default_function = "x**2-x**3-x**4+x**5"
default_borne1 = "-100"
default_borne2 = "100"
fonction_initiale_var = StringVar()
borne1_var = StringVar()
borne2_var = StringVar()
fonction_initiale_var.set(default_function)
borne1_var.set(default_borne1)
borne2_var.set(default_borne2)
entree_fonction_initiale = Entry(frame, width=20, font="Arial 12", bg= couleur_fond,text = fonction_initiale_var)
borne_1 = Entry(frame, width=8, font="Arial 12", bg=couleur_fond,text= borne1_var)
borne_2 = Entry(frame, width=8, font="Arial 12", bg=couleur_fond,text = borne2_var)

entree_fonction_initiale.place(x=225, y=60)
borne_1.place(x=500, y=60)
borne_2.place(x=630, y=60)
deuxieme_canvas = Canvas(canvas, width=900, height=400, background=couleur_fond)

#Tracer le tableau
def afficher_tableau():
    deuxieme_canvas.place(x=100, y=130)
    deuxieme_canvas.create_line(0, 60, 1000, 60, width=2, fill='black')
    deuxieme_canvas.create_line(100, 0, 100, 300, width=2, fill='black')
    deuxieme_canvas.create_line(0, 120, 1000, 120, width=2, fill='black')
    deuxieme_canvas.update()
    deuxieme_canvas.create_text(50, 35, text="x", font="Times 25 bold")
    deuxieme_canvas.create_text(50, 90, text="f '(x)", font="Times 25 bold")
    deuxieme_canvas.create_text(50, 180, text="f (x)", font="Times 25 bold")
    bbox = deuxieme_canvas.bbox("all")
    deuxieme_canvas.config(width=bbox[2] - bbox[0], height=bbox[3] - bbox[1])

def afficher_resultat():
    # def sp(expression):  
    #     expression1 = sympify(expression)
    #     expression2 = float(expression1)
    #     expression3 = '{:.2f}'.format(expression2)
    #     return expression3
    def arrondir(expression):
        
        expression_arrondie = '{:.2f}'.format(float(expression))
        return expression_arrondie
        
    #INTERVALLES
    deuxieme_canvas.delete("derivative")
    valeur_borne_1, valeur_borne_2 = borne_1.get(), borne_2.get()
    valeur_borne_1, valeur_borne_2 = sympify(valeur_borne_1), sympify(valeur_borne_2) 
    valeur_borne_1 = float(valeur_borne_1)
    valeur_borne_2 = float(valeur_borne_2)
    deuxieme_canvas.create_text(130, 35, text=valeur_borne_1, font= canvas_police, tags='derivative')
    deuxieme_canvas.create_text(950, 35, text=valeur_borne_2, font=canvas_police, tags='derivative')
    
    #DERIVEE
    fonction_initiale = entree_fonction_initiale.get()  # Récupère la fonction_initiale depuis le champ de saisie
    x = symbols('x')
    fonction_initiale = sympify(fonction_initiale)
    derivee = diff(fonction_initiale,x)
    valeur_derivee_en_0 = solve(derivee, x)
    valeur_derivee_en_0 = sorted(valeur_derivee_en_0)
    #valeur_derivee_en_0 = [solution for solution in valeur_derivee_en_0 if valeur_borne_1 <= solution <= valeur_borne_2]

    # PRINT DERIVEE EN 0
    nb_solutions = len(valeur_derivee_en_0)
    a = 1075  # Largeur totale 
    distance_entre_valeur = a / (nb_solutions + 1)  # Calcul de la distance entre les valeurs
    
    for element, solution in enumerate(valeur_derivee_en_0):
        position = (element+ 1) * distance_entre_valeur  # Calcul de la position horizontale
        solution = solution.evalf()
        position_y = 30
        solution_arrondie = '{:.2f}'.format(solution) #arrondie apres 3chiffres apres virgule 
        deuxieme_canvas.create_text(position, position_y, text=solution_arrondie, font=canvas_police , tags= 'derivative')
        deuxieme_canvas.create_text(position, position_y+60, text='0', font=canvas_police, tags = 'derivative')

        # LES SIGNES
        if element== 0:
            x_valeur = rd.uniform(valeur_borne_1, solution)
        else:
            x_valeur = rd.uniform(valeur_derivee_en_0[element- 1], solution)
        if element== len(valeur_derivee_en_0) - 1:
            x_value1 = rd.uniform(valeur_derivee_en_0[element], valeur_borne_2)
            signe_1 = derivee.subs(x, x_value1)
            if signe_1 > 0:
                signe = '+'
            else:
                signe = '-'  
            deuxieme_canvas.create_text(position + 40, 90, text=signe, tags='derivative')
        signe_1 = derivee.subs(x, x_valeur)
        if signe_1 > 0:
            signe = '+'
        else:
            signe = '-'        
        deuxieme_canvas.create_text(position - 40, 90, text=signe, tags='derivative')


        #F(x)
        
        # image_de_borne_1 = f.subs(x, valeur_borne_1)
        # image_de_borne_2 = f.subs(x, valeur_borne_2)
        # image_de_borne_1 = arrondir(image_de_borne_1)
        # image_de_borne_2 = arrondir(image_de_borne_2)
        # deuxieme_canvas.create_text(130, position_y+110, text=image_de_borne_1, font=canvas_police)
        # deuxieme_canvas.create_text(950, position_y+110, text=image_de_borne_2, font=canvas_police)
        # fx = f.subs(x, solution)
        # fx = arrondir(fx)
        # if element== 0 :       
        #     if fx > image_de_borne_1:
        #         deuxieme_canvas.create_text(position, position_y+110, text=fx, font=canvas_police)
        #     else:
        #         deuxieme_canvas.create_text(position, position_y+250, text=fx, font=canvas_police)
        # Liste_fx.append(fx)
        # print(Liste_fx)

        # if i>0:
        #     if fx > Liste_fx[i-1]:
        #         deuxieme_canvas.create_text(position, position_y+110, text=fx, font=canvas_police)
        #     else:
    # ... (votre code pour la dérivée et le tableau de variation)


    # ... (le reste de votre code pour la dérivée et le tableau de variation)

    # Écrivez le tableau LaTeX avec les valeurs de x dans un fichier
    x_values = [valeur_borne_1] + valeur_derivee_en_0 + [valeur_borne_2]
    x_values_latex = ['$' + latex(x) + '$' for x in x_values]
    signes = []  
    variations_fx = []

    for element, solution in enumerate(valeur_derivee_en_0):
        solution = solution.evalf()
        # LES SIGNES
        if element== 0:
            x_valeur = rd.uniform(valeur_borne_1, solution)
            signe_1 = derivee.subs(x, x_valeur)
        else:
            x_valeur = rd.uniform(valeur_derivee_en_0[element- 1], solution)
            signe_1 = derivee.subs(x, x_valeur)
        if signe_1 > 0:
            signe = '+'
        else:
            signe = '-'        
        signes.append(str(signe))
        if element== len(valeur_derivee_en_0) - 1:
            x_value1 = rd.uniform(valeur_derivee_en_0[element], valeur_borne_2)
            signe_1 = derivee.subs(x, x_value1)
            if signe_1 > 0:
                signe = '+'
            else:
                signe = '-'  
            signes.append(str(signe))
    
        fx = fonction_initiale.subs(x, solution).evalf(3)
        variations_fx.append('$' + latex(fx) + '$')

    image_de_borne_1 = fonction_initiale.subs(x, valeur_borne_1).evalf(3)
    image_de_borne_2 = fonction_initiale.subs(x, valeur_borne_2).evalf(3)
    variations_fonction_initiale = [image_de_borne_1] + variations_fx + [image_de_borne_2]

    image_de_la_premiere_valeur = fonction_initiale.subs(x,valeur_derivee_en_0[0]).evalf(2)
    if image_de_borne_1 > image_de_la_premiere_valeur:
        premiere_variation = '+/'
        variation = ['-/$' + latex(x)+ '$' for x in variations_fonction_initiale]
    else:
        premiere_variation = '-/'
        variation = ['/+$' + latex(x)+ '$' for x in variations_fonction_initiale]

    
    with open(r'C:\Users\Louis\Desktop\tableau variation\tableau_latex.tex', 'w') as file:
        file.write(r"""\documentclass{article}
\usepackage{tkz-tab}
\usepackage{amsmath} 
\usepackage{geometry}
\usepackage{indentfirst}
\setlength{\parindent}{-0.5cm} % Retrait du paragraphe
\geometry{
    left=1.5cm }
\begin{document}
TAbleau de variation de $f(x)$\\
                   
$f(x)=""" + latex(fonction_initiale) + r"""$\\
$f'(x)=""" + latex(derivee) + r"""$\\

\begin{tikzpicture}
\tkzTabInit[espcl=3]{$x$ / 1 , $f'(x)$ / 1, variation de $f(x)$/1.5}
{""" + ','.join(x_values_latex) + r"""}
\tkzTabLine{""" ','+ ",z ,".join(signes) + r"""}
\tkzTabVar{""" +premiere_variation + ",".join(variation) + r"""}
\end{tikzpicture}
\end{document}""")
    print (variations_fonction_initiale)

def tout_afficher():
    afficher_resultat()

    
bouton = Button(frame, text="Générer",font = "Times 11 bold", command=tout_afficher)
bouton.place(x=800, y=58)
frame.pack()
afficher_tableau()
nom.mainloop()