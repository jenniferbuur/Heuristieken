
dictionary = {}

## insert data into dictionary
with open('/Users/sem/Documents/Heuristieken/CargoLists/CargoList1.txt', 'rU') as f:
    for line in f:
            split = line.split()
            dictionary[split[0]] = split[1:]

print(dictionary)
