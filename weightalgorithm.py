
import itertools

cargolist = {}
spacecrafts = {}

## spacecrafts
spacecrafts['Cygnus'] = [2000, 18.9]
spacecrafts['Verne'] = [2300, 13.1]
spacecrafts['Progress'] = [2400, 7.6]
spacecrafts['Kounotori'] = [5200, 14]
## spacecrafts['TianZhou'] = [6500, 15]
## spacecrafts['Dragon'] = [3400, 42]

## initiate variables
items = 0; weight = 0; space = 1; ratio = 2

## insert data into dictionary
with open('/Users/jenniferbuur1/Documents/universiteit/UvAAEO/MinorProgrammeren/Heuristieken/Heuristieken/CargoLists/CargoList2.txt', 'rU') as f:
    for line in f:
            split = line.split()
            key = split[0][4:]
            if len(split) == 3:
                split[2] = split[2].replace(",", ".")
                cargolist[key] = [float(split[1]), float(split[2])]
                cargolist[key].append(cargolist[key][weight]/cargolist[key][space])
                items += 1

print(cargolist)
print(spacecrafts)
print(items)

## sort dictionary from light to heavy
sortedweight = sorted(cargolist, key = lambda x: [cargolist[x][weight]])
print(sortedweight)
sortedratio = sorted(cargolist, key = lambda x: [cargolist[x][ratio]])
print(sortedratio)

names = []
for key in spacecrafts:
    names.append(key)

print(names)

possibilities = itertools.permutations(names)
loadingsheme = {}
lastitem = 0
weightwasted = []
best = {}
count = 0
leftbehind = items
minimal = 1000

print('point reached 1')

for x in itertools.permutations(names):
    wastedweight = []
    for i in range(0,len(x)):
        wastedweight.append(spacecrafts[x[i]][0])
    while cargolist[sortedweight[0]][0] <= max(wastedweight):
        for spacecraft in range(0,len(wastedweight)):
            for item in range(lastitem,items):
                cargoitem = items - item - 1
                if cargolist[sortedweight[cargoitem]][weight] <= wastedweight[spacecraft]:
                    if (spacecraft+1) in loadingsheme.keys():
                        loadingsheme[spacecraft+1].append(sortedweight[cargoitem])
                    else:
                        loadingsheme[spacecraft+1] = [sortedweight[cargoitem]]
                    wastedweight[spacecraft] -= cargolist[sortedweight[cargoitem]][weight]
                    leftbehind -= 1
                else:
                    lastitem = item
                    break
    for i in range(0,len(x)):
        print('Spacecraft ' + str(x[i]) + ' must be filled with cargos: ' + str(loadingsheme[i+1]) + '.')
        print('Therefore ' + str(wastedweight[i]) + ' kilos are wasted.')
    print('In total there are ' + str(sum(wastedweight)) + ' kilos are wasted and ' + str(leftbehind) + ' items are left behind.')
    loadingsheme = {}
    lastitem = 0
    weightwasted.append(sum(wastedweight))
    if sum(wastedweight) < minimal:
        minimal = sum(wastedweight)
        best = {}
        best[count] = [x, leftbehind, loadingsheme]
    elif sum(wastedweight) == minimal:
        best[count] = [x, leftbehind, loadingsheme]
    count += 1
    leftbehind = items

if len(best) > 1:
    print('There are multiple permutations with a minimal wasted weight of ' + str(minimal) + ' kilos.')
    for key in best:
        print('Permutation ' + str(key) + ': ' + str(best[key][0]) + ' with ' + str(best[key][1]) + '.')
        for i in range(0,4):
            print('Spacecraft ' + str(best[key][0][i]) + ': ' + str(best[key][2][i+1]))
else:
    print('The best permutation of spacecrafts is ' + str(best) + ' with the minimal wasted weight of ' + str(minimal) + ' kilos.')
