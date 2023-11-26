import os
import random

def useless_robot_selector():
    dossier_robots = os.path.dirname(__file__)
    noms_fichiers = [fichier for fichier in os.listdir(dossier_robots) if fichier.endswith('.txt')]
    nom_fichier_choisi = random.choice(noms_fichiers)
    chemin_complet = os.path.join(dossier_robots, nom_fichier_choisi)
    with open(chemin_complet, 'r') as fichier:
        contenu_robot = fichier.read()

    return(contenu_robot)

