import random
from termcolor import colored

def mm(niv = 4, coul = 6):
    # on laisse les valeurs par défaut dans les paramètres
    c = 1
    couleurs = ("nothing", "bleu", "rouge", "jaune", "rose", "vert", "cyan", "blanc", "noir")

    couleurs_colorees = ("nothing", colored("bleu", "blue"), colored("rouge", "red"), colored("jaune", "yellow"), colored("rose", "magenta"), colored("vert", "green"), colored("cyan", "cyan"), colored("blanc", "white"), colored("noir", "grey", "on_white"))

    couleur_dict = {
        "nothing": "nothing", 
        "bleu": colored("bleu", "blue"), 
        "rouge": colored("rouge", "red"), 
        "jaune": colored("jaune", "yellow"), 
        "rose": colored("rose", "magenta"), 
        "vert": colored("vert", "green"), 
        "cyan": colored("cyan", "cyan"), 
        "blanc": colored("blanc", "white"), 
        "noir": colored("noir", "grey", "on_white")
    }

    str_couleurs = ""
    for col in couleurs_colorees[1:coul+1]:
        str_couleurs += col + ", "
    str_couleurs = str_couleurs.rstrip(", ")

    secret = [random.choice(couleurs[1:coul+1]) for i in range(niv)]
    
    secret_colore_lst = []
    for j in secret:
        secret_colore_lst.append(couleur_dict[j])

    secret_colore_str = ""
    for v in secret_colore_lst:
        secret_colore_str += v + ', '
    secret_colore_str.rstrip(", ")

    str_secret = ""
    for col in couleurs_colorees[1:coul+1]:
        str_secret += col + ", "
    str_secret = str_secret.rstrip(", ")

    while True:
        code = list(secret)
        saisie = (input(f"Entrez {niv} couleurs parmi les suivantes : {str_couleurs}, séparées par un espace. Essai n° {c} : "))
        essai = saisie.split(" ")
        # le joueur entre sa combinaison ou peut abandonner en ne rentrant rien.
        if len(essai) < niv: 
            print(f"Perdu... La combinaison était : {secret_colore_str}")
            break
        c += 1
        bien, mal = 0, 0
        for i,v in enumerate(essai):
            if v == code[i]: 
                bien += 1
                essai[i] = "#"
                code[i] = "*"
        if bien == niv: 
            print("Gagné!")
            break
        for i, v in enumerate(essai):
            if v in code: 
                mal =+ 1
                code[code.index(v)] = "*"
        print(f"Bien : {bien} , Mal : {mal}")

# maximum 8 couleurs
mm(4,6)        
