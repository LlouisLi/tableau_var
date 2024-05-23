def afficher_signes(valeur_derivee_en_0,valeur_borne_1,valeur_borne_2,derivee,x,valeur_de_x):
    signes = []
    for solution in range(len(valeur_de_x)-1):
            print(valeur_de_x)
            valeur_de_x_aleatoire = rd.uniform(valeur_de_x[solution], valeur_de_x[solution+1])
            signe_1 = derivee.subs(x, valeur_de_x_aleatoire)
            print(valeur_de_x_aleatoire)    
            if signe_1 > 0:
                signe = '+'
            if signe_1 < 0:
                signe = '-'
            if signe_1 == 0:
                signe = '0'
                       
            signes.append(str(signe))
    return signes