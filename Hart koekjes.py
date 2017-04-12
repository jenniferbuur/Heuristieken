
dictionary = {}
spacecrafts = {}
## spacecrafts
spacecrafts[1] = [2000, 18.9]
spacecrafts[2] = [2300, 13.1]
spacecrafts[3] = [2400, 7.6]
spacecrafts[4] = [5200, 14]
spacecrafts[5] = [6500, 15]
spacecrafts[6] = [3400, 42]

## insert data into dictionary
with open('/Users/jenniferbuur1/Documents/universiteit/UvAAEO/MinorProgrammeren/Heuristieken/Heuristieken/CargoLists/CargoList1.txt', 'rU') as f:
    for line in f:
            split = line.split()
            if len(split) == 3:
                split[2] = split[2].replace(",", ".")
                dictionary[split[0]] = [float(split[1]), float(split[2])]

for key in dictionary:
    ratio = dictionary[key][0]/dictionary[key][1]
    dictionary[key].append(ratio)

print(dictionary)
