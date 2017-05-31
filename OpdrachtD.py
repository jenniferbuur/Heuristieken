## Select the method you want to use by setting the speed parameter to one of the following:
too_fast = 100       # 2 second (15 cycles, 45 left)
very_fast = 1000     # 10 seconds (15 cycles, 24 left)
fast = 10000         # 80 seconds (14 cycles, 86 left)
normal = 100000      # 800 seconds (14 cycles, 61 left)
slow = 1000000       # 8000 seconds (14 cycles, 51 left)

speed = very_fast

import itertools
import Spacecrafts as sc
import random
# import CargoClass as cc


## initiate variables
items = 0; weight = 0; space = 1; ratio = 2; cargocount = 3; av_ratio = 4; bestscore = 99999999
cargolist = {}
cygnus = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
verne = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
progress = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
kounotori = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
tianzhou = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dragon = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
bestscore_cargo = []
count_total_spacecrafts_per_country = 0
first_spacecrafts_filled = False
last_cargolist = False
## insert data into dictionary
with open('CargoLists/CargoList3.txt', 'rU') as f:
    for line in f:
        split = line.split()
        key = split[0][4:]
        if len(split) == 3:
            split[2] = split[2].replace(",", ".")
            cargolist[int(key)] = [float(split[1]), float(split[2])]
            cargolist[int(key)].append(cargolist[int(key)][weight]/cargolist[int(key)][space])
            items += 1

## fill all spacecrafts one time, and do this again if they are filled and you have cargo's left
for cargoloop in range(0,20):
    count_total_spacecrafts_per_country += 1
    print('Cycle: ' + str(count_total_spacecrafts_per_country))

    ## remove used cargos from available list

    #print('TOTAL CARGOLIST: ' + str(cargolist))
    for used_cargo in bestscore_cargo:
        #print(used_cargo)
        cargolist.pop(used_cargo)
    print('Cargos to fill: ' + str(len(cargolist)))

    bestscore = 99999999
    bestscore_crafts = []

    ## optimze cargolist to reduce time of random algoritm
    cargolist_sorted = sorted(cargolist.items(), key=lambda i: i[space][ratio], reverse = True)
    random.shuffle(cargolist_sorted)

    # Theoratically we can fill the cargos with a max. weight of max_weight and max. space of max_space.
    # Based on this information we setup an optimized cargolist to reduce our 'random time'
    max_weight = 2300 + 2400+ 5200 + 6500 + 3400
    max_space = 13.1 + 7.6+ 14 + 15 + 42
    optimized_cargolist = {}
    total_cargospace = 0; total_cargoweight = 0; optimized_items = 0
    for item in range(0,len(cargolist)):
        if total_cargospace < max_space and total_cargoweight < max_weight:
            optimized_cargolist[cargolist_sorted[item][0]] = [cargolist_sorted[item][1][weight], cargolist_sorted[item][1][space], cargolist_sorted[item][1][ratio]]
            total_cargoweight += cargolist_sorted[item][1][weight]
            total_cargospace += cargolist_sorted[item][1][space]
            optimized_items += 1

    if optimized_items == len(cargolist):
        print('LAST CARGO')
        last_cargos_weight = 0
        last_cargos_space = 0
        last_cargolist = True
        for key, value in optimized_cargolist.items():

            last_cargos_weight += value[0]
            last_cargos_space += value[1]
        print(last_cargos_space)
        print(last_cargos_weight)

    print('We try to use put all the following cargos in the Spacecrafts: ' + str(optimized_cargolist))

    ## Start brute force and try to fit the optimized list as good as possible in the Spacecrafts
    for bruteforce in range(0, speed):

        # initialise spacecrafts in class
        cygnus[cargoloop] = sc.Spacecrafts("Cygnus", 2000, 18.9)
        verne[cargoloop] = sc.Spacecrafts("Verne", 2300, 13.1)
        progress[cargoloop] = sc.Spacecrafts("Progress", 2400, 7.6)
        kounotori[cargoloop] = sc.Spacecrafts("Kounotori", 5200, 14)
        tianzhou[cargoloop] = sc.Spacecrafts("TianZhou", 6500, 15)
        dragon[cargoloop] = sc.Spacecrafts("Dragon", 3400, 42)
        first_spacecrafts_filled = True

        ## randomize cargolist so every bruteforce will give another result
        randomlist = optimized_cargolist.keys()
        random.shuffle(randomlist)

        # use as less as possible spacecrafts if last cargo's are reached
        if last_cargolist == True:
            if last_cargos_weight < 6500 and last_cargos_space < 15:
                spacecrafts = [tianzhou[cargoloop]]
            elif last_cargos_weight < 3400 and last_cargos_space < 42:
                spacecrafts = [dragon[cargoloop]]
            elif last_cargos_weight < 9900 and last_cargos_space < 57:
                spacecrafts = [tianzhou[cargoloop], dragon[cargoloop]]
            elif last_cargos_weight < 15000 and last_cargos_space < 71:
                spacecrafts = [kounotori[cargoloop], tianzhou[cargoloop], dragon[cargoloop]]
            elif last_cargolist == True:
                spacecrafts = [verne[cargoloop], progress[cargoloop], kounotori[cargoloop], tianzhou[cargoloop], dragon[cargoloop]]
        # use all spacecrafts if there are a lot of cargo's left
        else:
            spacecrafts = [verne[cargoloop], progress[cargoloop], kounotori[cargoloop], tianzhou[cargoloop], dragon[cargoloop]]

        ## fill spacecrafts with cargo by putting item in spacecrafts with the same ratio as the average ratio of the cargo together
        for item in range(1, optimized_items + 1):

            ## setup variables for iterations
            randomcargo = randomlist[item-1]
            best_fit = 10000
            check_if_fits = False
            bestspacecraft = ''

            ## iterate over spacecrafts to check where item fits best
            for craft in spacecrafts:
                if craft.check_craft(cargolist[randomcargo][weight], cargolist[randomcargo][space]):
                    check_if_fits = True
                    diff = abs(craft.density - (craft.cargocount * craft.meancargoratio + optimized_cargolist[randomcargo][ratio])/(craft.cargocount+1))
                    if diff < best_fit:
                        best_fit = diff
                        bestspacecraft = craft

            ## add cargo to spacecraft which fits best
            if check_if_fits == True:
                bestspacecraft.load_cargo(optimized_cargolist[randomcargo][ratio], optimized_cargolist[randomcargo][weight], optimized_cargolist[randomcargo][space], randomcargo)

        totalwastedweight = 0; totalwastedspace = 0; loadeditems = 0

        ## find out how good the cargo is loaded
        for craft in spacecrafts:
            totalwastedweight += craft.wastedweight
            totalwastedspace += craft.wastedspace
            loadeditems += craft.cargocount
            ##print(craft.cargolist)

        unloadeditems = optimized_items - loadeditems

        ##print('total wasted weight: ' + str(totalwastedweight))
        ##print('total wasted space: ' + str(totalwastedspace))
        ##print(str(unloadeditems) + ' items are not loaded on the spacecrafts.')
        ##print(str(totalwastedweight) + ' kilos are not used.')
        ##print(str(totalwastedspace) + ' m3 are not used.')

        ## determine a score for the filled spacecraft, the lower the score the better.
        score = totalwastedweight * totalwastedspace

        ## save best score and the cargo's that are used to reach this score
        if score < bestscore:
            bestscore = score
            bestscore_cargo = []
            print('Score: ' + str(bestscore) + ', #: ' + str(bruteforce) +  ', Wasted Space: ' + str(totalwastedspace) + ', Wasted Weight: ' + str(totalwastedweight) + ', Unloaded Items: ' + str(unloadeditems))
            for craft in spacecrafts:
                #print('SpaceCraft: ' + str(craft.sc_id) + ', Wasted Space: ' + str(craft.wastedspace) + ', Wasted Weight: ' + str(craft.wastedweight))
                #print(craft.cargolist)
                bestscore_cargo.extend(craft.cargolist)
            #print('Randomlist: ' + str(randomlist))
            #print('Crafts used with best score: ' + str(bestscore_cargo))
    print('The following cargo has been packed:' + str(bestscore_cargo))
    print('')

    if len(cargolist) == 0:
        print('The total number of used Spacecrafts is: ' + str(int(count_total_spacecrafts_per_country)*5))
        break
