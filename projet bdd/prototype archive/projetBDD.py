from sqlalchemy import create_engine, text

import pandas as pd
import csv


# Chaîne de connexion à la base de données PostgreSQL
chaine_connexion = 'postgresql://postgres:speedademon25@localhost/projetBDD'

# Connexion à la base de données PostgreSQL
try:
    engine = create_engine(chaine_connexion)
    print("Connexion réussie à la base de données PostgreSQL")

except Exception as erreur:
    print("Erreur lors de la connexion à la base de données PostgreSQL:", erreur)


# Créer un objet de connexion
with engine.connect() as conn:

# Exécuter une requête SELECT
    query = "INSERT INTO Type VALUES \'Certificat de mariage\'"
    result = conn.execute(text(query))

    query = text("INSERT INTO Type (signification) VALUES 'Contrat de mariage' ")
    result = conn.execute(query)

    query = text("INSERT INTO Type (signification) VALUES 'Divorce' ")
    result = conn.execute(query)

    query = text("INSERT INTO Type (signification) VALUES 'Mariage' ")
    result = conn.execute(query)

    query = text("INSERT INTO Type (signification) VALUES 'Promesse de mariage - fiançailles' ")
    result = conn.execute(query)

    query = text("INSERT INTO Type (signification) VALUES 'Publication de mariage' ")
    result = conn.execute(query)

    query = text("INSERT INTO Type (signification) VALUES 'Rectification de mariage' ")
    result = conn.execute(query)

    query = text("INSERT INTO Departement VALUES '44' ")
    result = conn.execute(query)

    query = text("INSERT INTO Departement VALUES '49' ")
    result = conn.execute(query)

    query = text("INSERT INTO Departement VALUES '79' ")
    result = conn.execute(query)

    query = text("INSERT INTO Departement VALUES '85' ")
    result = conn.execute(query)


def notExiste(e, T):
    for i in T:
        if e == i:return False
    return True

def existe(e, T):
    for i in T:
        if e == i:return True
    return False

def crealiste(T):
    resultat = []
    for i in T:
        if notExiste(i, resultat):
            resultat.append(i)
    return resultat

def sansDoublon(T):
    resultat = []
    for i in T:
        if notExiste(i, T):
            resultat.append(i)
    return resultat

liste_departement = [44, 49, 79, 85]

# Ouvrir le fichier CSV en mode lecture
with open('mariages_l3_5k.csv', newline='') as csvfile:
    # Créer un objet lecteur CSV
    lecteur_csv = csv.reader(csvfile)

    #création de la liste qui acceuillera les commune département

#-------------------------------------------------------------#table commune#------------------------------------------------

    commune = []
    communeDepartement = []
    # Parcourir chaque ligne du fichier CSV
    for ligne in lecteur_csv:
        # Accéder aux données de chaque colonne de la ligne
        cache = []
        for i in range(len(ligne)):
            if i == 12:
                cache.append(ligne[i])
                if notExiste(ligne[i], commune):
                    commune.append(ligne[i])
            if i == 13:
                cache.append(ligne[i])
        communeDepartement.append(cache)

    communeDepartement = sansDoublon(communeDepartement)

    for i in communeDepartement:
        if existe(i[1], liste_departement):
            query = f"INSERT INTO Commune VALUES ('{i[0]}', (SELECT id FROM departement WHERE id={i[1]}))  "
            result = conn.execute(query, parametre="valeur")
#---------------------------------------------------------------#personnes#---------------------------------------------------
    personne = []
    lecteur_copy = lecteur_csv

    for ligne in lecteur_copy:
        # Accéder aux données de chaque colonne de la ligne
        cacheHomme = []
        cacheFemme = []
        for i in range(len(ligne)):
            #nom / nom pere
            if i == 2:
                cacheHomme.append(ligne[i])
            #prenom 
            if i == 3:
                cacheHomme.append(ligne[i])
            #prenom pere
            if i == 4:
                cacheHomme.append(ligne[i])
            #nom mere
            if i == 5:
                cacheHomme.append(ligne[i])
            #prenom mere
            if i == 6:
                cacheHomme.append(ligne[i])

            #nom femme / nom son pere
            if i == 7:
                cacheFemme.append(ligne[i])
            #prenom femme
            if i == 8:
                cacheFemme.append(ligne[i])
            #prenom pere (femme)
            if i == 9:
                cacheFemme.append(ligne[i])
            #nome mere (femme)
            if i == 10:
                cacheFemme.append(ligne[i])
            #prenom mere (femme)
            if i == 11:
                cacheFemme.append(ligne[i])
        personne.append(cacheHomme)
        personne.append(cacheFemme)

    #comment avoir les autres informations des parents ^^
    
        
    
#---------------------------------------------------------------#acte#---------------------------------------------------
    acte = []
    for ligne in lecteur_csv:
        # Accéder aux données de chaque colonne de la ligne
        cache = []
        for i in range(len(ligne)):
            for j in range(5):
                cache.append(ligne[j])
        acte.append(cache)




# Fermer la connexion
conn.close()