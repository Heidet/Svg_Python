import os

# # cible test /Users/admin/Desktop/test

chemin = input("Veillez saisir la cible ou vous souhaitez placer le dossier de sauvegarde: ")

print(f"Vous avec selectionner la cible {chemin} ")

creation = os.path.join(chemin, "sauvegarde")

a = 'oui'
b = 'non'

print(f"a = {a}")
print(f"b = {b}")

reponse = input("Réponse: ")

if reponse == "a" and not os.path.exists(creation):## Si le dossier n'existe pas
    os.makedirs(creation) #on le créer
    ### ou = os.makedirs(dossier, exist_os=True)
    print(f"Le dossier {creation} a bien été créer à la cible {chemin}")

else:
    print(f"Attention {creation} existe déjà")

