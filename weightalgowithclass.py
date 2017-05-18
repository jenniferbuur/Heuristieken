import itertools
import Spacecrafts as sc
import random

# initialise spacecrafts in class
cygnus = sc.Spacecrafts("Cygnus", 2000, 18.9)
verne = sc.Spacecrafts("Verne", 2300, 13.1)
progress = sc.Spacecrafts("Progress", 2400, 7.6)
kounotori = sc.Spacecrafts("Kounotori", 5200, 14)
tianzhou = sc.Spacecrafts("TianZhou", 6500, 15)
dragon = sc.Spacecrafts("Dragon", 3400, 42)

## initiate variables
items = 0; weight = 0; space = 1; ratio = 2; cargocount = 3; av_ratio = 4
cargolist = {}

## insert data into dictionary
with open('CargoLists/CargoList2.txt', 'rU') as f:
    for line in f:
        split = line.split()
        key = split[0][4:]
        if len(split) == 3:
            split[2] = split[2].replace(",", ".")
            cargolist[key] = [float(split[1]), float(split[2])]
            cargolist[key].append(cargolist[key][weight]/cargolist[key][space])
            items += 1

## sort dictionary from light to heavy
sortedweight = sorted(cargolist, key = lambda x: [cargolist[x][weight]])
# randomlist = cargolist.keys()
sortedweight = sortedweight[::-1]
all_over_best = [10000, 100]
# sortedweight = randomlist

spacecrafts = [cygnus, verne, progress, kounotori]
best = 10000

for crafts in itertools.permutations(spacecrafts):
    wastedweight = []
    for craft in crafts:
        wastedweight.append(craft.weight)
    for item in sortedweight:
        name = 0
        if cargolist[item][weight] > max(wastedweight):
            break
        for craft in crafts:
            if cargolist[item][weight] <= craft.wastedweight:
                craft.load_cargo(cargolist[item][ratio], cargolist[item][weight], cargolist[item][space], item)
                wastedweight[name] = craft.wastedweight
                break
            else:
                name += 1

    totalwastedweight = 0; totalwastedspace = 0; loadeditems = 0
    for craft in crafts:
        totalwastedweight += craft.wastedweight
        totalwastedspace += craft.wastedspace
        loadeditems += craft.cargocount
        craft.set_original()
    unloadeditems = items - loadeditems
    if totalwastedweight < best:
        best = totalwastedweight
        bestitems = unloadeditems
        print('Unloaded Items: ' + str(bestitems) + ', Wasted Weight: ' + str(best) + '.')
