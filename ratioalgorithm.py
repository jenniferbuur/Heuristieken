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
items = 0; weight = 0; space = 1; ratio = 2; cargocount = 3; av_ratio = 4

## insert data into dictionary
with open('/Users/jenniferbuur1/Documents/universiteit/UvAAEO/MinorProgrammeren/Heuristieken/Heuristieken/CargoLists/CargoList1.txt', 'rU') as f:
    for line in f:
            split = line.split()
            key = split[0][4:]
            if len(split) == 3:
                split[2] = split[2].replace(",", ".")
                cargolist[key] = [float(split[1]), float(split[2])]
                cargolist[key].append(cargolist[key][weight]/cargolist[key][space])
                items += 1

wastedweight = {}; wastedspace = {}

## fill spacecrafts dictionary with extra variables
for key in spacecrafts:
    spacecrafts[key].append(spacecrafts[key][weight]/spacecrafts[key][space])
    spacecrafts[key].append(0)
    spacecrafts[key].append(0)
    wastedweight[key] = spacecrafts[key][weight]
    wastedspace[key] = spacecrafts[key][space]

## fill spacecrafts with cargo by putting item in spacecrafts with the same ratio as the average ratio of the cargo together
for item in cargolist:
    best = 10000
    reminder = 0
    bestspacecraft = ''
    for name in spacecrafts:
        if cargolist[item][weight] <= wastedweight[name] and cargolist[item][space] <= wastedspace[name]:
            reminder = 1
            diff = abs(spacecrafts[name][ratio] - (spacecrafts[name][cargocount]*spacecrafts[name][av_ratio]+cargolist[item][ratio])/(spacecrafts[name][cargocount]+1))
            if diff < best:
                best = diff
                bestspacecraft = name
    if reminder == 1:
        spacecrafts[bestspacecraft][cargocount] += 1
        spacecrafts[bestspacecraft][av_ratio] = (spacecrafts[bestspacecraft][cargocount]*spacecrafts[bestspacecraft][av_ratio]+cargolist[item][ratio])/(spacecrafts[bestspacecraft][cargocount]+1)
        wastedweight[bestspacecraft] -= cargolist[item][weight]
        wastedspace[bestspacecraft] -= cargolist[item][space]

totalwastedweight = 0; totalwastedspace = 0; loadeditems = 0

## find out how good the cargo is loaded
for name in spacecrafts:
    totalwastedweight += wastedweight[name]
    totalwastedspace += wastedspace[name]
    loadeditems += spacecrafts[name][cargocount]

unloadeditems = items - loadeditems
print(wastedweight)
print(wastedspace)
print(str(unloadeditems) + ' items are not loaded on the spacecrafts.')
print(str(totalwastedweight) + ' kilos are not used.')
print(str(totalwastedspace) + ' m3 are not used.')
