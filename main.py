import itertools
import Spacecrafts as sc
import helpers
import random
# alle lists inladen
# importeer alle classes

# alle cargolists in een dictionary
cargolist1 = {}; cargolist2 = {}; cargolist3 = {}
lists = [cargolist1, cargolist2, cargolist3]
nritems = [0, 0, 0]
weight = 0; space = 1; ratio = 2;

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

# opdracht A (Cargolist 1)
# loading cargo sorted by weight
best_weight = 10000
for crafts in itertools.permutations(spacecrafts):
    helpers.weight(cargolist1, crafts)
    solution = helpers.solution(crafts, items1)
    if solution[0] < best_weight:
        best_weight = solution[0]
        best_space = solution[1]
        best_items = solution[2]

print('Wasted weight: ' + str(best_weight) + ', Wasted space: ' + str(best_space) + ', Unloaded cargo: ' + str(best_items) + '.')

# opdracht B (Cargolist 1)
# loading cargo sorted by density
sortedlist = sorted(cargolist1, key = lambda x: [cargolist1[x][2]])
helpers.ratio(cargolist1, sortedlist, spacecrafts)
solution = helpers.solution(spacecrafts, items1)
print('The solution found by sorting the cargo by density is as follows:')
print('Wasted weight: ' + str(solution[0]) + ', Wasted space: ' + str(solution[1]) + ', Unloaded cargo: ' + str(solution[2]) + '.')

# partly brute force on shortened cargolist
optimized = helpers.optimize(cargolist1, spacecrafts)
bestscore = 10000
for bruteforce in range(0, 100000):
    randomlist = optimized.keys()
    random.shuffle(randomlist)
    helpers.ratio(optimized, randomlist, spacecrafts)
    solution = helpers.solution(spacecrafts, items1)
    score = solution[0] + 0.01 * solution[2]
    if score < bestscore:
        bestscore = score
        print('#: ' + str(bruteforce) + ', Score: ' + str(score))
        print('Wasted weight: ' + str(solution[0]) + ', Wasted space: ' + str(solution[1]) + ', Unloaded cargo: ' + str(solution[2]) + '.')

# opdracht C (Cargolist 2)
# loading cargo sorted by weight
best_weight = 10000
for crafts in itertools.permutations(spacecrafts):
    helpers.weight(cargolist2, crafts)
    solution = helpers.solution(crafts, items2)
    if solution[0] < best_weight:
        best_weight = solution[0]
        best_space = solution[1]
        best_items = solution[2]

print('Wasted weight: ' + str(best_weight) + ', Wasted space: ' + str(best_space) + ', Unloaded cargo: ' + str(best_items) + '.')

# loading cargo sorted by density
sortedlist = sorted(cargolist2, key = lambda x: [cargolist2[x][2]])
helpers.ratio(cargolist2, sortedlist, spacecrafts)
solution = helpers.solution(spacecrafts, items2)
print('The solution found by sorting the cargo by density is as follows:')
print('Wasted weight: ' + str(solution[0]) + ', Wasted space: ' + str(solution[1]) + ', Unloaded cargo: ' + str(solution[2]) + '.')

# partly brute force on shortened cargolist
optimized = helpers.optimize(cargolist2, spacecrafts)
bestscore = 10000
for bruteforce in range(0, 10000):
    randomlist = optimized.keys()
    random.shuffle(randomlist)
    helpers.ratio(optimized, randomlist, spacecrafts)
    solution = helpers.solution(spacecrafts, items2)
    score = solution[0] + 0.01 * solution[2]
    if score < bestscore:
        bestscore = score
        print('#: ' + str(bruteforce) + ', Score: ' + str(score))
        print('Wasted weight: ' + str(solution[0]) + ', Wasted space: ' + str(solution[1]) + ', Unloaded cargo: ' + str(solution[2]) + '.')
