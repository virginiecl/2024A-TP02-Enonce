"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : 01
Numéro d'équipe :  19
Noms et matricules : Virginie Cloutier (2373838), Sara-Maude Laliberté (2384032)
"""
import csv
from datetime import datetime
##########################################################################################################
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
##########################################################################################################

# TODO : Écrire votre code ici

collec_actuelle = "collection_bibliotheque.csv"
bibliotheque = {}

with open(collec_actuelle, "r") as fichier1:
    c_a_read = csv.reader(fichier1)

    for row in c_a_read:
        if row[0] == "titre":
            continue
        else:
            titre = row[0]
            auteur = row[1]
            date = row[2]
            cote = row[3]

            bibliotheque[cote] = [titre, auteur, date]

print(f' \n Bibliotheque initiale : {bibliotheque} \n')


##########################################################################################################
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
##########################################################################################################

# TODO : Écrire votre code ici

nouvelle_collec = "nouvelle_collection.csv"

with open(nouvelle_collec, "r") as fichier2:
    n_c_read = csv.reader(fichier2)

    for row in n_c_read:
        if row[0] == "titre":
            continue
        else:
            titre = row[0]
            auteur = row[1]
            date = row[2]
            cote = row[3]

            if cote in bibliotheque:
                print(f"Le livre {cote} ---- {titre} par {auteur} ---- est déjà présent dans la bibliothèque")

            else:
                print(f"Le livre {cote} ---- {titre} par {auteur} ---- a été ajouté avec succès")
                bibliotheque[cote] = [titre, auteur, date]


##########################################################################################################
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
##########################################################################################################

# TODO : Écrire votre code ici

keys = list(bibliotheque.keys())

for element in keys:
    if "S" in element:
        if bibliotheque[element][1] == "William Shakespeare":
            titre = bibliotheque[element][0]
            auteur = bibliotheque[element][1]
            date = bibliotheque[element][2]

            nouv_cote = f"SW{element[1:]}"

            bibliotheque[nouv_cote] = [titre, auteur, date]
            bibliotheque.pop(element)

print(f' \n Bibliotheque avec modifications de cote : {bibliotheque} \n')


##########################################################################################################
# PARTIE 4 : Emprunts et retours de livres
##########################################################################################################

# TODO : Écrire votre code ici

liste_emprunts = "emprunts.csv"
keys_modif = list(bibliotheque.keys())

with open(liste_emprunts, "r") as fichier3:
    l_e_read = csv.reader(fichier3)

    for row in l_e_read:
        if row[0] == "cote_rangement":
            continue
        else:
            cote = row[0]
            date_emprunt = row[1]

            if cote not in keys_modif:
                continue
            else:
                new_elements = ["emprunté", date_emprunt]
                bibliotheque[cote].extend(new_elements)
                keys_modif.remove(cote)

    for i in keys_modif:
        new_element = ["disponible"]
        bibliotheque[i].extend(new_element)

print(f' \n Bibliotheque avec ajout des emprunts : {bibliotheque} \n')


##########################################################################################################
# PARTIE 5 : Livres en retard
##########################################################################################################

# TODO : Écrire votre code ici

liste_emprunts = "emprunts.csv"
livres_retard = []
with open(liste_emprunts, "r") as fichier3:
    l_e_read = csv.reader(fichier3)

    for row in l_e_read:
        if row[0] == "cote_rangement":
            continue
        else:
            cote = row[0]
            date_emprunt = row[1]

            formatage = date_emprunt.split("-")
            annee = int(formatage[0])
            mois = int(formatage[1])
            jour = int(formatage[2])

            start_time = datetime(annee, mois, jour)
            end_time = datetime.now()

            temps_emprunt = str(end_time - start_time)
            temps_emprunt.split()
            temps_final = int(temps_emprunt[:-21])

            montant = temps_final * 2

            if montant >= 100:
                montant = 100

            if cote in bibliotheque:
                frais_retard = [f"frais de retard: {montant}$"]
                bibliotheque[cote].extend(frais_retard)

                information = [f"{bibliotheque[cote][0]}: {montant}$"]

                livres_retard.extend(information)

            if temps_final >= 365:
                livre_perdu = ["perdu"]
                bibliotheque[cote].extend(livre_perdu)

print(livres_retard)
print(f' \n Bibliotheque avec ajout des retards et frais : {bibliotheque} \n')