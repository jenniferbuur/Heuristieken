import itertools
import Spacecrafts as cs
import random

"""
This file has several functions neccessary for main.py
"""

"""
This function import a cargolist an puts it into a dictionary
"""
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

"""
This function is the algorithm used to fill spacecrafts based on weight
"""
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

"""
This function is the algorithm used to fill spacecrafts based on weight and space
"""
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

"""
This function determines the solution based on whats loaded into the spacecrafts
"""
def solution(spacecrafts, items):
    totalwastedweight = 0; totalwastedspace = 0; loadeditems = 0
    for craft in spacecrafts:
        totalwastedweight += craft.wastedweight
        totalwastedspace += craft.wastedspace
        loadeditems += craft.cargocount
        craft.set_original()
    unloadeditems = items - loadeditems
    return totalwastedweight, totalwastedspace, unloadeditems

"""
This function determines the score for exercises D and E
and gives the solution based on whats loaded into the spacecrafts
"""
def score(spacecrafts, items):
    totalwastedweight = 0; totalwastedspace = 0; loadeditems = 0
    for craft in spacecrafts:
        totalwastedweight += craft.wastedweight
        totalwastedspace += craft.wastedspace
        loadeditems += craft.cargocount
    unloadeditems = items - loadeditems
    score = totalwastedweight * totalwastedspace
    return score, totalwastedweight, totalwastedspace, unloadeditems

"""
This function optimizes the list for exercises B and C based on density
and return a dictionary with all items in the optimized list
The optimized list filled from biggest density to smallest, hereby iterating over every item
"""
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

"""
This function shortens the list for exercises D and E based on density
and return a dictionary with all items in the shortened list
The shortened list filled randomly, hereby iterating over every item
"""
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

"""
This function determines which spacecrafts to use when the lenght of the shortened list
is equal to the items left, hereby minimalizing the number of spacecrafts used in D and E 
"""
def spacecrafts(last_weight, last_space, spacecrafts):
    if last_weight < spacecrafts[0].weight and last_space < spacecrafts[0].volume:
        spacecrafts = spacecrafts[0]
    elif last_weight < spacecrafts[1].weight and last_space < spacecrafts[1].volume:
        spacecrafts = spacecrafts[1]
    elif last_weight < spacecrafts[2].weight and last_space < spacecrafts[2].volume:
        spacecrafts = spacecrafts[2]
    elif last_weight < spacecrafts[3].weight and last_space < spacecrafts[3].volume:
        spacecrafts = spacecrafts[3]
    elif last_weight < spacecrafts[4].weight and last_space < spacecrafts[4].volume:
        spacecrafts = spacecrafts[4]
    elif last_weight < spacecrafts[5].weight and last_space < spacecrafts[5].volume:
        spacecrafts = spacecrafts[5]
    elif last_weight < spacecrafts[4].weight + spacecrafts[5].weight and last_space < spacecrafts[4].volume +spacecrafts[5].volume:
        spacecrafts = [spacecrafts[4], spacecrafts[5]]
    elif last_weight < spacecrafts[3].weight + spacecrafts[4].weight + spacecrafts[5].weight and last_space < spacecrafts[3].volume + spacecrafts[4].volume + spacecrafts[5].volume:
        spacecrafts = [spacecrafts[3], spacecrafts[4], spacecrafts[5]]
    else:
        spacecrafts = [spacecrafts[1], spacecrafts[2], spacecrafts[3], spacecrafts[4], spacecrafts[5]]
    return spacecrafts
