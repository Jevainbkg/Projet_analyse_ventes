# Import des librairy necessaire
import utils
import csv
import sys
from pathlib import Path

# Lecture des data

base_dir = Path(__file__).parent
link = base_dir / "data" / "ventes.csv"

with open(link, mode="r", encoding="utf-8") as file:
    data = file.read().splitlines()

data = csv.reader(data)
en_tete = next(data)
data = list(data)


message_input = f"""\n1. Voir toutes les ventes\n
2. Voir le chiffre d'affaires total\n
3. Voir les ventes par ville\n
4. Voir les ventes par catégorie\n
5. Générer un rapport\n
6. Quitter\n 
Votre choix : """

while True:  # Permet d'executer le programme en continue
    user_choice = input(message_input)  # Choix effectué par l'utilisateur

    match user_choice:
        case "1":
            utils.Show_all(data)
        case "2":
            print(
                f"Le chiffre d'affaire total est de {utils.Chiffre_affaire_total(data)}"
            )
        case "3":
            utils.Ventes_par_ville(data)
        case "4":
            utils.Ventes_par_categorie(data)
        case "5":
            utils.Generer_rapport(data)
        case _:

            sys.exit("Au revoir")

# Fin du programme
