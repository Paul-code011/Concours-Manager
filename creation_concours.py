import os
import json


def charger_concours(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {"concours": []}


def sauvegarder_concours(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def creer_concours():
    num_concours = input("Numéro du concours : ")
    nom_concours = input("Nom du concours : ")
    date_concours = input("Date du concours (YYYY-MM-DD) : ")
    lieu_concours = input("Lieu du concours : ")
    organisateur = input("Organisateur : ")
    description = input("Description : ")
    # Catégories
    categories = []
    nb_categories = int(input("Combien de catégories ? "))
    for i in range(nb_categories):
        print(f"Catégorie {i+1} :")
        nom_categorie = input("  Nom de la catégorie : ")
        difficulte = input("  Difficulté : ")
        categories.append({"nom_catégorie": nom_categorie, "difficulté": difficulte})
    # Prix
    prix = []
    nb_prix = int(input("Combien de prix ? "))
    for i in range(nb_prix):
        print(f"Prix {i+1} :")
        type_prix = input("  Type de prix : ")
        while True:
            valeur_str = input("  Valeur du prix : ")
            try:
                valeur_prix = int(valeur_str)
                break
            except ValueError:
                print("  ➔ Veuillez entrer un nombre entier valide.")
        prix.append({"type_prix": type_prix, "valeur_prix": valeur_prix})
    return {
        "numéro_concours": num_concours,
        "nom_concours": nom_concours,
        "date_concours": date_concours,
        "lieu_concours": lieu_concours,
        "organisateur": organisateur,
        "description": description,
        "catégories": categories,
        "prix": prix,
    }


def afficher_concours(concours):
    for c in concours["concours"]:
        print(f"\nConcours n°{c['numéro_concours']} : {c['nom_concours']}")
        print(f"  Date : {c['date_concours']} | Lieu : {c['lieu_concours']}")
        print(f"  Organisateur : {c['organisateur']}")
        print(f"  Description : {c['description']}")
        print("  Catégories :")
        for cat in c["catégories"]:
            print(f"    - {cat['nom_catégorie']} (Difficulté : {cat['difficulté']})")
        print("  Prix :")
        for p in c["prix"]:
            print(f"    - {p['type_prix']} : {p['valeur_prix']}€")


# --- Programme principal ---
FICHIER = "bsd_concours.json"

while True:
    print("\nQue voulez-vous faire ?")
    print("1. Créer un concours")
    print("2. Gérer vos concours (afficher)")
    print("3. Quitter")
    reponse = input("Entrez votre réponse : ")
    if reponse == "1":
        data = charger_concours(FICHIER)
        nouveau = creer_concours()
        data["concours"].append(nouveau)
        sauvegarder_concours(FICHIER, data)
        print("✅ Concours ajouté avec succès !")
    elif reponse == "2":
        data = charger_concours(FICHIER)
        afficher_concours(data)
    elif reponse == "3":
        print("Au revoir !")
        break
    else:
        print("Choix invalide.")
