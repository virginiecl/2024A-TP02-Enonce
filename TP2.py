"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : 01
Numéro d'équipe : 19
Noms et matricules : Virginie Cloutier (2373838), Sara-Maude Laliberté (2384032)
"""

########################################################################################################## 
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
########################################################################################################## 

# TODO : Écrire votre code ici
import csv

csvfile = open('collection_bibliotheque.csv', newline='')


c = csv.reader(csvfile)

bibliotheque = {}

for row in c:
    if row[0] == "titre":
        continue
    else:
        titre = row[0]
        auteur = row[1]
        date_publication = row[2]
        cote = row[3]

        bibliotheque[cote] = {"titre" : titre, "auteur" : auteur, "date_publication" : date_publication}

print(f' \n Bibliotheque initiale : {bibliotheque} \n')

csvfile.close()


########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

# TODO : Écrire votre code ici
csvfile = open('nouvelle_collection.csv', newline='')

c = csv.reader(csvfile)

for row in c:
    if row[0] == "titre":
        continue
    else:
        titre = row[0]
        auteur = row[1]
        date_publication = row[2]
        cote = row[3]

        if cote in bibliotheque:
            print(f"Le livre {cote} ---- {titre} par {auteur} ---- est déjà présent dans la bibliothèque")

        else:
            print(f"Le livre {cote} ---- {titre} par {auteur} ---- a été ajouté avec succès")
            bibliotheque[cote] = {"titre" : titre, "auteur" : auteur, "date_publication" : date_publication}




########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici
new_bibliotheque = {}
for cote in bibliotheque:
    titre = bibliotheque[cote]["titre"]
    auteur = bibliotheque[cote]["auteur"]
    date_publication = bibliotheque[cote]["date_publication"]
    if bibliotheque[cote]["auteur"] == "William Shakespeare":

            cote = f"WS{cote[1:]}"
            new_bibliotheque[cote] = {"titre" : titre, "auteur" : auteur, "date_publication" : date_publication}

    else:
        new_bibliotheque[cote] = {"titre": titre, "auteur": auteur, "date_publication": date_publication}


bibliotheque = new_bibliotheque



print(f' \n Bibliotheque avec modifications de cote : {bibliotheque} \n')

########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici
csvfile = open('emprunts.csv', newline='')


c = csv.reader(csvfile)
for cote in bibliotheque:
        bibliotheque[cote]["emprunts"] = "disponible"
        bibliotheque[cote]["date_emprunt"] = "-"

for row in c:
    if row[0] in bibliotheque:
        bibliotheque[row[0]]["emprunts"] = "emprunté"
        bibliotheque[row[0]]["date_emprunt"] = row[1]


print(f' \n Bibliotheque avec ajout des emprunts : {bibliotheque} \n')



########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici
import datetime

livre_retard = []
livres_perdus = []
for cote in bibliotheque:

    if bibliotheque[cote]["emprunts"] == "emprunté":
        date_emprunt = bibliotheque[cote]["date_emprunt"]
        date_emprunt = date_emprunt.split("-")
        annee = int(date_emprunt[0])
        mois = int(date_emprunt[1])
        jour = int(date_emprunt[2])

        date_emprunt = datetime.datetime(annee, mois, jour)

        date_actuelle = datetime.datetime.now()

        temps_ecoule = (date_actuelle - date_emprunt).days


        if temps_ecoule > 30:
            frais_retard = (temps_ecoule - 30)*2

            if frais_retard > 100:
                frais_retard = 100

            livre_retard.append(f"{bibliotheque[cote]['titre']} : {frais_retard}$")
            bibliotheque[cote]["frais_retard"] = f"{frais_retard}$"
            bibliotheque[cote]["livres_perdus"] = "non perdu"

        if temps_ecoule > 365:
            livres_perdus.append(bibliotheque[cote]["titre"])
            bibliotheque[cote]["livres_perdus"] = "livre perdu"

    else:
        bibliotheque[cote]["frais_retard"] = "-"
        bibliotheque[cote]["livres_perdus"] = "non perdu"

print(f"liste des livres en retard avec les frais applicables: {livre_retard}")
print(f"liste des livres perdus: {livres_perdus}")

print(f' \n Bibliotheque avec ajout des retards et frais : {bibliotheque} \n')