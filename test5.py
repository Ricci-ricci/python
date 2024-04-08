def table_verite_forme_canonique(expression_logique):
    # Extraction des variables de l'expression logique
    variables = set([char for char in expression_logique if char.isupper()])
    
    # Génération de toutes les combinaisons possibles de valeurs binaires pour les variables
    combinaisons = [[int(bit) for bit in format(i, '#0{}b'.format(len(variables)+2))[2:]] for i in range(2**len(variables))]
    
    # Évaluation de l'expression logique pour chaque combinaison de valeurs binaires
    resultats = [eval(expression_logique) for combinaison in combinaisons]
    
    # Affichage de la table de vérité
    print("Table de vérité :")
    print(" | ".join([var for var in variables]) + " | Résultat")
    print("-" * (len(variables) * 4 + 7))
    for i, combinaison in enumerate(combinaisons):
        print(" | ".join([str(bit) for bit in combinaison]) + " | " + str(resultats[i]))
    
    # Calcul de la première forme canonique (forme disjonctive normale)
    premiere_forme = " + ".join(["&".join([var if bit else ""+var for var, bit in zip(variables, combinaison)]) for combinaison, resultat in zip(combinaisons, resultats) if resultat])
    
    # Calcul de la deuxième forme canonique (forme conjonctive normale)
    deuxieme_forme = " + ".join(["&".join([""+var if bit else var for var, bit in zip(variables, combinaison)]) for combinaison, resultat in zip(combinaisons, resultats) if not resultat])
    
    # Affichage des formes canoniques
    print("\nPremière forme canonique :", premiere_forme)
    print("Deuxième forme canonique :", deuxieme_forme)

# Exemple d'utilisation
expression_logique = input("Entrez l'expression logique : ")
table_verite_forme_canonique(expression_logique)

