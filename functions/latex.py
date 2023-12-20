import sympy as sp
from sympy import *

def afficher_latex(fonction_initiale , derivee , valeur_de_x_latex , signes , variations_fonction_latex , derniere_variation_latex):
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
{""" + ','.join(valeur_de_x_latex) + r"""}
\tkzTabLine{""" ','+ ",z,".join(signes) + r"""}
\tkzTabVar{""" + "".join(variations_fonction_latex) + derniere_variation_latex  + r"""}
\end{tikzpicture}
\end{document}""")

