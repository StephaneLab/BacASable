#!/usr/bin/python3.9
# Licence BSD copyright (c) 2022 Stéphane Lassalvy
#
# Fonction : my_triangleDePascal
# Calcule la N-ème ligne du triangle de Pascal
#
# Paramètre d'entrée :
# N : numéro de la ligne du triangle de Pascal à  Calculer
#
# Sortie :
# resultat : N-ème ligne du triangle de Pascal ou N est le parametre d'entrée
#
def my_TriangleDePascal(N):
    if N == 0:
        resultat = []
        print("Ligne 0, pas de résultat.")
    else:
        if N == 1:
            resultat = [1]
            print(f"Ligne {1}  : {resultat}")
        else:
            if N == 2:
                resultat = [1,1]
                print(f"Ligne {1}  : {[1]}")
                print(f"Ligne {2}  : {[1,1]}")
            else:
                if N > 2:
                    print("N > 2")
                    print(f"ligne {1}  : {[1]}")
                    print(f"ligne {2}  : {[1,1]}")
                    precedent = [1,1]
                    for n in range(3, N+1):
                        resultat = [1]
                        for i in range(1, len(precedent)):
                            resultat = resultat + [precedent[i-1] + precedent[i]]
                        resultat = resultat + [1]
                        precedent= resultat.copy()
                        print(f"ligne {i+2}  : {precedent}")
    return resultat
