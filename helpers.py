import itertools
import Spacecrafts as cs

def weight(cargolist, spacecrafts):
    sortedlist = sorted(cargolist, key = lambda x: [cargolist[x][0]], reverse = True)
    wastedweight = []
    for craft in spacecrafts:
        wastedweight.append(craft.weight)
    for item in sortedlist:
        name = 0
        if cargolist[item][0] > max(wastedweight):
            break
        for craft in spacecrafts:
            if cargolist[item][0] <= craft.wastedweight:
                craft.load_cargo(cargolist[item][2], cargolist[item][0], cargolist[item][1], item)
                wastedweight[name] = craft.wastedweight
                break
            else:
                name += 1
    return

def ratio(cargolist, keyslist, spacecrafts):
    for item in keyslist:
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
        craft.set_original()
    unloadeditems = items - loadeditems
    return totalwastedweight, totalwastedspace, unloadeditems

def optimize(cargolist, spacecrafts):
    sortedlist = sorted(cargolist, key=lambda x: [cargolist[x][2]], reverse = True)
    max_weight = 0; max_space = 0; optimizedlist = {}; total_cargospace = 0; total_cargoweight = 0
    for craft in spacecrafts:
        max_weight += craft.weight
        max_space += craft.volume
    for item in sortedlist:
        if total_cargospace < max_space and total_cargoweight < max_weight:
            optimizedlist[item] = [cargolist[item][0], cargolist[item][1], cargolist[item][2]]
            total_cargoweight += cargolist[item][0]
            total_cargospace += cargolist[item][1]
    return optimizedlist
