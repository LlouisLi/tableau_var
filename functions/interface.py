import sympy as sp
import tkinter as tk
from sympy import *
from tkinter import *
import random as rd

def interface_tkinter():
    global fonction_initiale_var, borne1_var, borne2_var
    global entree_fonction_initiale, borne_1, borne_2, frame

    couleur_fond = "gray"
    police_ecriture = "Arial 12 bold"
    police_ecriture = "Times 14 bold"

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

    entree_fonction_initiale = Entry(frame, width=20, font="Arial 12", bg=couleur_fond, text=fonction_initiale_var)
    borne_1 = Entry(frame, width=8, font="Arial 12", bg=couleur_fond, text=borne1_var)
    borne_2 = Entry(frame, width=8, font="Arial 12", bg=couleur_fond, text=borne2_var)

    entree_fonction_initiale.place(x=225, y=60)
    borne_1.place(x=500, y=60)
    borne_2.place(x=630, y=60)


    frame.pack()
    nom.mainloop()