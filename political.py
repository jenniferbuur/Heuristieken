# just a test run to see if opdracht D can be solved

import itertools
import Spacecrafts as sc
import helpers
import random

cargolist1 = {}; cargolist2 = {}; cargolist3 = {}
lists = [cargolist1, cargolist2, cargolist3]
nritems = [0, 0, 0]
weight = 0; space = 1; ratio = 2;

# open the cargolists and replace the comma with a period
for i in range(1,4):
    with open('CargoLists/CargoList' + str(i) + '.txt', 'rU') as f:
        for line in f:
            split = line.split()
            key = split[0][4:]
            if len(split) == 3:
                split[2] = split[2].replace(",", ".")
                lists[i-1][key] = [float(split[1]), float(split[2])]
                lists[i-1][key].append(lists[i-1][key][weight]/lists[i-1][key][space])
                nritems[i-1] += 1

items1 = nritems[0]; items2 = nritems[1]; items3 = nritems[2]

# initialise spacecrafts in class
cygnus = sc.Spacecrafts("Cygnus", 2000, 18.9)
verne = sc.Spacecrafts("Verne", 2300, 13.1)
progress = sc.Spacecrafts("Progress", 2400, 7.6)
kounotori = sc.Spacecrafts("Kounotori", 5200, 14)
tianzhou = sc.Spacecrafts("TianZhou", 6500, 15)
dragon = sc.Spacecrafts("Dragon", 3400, 42)

# initializing array with spacecrafts for A, B and C
spacecrafts = [cygnus, verne, progress, kounotori]

# sorting list by ratio and load in 
sortedlist = sorted(cargolist2, key = lambda x: [cargolist2[x][2]])
helpers.ratio(cargolist2, sortedlist, spacecrafts)
solution = helpers.solution(spacecrafts, items2)
print('The solution found by sorting the cargo by density is as follows:')
print('Wasted weight: ' + str(solution[0]) + ', Wasted space: ' + str(solution[1]) + ', Unloaded cargo: ' + str(solution[2]) + '.')
