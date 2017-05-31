import itertools
import Spacecrafts as cs
import random

def importlist(number):
    cargolist = {}; items = 0
    with open('CargoLists/CargoList' + str(number) + '.txt', 'rU') as f:
        for line in f:
            split = line.split()
            key = split[0][4:]
            if len(split) == 3:
                split[2] = split[2].replace(",", ".")
                cargolist[key] = [float(split[1]), float(split[2])]
                cargolist[key].append(cargolist[key][0]/cargolist[key][1])
    return cargolist

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

def score(spacecrafts, items):
    totalwastedweight = 0; totalwastedspace = 0; loadeditems = 0
    for craft in spacecrafts:
        totalwastedweight += craft.wastedweight
        totalwastedspace += craft.wastedspace
        loadeditems += craft.cargocount
    unloadeditems = items - loadeditems
    score = totalwastedweight * totalwastedspace
    return score, totalwastedweight, totalwastedspace, unloadeditems

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

def shorten(cargolist, spacecrafts):
    randomlist = cargolist.keys()
    random.shuffle(randomlist)
    max_weight = 0; max_space = 0; optimizedlist = {}; total_cargospace = 0; total_cargoweight = 0
    for craft in spacecrafts:
        max_weight += craft.weight
        max_space += craft.volume
    for item in randomlist:
        if total_cargospace < max_space and total_cargoweight < max_weight:
            optimizedlist[item] = [cargolist[item][0], cargolist[item][1], cargolist[item][2]]
            total_cargoweight += cargolist[item][0]
            total_cargospace += cargolist[item][1]
    return optimizedlist

def spacecrafts(last_weight, last_space, spacecrafts):
    if last_weight < 2000 and last_space < 18.9:
        spacecrafts = spacecrafts[0]
    elif last_weight < 2300 and last_space < 13.1:
        spacecrafts = spacecrafts[1]
    elif last_weight < 2400 and last_space < 7.6:
        spacecrafts = spacecrafts[2]
    elif last_weight < 5200 and last_space < 14:
        spacecrafts = spacecrafts[3]
    elif last_weight < 6500 and last_space < 15:
        spacecrafts = spacecrafts[4]
    elif last_weight < 3400 and last_space < 42:
        spacecrafts = spacecrafts[5]
    elif last_weight < 9900 and last_space < 57:
        spacecrafts = [spacecrafts[4], spacecrafts[5]]
    elif last_weight < 15000 and last_space < 71:
        spacecrafts = [spacecrafts[3], spacecrafts[4], spacecrafts[5]]
    else:
        spacecrafts = [spacecrafts[1], spacecrafts[2], spacecrafts[3], spacecrafts[4], spacecrafts[5]]
    return spacecrafts
