import itertools
import Spacecrafts as sc
import random
# import CargoClass as cc


## initiate variables
items = 0; weight = 0; space = 1; ratio = 2; cargocount = 3; av_ratio = 4; bestscore = 99999999
cargolist = {}

## insert data into dictionary
with open('CargoLists/CargoList2.txt', 'rU') as f:
    for line in f:
        split = line.split()
        key = split[0][4:]
        if len(split) == 3:
            split[2] = split[2].replace(",", ".")
            cargolist[int(key)] = [float(split[1]), float(split[2])]
            cargolist[int(key)].append(cargolist[int(key)][weight]/cargolist[int(key)][space])
            items += 1

for bruteforce in range(0, 100000):
    # initialise spacecrafts in class
    cygnus = sc.Spacecrafts("Cygnus", 2000, 18.9)
    verne = sc.Spacecrafts("Verne", 2300, 13.1)
    progress = sc.Spacecrafts("Progress", 2400, 7.6)
    kounotori = sc.Spacecrafts("Kounotori", 5200, 14)
    tianzhou = sc.Spacecrafts("TianZhou", 6500, 15)
    dragon = sc.Spacecrafts("Dragon", 3400, 42)

    ## randomize cargolist
    randomlist = cargolist.keys()
    random.shuffle(randomlist)

    spacecrafts = [cygnus, verne, progress, kounotori]

    ## fill spacecrafts with cargo by putting item in spacecrafts with the same ratio as the average ratio of the cargo together
    for item in range(1, items + 1):

        ## setup variables for iterations
        randomcargo = randomlist[item-1]
        best_fit = 10000
        check_if_fits = False
        bestspacecraft = ''

        ## iterate over spacecrafts to check where item fits best
        for craft in spacecrafts:
            if craft.check_craft(cargolist[randomcargo][weight], cargolist[randomcargo][space]):
                check_if_fits = True
                diff = abs(craft.density - (craft.cargocount * craft.meancargoratio + cargolist[randomcargo][ratio])/(craft.cargocount+1))
                if diff < best_fit:
                    best_fit = diff
                    bestspacecraft = craft

        ## add cargo to spacecraft which fits best
        if check_if_fits == True:
            bestspacecraft.load_cargo(cargolist[randomcargo][ratio], cargolist[randomcargo][weight], cargolist[randomcargo][space], randomcargo)

    totalwastedweight = 0; totalwastedspace = 0; loadeditems = 0

    ## find out how good the cargo is loaded
    for craft in spacecrafts:
        totalwastedweight += craft.wastedweight
        totalwastedspace += craft.wastedspace
        loadeditems += craft.cargocount
        ##print(craft.cargolist)

    unloadeditems = items - loadeditems

    ##print('total wasted weight: ' + str(totalwastedweight))
    ##print('total wasted space: ' + str(totalwastedspace))
    ##print(str(unloadeditems) + ' items are not loaded on the spacecrafts.')
    ##print(str(totalwastedweight) + ' kilos are not used.')
    ##print(str(totalwastedspace) + ' m3 are not used.')

    ## determine a score for the filled spacecraft
    score = totalwastedweight + unloadeditems + 28

    ## save best score and show the result of the packed spacecraft
    if score < bestscore:
        bestscore = score
        print('Score: ' + str(bestscore) + ', #: ' + str(bruteforce) +  ', Wasted Space: ' + str(totalwastedspace) + ', Wasted Weight: ' + str(totalwastedweight) + ', Unloaded Items: ' + str(unloadeditems))
        for craft in spacecrafts:
            print(craft.cargolist)
        print("")
