
def table_verite_forme_canonique(expression_logique):
    from itertools import product

    # Fonction pour évaluer l'expression logique
    def eval_expr(expr, vals):
        expr = expr.replace('AND', '&').replace('OR', '|').replace('NOT', '~')
        for var, val in vals.items():
            expr = expr.replace(var, str(val))
        return eval(expr)

    variables = set([char for char in expression_logique if char.isupper()])

    # Créer la liste de toutes les combinaisons possibles des variables
    combinaisons = list(product([0, 1], repeat=len(variables)))

    # Afficher la table de vérité
    print("Table de vérité :")
    print(" | ".join([var for var in variables]) + " | Résultat")
    print("-" * (len(variables) * 4 + 7))

    for combinaison in combinaisons:
        vals = {var: val for var, val in zip(variables, combinaison)}
        resultat = eval_expr(expression_logique, vals)
        print(" | ".join([str(val) for val in combinaison]) + " | " + str(resultat))

    # Calculer la première forme canonique
    premiere_forme = " + ".join(["(" + " & ".join(["NOT " + var if not bit else var for var, bit in zip(variables, combinaison)]) + ")" for combinaison in combinaisons if eval_expr(expression_logique, {var: bit for var, bit in zip(variables, combinaison)})])

    # Calculer la deuxième forme canonique
    deuxieme_forme = " | ".join(["(" + " | ".join(["NOT " + var if not bit else var for var, bit in zip(variables, combinaison)]) + ")" for combinaison in combinaisons if not eval_expr(expression_logique, {var: bit for var, bit in zip(variables, combinaison)})])

    # Afficher les formes canoniques
    print("\nPremière forme canonique :", premiere_forme)
    print("Deuxième forme canonique :", deuxieme_forme)

# Exemple d'utilisation
expression_logique = input("Entrez l'expression logique : ")
table_verite_forme_canonique(expression_logique)
 

