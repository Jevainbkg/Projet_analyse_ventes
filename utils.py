import datetime


def Show_all(data):
    for line in data:
        print(line)


def Chiffre_affaire_total(data):
    chiffre_affaire_total = 0
    for line in data:
        if float(line[3]) > 0 and float(line[4]) > 0:
            chiffre_affaire = float(line[3]) * float(line[4])
            chiffre_affaire_total += chiffre_affaire
        else:
            chiffre_affaire_total += 0

    return round(chiffre_affaire_total, 3)


def Ventes_par_ville(data):
    ventes_par_ville = {}

    for line in data:
        if line[-1] in ventes_par_ville:
            ventes_par_ville[line[-1]] += 1
        else:
            ventes_par_ville[line[-1]] = 1
    print(f"{ventes_par_ville}")


def Ventes_par_categorie(data):
    ventes_par_categorie = {}

    for line in data:
        if line[2] in ventes_par_categorie:
            ventes_par_categorie[line[2]] += 1
        else:
            ventes_par_categorie[line[2]] = 1
    print(f"{ventes_par_categorie}")


def Best_city(data):
    villes = {}
    best_city = {}
    for line in data:
        if line[-1] in villes:
            villes[line[-1]] += 1
        else:
            villes[line[-1]] = 1

    for city, sales in villes.items():
        if sales == max(villes.values()):
            best_city = {city: sales}

    return best_city


def Best_category(data):
    categories = {}
    best_category = {}
    for line in data:
        if line[2] in categories:
            categories[line[2]] += 1
        else:
            categories[line[2]] = 1

    for category, sales in categories.items():
        if sales == max(categories.values()):
            best_category = {category: sales}

    return best_category


def Top_products(data):
    products = {}
    for line in data:
        if line[1] in products:
            products[line[1]] += 1 * int(line[3])
        else:
            products[line[1]] = 1 * int(line[3])

    products_sorted = sorted(products.items(), key=lambda x: x[1], reverse=True)
    return products_sorted[:3]


def Normaliser_date(date):
    now_norm = str(date).split(".")
    now_norm = datetime.datetime.strptime(now_norm[0], "%Y-%m-%d %H:%M:%S")
    return now_norm


def Generer_rapport(data):
    # en_tete =  ["Date", "Chiffre d'affaire", "Best city", "Best category", "Top products"] # Pourrait servir en cas de generation de rapport au format csv

    date_rapport = Normaliser_date(datetime.datetime.now())
    total_sales = len(data)
    chiffre_affaire_total = Chiffre_affaire_total(data)
    best_city = Best_city(data)
    best_category = Best_category(data)
    top_produits = Top_products(data)

    rapport = f"""Date : {date_rapport}
            Chiffre d'affaire : {chiffre_affaire_total}
            Meilleure ville : {best_city}
            Meilleure categorie : {best_category}
            Top 3 produits : {top_produits}
            Total ventes : {total_sales}
        """
    path_rapport = f"D:\\JevainBkg\\Formations\\Python pour la DATA  le cours ULTIME (+52h)\\00. Exercices\\Python's_Project\\mini_analyse_ventes\\rapports\ Rapport-{date_rapport.strftime("%Y-%m-%d_%H-%M-%S")}.txt"
    with open(path_rapport, mode="w", encoding="utf-8") as file:
        file.writelines(rapport)
        print("Rapport généré avec succès")


def Len_rapport(data):
    return len(data)
