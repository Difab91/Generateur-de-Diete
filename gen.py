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