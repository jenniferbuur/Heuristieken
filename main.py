# alle functies naar helpers oid verplaatsen!!!!!!!!

import itertools
import Spacecrafts as sc
import helpers as helpers
import random
import Spacemission as sm
# alle lists inladen
# importeer alle classes

weight = 0; space = 1; ratio = 2;

# initialise spacecrafts in class
cygnus = sc.Spacecrafts("Cygnus", 2000, 18.9, "USA")
verne = sc.Spacecrafts("Verne", 2300, 13.1, "Europe")
progress = sc.Spacecrafts("Progress", 2400, 7.6, "Russia")
kounotori = sc.Spacecrafts("Kounotori", 5200, 14, "Japan")
tianzhou = sc.Spacecrafts("TianZhou", 6500, 15, "China")
dragon = sc.Spacecrafts("Dragon", 3400, 42, "USA")

# initializing array with spacecrafts for A, B and C
spacecrafts = [cygnus, verne, progress, kounotori]

# opdracht A (Cargolist 1)
# loading cargo sorted by weight
cargolist = helpers.importlist(1)
items = len(cargolist.keys())
best_weight = 10000
#
# # iterate over permutations
for crafts in itertools.permutations(spacecrafts):
    helpers.weight(cargolist, crafts)
    solution = helpers.solution(crafts, items)
    # remember best solution
    if solution[0] < best_weight:
        best_weight = solution[0]
        best_space = solution[1]
        best_items = solution[2]

print('Wasted weight: ' + str(best_weight) + ', Wasted space: ' + str(best_space) + ', Unloaded cargo: ' + str(best_items) + '.')

# # opdracht B (Cargolist 1)
# # loading cargo sorted by density
sortedlist = sorted(cargolist, key = lambda x: [cargolist[x][2]])
helpers.ratio(cargolist, sortedlist, spacecrafts)
solution = helpers.solution(spacecrafts, items)
print('The solution found by sorting the cargo by density is as follows:')
print('Wasted weight: ' + str(solution[0]) + ', Wasted space: ' + str(solution[1]) + ', Unloaded cargo: ' + str(solution[2]) + '.')

# # partly brute force on shortened cargolist
optimized = helpers.optimize(cargolist, spacecrafts)
bestscore = 10000

for bruteforce in range(0, 100000):
    randomlist = optimized.keys()
    random.shuffle(randomlist)
    helpers.ratio(optimized, randomlist, spacecrafts)
    solution = helpers.solution(spacecrafts, items)
    # score function
    score = solution[0] + 0.01 * solution[2]
    # remember best solution
    if score < bestscore:
        bestscore = score
        print('#: ' + str(bruteforce) + ', Score: ' + str(score))
        print('Wasted weight: ' + str(solution[0]) + ', Wasted space: ' + str(solution[1]) + ', Unloaded cargo: ' + str(solution[2]) + '.')

# # opdracht C (Cargolist 2)
# # loading cargo sorted by weight
cargolist = helpers.importlist(2)
items = len(cargolist.keys())
best_weight = 10000
# iterate over permutations
for crafts in itertools.permutations(spacecrafts):
    helpers.weight(cargolist, crafts)
    solution = helpers.solution(crafts, items)
    # remember best solution
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
    # score function
    score = solution[0] + 0.01 * solution[2]
    # remember best solution
    if score < bestscore:
        bestscore = score
        print('#: ' + str(bruteforce) + ', Score: ' + str(score))
        print('Wasted weight: ' + str(solution[0]) + ', Wasted space: ' + str(solution[1]) + ', Unloaded cargo: ' + str(solution[2]) + '.')

# opdracht C (Cargolist 2)
# loading cargo sorted by weight
cargolist = helpers.importlist(2)
items = len(cargolist.keys())
best_weight = 10000
# iterate over permutations
for crafts in itertools.permutations(spacecrafts):
    helpers.weight(cargolist, crafts)
    solution = helpers.solution(crafts, items)
    # remember best solution
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
    # score function
    score = solution[0] + 0.01 * solution[2]
    # remember best solution
    if score < bestscore:
        bestscore = score
        print('#: ' + str(bruteforce) + ', Score: ' + str(score))
        print('Wasted weight: ' + str(solution[0]) + ', Wasted space: ' + str(solution[1]) + ', Unloaded cargo: ' + str(solution[2]) + '.')

# opdracht D
# loading a massive cargolist (3) into multiple spacecrafts
# with this every country has to send an equal amount with a maximum difference of 1
cygnus = []; verne = []; progress = []; kounotori = []; tianzhou = []; dragon = []
packed_cargo = []; speed = 1000; used_spacecrafts = []; first_lastlist = False; count = 0

# load cargolist
cargolist = helpers.importlist(3); items = len(cargolist.keys())
countries = [sm.Spacemission("USA"), sm.Spacemission("Europe"), sm.Spacemission("Russia"), sm.Spacemission("Japan"), sm.Spacemission("China")]

for cycle in range(0, 100):
    print('Cycle: ' + str(cycle))
    bestscore = 99999999;

    # make new spacecrafts for every new cycle
    cygnus.append(sc.Spacecrafts("Cygnus", 2000, 18.9, "USA"))
    verne.append(sc.Spacecrafts("Verne", 2300, 13.1, "Europe"))
    progress.append(sc.Spacecrafts("Progress", 2400, 7.6, "Russia"))
    kounotori.append(sc.Spacecrafts("Kounotori", 5200, 14, "Japan"))
    tianzhou.append(sc.Spacecrafts("TianZhou", 6500, 15, "China"))
    dragon.append(sc.Spacecrafts("Dragon", 3400, 42, "USA"))

    # used spacecrafts for every cycle excluding the last cycle
    spacecrafts = [verne[cycle], progress[cycle], kounotori[cycle], tianzhou[cycle], dragon[cycle]]

    # pull all items packed before
    for item in packed_cargo:
        cargolist.pop(item)

    print('Cargo left: ' + str(len(cargolist)))

    # if there are no cargoitems left, break
    if len(cargolist) == 0:
        print('The total number of spacecrafts is: ' + str(len(used_spacecrafts)))
        print(str(used_spacecrafts.count("Cygnus")) + ' of Cygnus, ' + str(used_spacecrafts.count("Verne")) + ' of Verne, ' + str(used_spacecrafts.count("Progress")) + ' of Progress,')
        print(str(used_spacecrafts.count("Kounotori")) + ' of Kounotori, ' + str(used_spacecrafts.count("TianZhou")) + ' of TianZhou, ' + str(used_spacecrafts.count("Dragon")) + ' of Dragon.')
        print('')
        break

    # shorten list and randomize it
    shortened = helpers.shorten(cargolist, spacecrafts)
    randomlist = shortened.keys()
    all_spacecrafts = [cygnus[cycle], verne[cycle], progress[cycle], kounotori[cycle], tianzhou[cycle], dragon[cycle]]

    # if the last cycle has been reached, change spacecrafts
    if len(shortened) == len(cargolist):
        last_weight = 0; last_space = 0; diff = []
        for item in optimized:
            last_weight += optimized[item][weight]
            last_space += optimized[item][space]
        for country in countries:
            diff.append(country.count - count)
        if diff.count(0) == 5:
            spacecrafts = helpers.spacecrafts(last_weight, last_space, all_spacecrafts)
        else:
            for i in range(0, 5):
                if diff[i] == 0:
                    spacecrafts.remove(all_spacecrafts[i+1])

    for craft in spacecrafts:
        for spacemission in countries:
            if spacemission.sm_id == craft.country:
                spacemission.counter()
    count += 1

    # remember all used spacecrafts
    if len(spacecrafts) == 1:
        used_spacecrafts.append(spacecrafts.sc_id)
    else:
        for craft in spacecrafts:
            used_spacecrafts.append(craft.sc_id)

    # start bruteforce
    for bruteforce in range(0, speed):

        # set spacecrafts to original
        if len(spacecrafts) == 1:
            spacecrafts.set_orignal()
        else:
            for craft in spacecrafts:
                craft.set_original()

        random.shuffle(randomlist)

        helpers.ratio(shortened, randomlist, spacecrafts)
        score = helpers.score(spacecrafts, items)

        # remember best score
        if score[0] < bestscore:
            bestscore = score[0]
            packed_cargo = []
            for craft in spacecrafts:
                packed_cargo.extend(craft.cargolist)

    print('The following cargo has been packed: ' + str(packed_cargo))
    print('')

# opdracht E
# the last restriction doesn't matter any more

cygnus = []; verne = []; progress = []; kounotori = []; tianzhou = []; dragon = []
packed_cargo = []; speed = 1000; number_of_sc = 0; used_spacecrafts = []
cargolist = helpers.importlist(3); items = len(cargolist.keys())

for cycle in range(0, 100):
    print('Cycle: ' + str(cycle))
    bestscore = 99999999

    # make new spacecrafts for every new cycle
    cygnus.append(sc.Spacecrafts("Cygnus", 2000, 18.9, "USA"))
    verne.append(sc.Spacecrafts("Verne", 2300, 13.1, "Europe"))
    progress.append(sc.Spacecrafts("Progress", 2400, 7.6, "Russia"))
    kounotori.append(sc.Spacecrafts("Kounotori", 5200, 14, "Japan"))
    tianzhou.append(sc.Spacecrafts("TianZhou", 6500, 15, "China"))
    dragon.append(sc.Spacecrafts("Dragon", 3400, 42, "USA"))

    # take biggest spacecrafts to fill
    spacecrafts = [tianzhou[cycle], dragon[cycle]]
    for item in packed_cargo:
        cargolist.pop(item)
    print('Cargo left: ' + str(len(cargolist)))
    if len(cargolist) == 0:
        print('The total number of spacecrafts is: ' + str(number_of_sc))
        print(str(used_spacecrafts.count("Cygnus")) + ' of Cygnus, ' + str(used_spacecrafts.count("Verne")) + ' of Verne, ' + str(used_spacecrafts.count("Progress")) + ' of Progress,')
        print(str(used_spacecrafts.count("Kounotori")) + ' of Kounotori, ' + str(used_spacecrafts.count("TianZhou")) + ' of TianZhou, ' + str(used_spacecrafts.count("Dragon")) + ' of Dragon.')
        print('')
        break

    shortened = helpers.shorten(cargolist, spacecrafts)
    randomlist = shortened.keys()
    all_spacecrafts = [cygnus[cycle], verne[cycle], progress[cycle], kounotori[cycle], tianzhou[cycle], dragon[cycle]]

    # if last cycle has been reached
    if len(optimized) == len(cargolist):
        last_weight = 0; last_space = 0;
        for item in optimized:
            last_weight += optimized[item][weight]
            last_space += optimized[item][space]
        spacecrafts = helpers.spacecrafts(last_weight, last_space, all_spacecrafts)

    # remember all used spacecrafts
    if len(spacecrafts) == 1:
        used_spacecrafts.append(spacecrafts.sc_id)
    else:
        for craft in spacecrafts:
            used_spacecrafts.append(craft.sc_id)

    # start bruteforce
    for bruteforce in range(0, speed):

        if len(spacecrafts) == 1:
            spacecrafts.set_original()
        else:
            for craft in spacecrafts:
                craft.set_original()

        random.shuffle(randomlist)

        helpers.ratio(shortened, randomlist, spacecrafts)
        score = helpers.score(spacecrafts, items)

        # remember best score
        if score[0] < bestscore:
            bestscore = score[0]
            packed_cargo = []
            for craft in spacecrafts:
                packed_cargo.extend(craft.cargolist)

    number_of_sc += len(spacecrafts)
    print('The following cargo has been packed: ' + str(packed_cargo))
    print('')
