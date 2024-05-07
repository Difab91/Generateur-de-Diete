def list():
    PetitDej = [
        [["100g de fromage blanc 0%", 10, 2, 0], ["15g de miel", 0, 13, 0], ["20g de flocons d'avoines", 3, 12, 2]],
        [["200g de fromage blanc 0%", 20, 4, 0], ["30g de miel", 0, 26, 0], ["40g de flocons d'avoines", 6, 24, 4]],
        [["2 oeufs au plat", 12, 2, 10], ["5 tranches de bacon à 3% de matières grasses, grillées", 15, 0, 2]],
        [["4 oeufs au plat", 24, 4, 20], ["6 tranches de bacon à 3% de matières grasses, grillées", 18, 0, 2]],
        [["100g de fromage blanc 0%", 10, 2, 0], ["15g de miel", 0, 13, 0], ["20g d'amandes", 4, 10, 4]],
        [["200g de fromage blanc 0%", 20, 4, 0], ["30g de miel", 0, 26, 0], ["20g d'amandes", 8, 20, 8]],
        [["100g de Pancake protéiné: recette", 30, 30, 7], ["20g de sirop d'agave", 0, 16, 0]],
        [["Wrap de paint complet avec oeuf, avocat, salade de 200g", 15, 32, 22]],
        [["Wrap de pain complet avec tranche de blanc de poulet, salade, tomate, boursin ", 23, 45, 14]],
        [["Wrap de pain complet avec tranche de blanc de poulet avec salade, tomate et leerdamer allégé ", 23, 45, 11]],
        [[
             "porridge de 80g de flocons d'avoines dans 40cl de lait et 50g de framboise à l'intèrieur saupoudrez avec 10g de graines de chia",
             12, 40, 9]], [[
                               "porridge de 80g de flocons d'avoines dans 40cl de lait et 50g de banane à l'intèrieur saupoudrez avec 10g de graines de chia",
                               11, 46, 9]], [[
                                                 "porridge de 80g de flocons d'avoines dans 40cl de lait et 50g de myrtilles à l'intèrieur saupoudrez avec 10g de graines de chia",
                                                 12, 41, 9]], [[
                                                                   "porridge de 80g de flocons d'avoines dans 40cl de lait et 50g de framboise à l'intèrieur saupoudrez avec 20g de noix",
                                                                   15, 42, 15]], [[
                                                                                      "porridge de 80g de flocons d'avoines dans 40cl de lait et 50g de banane à l'intèrieur saupoudrez avec 20g de noix",
                                                                                      16, 45, 15]], [[
                                                                                                         "porridge de 80g de flocons d'avoines dans 40cl de lait et 50g de myrtilles à l'intèrieur saupoudrez avec 20g de noix",
                                                                                                         14, 43, 15]],
        [["100g de fromage blanc 0%", 10, 2, 0], ["50g de mangue", 0, 8, 0], ["20g de flocons d'avoines", 3, 12, 2]],
        [["200g de fromage blanc 0%", 20, 4, 0], ["100g de mangue", 1, 15, 0], ["40g de flocons d'avoines", 6, 24, 4]],
        [["100g de fromage blanc 0%", 10, 2, 0], ["50g de framboise", 1, 6, 0], ["20g de flocons d'avoines", 3, 12, 2]],
        [["200g de fromage blanc 0%", 20, 4, 0], ["100g de framboise", 2, 12, 1],
         ["40g de flocons d'avoines", 6, 24, 4]],
        [["100g de fromage blanc 0%", 10, 2, 0], ["50g de myrtilles", 0, 13, 0],
         ["20g de flocons d'avoines", 3, 12, 2]],
        [["200g de fromage blanc 0%", 20, 4, 0], ["100g de myrtilles", 1, 15, 1],
         ["40g de flocons d'avoines", 6, 24, 4]],
        [["100g de fromage blanc 0%", 10, 2, 0], ["50g de mangue découpé", 0, 8, 0],
         ["20g de flocons d'avoines", 3, 12, 2], ["20g de miel", 0, 17, 0]],
        [["200g de fromage blanc 0%", 20, 4, 0], ["100g de mangue découpé en dé", 1, 15, 0],
         ["40g de flocons d'avoines", 6, 24, 4], ["20g de miel", 0, 17, 0]],
        [["100g de fromage blanc 0%", 10, 2, 0], ["50g de framboise", 1, 6, 0], ["20g de flocons d'avoines", 3, 12, 2],
         ["20g de miel", 0, 17, 0]], [["200g de fromage blanc 0%", 20, 4, 0], ["100g de framboise", 2, 12, 1],
                                      ["40g de flocons d'avoines", 6, 24, 4], ["20g de miel", 0, 17, 0]],
        [["100g de fromage blanc 0%", 10, 2, 0], ["50g de myrtilles", 0, 13, 0], ["20g de flocons d'avoines", 3, 12, 2],
         ["20g de miel", 0, 17, 0]], [["200g de fromage blanc 0%", 20, 4, 0], ["100g de myrtilles", 1, 15, 1],
                                      ["40g de flocons d'avoines", 6, 24, 4], ["20g de miel", 0, 17, 0]],
        [["2 oeufs au plat", 12, 2, 10], ["5 tranches de bacon à 3% de matières grasses, grillées", 15, 0, 2]],
        [["4 oeufs au plat", 24, 4, 20], ["6 tranches de bacon à 3% de matières grasses, grillées", 18, 0, 2]],
        [["100f d'Œufs brouillés aux épinards", 7, 1, 6]], [["100g d'Œufs brouillés aux poivrons", 7, 3, 6]],
        [["100g d'Œufs brouillés aux tomates", 5, 3, 5]], [["300g d'Œufs brouillés aux épinards", 21, 3, 18]],
        [["200g d'Œufs brouillés aux épinards", 14, 2, 12]],
        [["3 crepes à l'avoine garnit de 200g de yaourt et 50g de myrtilles au toales", 9, 43, 9]],
        [["3 crepes à l'avoine garnit de 200g de yaourt et 50g de framboise au toales", 10, 41, 9]],
        [["3 crepes aux amandes garnit de 200g de yaourt et 100g de banane au toales", 10, 58, 9]],
        [["3 crepes aux amandes garnit de 200g de yaourt et 50g de mangue au toales", 9, 43, 9]], [
            ["2 toasts de pain complet, garni d'avocat écrasé,de flocons de piment rouge et d'un œuf au plat ", 15, 33,
             23]]]
    Juicepti = [[["50cl de vrai jus d'oranges pressé", 3, 50, 0]], [["50cl de vrai jus de citron pressé", 1, 5, 0]],
                [["50 cl de jus de pamplemouse pressé", 2, 25, 0]],
                [["smoothie d'epinard, de whey, de banane et de lait", 25, 35, 7]],
                [["smoothie d'agrumes: clémentine, citron, oranges, pamplemouse", 3, 40, 1]]]
    EntreDejDinner = [[[
                           "Salades de lentilles en entrée: 100g de lentilles, 2 cuillères à soupes d'huiles d'olive, 1 cuillère à soupe de vinaigre de vin rouge,1/2 oignon rouge, 1 gousse d'ail, 1/2 poivron rouge, 1/2 tomate, jus de citron, persil, menthe, corriande",
                           20, 70, 16]], [["50g de salade verte, 2 tomates et huile d’olive en entrée", 3, 14, 14]],
                      [["240g de salade de pois chiches", 9, 37, 4]],
                      [["100g de feta avec 1/2 tomates et quelques feuilles de salades", 15, 7, 22]],
                      [["50g de tapenade avec toast", 8, 19, 16]], [["100g de concombres", 1, 4, 0]],
                      [["100g d'endives au jambon", 6, 4, 5]], [["100g d'asperges cuites", 2, 4, 0]]]
    DejDinner = [[[
                      "200g pâtes crémeuses aux poivrons: 2 poivrons rouges, 1 échalote, 1 cuillère à soupe d'huile d'olives,30g de feta, 5cl de lait, 1 gousse d'ail , sel et poivre et parika , 1 oeuf poché, pates",
                      12, 42, 18]], [[
                                         "200g de poulet au curry : poulet coupé en dés, 1 oignon moyen haché, 2 gousses d'ail hachées, 1 cuillère à soupe d'huile d'olive, 2 cuillères à soupe de pâte de curry, lait de coco, 1 cuillère à soupe de sauce soja, sel et poivre",
                                         55, 25, 55], ["200g de riz cuit", 5, 48, 1]],
                 [["60g de saumon grillé", 15, 0, 10], ["150g d’épinards cuits", 4, 5, 1]],
                 [["60g de saumon grillé", 15, 0, 10], ["200g de riz cuits", 5, 48, 1]],
                 [["250g de tagliatelles au saumon (cuites)", 24, 50, 20]],
                 [["une omeltte de 2 oeufs avec 2 tranche de leerdamer 0% à l'interieur", 17, 2, 10],
                  ["100g de coeur de palmier", 2, 5, 0]],
                 [["100g de thon en conserve", 20, 0, 2], ["200g de riz cuits", 5, 48, 1]],
                 [["100g d'escalope de dinde", 30, 0, 1], ["200g de riz cuits", 5, 48, 1]],
                 [["60g d'escalope de dinde", 18, 0, 1], ["200g de riz cuits", 5, 48, 1]],
                 [["100g d'escalope de dinde", 30, 0, 1], ["250g de riz cuits", 6, 60, 1]],
                 [["60g d'escalope de dinde", 18, 0, 1], ["250g de riz cuits", 6, 48, 1]],
                 [["100g d'escalope de poulet", 31, 0, 4], ["200g de riz cuits", 5, 48, 1]],
                 [["60g d'escalope de dinde", 19, 0, 3], ["250g de riz cuits", 6, 60, 1]],
                 [["100g de cabillaud", 19, 0, 1], ["200g de riz cuits", 5, 48, 1]],
                 [["Moules(200g)-frites de patate douce maison(150g)", 28, 55, 21]], [
                     ["140g de boeuf sauté à la sauce soja avec poivrons, nouilles(50g) et patate douce(50g)", 25, 32,
                      10]], [["100g d'éminces de poulet avec 200g de riz et sauce au lait de coco", 38, 47, 17]],
                 [["100g de crevettes au citron avec 200g de riz cuits et sauce au lait de coco", 25, 47, 18]],
                 [["70g de steak haché 5%", 16, 0, 3], ["100g d'haricots vert", 2, 7, 0]],
                 [["140g de steak haché 5%", 32, 0, 6], ["100g d'haricots vert", 2, 7, 0]],
                 [["210g de steak haché 5%", 48, 0, 9], ["100g d'haricots vert", 2, 7, 0]],
                 [["300g de pates(cuites) à la bolognaise", 21, 51, 8]],
                 [["300g de pates(cuites) à la carbonara", 42, 45, 42]], [[
                                                                              "100 grammes de viande hachée assaisonnée avec des oignons et un mélange d'épices comprenant du curry, du cumin, du paprika, de l'ail, du sel et du poivre",
                                                                              23, 4, 17],
                                                                          ["200g de riz cuits", 5, 45, 1]],
                 [["300g de choucroute", 3, 14, 2]], [["un couscous de 300g", 12, 67, 1]],
                 [["200g de boeuf aux oignons", 25, 7, 13], ["100g de semoule", 2, 19, 0]], [[
                                                                                                 "400g pâtes crémeuses aux poivrons: 2 poivrons rouges, 1 échalote, 1 cuillère à soupe d'huile d'olives,30g de feta, 5cl de lait, 1 gousse d'ail , sel et poivre et parika , 1 oeuf poché, pates",
                                                                                                 12, 42, 18]], [[
                                                                                                                    "200g de poulet au curry : poulet coupé en dés, 1 oignon moyen haché, 2 gousses d'ail hachées, 1 cuillère à soupe d'huile d'olive, 2 cuillères à soupe de pâte de curry, lait de coco, 1 cuillère à soupe de sauce soja, sel et poivre",
                                                                                                                    110,
                                                                                                                    50,
                                                                                                                    110],
                                                                                                                [
                                                                                                                    "400g de riz cuit",
                                                                                                                    10,
                                                                                                                    96,
                                                                                                                    2]],
                 [["120g de saumon grillé", 30, 0, 20], ["300g d’épinards cuits", 8, 10, 2]],
                 [["120g de saumon grillé", 30, 0, 20], ["400g de riz cuits", 10, 96, 2]],
                 [["500g de tagliatelles au saumon (cuites)", 48, 100, 40]],
                 [["une omeltte de 4 oeufs avec 4 tranche de leerdamer 0% à l'interieur", 34, 4, 20],
                  ["200g de coeur de palmier", 4, 10, 0]], [[
                                                                "200 grammes de viande hachée assaisonnée avec des oignons et un mélange d'épices comprenant du curry, du cumin, du paprika, de l'ail, du sel et du poivre",
                                                                64, 8, 34], ["400g de riz cuits", 10, 90, 2]],
                 [["200g d'escalope de poulet", 62, 0, 8], ["400g de riz cuits", 10, 96, 2]],
                 [["120g d'escalope de dinde", 38, 0, 6], ["250g de riz cuits", 6, 60, 1]],
                 [["200g de cabillaud", 38, 0, 2], ["400g de riz cuits", 10, 96, 2]],
                 [["Moules(400g)-frites de patate douce maison(300g)", 56, 110, 42]], [
                     ["280g de boeuf sauté à la sauce soja avec poivrons, nouilles(100g) et patate douce(100g)", 50, 64,
                      20]], [["200g d'éminces de poulet avec 400g de riz et sauce au lait de coco", 76, 94, 34]],
                 [["200g de crevettes au citron avec 400g de riz cuits et sauce au lait de coco", 50, 94, 36]],
                 [["500g de pates(cuites) à la bolognaise", 35, 85, 14]],
                 [["500g de pates(cuites) à la carbonara", 70, 75, 70]]]

    Fruits = [[["1 peche", 0, 10, 0]], [["20g de pruneau sec", 0, 12, 0]], [["40g de pruneau sec", 0, 24, 0]],
              [["1 poire", 1, 26, 0]], [["1 pomme", 0, 25, 0]], [["1 banane", 1, 30, 0]], [["1 pamplemouse", 1, 15, 0]],
              [["100g de dattes", 3, 75, 0]], [["100g de grenades", 2, 19, 1]], [["1 kiwi", 1, 16, 1]],
              [["clémentine", 1, 9, 0]]]

    Dessert = Fruits + [
        [["100g de fromage blanc 0%", 10, 2, 0], ["15g de miel", 0, 13, 0], ["20g de flocons d'avoines", 3, 12, 2]],
        [["1 yaourt nature", 5, 5, 3]], [["200g de petit suisse 0%", 15, 9, 1]]]

    complementRepas = [[["80g de graine de Chia", 14, 26, 36]], [["40g de graine de Chia", 7, 13, 18]],
                       [["100g d'asperges cuites", 2, 4, 0]], [["150g d'haricots rouges", 13, 34, 1]],
                       [["100g d'haricots rouges", 9, 23, 1]], [["100g de choux fleurs cuit", 2, 5, 0]],
                       [["50g de graine de lin", 9, 2, 21]], [["100g d'aubergines cuites", 1, 6, 0]],
                       [["100g de choux de bruxelles cuits", 3, 9, 0]], [["100g de brocolie cuits", 4, 11, 1]],
                       [["100g de lentilles cuites", 9, 20, 0]], [["100g de patate douce cuite", 2, 21, 0]],
                       [["100g de purée de pommes de terre", 2, 18, 0]], [["100g de riz cuits", 3, 29, 0]],
                       [["100g de boulghour", 3, 19, 0]], [["100g de carottes cuites à la vapeur", 1, 10, 0]],
                       [["100g de coeur de palmier", 2, 5, 0]], [["100g d'haricots verts", 2, 7, 0]]]

    Collation = Dessert + [[["30g d'amandes", 6, 6, 15]], [["30g d'amandes", 6, 6, 15]], [["30g d'amandes", 6, 6, 15]],
                           [["30g de noix de cajoux", 5, 9, 13]], [["30g de noix de cajoux", 5, 9, 13]],
                           [["2 kinder bueno", 4, 23, 15]], [["30g de chocolat noir 80% de cacao", 2, 10, 15]],
                           [["20g de chocolat noir 80% de cacao", 2, 6, 10]],
                           [["40g de chocolat noir 80% de cacao", 3, 13, 20]],
                           [["100g de tzatziki repartit sur 4 tranches de pain complet", 15, 73, 11]],
                           [["100g de Pancake protéiné: recette", 30, 30, 7], ["20g de sirop d'agave", 0, 16, 0]],
                           [["1 avocat", 4, 18, 33]]]

    return {
        'PetitDej': PetitDej,
        'JuicePti': Juicepti,
        'EntreDejDinner': EntreDejDinner,
        'DejDinner': DejDinner,
        'Fruits': Fruits,
        'Dessert': Dessert,
        'complementRepas': complementRepas,
        'Collation': Collation,
    }



