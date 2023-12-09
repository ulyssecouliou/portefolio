import platform
import os


joueur = 0


damier = [
    [" ", "n", " ", "n", " ", "n", " ", "n", " ", "n"],
    ["n", " ", "n", " ", "n", " ", "n", " ", "n", " "],
    [" ", "n", " ", "n", " ", "n", " ", "n", " ", "n"],
    ["n", " ", "n", " ", "n", " ", "n", " ", "n", " "],
    [" ", "*", " ", "*", " ", "*", " ", "*", " ", "*"],
    ["*", " ", "*", " ", "*", " ", "*", " ", "*", " "],
    [" ", "b", " ", "b", " ", "b", " ", "b", " ", "b"],
    ["b", " ", "b", " ", "b", " ", "b", " ", "b", " "],
    [" ", "b", " ", "b", " ", "b", " ", "b", " ", "b"],
    ["b", " ", "b", " ", "b", " ", "b", " ", "b", " "],
]


case_noir = [
    [0, 1],
    [0, 3],
    [0, 5],
    [0, 7],
    [0, 9],
    [1, 0],
    [1, 2],
    [1, 4],
    [1, 6],
    [1, 8],
    [2, 1],
    [2, 3],
    [2, 5],
    [2, 7],
    [2, 9],
    [3, 0],
    [3, 2],
    [3, 4],
    [3, 6],
    [3, 8],
    [4, 1],
    [4, 3],
    [4, 5],
    [4, 7],
    [4, 9],
    [5, 0],
    [5, 2],
    [5, 4],
    [5, 6],
    [5, 8],
    [6, 1],
    [6, 3],
    [6, 5],
    [6, 7],
    [6, 9],
    [7, 0],
    [7, 2],
    [7, 4],
    [7, 6],
    [7, 8],
    [8, 1],
    [8, 3],
    [8, 5],
    [8, 7],
    [8, 9],
    [9, 0],
    [9, 2],
    [9, 4],
    [9, 6],
    [9, 8],
]


def clean():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")


def stopper_jeu():
    if (pion_noir == []) or (pion_blanc == []):
        if pion_noir == []:
            print("Les Blancs ont gagnés !!!!")
        else:
            print("Les Noirs ont gagnés !!!!")
        return True
    elif tab_bouger == []:
        if tab_manger == []:
            if joueur == 0:
                print("Les Blancs ont gagnés car les noirs l'ont bloqué !!!!")
            else:
                print("Les Noirs ont gagnés car les blancs l'ont bloqué !!!!")
            return True
        else:
            return False

    else:
        return False


def joueur_suivant():
    global joueur

    if joueur == 0:
        joueur = 1  #   COULEUR = Noir

    else:
        joueur = 0  #   Couleur = Blanc


def coul_equipe(couleur):
    if couleur == 0:
        return "B"

    else:
        return "N"


def reset_var():
    # La variable joueur est localisé dans la fonction "joueur_suivant"
    global pion_noir
    global pion_blanc
    global tab_manger
    global tab_bouger
    global pion_mangeur
    global pion_jouable
    global dame_blanc
    global dame_noir

    (
        dame_blanc,
        dame_noir,
        pion_noir,
        pion_blanc,
        pion_jouable,
        pion_mangeur,
        tab_bouger,
        tab_manger,
    ) = ([], [], [], [], [], [], [], [])


def coul_adverse(couleur):
    if couleur == 0:
        return "N"

    else:
        return "B"


def afficher_couleur():
    if joueur == 0:
        return "\n     Le joueur Blanc joue\n\n"

    else:
        return "\n     Le joueur Noir joue\n\n"


def afficherDamier():
    x = 0
    print(
        afficher_couleur(),
        " ",
        "  ",
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "    ",
    )
    print(" ", " ", "_____________________")
    for case in damier:
        print(
            x,
            " |",
            case[0],
            case[1],
            case[2],
            case[3],
            case[4],
            case[5],
            case[6],
            case[7],
            case[8],
            case[9],
            " |",
        )
        x = x + 1
    print(" ", " ", "_____________________")


def coord_pion():
    for i in range(len(damier)):
        for j in range(len(damier[i])):
            if damier[i][j].upper() == "N":
                pion_noir.append([i, j])

                if damier[i][j] == "N":
                    dame_noir.append([i, j])

            if damier[i][j].upper() == "B":
                pion_blanc.append([i, j])

                if damier[i][j] == "B":
                    dame_blanc.append([i, j])

    return [pion_blanc, pion_noir]


def deplacer_pion(case):
    tab_bouger = []

    if joueur == 0:
        if ([case[0] - 1, case[1] - 1] in case_noir) and (
            damier[case[0] - 1][case[1] - 1] == "*"
        ):
            tab_bouger.append([case[0] - 1, case[1] - 1])

        if ([case[0] - 1, case[1] + 1] in case_noir) and (
            damier[case[0] - 1][case[1] + 1] == "*"
        ):
            tab_bouger.append([case[0] - 1, case[1] + 1])

    else:
        if ([case[0] + 1, case[1] + 1] in case_noir) and (
            damier[case[0] + 1][case[1] + 1] == "*"
        ):
            tab_bouger.append([case[0] + 1, case[1] + 1])

        if ([case[0] + 1, case[1] - 1] in case_noir) and (
            damier[case[0] + 1][case[1] - 1] == "*"
        ):
            tab_bouger.append([case[0] + 1, case[1] - 1])

    return tab_bouger


def manger_pion(case, joueur):
    tab_manger = []

    if ([case[0] - 2, case[1] + 2] in case_noir) and (
        damier[case[0] - 2][case[1] + 2] == "*"
    ):
        if damier[case[0] - 1][case[1] + 1].upper() == coul_adverse(joueur):
            tab_manger.append([case[0] - 2, case[1] + 2])

    if ([case[0] - 2, case[1] - 2] in case_noir) and (
        damier[case[0] - 2][case[1] - 2] == "*"
    ):
        if damier[case[0] - 1][case[1] - 1].upper() == coul_adverse(joueur):
            tab_manger.append([case[0] - 2, case[1] - 2])

    if ([case[0] + 2, case[1] + 2] in case_noir) and (
        damier[case[0] + 2][case[1] + 2] == "*"
    ):
        if damier[case[0] + 1][case[1] + 1].upper() == coul_adverse(joueur):
            tab_manger.append([case[0] + 2, case[1] + 2])

    if ([case[0] + 2, case[1] - 2] in case_noir) and (
        damier[case[0] + 2][case[1] - 2] == "*"
    ):
        if damier[case[0] + 1][case[1] - 1].upper() == coul_adverse(joueur):
            tab_manger.append([case[0] + 2, case[1] - 2])

    return tab_manger


def manger_dame(case, joueur):
    i = 1

    while i < 10:
        if [case[0] + i, case[1] + i] in case_noir:
            if damier[case[0] + i][case[1] + i] == "*":
                tab_bouger.append([case[0] + i, case[1] + i])
                i = i + 1

            elif damier[case[0] + i][case[1] + i].upper() == coul_adverse(joueur):
                if ([case[0] + i + 1, case[1] + i + 1] in case_noir) and (
                    damier[case[0] + i + 1][case[1] + i + 1] == "*"
                ):
                    while ([case[0] + i + 1, case[1] + i + 1] in case_noir) and (
                        damier[case[0] + i + 1][case[1] + i + 1] == "*"
                    ):
                        tab_manger.append([case[0] + i + 1, case[1] + i + 1])
                        i = i + 1
                    break

                else:
                    break

            elif damier[case[0] + i][case[1] + i].upper() == coul_equipe(joueur):
                break
        else:
            break

    i = 1

    while i < 10:
        if [case[0] - i, case[1] - i] in case_noir:
            if damier[case[0] - i][case[1] - i] == "*":
                tab_bouger.append([case[0] - i, case[1] - i])
                i = i + 1

            elif damier[case[0] - i][case[1] - i].upper() == coul_adverse(joueur):
                if ([case[0] - i - 1, case[1] - i - 1] in case_noir) and (
                    damier[case[0] - i - 1][case[1] - i - 1] == "*"
                ):
                    while ([case[0] - i - 1, case[1] - i - 1] in case_noir) and (
                        damier[case[0] - i - 1][case[1] - i - 1] == "*"
                    ):
                        tab_manger.append([case[0] - i - 1, case[1] - i - 1])
                        i = i + 1
                    break

                else:
                    break

            elif damier[case[0] - i][case[1] - i].upper() == coul_equipe(joueur):
                break
        else:
            break

    i = 1

    while i < 10:
        if [case[0] + i, case[1] - i] in case_noir:
            if damier[case[0] + i][case[1] - i] == "*":
                tab_bouger.append([case[0] + i, case[1] - i])
                i = i + 1

            elif damier[case[0] + i][case[1] - i].upper() == coul_adverse(joueur):
                if ([case[0] + i + 1, case[1] - i - 1] in case_noir) and (
                    damier[case[0] + i + 1][case[1] - i - 1] == "*"
                ):
                    while ([case[0] + i + 1, case[1] - i - 1] in case_noir) and (
                        damier[case[0] + i + 1][case[1] - i - 1] == "*"
                    ):
                        tab_manger.append([case[0] + i + 1, case[1] - i - 1])
                        i = i + 1
                    break

                else:
                    break

            elif damier[case[0] + i][case[1] - i].upper() == coul_equipe(joueur):
                break
        else:
            break
    i = 1

    while i < 10:
        if [case[0] - i, case[1] + i] in case_noir:
            if damier[case[0] - i][case[1] + i] == "*":
                tab_bouger.append([case[0] - i, case[1] + i])
                i = i + 1

            elif damier[case[0] - i][case[1] + i].upper() == coul_adverse(joueur):
                if ([case[0] - i - 1, case[1] + i + 1] in case_noir) and (
                    damier[case[0] - i - 1][case[1] + i + 1] == "*"
                ):
                    while ([case[0] - i - 1, case[1] + i + 1] in case_noir) and (
                        damier[case[0] - i - 1][case[1] + i + 1] == "*"
                    ):
                        tab_manger.append([case[0] - i - 1, case[1] + i + 1])
                        i = i + 1

                    break
                else:
                    break

            elif damier[case[0] - i][case[1] + i].upper() == coul_equipe(joueur):
                break
        else:
            break

    return [tab_bouger, tab_manger]


def calcule():
    if joueur == 0:
        for case in pion_blanc:
            if case in dame_blanc:
                if manger_dame(case, joueur)[1] != []:
                    tab_manger.append(manger_dame(case, joueur)[1])
                    pion_mangeur.append(case)

                elif (manger_dame(case, joueur)[0]) != []:
                    tab_bouger.append(manger_dame(case, joueur)[0])
                    pion_jouable.append(case)

            else:
                if manger_pion(case, joueur) != []:
                    tab_manger.append(manger_pion(case, joueur))
                    pion_mangeur.append(case)

                elif deplacer_pion(case) != []:
                    tab_bouger.append(deplacer_pion(case))
                    pion_jouable.append(case)

    else:
        for case in pion_noir:
            if case in dame_noir:
                if manger_dame(case, joueur)[1] != []:
                    tab_manger.append(manger_dame(case, joueur)[1])
                    pion_mangeur.append(case)

                elif (manger_dame(case, joueur)[0]) != []:
                    tab_bouger.append(manger_dame(case, joueur)[0])
                    pion_jouable.append(case)

            else:
                if manger_pion(case, joueur) != []:
                    tab_manger.append(manger_pion(case, joueur))
                    pion_mangeur.append(case)

                elif deplacer_pion(case) != []:
                    tab_bouger.append(deplacer_pion(case))
                    pion_jouable.append(case)

    return tab_bouger, tab_manger, pion_jouable, pion_mangeur


def casesurdamier(depart):
    if depart in case_noir:
        return True

    else:
        return False


def possibilite_de_jouer(depart, joueur):
    if (depart in dame_blanc) or (depart in dame_noir):
        bouger, manger = manger_dame(depart, joueur)
    else:
        bouger = deplacer_pion(depart)
        manger = manger_pion(depart, joueur)

    if (manger == []) and (bouger == []):
        return False

    return True


def bonne_equipe(depart):
    cond_depart = True
    tabPionsBlanc = coord_pion()[0]
    tabPionsNoir = coord_pion()[1]

    if joueur == 0:
        if depart not in tabPionsBlanc:
            cond_depart = False

    elif depart not in tabPionsNoir:
        cond_depart = False

    return cond_depart


def supr_pion(damier, depart, arrive):
    i = 1

    if (depart not in dame_noir) and (depart not in dame_blanc):
        if [arrive[0] - 1, arrive[1] + 1] == [depart[0] + 1, depart[1] - 1]:
            damier[depart[0] + 1][depart[1] - 1] = "*"

        elif [arrive[0] + 1, arrive[1] - 1] == [depart[0] - 1, depart[1] + 1]:
            damier[depart[0] - 1][depart[1] + 1] = "*"

        elif [arrive[0] - 1, arrive[1] - 1] == [depart[0] + 1, depart[1] + 1]:
            damier[depart[0] + 1][depart[1] + 1] = "*"

        elif [arrive[0] + 1, arrive[1] + 1] == [depart[0] - 1, depart[1] - 1]:
            damier[depart[0] - 1][depart[1] - 1] = "*"
    else:
        while i < 10:
            if [depart[0] + i, depart[1] + i] == arrive:
                j = 1
                while [depart[0] + j, depart[1] + j] in case_noir:
                    if damier[depart[0] + j][depart[1] + j].upper() == coul_adverse(
                        joueur
                    ):
                        damier[depart[0] + j][depart[1] + j] = "*"
                        break
                    else:
                        j = j + 1
                break
            if [depart[0] - i, depart[1] - i] == arrive:
                j = 1
                while (j < 10) and ([depart[0] - j, depart[1] - j] in case_noir):
                    if damier[depart[0] - j][depart[1] - j].upper() == coul_adverse(
                        joueur
                    ):
                        damier[depart[0] - j][depart[1] - j] = "*"
                        break
                    else:
                        j = j + 1
                break
            if [depart[0] - i, depart[1] + i] == arrive:
                j = 1
                while (j < 10) and ([depart[0] - j, depart[1] + j] in case_noir):
                    if damier[depart[0] - j][depart[1] + j].upper() == coul_adverse(
                        joueur
                    ):
                        damier[depart[0] - j][depart[1] + j] = "*"
                        break
                    else:
                        j = j + 1
                break
            if [depart[0] + i, depart[1] - i] == arrive:
                j = 1
                while (j < 10) and ([depart[0] + j, depart[1] - j] in case_noir):
                    if damier[depart[0] + j][depart[1] - j].upper() == coul_adverse(
                        joueur
                    ):
                        damier[depart[0] + j][depart[1] - j] = "*"
                        break
                    else:
                        j = j + 1
                break

            i = i + 1


def jouer_coup(damier, depart, arrive):
    damier[arrive[0]][arrive[1]] = damier[depart[0]][depart[1]]

    damier[depart[0]][depart[1]] = "*"

    cree_dame()


def cree_dame():
    if joueur == 0:
        for j in range(len(damier[0])):
            if damier[0][j] == "b":
                damier[0][j] = "B"
                dame_blanc.append([0, j])

            if damier[9][j] == "n":
                damier[9][j] = "N"
                dame_noir.append([9, j])

    return [dame_blanc, dame_noir]


def prio_manger():
    if tab_manger != []:
        print("Vos possibilités : ", tab_manger)

    else:
        print("Vos possibilités : ", tab_bouger)
    print("\nSélectionner l'arrivée")


def demander_arrive():
    global arrive

    while arrive not in tab_manger:
        clean()
        afficherDamier()
        print("Vos possibilités : ", tab_manger)

        arrive = [input(), input()]

        while entier(arrive) == False:
            clean()
            afficherDamier()
            print("Vos possibilités : ", tab_manger)
            arrive = [input(), input()]

        arrive = [int(arrive[0]), int(arrive[1])]
    return arrive


def entier(coord):
    try:
        coord = [int(coord[0]), int(coord[1])]
        return coord

    except ValueError:
        return False


while True:
    os.system("cls" if os.name == "nt" else "clear")
    reset_var()
    cree_dame()
    arrive, depart = [], []
    coord_pion()
    calcule()
    if stopper_jeu():
        break
    afficherDamier()

    if pion_mangeur != []:
        pion_jouable = pion_mangeur

    print("\nVos pions jouables sont : ", pion_jouable)
    print("\nSélectionner un pion")

    depart = [input(), input()]

    while entier(depart) == False:
        clean()
        afficherDamier()
        print("\nVos pions jouables sont : ", pion_jouable)
        print("\nSélectionner un pion")
        depart = [input(), input()]

    depart = [int(depart[0]), int(depart[1])]

    while (
        (casesurdamier(depart) == False)
        or (bonne_equipe(depart) == False)
        or (possibilite_de_jouer(depart, joueur) == False)
        or (depart not in pion_jouable)
    ):
        clean()
        afficherDamier()
        print("\nVos pions jouables sont : ", pion_jouable)
        print("\nSélectionner un pion")
        depart = [input(), input()]

        while entier(depart) == False:
            clean()
            afficherDamier()
            print("\nVos pions jouables sont : ", pion_jouable)
            print("\nSélectionner un pion")
            depart = [input(), input()]

        depart = [int(depart[0]), int(depart[1])]

    clean()
    afficherDamier()

    tab_manger = []
    tab_bouger = []

    if (depart in dame_blanc) or (
        depart in dame_noir
    ):  # Verifie que la nature du pion (Dame ou pion)
        tab_bouger, tab_manger = manger_dame(depart, joueur)
    else:
        tab_manger = manger_pion(depart, joueur)
        tab_bouger = deplacer_pion(depart)

    prio_manger()

    arrive = [input(), input()]

    while entier(arrive) == False:
        clean()
        afficherDamier()
        prio_manger()
        arrive = [input(), input()]

    arrive = [int(arrive[0]), int(arrive[1])]

    if tab_manger != []:  # Si le joueur peut manger
        demander_arrive()
        supr_pion(damier, depart, arrive)
        jouer_coup(damier, depart, arrive)
        clean()
        afficherDamier()
        reset_var()
        coord_pion()

        if (arrive in dame_blanc) or (arrive in dame_noir):
            tab_bouger, tab_manger = manger_dame(arrive, joueur)
        else:
            tab_manger = manger_pion(arrive, joueur)

        while (
            tab_manger != []
        ):  # Redemande une case d'arrivée jusqu'à ce que le pion joueur ne puisse plus manger de pion adversse
            clean()
            afficherDamier()
            print("Vos possibilités : ", tab_manger)
            depart = arrive

            arrive = [input(), input()]

            while entier(arrive) == False:
                clean()
                afficherDamier()
                print("Vos possibilités : ", tab_manger)
                arrive = [input(), input()]

            arrive = [int(arrive[0]), int(arrive[1])]

            demander_arrive()
            supr_pion(damier, depart, arrive)
            jouer_coup(damier, depart, arrive)
            afficherDamier()
            reset_var()
            coord_pion()
            clean()

            if (arrive in dame_blanc) or (arrive in dame_noir):
                tab_bouger, tab_manger = manger_dame(arrive, joueur)
            else:
                tab_manger = manger_pion(arrive, joueur)

    elif (
        tab_bouger != []
    ):  # Si le joueur ne peut pas manger, on demande une case d'arrivée pour déplacement
        while arrive not in tab_bouger:
            clean()
            afficherDamier()
            print("Vos possibilités sont : ", tab_bouger)
            arrive = [input(), input()]

            while entier(arrive) == False:
                clean()
                afficherDamier()
                print("Vos possibilités sont : ", tab_bouger)
                arrive = [input(), input()]
            arrive = [int(arrive[0]), int(arrive[1])]
        jouer_coup(damier, depart, arrive)

    clean()
    joueur_suivant()


print("Fin du jeu")
