import itertools
import Spacecrafts as sc
# import CargoClass as cc

# initialise spacecrafts in class
cygnus = sc.Spacecrafts("Cygnus", 2000, 18.9)
verne = sc.Spacecrafts("Verne", 2300, 13.1)
progress = sc.Spacecrafts("Progress", 2400, 7.6)
kounotori = sc.Spacecrafts("Kounotori", 5200, 14)
# tianzhou = sc.Spacecrafts("TianZhou", 6500, 15)
# dragon = sc.Spacecrafts("Dragon", 3400, 42)

## initiate variables
items = 0; weight = 0; space = 1; ratio = 2; cargocount = 3; av_ratio = 4
cargolist = {}

## insert cargo data into dictionary
## insert data into dictionary
with open('CargoLists/CargoList1.txt', 'rU') as f:
    for line in f:
        split = line.split()
        key = split[0][4:]
        if len(split) == 3:
            split[2] = split[2].replace(",", ".")
            cargolist[key] = [float(split[1]), float(split[2])]
            cargolist[key].append(cargolist[key][weight]/cargolist[key][space])
            items += 1

spacecrafts = [cygnus, verne, progress, kounotori]
sortedratio = sorted(cargolist, key = lambda x: [cargolist[x][ratio]])


## fill spacecrafts with cargo by putting item in spacecrafts with the same ratio as the average ratio of the cargo together
for item in range(1, items + 1):
    sortedcargo = sortedratio[item - 1]
    best = 10000
    reminder = 0
    bestspacecraft = ''
    for craft in spacecrafts:
        if craft.check_craft(cargolist[sortedcargo][weight], cargolist[sortedcargo][space]):
            reminder = 1
            diff = abs(craft.density - (craft.cargocount * craft.meancargoratio + cargolist[sortedcargo][ratio])/(craft.cargocount+1))
            if diff < best:
                best = diff
                bestspacecraft = craft
    if reminder == 1:
        bestspacecraft.load_cargo(cargolist[sortedcargo][ratio], cargolist[sortedcargo][weight], cargolist[sortedcargo][space], sortedcargo)

totalwastedweight = 0; totalwastedspace = 0; loadeditems = 0

## find out how good the cargo is loaded
for craft in spacecrafts:
    totalwastedweight += craft.wastedweight
    totalwastedspace += craft.wastedspace
    loadeditems += craft.cargocount
    print(craft.cargolist)

unloadeditems = items - loadeditems

print(totalwastedweight)
print(totalwastedspace)
print(str(unloadeditems) + ' items are not loaded on the spacecrafts.')
print(str(totalwastedweight) + ' kilos are not used.')
print(str(totalwastedspace) + ' m3 are not used.')
