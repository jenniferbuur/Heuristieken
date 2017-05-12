import itertools
import Spacecrafts as sc
# import Spacefreight as sf
# alle lists inladen
# importeer alle classes

# alle cargolists in een dictionary
cargolist1 = {}; cargolist2 = {}; cargolist3 = {}
items1 = 0; item2 = 0; item3 = 0
lists = [cargolist1, cargolist2, cargolist3]
nritems = [items1, item2, item3]
weight = 0; space = 1; ratio = 2;

for i in range(1,4):
    print('new list')
    with open('CargoLists/CargoList' + str(i) + '.txt', 'rU') as f:
        for line in f:
            split = line.split()
            key = split[0][4:]
            if len(split) == 3:
                split[2] = split[2].replace(",", ".")
                lists[i+1][key] = [float(split[1]), float(split[2])]
                lists[i+1][key].append(lists[i+1][key][weight]/lists[i+1][key][space])
                nritems[i+1] += 1

# initialise spacecrafts in class
cygnus = sc.Spacecrafts("Cygnus", 2000, 18.9)
verne = sc.Spacecrafts("Verne", 2300, 13.1)
progress = sc.Spacecrafts("Progress", 2400, 7.6)
kounotori = sc.Spacecrafts("Kounotori", 5200, 14)
tianzhou = sc.Spacecrafts("TianZhou", 6500, 15)
dragon = sc.Spacecrafts("Dragon", 3400, 42)

spacecrafts = [cygnus, verne, progress, kounotori]

sortedlist = sorted(cargolist, key = lambda x: [cargolist[x][weight]])
solution = weight(spacecrafts, cargolist1, sortedlist, items1)
print('Solution to exercise 1:')
for craft in solution:
    totalwastedweight += craft.wastedweight
    totalwastedspace += craft.wastedspace
    loadeditems += craft.cargocount
    print(craft)
print('Weight wasted: ' + str(totalwastedweight))
print('Space wasted: ' + str(totalwastedspace))
print('Unloaded items: ' + str(items1 - loadeditems))


solution = ratio(spacecrafts, cargolist1, items1)

# nog iets bedenken om misschien niet meegenomen items te onthouden!!!!!!
# functions
def ratio(spacecrafts, cargolist, items):
    for item in range(1, items + 1):
        best = 10000
        reminder = 0
        bestspacecraft = ''
        for craft in spacecrafts:
            if craft.check_craft(cargolist[str(item)][weight], cargolist[str(item)][space]):
                reminder = 1
                diff = abs(craft.density - (craft.cargocount * craft.meancargoratio + cargolist[str(item)][ratio])/(craft.cargocount+1))
                if diff < best:
                    best = diff
                    bestspacecraft = craft
        if reminder == 1:
            bestspacecraft.load_cargo(cargolist[str(item)][ratio], cargolist[str(item)][weight], cargolist[str(item)][space], item)
    return spacecrafts

def weight(spacecrafts, cargolist, sort, items):
    wastedweight = []; leftover = []
    for i in range(0, len(spacecrafts)):
        wastedweight.append(spacecrafts[i].weight)
    # while klopt nu niet helemaal
    while cargolist[sorted[0]][weight] <= max(wastedweight):
        for craft in spacecrafts:
            for item in range(1, items + 1):
                if cargolist[sort[item]] <= craft.wastedweight:
                    craft.load_cargo(cargolist[sort[item]][ratio], cargolist[sort[item]][weight], cargolist[sort[item]][space], sort[item])
                else:
                    leftover.append(sort[item])
                    break
    return spacecrafts, leftover
