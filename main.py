# alle functies naar helpers oid verplaatsen!!!!!!!!

import itertools
import Spacecrafts as sc
import helpers as helpers
import random
# alle lists inladen
# importeer alle classes

<<<<<<< Updated upstream
=======
# alle cargolists in een dictionary
cargolist1 = {}; cargolist2 = {}; cargolist3 = {}
lists = [cargolist1, cargolist2, cargolist3]
nritems = [0, 0, 0]
weight = 0; space = 1; ratio = 2;

# open the cargolists and replace the comma with a period and puts it in dictionaries for each cargolist
# deze ook naar helpers?
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

>>>>>>> Stashed changes
# initialise spacecrafts in class
cygnus = sc.Spacecrafts("Cygnus", 2000, 18.9)
verne = sc.Spacecrafts("Verne", 2300, 13.1)
progress = sc.Spacecrafts("Progress", 2400, 7.6)
kounotori = sc.Spacecrafts("Kounotori", 5200, 14)
tianzhou = sc.Spacecrafts("TianZhou", 6500, 15)
dragon = sc.Spacecrafts("Dragon", 3400, 42)

# initializing array with spacecrafts for A, B and C
spacecrafts = [cygnus, verne, progress, kounotori]

# opdracht A (Cargolist 1)
# loading cargo sorted by weight
cargolist = helpers.importlist(1)
items = len(cargolist.keys())
best_weight = 10000
for crafts in itertools.permutations(spacecrafts):
    helpers.weight(cargolist, crafts)
    solution = helpers.solution(crafts, items)
    if solution[0] < best_weight:
        best_weight = solution[0]
        best_space = solution[1]
        best_items = solution[2]

print('Wasted weight: ' + str(best_weight) + ', Wasted space: ' + str(best_space) + ', Unloaded cargo: ' + str(best_items) + '.')

# opdracht B (Cargolist 1)
# loading cargo sorted by density
sortedlist = sorted(cargolist, key = lambda x: [cargolist[x][2]])
helpers.ratio(cargolist, sortedlist, spacecrafts)
solution = helpers.solution(spacecrafts, items)
print('The solution found by sorting the cargo by density is as follows:')
print('Wasted weight: ' + str(solution[0]) + ', Wasted space: ' + str(solution[1]) + ', Unloaded cargo: ' + str(solution[2]) + '.')

# partly brute force on shortened cargolist
optimized = helpers.optimize(cargolist, spacecrafts)
bestscore = 10000
<<<<<<< Updated upstream
for bruteforce in range(0, 1):
=======
# eventueel functie van maken in algoritmes zodat je geen for loops meer hebt in main
# want is eigenlijk een algoritme
for bruteforce in range(0, 100000):
>>>>>>> Stashed changes
    randomlist = optimized.keys()
    random.shuffle(randomlist)
    helpers.ratio(optimized, randomlist, spacecrafts)
    solution = helpers.solution(spacecrafts, items)
    score = solution[0] + 0.01 * solution[2]
    if score < bestscore:
        bestscore = score
        print('#: ' + str(bruteforce) + ', Score: ' + str(score))
        print('Wasted weight: ' + str(solution[0]) + ', Wasted space: ' + str(solution[1]) + ', Unloaded cargo: ' + str(solution[2]) + '.')

# opdracht C (Cargolist 2)
# loading cargo sorted by weight
cargolist = helpers.importlist(2)
items = len(cargolist.keys())
best_weight = 10000
for crafts in itertools.permutations(spacecrafts):
    helpers.weight(cargolist, crafts)
    solution = helpers.solution(crafts, items)
    if solution[0] < best_weight:
        best_weight = solution[0]
        best_space = solution[1]
        best_items = solution[2]

print('Wasted weight: ' + str(best_weight) + ', Wasted space: ' + str(best_space) + ', Unloaded cargo: ' + str(best_items) + '.')

# loading cargo sorted by density
sortedlist = sorted(cargolist, key = lambda x: [cargolist[x][2]])
helpers.ratio(cargolist, sortedlist, spacecrafts)
solution = helpers.solution(spacecrafts, items)
print('The solution found by sorting the cargo by density is as follows:')
print('Wasted weight: ' + str(solution[0]) + ', Wasted space: ' + str(solution[1]) + ', Unloaded cargo: ' + str(solution[2]) + '.')

# partly brute force on shortened cargolist
optimized = helpers.optimize(cargolist, spacecrafts)
bestscore = 10000
for bruteforce in range(0, 1):
    randomlist = optimized.keys()
    random.shuffle(randomlist)
    helpers.ratio(optimized, randomlist, spacecrafts)
    solution = helpers.solution(spacecrafts, items)
    score = solution[0] + 0.01 * solution[2]
    if score < bestscore:
        bestscore = score
        print('#: ' + str(bruteforce) + ', Score: ' + str(score))
        print('Wasted weight: ' + str(solution[0]) + ', Wasted space: ' + str(solution[1]) + ', Unloaded cargo: ' + str(solution[2]) + '.')

# opdracht D
# loading a massive cargolist (3) into multiple spacecrafts
# with this every country has to send an equal amount with a maximum difference of 1
cygnus = []; verne = []; progress = []; kounotori = []; tianzhou = []; dragon = []
packed_cargo = []; speed = 1000; last_list = False; number_of_sc = 0
cargolist = helpers.importlist(3); items = len(cargolist.keys())

for cycle in range(0, 100):
    print('Cycle: ' + str(cycle))
    bestscore = 99999999

    cygnus.append(sc.Spacecrafts("Cygnus", 2000, 18.9))
    verne.append(sc.Spacecrafts("Verne", 2300, 13.1))
    progress.append(sc.Spacecrafts("Progress", 2400, 7.6))
    kounotori.append(sc.Spacecrafts("Kounotori", 5200, 14))
    tianzhou.append(sc.Spacecrafts("TianZhou", 6500, 15))
    dragon.append(sc.Spacecrafts("Dragon", 3400, 42))

    spacecrafts = [verne[cycle], progress[cycle], kounotori[cycle], tianzhou[cycle], dragon[cycle]]
    for item in packed_cargo:
        cargolist.pop(item)

    print('Cargo left: ' + str(len(cargolist)))
    if len(cargolist) == 0:
        print('The total number of spacecrafts is: ' + str(number_of_sc))
        print('')
        break

    shortened = helpers.shorten(cargolist, spacecrafts)
    randomlist = shortened.keys()
    all_spacecrafts = [cygnus[cycle], verne[cycle], progress[cycle], kounotori[cycle], tianzhou[cycle], dragon[cycle]]

    if len(optimized) == len(cargolist):
        last_list = True; last_weight = 0; last_space = 0;
        for item in optimized:
            last_weight += optimized[item][weight]
            last_space += optimized[item][space]

    if last_list == True:
        spacecrafts = helpers.spacecrafts(last_weight, last_space, all_spacecrafts)

    for bruteforce in range(0, speed):

        if len(spacecrafts) == 1:
            spacecrafts.set_orignal()
        else:
            for craft in spacecrafts:
                craft.set_original()

        random.shuffle(randomlist)

        helpers.ratio(shortened, randomlist, spacecrafts)
        score = helpers.score(spacecrafts, items)

        if score[0] < bestscore:
            bestscore = score[0]
            packed_cargo = []
            # print('#: ' + str(bruteforce) + ', Score: ' + str(score[0]))
            # print('Wasted weight: ' + str(score[1]) + ', Wasted space: ' + str(score[2]) + '.')
            for craft in spacecrafts:
                packed_cargo.extend(craft.cargolist)

    number_of_sc += len(spacecrafts)
    print('The following cargo has been packed: ' + str(packed_cargo))
    print('')

# opdracht E
# the last restriction doesn't matter any more

cygnus = []; verne = []; progress = []; kounotori = []; tianzhou = []; dragon = []
packed_cargo = []; speed = 1000; last_list = False; number_of_sc = 0
cargolist = helpers.importlist(3); items = len(cargolist.keys())

for cycle in range(0, 100):
    print('Cycle: ' + str(cycle))
    bestscore = 99999999

    cygnus.append(sc.Spacecrafts("Cygnus", 2000, 18.9))
    verne.append(sc.Spacecrafts("Verne", 2300, 13.1))
    progress.append(sc.Spacecrafts("Progress", 2400, 7.6))
    kounotori.append(sc.Spacecrafts("Kounotori", 5200, 14))
    tianzhou.append(sc.Spacecrafts("TianZhou", 6500, 15))
    dragon.append(sc.Spacecrafts("Dragon", 3400, 42))

    # aanpassen op hoe je wil indelen, met resticties e.d.
    spacecrafts = [tianzhou[cycle], dragon[cycle]]
    for item in packed_cargo:
        cargolist.pop(item)
    print('Cargo left: ' + str(len(cargolist)))
    if len(cargolist) == 0:
        print('The total number of spacecrafts is: ' + str(number_of_sc))
        print('')
        break

    shortened = helpers.shorten(cargolist, spacecrafts)
    randomlist = shortened.keys()
    all_spacecrafts = [cygnus[cycle], verne[cycle], progress[cycle], kounotori[cycle], tianzhou[cycle], dragon[cycle]]

    if len(optimized) == len(cargolist):
        last_list = True; last_weight = 0; last_space = 0;
        for item in optimized:
            last_weight += optimized[item][weight]
            last_space += optimized[item][space]

    if last_list == True:
        spacecrafts = helpers.spacecrafts(last_weight, last_space, all_spacecrafts)

    for bruteforce in range(0, speed):

        if len(spacecrafts) == 1:
            spacecrafts.set_original()
        else:
            for craft in spacecrafts:
                craft.set_original()

        random.shuffle(randomlist)

        helpers.ratio(shortened, randomlist, spacecrafts)
        score = helpers.score(spacecrafts, items)

        if score[0] < bestscore:
            bestscore = score[0]
            packed_cargo = []
            # print('#: ' + str(bruteforce) + ', Score: ' + str(score[0]))
            # print('Wasted weight: ' + str(score[1]) + ', Wasted space: ' + str(score[2]) + '.')
            for craft in spacecrafts:
                packed_cargo.extend(craft.cargolist)

    number_of_sc += len(spacecrafts)
    print('The following cargo has been packed: ' + str(packed_cargo))
    print('')
