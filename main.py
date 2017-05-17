import itertools
import Spacecrafts as sc
import helpers
# alle lists inladen
# importeer alle classes

# alle cargolists in een dictionary
cargolist1 = {}; cargolist2 = {}; cargolist3 = {}
items1 = 0; item2 = 0; item3 = 0
lists = [cargolist1, cargolist2, cargolist3]
nritems = [items1, item2, item3]
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


# initialise spacecrafts in class
cygnus = sc.Spacecrafts("Cygnus", 2000, 18.9)
verne = sc.Spacecrafts("Verne", 2300, 13.1)
progress = sc.Spacecrafts("Progress", 2400, 7.6)
kounotori = sc.Spacecrafts("Kounotori", 5200, 14)
tianzhou = sc.Spacecrafts("TianZhou", 6500, 15)
dragon = sc.Spacecrafts("Dragon", 3400, 42)

# opdracht A
spacecrafts = [cygnus, verne, progress, kounotori]

helpers.weight(cargolist1, spacecrafts)
solution = cc.solution(spacecrafts, items1)

print('Wasted weight: ' + str(solution[0]) + ', Wasted space: ' + str(solution[1]) + ', Unloaded cargo: ' + str(solution[2]) + '.')

# opdracht B


# opdracht C
