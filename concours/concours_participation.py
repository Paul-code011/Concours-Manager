import json

code_1 = ""
code_2 = ""
nom_utilisateur = ""


print("Bienvenue, tout d'abord, voici un petit rappel des règles du concours.")
print(
    "Vous devez acheter deux [nom du produit] de la marque [nom de la marque]. Un code est fourni sur l'étiquette collée sur le produit. Veuillez ensuite saisir ce code."
)
code_1 = input("Entrez votre code n°1 : ")
code_2 = input("Entrez votre code n°2 : ")

# Vérification des codes dans le fichier JSON
with open("bsd_code.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    codes_valides = set(data["codes"])

if code_1 in codes_valides and code_2 in codes_valides:
    print("Félicitations, vos deux codes sont valides !")
else:
    print("Erreur : au moins un des codes n'est pas valide.")
