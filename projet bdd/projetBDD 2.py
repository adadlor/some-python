import csv

def trier_csv_par_colonne(fichier_entree, fichier_sortie, colonne):
    # Lecture des données CSV
    with open(fichier_entree, 'r', newline='') as csvfile:
        lecteur_csv = csv.reader(csvfile)
        entetes = next(lecteur_csv)  # Ignorer la première ligne (entêtes)
        lignes = list(lecteur_csv)    # Lire les lignes restantes

    # Tri des lignes en utilisant la fonction lambda pour sélectionner la colonne spécifiée
    lignes_triees = sorted(lignes, key=lambda x: x[colonne] )

    # Écriture des données triées dans un nouveau fichier CSV
    with open(fichier_sortie, 'w', newline='') as csvfile:
        ecrivain_csv = csv.writer(csvfile)
        ecrivain_csv.writerow(entetes)  # Écriture des entêtes
        ecrivain_csv.writerows(lignes_triees)  # Écriture des lignes triées


# Fonction pour lire le fichier CSV et générer les instructions SQL
def csv_to_sql(csv_file):
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header

        # Générer les instructions SQL
        create_table_commune = """
        DROP table commune CASCADE;
        DROP table personne CASCADE;
        DROP table acte CASCADE;
            CREATE TABLE Commune (
                id SERIAL PRIMARY KEY,
                nom VARCHAR,
                departement VARCHAR
            );
        """

        create_table_personne = """
            CREATE TABLE Personne (
                id SERIAL PRIMARY KEY,
                nom VARCHAR,
                prenom VARCHAR,
                parent1_id INTEGER,
                parent2_id INTEGER,
                FOREIGN KEY (parent1_id) REFERENCES Personne(id),
                FOREIGN KEY (parent2_id) REFERENCES Personne(id)
            );
        """

        create_table_acte = """
        SET datestyle = 'European';
            CREATE TABLE Acte (
                id SERIAL PRIMARY KEY,
                id_acte VARCHAR,
                type_acte VARCHAR,
                personne1_id INTEGER,
                personne2_id INTEGER,
                commune_id INTEGER,
                date VARCHAR,
                num_vue VARCHAR,
                FOREIGN KEY (personne1_id) REFERENCES Personne(id),
                FOREIGN KEY (personne2_id) REFERENCES Personne(id),
                FOREIGN KEY (commune_id) REFERENCES Commune(id)
            );
        """

        communes = set()
        personnes = set()
        actes = set()  

        # Générer les données
        for row in reader:

             # Communes
            commune = (row[12].replace("'", " "), row[13].replace("'", " "))
            if commune not in communes:
                communes.add(commune)
                # Personnes
            A = (row[2].replace("'", " "), row[3].replace("'", " "), row[4].replace("'", " "), row[5].replace("'", " "), row[6].replace("'", " "), row[14])
            B = (row[7].replace("'", " "), row[8].replace("'", " "), row[9].replace("'", " "), row[10].replace("'", " "), row[11].replace("'", " "), row[14])
    
            if A not in personnes:
                personnes.add(A)
            if B not in personnes:
                personnes.add(B)


            # Actes
            acte = (row[0].replace("'", " "), row[1].replace("'", " "), row[2].replace("'", " "), row[3].replace("'", " "), row[14].replace("'", " "), row[15].replace("'", " "), row[12].replace("'", " "), row[13].replace("'", " "))
            actes.add(acte)

           

        insert_communes = "INSERT INTO Commune (nom, departement) VALUES\n"
        insert_communes += ',\n'.join([f"('{c[0]}', '{c[1]}')" for c in communes])
        insert_communes += ';'

        insert_personnes = "INSERT INTO Personne (nom, prenom, parent1_id, parent2_id) VALUES\n"
        insert_personnes += ',\n'.join([f"('{p[0]}', '{p[1]}', (SELECT id FROM Personne WHERE nom='{p[0]}' AND prenom='{p[2]}' LIMIT 1), (SELECT id FROM Personne WHERE nom='{p[3]}' AND prenom='{p[4]}' LIMIT 1))" for p in personnes])
        insert_personnes += ';'

        insert_personnesV2 = ""
        for p in personnes:
            insert_personnesV2 += "INSERT INTO Personne (nom, prenom, parent1_id, parent2_id) VALUES "
            insert_personnesV2 += "('" + p[0] + "','"+p[1]+ "', (SELECT id FROM Personne WHERE nom='" + p[0] + "' AND prenom='" + p[2] + "' LIMIT 1), (SELECT id FROM Personne WHERE nom='" + p[3] + "' AND prenom='" + p[4] + "' LIMIT 1))"
            insert_personnesV2 += ";\n"

        insert_actes = "INSERT INTO Acte (id_acte, type_acte, date, num_vue, personne1_id, personne2_id, commune_id) VALUES\n"
        insert_actes += ',\n'.join([f"('{a[0]}', '{a[1]}'," + ('NULL' if a[4] == 'n/a' else f"'{a[4]}'") + f", '{a[3]}', (SELECT id FROM Personne WHERE nom='{a[4]}' AND prenom='{a[5]}' LIMIT 1), (SELECT id FROM Personne WHERE nom='{a[6]}' AND prenom='{a[7]}' LIMIT 1), (SELECT id FROM Commune WHERE nom='{a[6]}' AND departement='{a[7]}' LIMIT 1))" for a in actes])
        insert_actes += ';'


        

        return f"{create_table_commune}\n{create_table_personne}\n{create_table_acte}\n{insert_communes}\n{insert_personnesV2}\n{insert_actes}"

def main():
    input_csv = 'mariages/mariages_L3_5k.csv'
    output_sql = 'output.sql'

    trier_csv_par_colonne(input_csv, "mariage.csv", 14)

    sql = csv_to_sql('mariage.csv')

    with open(output_sql, 'w', encoding='utf-8') as sql_file:
        sql_file.write(sql)

if __name__ == "__main__":
    main()