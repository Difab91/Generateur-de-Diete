def list():
    PetitDej = [
        [["100g de fromage blanc 0% avec 15g de miel et 20g de flocons d'avoines", 13, 27, 2]],
        [["200g de fromage blanc 0% avec 30g de miel et 40g de flocons d'avoines", 26, 44, 4]],
        [["2 oeufs au plat", 12, 2, 10], ["5 tranches de bacon à 3% de matières grasses, grillées", 15, 0, 2]],
        [["4 oeufs au plat", 24, 4, 20], ["6 tranches de bacon à 3% de matières grasses, grillées", 18, 0, 2]],
        [["100g de fromage blanc 0% avec 15g de miel et 20g d'amandes", 14, 25, 4]],
        [["200g de fromage blanc 0% avec 30g de miel et 20g d'amndes", 28, 50, 8]],
        [["100g de Pancake protéiné avec 20g de sirop d'agave", 30, 46, 7]],
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
        [["100g de fromage blanc 0% avec 50g de mangue découpée en dé et 20g de flocons d'avoines", 13, 22, 2]],
        [["200g de fromage blanc 0% avec 100g de mangue découpée en dé et 40g de flocons d'avoines", 27, 43, 4]],
        [["100g de fromage blanc 0% avec 50g de framboise et 20g de flocons d'avoines", 14, 8, 2]],
        [["200g de fromage blanc 0% avec 100g de framboise et 40g de flocons d'avoines", 28, 16, 5]
         ],
        [["100g de fromage blanc 0% avec 50g de myrtilles et 20g de flocons d'avoines", 13, 27, 2]],
        [["200g de fromage blanc 0% avec 100g de myrtilles et 40g de flocons d'avoines", 26, 54, 5]],
        [["100g de fromage blanc 0% avec 50g de mangue découpée en dé 20g de flocons d'avoines et 20g de miel ", 13, 39, 2]],
        [["200g de fromage blanc 0%  avec 100g de mangue découpée en dé  40g de flocons d'avoines et 20g de miel ", 27, 60, 4]],
        [["100g de fromage blanc 0% avec 50g de framboiset 20g de flocons d'avoines et 20g de miel", 14, 25, 2]], [["200g de fromage blanc 0% avec 100g de framboise et 40g de flocons d'avoines et 20g de miel", 28, 33, 5]],
        [["100g de fromage blanc 0%  avec 50g de myrtilles  20g de flocons d'avoines et 20g de miel", 13, 44, 2]], [["200g de fromage blanc 0%avec 100g de myrtilles et 40g de flocons d'avoines et 20g de miel", 26, 72, 5]],
        [["2 oeufs au plat", 12, 2, 10], ["5 tranches de bacon à 3% de matières grasses, grillées", 15, 0, 2]],
        [["4 oeufs au plat", 24, 4, 20], ["6 tranches de bacon à 3% de matières grasses, grillées", 18, 0, 2]],
        [["100g d'Œufs brouillés aux épinards (3 oeufs - 50g d'epinards)", 7, 1, 6]], [["100g d'Œufs brouillés aux poivrons (3 oeufs - 50g de poivrons)", 7, 3, 6]],
        [["100g d'Œufs brouillés aux tomates (3 oeufs - 50g de tomates)", 5, 3, 5]],
        [["200g d'Œufs brouillés aux épinards (6 oeufs - 100g d'epinards)", 14, 2, 12]],
        [["3 crepes à l'avoine garnit de 200g de yaourt et 50g de myrtilles au toales", 9, 43, 9]],
        [["3 crepes à l'avoine garnit de 200g de yaourt et 50g de framboise au toales", 10, 41, 9]],
        [["3 crepes aux amandes garnit de 200g de yaourt et 100g de banane au toales", 10, 58, 9]], [["Omelette aux Épinards, Champignons et Fromage de Chèvre: 3 œufs avec 50g d'épinards frais, 50g de champignons tranchés, 30g de fromage de chèvre émietté, 1 cuillère à soupe d'huile d'olive, Sel, poivre",24,5,30]],
        [["3 crepes aux amandes garnit de 200g de yaourt et 50g de mangue au toales", 9, 43, 9]], [
            ["2 toasts de pain complet, garni d'avocat écrasé,de flocons de piment rouge et d'un œuf au plat ", 15, 33,
             23]],[["Bol d'Açai avec Granola et Fruits Frais avec 100g de purée d'açai non sucrée, 50g de granola ,100g de fruits frais mélangés (bananes, fraises, myrtilles) et 1 cuillère à soupe de beurre d'amande", 10, 75, 20]]
              ,  [["muffins à la banane (2 oeufs , 2 bananes, 50g de whey, sucre, 100g de farine d'avoine", 8,20,5]],  [[" Pudding de Chia au Lait de Coco: 40cl de lait de coco, 4 cuilleres à soupes de graine de chia ,1 cuillère à soupe de miel ou de sirop d'érable, quelques fruits rouges pour garnir", 3,15,155]]]
    Juicepti = [[["50cl de vrai jus d'oranges pressé", 3, 50, 0]], [["50cl de vrai jus de citron pressé", 1, 5, 0]],
                [["50 cl de jus de pamplemouse pressé", 2, 25, 0]],
                [["smoothie d'epinard (50g) avec 30g de whey une banane et 25cl lait", 25, 35, 7]],
                [["smoothie d'agrumes: clémentine, citron, oranges, pamplemouse", 3, 40, 1]]]
    EntreDejDinner = [[[
                           "Salades de lentilles en entrée: 100g de lentilles, 2 cuillères à soupes d'huiles d'olive, 1 cuillère à soupe de vinaigre de vin rouge,1/2 oignon rouge, 1 gousse d'ail, 1/2 poivron rouge, 1/2 tomate, jus de citron, persil, menthe, corriande",
                           20, 70, 16]], [["50g de salade verte, 2 tomates et huile d’olive en entrée", 3, 14, 14]],
                      [["240g de salade de pois chiches", 9, 37, 4]],
                      [["100g de feta avec 1/2 tomates et quelques feuilles de salades", 15, 7, 22]],
                      [["50g de tapenade avec toast", 8, 19, 16]], [["100g de concombres", 1, 4, 0]],
                      [["100g d'endives au jambon", 6, 4, 5]], [["100g d'asperges cuites", 2, 4, 0]], [["Omelette aux Épinards, Champignons et Fromage de Chèvre: 3 œufs avec 50g d'épinards frais, 50g de champignons tranchés, 30g de fromage de chèvre émietté, 1 cuillère à soupe d'huile d'olive, Sel, poivre",24,5,30]],
                        [["1 tranche de melon (150g environ)", 1, 12, 0]], [[" Salade de Pâtes au Thon et aux Légumes: 100g de pâtes complètes cuites avec, 150g de thon en conserve (à l'eau) , 50g de poivrons rouges en dés, 50g de concombre en dés, 30g d'oignons rouges finement hachés, 1 cuillère à soupe d'huile d'olive, 1 cuillère à soupe de vinaigre balsamique",35 ,50, 12]]]
    DejDinner = [[[
                      "200g pâtes crémeuses aux poivrons: 2 poivrons rouges, 1 échalote, 1 cuillère à soupe d'huile d'olives,30g de feta, 5cl de lait, 1 gousse d'ail , sel et poivre et parika , 1 oeuf poché, pates",
                      12, 42, 18]], [[
                                         "200g de poulet au curry : poulet coupé en dés, 1 oignon moyen haché, 2 gousses d'ail hachées, 1 cuillère à soupe d'huile d'olive, 2 cuillères à soupe de pâte de curry, lait de coco, 1 cuillère à soupe de sauce soja, sel et poivre",
                                         55, 25, 55], ["200g de riz cuit", 5, 48, 1]],
                 [["60g de saumon grillé", 15, 0, 10], ["150g d’épinards cuits", 4, 5, 1]], [["Bol de Quinoa au Poulet Grillé et Légumes Rôtis: 150g de quinoa cuit avec 200gde poitrine de poulet grillée, 100g de patates douces rôties,50g de brocoli rôti,50g de poivrons rouges rôtis, 1 cuillère à soupe d'huile d'olive du Jus de citron et sel, poivre, paprika",50,60,20]],
                [["60g de saumon grillé", 15, 0, 10], ["200g de riz cuits", 5, 48, 1]],
                 [["250g de tagliatelles au saumon (cuites)", 24, 50, 20]],  [["Bol de Saumon, Riz Brun et Avocat:150g de riz brun cuit avec 150g de filet de saumon cuit 1/2 avocat (environ 70g),50g de concombre en dés,1 cuillère à soupe de sauce soja,1 cuillère à café de graines de sésame", 40,70,30]],
                 [["une omeltte de 2 oeufs avec 2 tranche de leerdamer 0% à l'interieur", 17, 2, 10],
                  ["100g de coeur de palmier", 2, 5, 0]],  [["Wrap de Poulet, Houmous et Légumes: 1 wrap complet avec 150 gde poitrine de poulet grillée, 50g de homous ,50g de carottes rapeées,50g de salade, 30g de poivrons rouges en lanières",30,45,15]] ,
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
                 [["500g de pates(cuites) à la bolognaise", 35, 85, 14]], [[" Bol de Patate Douce Farcie aux Haricots Noirs et Avocat: 1 grande patate douce (environ 200g)avec 100g de haricots noirs cuits, 1/2 avocat (environ 70g), 50g de maïs, 50g de tomates cerises coupées en deux, 1 cuillère à soupe de yaourt grec et Jus de citron, sel, poivre, cumin",15 ,70, 20]],
                 [["500g de pates(cuites) à la carbonara", 70, 75, 70]],[["200g de crevettes au citron avec 400g de riz cuits et sauce au lait de coco", 50, 94, 36]]
                 , [["  Poêlée de Tofu, Riz de Chou-Fleur et Légumes: 150g de tofu ferme avec 200g de riz de choux fleur, 50g de carottes, 50g de pois mange-tout, 1 cuillère à soupe de sauce soja , d'huile de sézame et de gingembre",25 ,30, 20]]
                 ]

    Fruits = [[["1 peche", 0, 10, 0]], [["20g de pruneau sec", 0, 12, 0]], [["40g de pruneau sec", 0, 24, 0]],
              [["1 poire", 1, 26, 0]], [["1 pomme", 0, 25, 0]], [["1 banane", 1, 30, 0]], [["1 pamplemouse", 1, 15, 0]],
              [["100g de dattes", 3, 75, 0]], [["100g de grenades", 2, 19, 1]], [["1 kiwi", 1, 16, 1]],
              [["1 clémentine", 1, 9, 0]], [["100g de myrtilles", 1, 15, 0]], [["100g de framboise", 1, 12, 1]] , [["100g de fraise", 1, 8, 0]], [["1 tranche d'ananas (150g environ)", 1, 20, 0]]]

    Dessert = Fruits + [
        [["100g de fromage blanc 0% avec 15g de miel et 20g de flocons d'avoines", 13, 27, 2]],
        [["1 yaourt nature", 5, 5, 3]], [["200g de petit suisse 0%", 15, 9, 1]], [["100g de fromage blanc 0% avec 50g de mangue découpée en dé et 20g de flocons d'avoines", 13, 22, 2]],
        [["200g de fromage blanc 0% avec 100g de mangue découpée en dé et 40g de flocons d'avoines", 27, 43, 4]],
        [["100g de fromage blanc 0% avec 50g de framboise et 20g de flocons d'avoines", 14, 8, 2]], [["1 tranche d'ananas (150g environ)", 1, 20, 0]],
        [["200g de fromage blanc 0% avec 100g de framboise et 40g de flocons d'avoines", 28, 16, 5]
         ],[["100g de framboise", 1, 12, 1]],[["100g de fraise", 1, 8, 0]] ,
        [["100g de fromage blanc 0% avec 50g de myrtilles et 20g de flocons d'avoines", 13, 27, 2]],
        [["200g de fromage blanc 0% avec 100g de myrtilles et 40g de flocons d'avoines", 26, 54, 5]],
        [["100g de fromage blanc 0% avec 50g de mangue découpée en dé 20g de flocons d'avoines et 20g de miel ", 13, 39, 2]],
        [["200g de fromage blanc 0%  avec 100g de mangue découpée en dé  40g de flocons d'avoines et 20g de miel ", 27, 60, 4]],
        [["100g de fromage blanc 0% avec 50g de framboiset 20g de flocons d'avoines et 20g de miel", 14, 25, 2]], [["200g de fromage blanc 0% avec 100g de framboise et 40g de flocons d'avoines et 20g de miel", 28, 33, 5]],
        [["100g de fromage blanc 0%  avec 50g de myrtilles  20g de flocons d'avoines et 20g de miel", 13, 44, 2]], [["200g de fromage blanc 0%avec 100g de myrtilles et 40g de flocons d'avoines et 20g de miel", 26, 72, 5]],
         [["1 yaourt nature", 5, 5, 3]], [["200g de petit suisse 0%", 15, 9, 1]] , [["1 yaourt nature", 5, 5, 3]], [["200g de petit suisse 0%", 15, 9, 1]],
        [["1 part de tiramisu", 6,35,20]], [["1 mousse au chocolat", 6,20,18]], [["1 panna cotta", 3,20,20]], [["1 creme brulée", 4,20,25]],  [["muffins à la banane (2 oeufs , 2 bananes, 50g de whey, sucre, 100g de farine d'avoine", 8,20,5]],  [[" Pudding de Chia au Lait de Coco: 40cl de lait de coco, 4 cuilleres à soupes de graine de chia ,1 cuillère à soupe de miel ou de sirop d'érable, quelques fruits rouges pour garnir", 3,15,155]],
        [["1 tranche de pasteque (150g environ)", 1, 11, 0]],  [["1 tranche de melon (150g environ)", 1, 12, 0]]]

    complementRepas = [[["80g de graine de Chia", 14, 26, 36]], [["40g de graine de Chia", 7, 13, 18]],
                       [["100g d'asperges cuites", 2, 4, 0]], [["150g d'haricots rouges", 13, 34, 1]],
                       [["100g d'haricots rouges", 9, 23, 1]], [["100g de choux fleurs cuit", 2, 5, 0]],
                       [["50g de graine de lin", 9, 2, 21]], [["100g d'aubergines cuites", 1, 6, 0]],
                       [["100g de choux de bruxelles cuits", 3, 9, 0]], [["100g de brocolie cuits", 4, 11, 1]],
                       [["100g de lentilles cuites", 9, 20, 0]], [["100g de patate douce cuite", 2, 21, 0]],
                       [["100g de purée de pommes de terre", 2, 18, 0]], [["100g de riz cuits", 3, 29, 0]],
                       [["100g de boulghour", 3, 19, 0]], [["100g de carottes cuites à la vapeur", 1, 10, 0]],
                       [["100g de coeur de palmier", 2, 5, 0]], [["100g d'haricots verts", 2, 7, 0]]]

    Collation = Dessert + [[["30g d'amandes", 6, 6, 15]],  [["30g d'amandes", 6, 6, 15]],
                           [["30g de noix de cajoux", 5, 9, 13]], [["30g de noix de cajoux", 5, 9, 13]],
                           [["2 kinder bueno", 4, 23, 15]], [["30g de chocolat noir 80% de cacao", 2, 10, 15]],
                           [["100g de tzatziki repartit sur 4 tranches de pain complet", 15, 73, 11]],
                           [["20g de chocolat noir 80% de cacao", 2, 6, 10]],
                           [["40g de chocolat noir 80% de cacao", 3, 13, 20]],
                           [["100g de tzatziki repartit sur 4 tranches de pain complet", 15, 73, 11]],
                           [["100g de Pancake protéiné avec 20g de sirop d'agave", 30, 46, 7]],
                           [["1 avocat", 4, 18, 33]] ,[["Bol d'Açai avec Granola et Fruits Frais avec 100g de purée d'açai non sucrée, 50g de granola ,100g de fruits frais mélangés (bananes, fraises, myrtilles) et 1 cuillère à soupe de beurre d'amande", 10, 75, 20]]]

    return {
        'PetitDej': PetitDej,
        'Juicepti': Juicepti,
        'EntreDejDinner': EntreDejDinner,
        'DejDinner': DejDinner,
        'Fruits': Fruits,
        'Dessert': Dessert,
        'complementRepas': complementRepas,
        'Collation': Collation,
    }



