import sympy as sp
import tkinter as tk
from sympy import *
from tkinter import *
import random as rd

# INTERFACE
couleur_fond = "gray"
police_ecriture = "Arial 12 bold"
canvas_police= "Times 14 bold"
nom = Tk()
nom.title('Générateur de afficher_tableau de variation')
nom.config(bg=couleur_fond)
frame = Frame(nom, bg=couleur_fond)
canvas = Canvas(frame, width=900, height=150, background=couleur_fond)
canvas.pack()
canvas.create_text(140, 70, text="Entrez une fonction :", font=police_ecriture)
canvas.create_text(538, 45, text="Borne 1", font=police_ecriture)
canvas.create_text(668, 45, text="Borne 2", font=police_ecriture)
default_function = "(x-2)*(x-1)*(x+1)*(x+2)"
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



def afficher_resultat():

    def arrondir(expression):
        expression_arrondie = '{:.2f}'.format(float(expression))
        return expression_arrondie  
        
    #INTERVALLES
    valeur_borne_1, valeur_borne_2 = borne_1.get(), borne_2.get()
    valeur_borne_1, valeur_borne_2 = sympify(valeur_borne_1), sympify(valeur_borne_2) 
    valeur_borne_1 = float(valeur_borne_1)
    valeur_borne_2 = float(valeur_borne_2)

    #DERIVEE
    fonction_initiale = entree_fonction_initiale.get()  # Récupère la fonction_initiale depuis le champ de saisie
    x = symbols('x')
    fonction_initiale = sympify(fonction_initiale)
    derivee = diff(fonction_initiale,x)
    valeur_derivee_en_0 = solve(derivee, x)
    valeur_derivee_en_0 = sorted(valeur_derivee_en_0)
    valeur_de_x = [valeur_borne_1] + valeur_derivee_en_0 + [valeur_borne_2]
    valeur_de_x_latex = ['$' + latex(x) + '$' for x in valeur_de_x]

    signes = []  
    variations_fx = []
    # if not valeur_derivee_en_0:
    #     valeur_derivee_en_0 = [valeur_borne_1]


    for element, solution in enumerate(valeur_derivee_en_0):

        # LES SIGNES
        if element== 0:
            valeur_de_x = rd.uniform(valeur_borne_1, solution)
            signe_1 = derivee.subs(x, valeur_de_x)
        else:
            valeur_de_x = rd.uniform(valeur_derivee_en_0[element- 1], solution)
            signe_1 = derivee.subs(x, valeur_de_x)
        if signe_1 > 0:
            signe = '+'
        else:
            signe = '-'       
        signes.append(str(signe))
        if element== len(valeur_derivee_en_0) - 1:
            valeur_de_x = rd.uniform(valeur_derivee_en_0[element], valeur_borne_2)
            signe_1 = derivee.subs(x, valeur_de_x)
            if signe_1 > 0:
                signe = '+'
            else:
                signe = '-'
            signes.append(str(signe))


        fx = fonction_initiale.subs(x, solution).evalf(3)
        variations_fx.append(latex(fx))
        image_de_borne_1 = fonction_initiale.subs(x, valeur_borne_1).evalf(3)
        image_de_borne_2 = fonction_initiale.subs(x, valeur_borne_2).evalf(3)
        variations_fonction_initiale = [image_de_borne_1] + variations_fx + [image_de_borne_2]
        image_de_la_derniere_valeur = fonction_initiale.subs(x,valeur_derivee_en_0[-1]).evalf(3)
        
        #VARIATION LATEX
        variations_fonction=[]
        if image_de_la_derniere_valeur >image_de_borne_2:
            derniere_variation = '-/$'+str(image_de_borne_2)+'$'
        else:
            derniere_variation = '+/$'+str(image_de_borne_2)+'$'
        for element in range(len(signes)):
            if signes[element]=='+':
                variations_fonction.append('-/$'+str(variations_fonction_initiale[element])+'$,')
            if signes[element]=='-':
                variations_fonction.append('+/$'+str(variations_fonction_initiale[element])+'$,')
    
    print(variations_fonction_initiale)
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
Tableau de variation de $f(x)$\\
                   
$f(x)=""" + latex(fonction_initiale) + r"""$\\
$f'(x)=""" + latex(derivee) + r"""$\\

\begin{tikzpicture}
\tkzTabInit[espcl=3]{$x$ / 1 , $f'(x)$ / 1, variation de $f(x)$/1.2}
{""" + ','.join(valeur_de_x_latex) + r"""}
\tkzTabLine{""" ','+ ",z,".join(signes) + r"""}
\tkzTabVar{""" + "".join(variations_fonction) + derniere_variation  + r"""}
\end{tikzpicture}
\end{document}""")
        
    # print(variations_fonction_initiale)
    # print (variations_fonction)
    # print(valeur_derivee_en_0)

def tout_afficher():
    afficher_resultat()

bouton = Button(frame, text="Générer",font = "Times 11 bold", command=tout_afficher)
bouton.place(x=800, y=58)
frame.pack()
nom.mainloop()