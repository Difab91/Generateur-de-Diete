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
        complement1 = []
        entre1= []
        entre2 = []
        complement2 = []
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
        totdej= dejeuner + dessert1
        totdin= dinner + dessert2
        if cal < 2600:
            diet = petitdej + dejeuner + dessert1 + collation1 + dinner + dessert2
        else:
            diet = petitdej + collation2 + dejeuner + dessert1 + collation1 + dinner + dessert2
        protdiet = 0
        gludiet = 0
        lipdiet = 0
        for i in range(0, len(diet)):
            protdiet = protdiet + diet[i][1]
            gludiet = gludiet + diet[i][2]
            lipdiet = lipdiet + diet[i][3]
        if protdiet < bp or lipdiet < bl or gludiet < bg and protdiet < hp and lipdiet < hl and gludiet < hg:
            entre1 = random.choice(EntreDejDinner)
            totdej= totdej + entre1
            if cal < 2600:
                diet = petitdej + entre1 + dejeuner + dessert1 + collation1 + dinner + dessert2
            else:
                diet = petitdej + collation2 + entre1 + dejeuner + dessert1 + collation1 + dinner + dessert2
        protdiet = 0
        gludiet = 0
        lipdiet = 0
        for i in range(0, len(diet)):
            protdiet = protdiet + diet[i][1]
            gludiet = gludiet + diet[i][2]
            lipdiet = lipdiet + diet[i][3]
        if protdiet < bp or lipdiet < bl or gludiet < bg and protdiet < hp and lipdiet < hl and gludiet < hg:
            complement1 = random.choice(complementRepas)
            totdej = totdej + complement1
            if cal < 2600:
                diet = petitdej + entre1 + dejeuner + complement1 + dessert1 + collation1 + dinner + dessert2
            else:
                diet = petitdej + collation2 + entre1 + dejeuner + complement1 + dessert1 + collation1 + dinner + dessert2
        protdiet = 0
        gludiet = 0
        lipdiet = 0
        for i in range(0, len(diet)):
            protdiet = protdiet + diet[i][1]
            gludiet = gludiet + diet[i][2]
            lipdiet = lipdiet + diet[i][3]
        if protdiet < bp or lipdiet < bl or gludiet < bg and protdiet < hp and lipdiet < hl and gludiet < hg:
            dessert1 = dessert1 + fruit2
            totdej= totdej + fruit2
        if cal < 2600:
            diet =  petitdej + entre1 + dejeuner + complement1 + dessert1 + collation1 + dinner + dessert2
        else:
            diet = petitdej + collation2 + entre1 + dejeuner + complement1 + dessert1 + collation1 + dinner + dessert2
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
            diet = petitdej + entre1 + dejeuner + complement1 + dessert1 + collation1 + dinner + dessert2
        else:
            diet = petitdej + collation2 + entre1 + dejeuner + complement1 + dessert1 + collation1 + dinner + dessert2
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
            diet = petitdej + entre1 + dejeuner + complement1 + dessert1 + collation1 + dinner + dessert2
        else:
            diet = petitdej + collation2 + entre1 + dejeuner + complement1 + dessert1 + collation1 + dinner + dessert2
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
            diet = petitdej  + entre1 + dejeuner + complement1 + dessert1 + collation1 + dinner + dessert2
        else:
            diet = petitdej + collation2 + entre1 + dejeuner + complement1 + dessert1 + collation1 + dinner + dessert2
        protdiet = 0
        gludiet = 0
        lipdiet = 0
        for i in range(0, len(diet)):
            protdiet = protdiet + diet[i][1]
            gludiet = gludiet + diet[i][2]
            lipdiet = lipdiet + diet[i][3]
        if protdiet < bp or lipdiet < bl or gludiet < bg and protdiet < hp and lipdiet < hl and gludiet < hg:
            entre2 = random.choice(EntreDejDinner)
            totdin = totdin + entre2
            if cal < 2600:
                diet = petitdej + entre1 + dejeuner + complement1 + dessert1 + collation1 + entre2 + dinner + dessert2
            else:
                diet = petitdej + collation2 + entre1 + dejeuner + complement1 + dessert1 + collation1 + entre2 + dinner + dessert2
        protdiet = 0
        gludiet = 0
        lipdiet = 0
        for i in range(0, len(diet)):
            protdiet = protdiet + diet[i][1]
            gludiet = gludiet + diet[i][2]
            lipdiet = lipdiet + diet[i][3]
        if protdiet < bp or lipdiet < bl or gludiet < bg and protdiet < hp and lipdiet < hl and gludiet < hg:
            complement2 = random.choice(complementRepas)
            totdin = totdin + complement2
            if cal < 2600:
                diet = petitdej + entre1 + dejeuner + complement1 + dessert1 + collation1 + entre2 + dinner + complement2 + dessert2
            else:
                diet = petitdej + collation2 + entre1 + dejeuner + complement1 + dessert1 + collation1 + entre2 + dinner + complement2 + dessert2
        protdiet = 0
        gludiet = 0
        lipdiet = 0
        for i in range(0, len(diet)):
            protdiet = protdiet + diet[i][1]
            gludiet = gludiet + diet[i][2]
            lipdiet = lipdiet + diet[i][3]
        if protdiet < bp or lipdiet < bl or gludiet < bg and protdiet < hp and lipdiet < hl and gludiet < hg:
            dessert2 = dessert2 + fruit3
            totdin = totdin + fruit3
        if cal < 2600:
            diet = petitdej + entre1 + dejeuner + complement1 + dessert1 + collation1 + entre2 + dinner + complement2 + dessert2
        else:
            diet = petitdej + collation2 + entre1 + dejeuner + complement1 + dessert1 + collation1 + entre2 + dinner + complement2 + dessert2
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
            diet = petitdej + entre1 + dejeuner + complement1 + dessert1 + collation1 + entre2 + dinner + dessert2
        else:
            diet = petitdej + collation2 + entre1 + dejeuner + complement1 + dessert1 + collation1 + entre2 + dinner + dessert2
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

    # tester ca et voir par quoi remplacer pour l'initialsation du vide compatible avec data
    ent1 = " "
    for ttt in range(len(entre1)): ent1 = ent1+ entre1[ttt][0] + ", "

    ent1 = ent1[:-2]



    dej = ""
    for ii in range(len(dejeuner)): dej = dej + dejeuner[ii][0] + ", "

    dej = dej[:-2]

    des1 = ""
    for pp in range(len(dessert1)): des1 = des1 + dessert1[pp][0] + ", "

    des1 = des1[:-2]



    comp1 = " "
    for ll in range(len(complement1)): comp1 = comp1 + complement1[ll][0] + ", "

    comp1 = comp1[:-2]




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

    din= din[:-2]

    des2 = ""
    for cc in range(len(dessert2)): des2 = des2 + dessert2[cc][0] + ", "

    des2 = des2[:-2]

    ent2 = " "
    for kk in range(len(entre2)): ent2 = ent2 + entre2[kk][0] + ", "

    ent2 = ent2[:-2]

    comp2 = " "
    for kkk in range(len(complement2)): comp2 = comp2 + complement2[kkk][0] + ", "

    comp2 = comp2[:-2]

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
    for i in range(len(totdej)):
        protdej = protdej + totdej[i][1]
        gludej = gludej + totdej[i][2]
        lipdej = lipdej + totdej[i][3]

    protdin = 0
    gludin = 0
    lipdin = 0
    for i in range(len(totdin)):
        protdin = protdin + totdin[i][1]
        gludin = gludin + totdin[i][2]
        lipdin = lipdin + totdin[i][3]

    ################################################################




    if cal > 2600:
        return protpt, glupt, lippt, pt, protcol2, glucol2, lipcol2, col2, protdej, gludej, lipdej, ent1, dej, comp1, des1, protcol1, glucol1, lipcol1, col1, protdin, gludin, lipdin, ent2, din, comp2, des2, protdiet, gludiet, lipdiet, cal2

    else:
        return protpt, glupt, lippt, pt, protdej, gludej, lipdej, ent1, dej, comp1, des1, protcol1, glucol1, lipcol1, col1, protdin, gludin, lipdin, ent2, din, comp2, des2, protdiet, gludiet, lipdiet, cal2

