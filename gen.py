import random

from data import list


def algo(bp,hp,hl,bl,hg,bg,cal):

    data = list()
    PetitDej = data['PetitDej']
    Juicepti = data['Juicepti']
    EntreDejDinner = data['EntreDejDinner']
    DejDinner = data['DejDinner']
    Fruits = data['Fruits']
    Dessert = data['Dessert']
    complementRepas = data['complementRepas']
    Collation = data['Collation']

    protdiet = 0
    gludiet = 0
    lipdiet = 0

    while protdiet < bp or protdiet > hp or lipdiet > hl or lipdiet < bl or gludiet > hg or gludiet < bg:
        dejeuner = random.choice(DejDinner)
        jus = random.choice(Juicepti)
        entre1 = random.choice(EntreDejDinner)
        complement1 = random.choice(complementRepas)
        entre2 = random.choice(EntreDejDinner)
        complement2 = random.choice(complementRepas)
        dessert1 = random.choice(Dessert)
        dessert2 = random.choice(Dessert)
        collation1 = random.choice(Collation)
        collation2 = random.choice(Collation)
        petitdej = random.choice(PetitDej)
        fruits1 = random.choice(Fruits)
        fruit2 = random.choice(Fruits)
        fruit3 = random.choice(Fruits)
        collation4 = collation1
        collation3 = collation2
        while collation1 == collation4 and collation2 == collation3:
            collation3 = random.choice(Collation)
            collation4 = random.choice(Collation)

        dinner = dejeuner
        while dinner == dejeuner:
            dinner = random.choice(DejDinner)
        if cal < 2600:
            diet = petitdej + dejeuner + collation1 + dinner + dessert2
        else:
            diet = petitdej + collation2 + dejeuner + collation1 + dinner + dessert2
        protdiet = 0
        gludiet = 0
        lipdiet = 0
        for i in range(0, len(diet)):
            protdiet = protdiet + diet[i][1]
            gludiet = gludiet + diet[i][2]
            lipdiet = lipdiet + diet[i][3]
        if protdiet < bp or lipdiet < bl or gludiet < bg and protdiet < hp and lipdiet < hl and gludiet < hg:
            dejeuner = dejeuner + entre1
        if cal < 2600:
            diet = petitdej + dejeuner + collation1 + dinner + dessert2
        else:
            diet = petitdej + collation2 + dejeuner + collation1 + dinner + dessert2
        protdiet = 0
        gludiet = 0
        lipdiet = 0
        for i in range(0, len(diet)):
            protdiet = protdiet + diet[i][1]
            gludiet = gludiet + diet[i][2]
            lipdiet = lipdiet + diet[i][3]
        if protdiet < bp or lipdiet < bl or gludiet < bg and protdiet < hp and lipdiet < hl and gludiet < hg:
            dejeuner = dejeuner + complement1
        if cal < 2600:
            diet = petitdej + dejeuner + collation1 + dinner + dessert2
        else:
            diet = petitdej + collation2 + dejeuner + collation1 + dinner + dessert2
        protdiet = 0
        gludiet = 0
        lipdiet = 0
        for i in range(0, len(diet)):
            protdiet = protdiet + diet[i][1]
            gludiet = gludiet + diet[i][2]
            lipdiet = lipdiet + diet[i][3]
        if protdiet < bp or lipdiet < bl or gludiet < bg and protdiet < hp and lipdiet < hl and gludiet < hg:
            dejeuner = dejeuner + fruit2
        if cal < 2600:
            diet = petitdej + dejeuner + collation1 + dinner + dessert2
        else:
            diet = petitdej + collation2 + dejeuner + collation1 + dinner + dessert2
        protdiet = 0
        gludiet = 0
        lipdiet = 0
        for i in range(0, len(diet)):
            protdiet = protdiet + diet[i][1]
            gludiet = gludiet + diet[i][2]
            lipdiet = lipdiet + diet[i][3]
        if protdiet < bp or lipdiet < bl or gludiet < bg and protdiet < hp and lipdiet < hl and gludiet < hg and random.randint(
                1, 3) == 1:
            petitdej = petitdej + jus
        if cal < 2600:
            diet = petitdej + dejeuner + collation1 + dinner + dessert2
        else:
            diet = petitdej + collation2 + dejeuner + collation1 + dinner + dessert2
        protdiet = 0
        gludiet = 0
        lipdiet = 0
        for i in range(0, len(diet)):
            protdiet = protdiet + diet[i][1]
            gludiet = gludiet + diet[i][2]
            lipdiet = lipdiet + diet[i][3]
        if protdiet < bp or lipdiet < bl or gludiet < bg and protdiet < hp and lipdiet < hl and gludiet < hg:
            petitdej = petitdej + fruits1
        if cal < 2600:
            diet = petitdej + dejeuner + collation1 + dinner + dessert2
        else:
            diet = petitdej + collation2 + dejeuner + collation1 + dinner + dessert2
        protdiet = 0
        gludiet = 0
        lipdiet = 0
        for i in range(0, len(diet)):
            protdiet = protdiet + diet[i][1]
            gludiet = gludiet + diet[i][2]
            lipdiet = lipdiet + diet[i][3]
        if protdiet < bp or lipdiet < bl or gludiet < bg and protdiet < hp and lipdiet < hl and gludiet < hg:
            collation1 = collation1 + collation4
        if cal < 2600:
            diet = petitdej + dejeuner + collation1 + dinner + dessert2
        else:
            diet = petitdej + collation2 + dejeuner + collation1 + dinner + dessert2
        protdiet = 0
        gludiet = 0
        lipdiet = 0
        for i in range(0, len(diet)):
            protdiet = protdiet + diet[i][1]
            gludiet = gludiet + diet[i][2]
            lipdiet = lipdiet + diet[i][3]
        if protdiet < bp or lipdiet < bl or gludiet < bg and protdiet < hp and lipdiet < hl and gludiet < hg:
            dinner = dinner + entre2
        if cal < 2600:
            diet = petitdej + dejeuner + collation1 + dinner + dessert2
        else:
            diet = petitdej + collation2 + dejeuner + collation1 + dinner + dessert2
        protdiet = 0
        gludiet = 0
        lipdiet = 0
        for i in range(0, len(diet)):
            protdiet = protdiet + diet[i][1]
            gludiet = gludiet + diet[i][2]
            lipdiet = lipdiet + diet[i][3]
        if protdiet < bp or lipdiet < bl or gludiet < bg and protdiet < hp and lipdiet < hl and gludiet < hg:
            dinner = dinner + complement2
        if cal < 2600:
            diet = petitdej + dejeuner + collation1 + dinner + dessert2
        else:
            diet = petitdej + collation2 + dejeuner + collation1 + dinner + dessert2
        protdiet = 0
        gludiet = 0
        lipdiet = 0
        for i in range(0, len(diet)):
            protdiet = protdiet + diet[i][1]
            gludiet = gludiet + diet[i][2]
            lipdiet = lipdiet + diet[i][3]
        if protdiet < bp or lipdiet < bl or gludiet < bg and protdiet < hp and lipdiet < hl and gludiet < hg:
            dinner = dinner + fruit3
        if cal < 2600:
            diet = petitdej + dejeuner + collation1 + dinner + dessert2
        else:
            diet = petitdej + collation2 + dejeuner + collation1 + dinner + dessert2
        protdiet = 0
        gludiet = 0
        lipdiet = 0
        for i in range(0, len(diet)):
            protdiet = protdiet + diet[i][1]
            gludiet = gludiet + diet[i][2]
            lipdiet = lipdiet + diet[i][3]
        if protdiet < bp or lipdiet < bl or gludiet < bg and protdiet < hp and lipdiet < hl and gludiet < hg:
            collation2 = collation2 + collation3
        if cal < 2600:
            diet = petitdej + dejeuner + collation1 + dinner + dessert2
        else:
            diet = petitdej + collation2 + dejeuner + collation1 + dinner + dessert2
        protdiet = 0
        gludiet = 0
        lipdiet = 0
        for i in range(0, len(diet)):
            protdiet = protdiet + diet[i][1]
            gludiet = gludiet + diet[i][2]
            lipdiet = lipdiet + diet[i][3]

    cal2 = 4 * protdiet + 4 * gludiet + 9 * lipdiet

    sortpetit = []

    # print(diet,protdiet,gludiet,lipdiet,cal)

    # print(f"{diet} {protdiet} grammes de protéines, {gludiet} grammes de glucides, {lipdiet} grammes de lipides soit un total de {cal2} calories")

    pt = ""
    for i in range(len(petitdej)): pt = pt + petitdej[i][0] + ", "

    pt = pt[:-2]

    # print(pt)
    ###############################################

    dej = ""
    for ii in range(len(dejeuner)): dej = dej + dejeuner[ii][0] + ", "

    dej = dej[:-2]

    # print(dej)

    ###############################################

    col1 = ""
    for iii in range(len(collation1)): col1 = col1 + collation1[iii][0] + ", "

    col1 = col1[:-2]

    # print(col1)

    ###############################################

    col2 = ""
    for iiii in range(len(collation2)): col2 = col2 + collation2[iiii][0] + ", "

    col2 = col2[:-2]

    # print(col2)

    ###############################################

    din = ""
    for t in range(len(dinner)): din = din + dinner[t][0] + ", "

    din = din + dessert2[0][0]

    # print(din)

    ################################################################

    protpt = 0
    glupt = 0
    lippt = 0
    for i in range(len(petitdej)):
        protpt = protpt + petitdej[i][1]
        glupt = glupt + petitdej[i][2]
        lippt = lippt + petitdej[i][3]

    print(protpt, glupt)

    protcol1 = 0
    glucol1 = 0
    lipcol1 = 0
    for i in range(len(collation1)):
        protcol1 = protcol1 + collation1[i][1]
        glucol1 = glucol1 + collation1[i][2]
        lipcol1 = lipcol1 + collation1[i][3]

    protcol2 = 0
    glucol2 = 0
    lipcol2 = 0
    for i in range(len(collation2)):
        protcol2 = protcol2 + collation2[i][1]
        glucol2 = glucol2 + collation2[i][2]
        lipcol2 = lipcol2 + collation2[i][3]

    protdej = 0
    gludej = 0
    lipdej = 0
    for i in range(len(dejeuner)):
        protdej = protdej + dejeuner[i][1]
        gludej = gludej + dejeuner[i][2]
        lipdej = lipdej + dejeuner[i][3]

    protdin = 0
    gludin = 0
    lipdin = 0
    for i in range(len(dinner)):
        protdin = protdin + dinner[i][1]
        gludin = gludin + dinner[i][2]
        lipdin = lipdin + dinner[i][3]

    ################################################################
    resultat_repas = ""  # Initialisation de la variable

    if cal > 2600:
        resultat_repas += f" Petit dejeuner({protpt}g de protéines, {glupt}g de glucides, {lippt}g de lipides): {pt}\n"
        resultat_repas += f"collation du matin({protcol2}g de protéines, {glucol2}g de glucides, {lipcol2}g de lipides): {col2}\n"
        resultat_repas += f"dejeuner({protdej}g de protéines, {gludej}g de glucides, {lipdej}g de lipides): {dej}\n"
        resultat_repas += f"collation de l'après-midi({protcol1}g de protéines, {glucol1}g de glucides, {lipcol1}g de lipides): {col1}\n"
        resultat_repas += f"dinner({protdin}g de protéines, {gludin}g de glucides, {lipdin}g de lipides): {din}\n"
        resultat_repas += f"Soit un total de {protdiet} grammes de protéines, {gludiet} grammes de glucides, {lipdiet} grammes de lipides ce qui fait un total de {cal2} calories"
    else:
        resultat_repas += f" Petit dejeuner({protpt}g de protéines, {glupt}g de glucides, {lippt}g de lipides): {pt}\n"
        resultat_repas += f"collation({protcol1}g de protéines, {glucol1}g de glucides, {lipcol1}g de lipides): {col1}\n"
        resultat_repas += f"dejeuner({protdej}g de protéines, {gludej}g de glucides, {lipdej}g de lipides): {dej}\n"
        resultat_repas += f"dinner({protdin}g de protéines, {gludin}g de glucides, {lipdin}g de lipides): {din}\n"
        resultat_repas += f"Soit un total de {protdiet} grammes de protéines, {gludiet} grammes de glucides, {lipdiet} grammes de lipides ce qui fait un total de {cal2} calories"

    return resultat_repas




