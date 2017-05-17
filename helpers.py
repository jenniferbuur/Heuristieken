import itertools
import Spacecrafts as cs

def weight(cargolist, spacecrafts):
    sortedweight = sorted(cargolist, key = lambda x: [cargolist[x][0]])
    sortedlist = sortedweight[::-1]
    for crafts in itertools.permutations(spacecrafts):
        wastedweight = []
        for craft in crafts:
            wastedweight.append(craft.weight)
        for item in sortedlist:
            name = 0
            if cargolist[item][0] > max(wastedweight):
                break
            for craft in crafts:
                if cargolist[item][0] <= craft.wastedweight:
                    craft.load_cargo(cargolist[item][2], cargolist[item][0], cargolist[item][1], item)
                    wastedweight[name] = craft.wastedweight
                    break
                else:
                    name += 1
    return

def ratio(cargolist, spacecrafts, items):
    for item in cargolist:
        best = ''; best_fit = 10000; check = False
        for craft in spacecrafts:
            if craft.check_craft(cargolist[item][0], cargolist[item][1]):
                check = True
                diff = abs(craft.density - (craft.cargocount * craft.meancargoratio + cargolist[item][2])/(craft.cargocount+1))
                if diff < best_fit:
                    best_fit = diff
                    best = craft
        if check == True:
            best.load_cargo(cargolist[item][2], cargolist[item][0], cargolist[item][1], item)
    return

def solution(spacecrafts, items):
    totalwastedweight = 0; totalwastedspace = 0; loadeditems = 0
    for craft in spacecrafts:
        totalwastedweight += craft.wastedweight
        totalwastedspace += craft.wastedspace
        loadeditems += craft.cargocount
    unloadeditems = items - loadeditems
    return totalwastedweight, totalwastedspace, unloadeditems

def optimize(cargolist, spacecrafts, items):
    sortedlist = sorted(cargolist, key=lambda x: [cargolist[x][ratio]], reverse = True)
    max_weight = 0; max_space = 0; optimizedlist = {}; total_cargospace = 0; total_cargoweight = 0; optimizeditems = 0
    for craft in spacecrafts:
        max_weight += craft.weight
        max_space += craft.space
    for item in range(0, items):
        if total_cargospace < max_space and total_cargoweight < max_weight:
            optimizedlist[sortedlist[item][0]] = []
    return optimizedlist, optimizeditems
