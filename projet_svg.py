import os

# cible test /Users/admin/Desktop/test

chemin = input("Veillez saisir la cible ou vous souhaitez placer le dossier de sauvegarde: ")

#chemin = str(chemin)

#print(chemin)
creation = os.path.join(chemin, "sauvegarde")

if not os.path.exists(creation):## Si le dossier n'existe pas
    os.makedirs(creation) #on le créer
    ### ou = os.makedirs(dossier, exist_os=True)
    print(f"Le dossier {creation} a bien été créer à la cible {chemin}")

else:
    print(f"Attention {creation} existe déjà")

#os.makedirs(creation)

#print(creation)

#print(f"Vous avec selectionner la cible {cible}")

#a = 'oui'
#b = 'non'

#demande = input("Confirmer le choix ")

"""if demande2 == a:  ## Si le dossier n'existe pas
        os.makedirs(cible)

else:
    exit()"""



# os.mkdir peu avec 1 seule dossier

#os.removedirs(dossier) // supprimer dossier
