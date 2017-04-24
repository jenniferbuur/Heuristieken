import operator

cargolist = {}
spacecrafts = {}

## initiate spacecrafts
spacecrafts['Cygnus'] = [2000, 18.9]
spacecrafts['Verne'] = [2300, 13.1]
spacecrafts['Progress'] = [2400, 7.6]
spacecrafts['Kounotori'] = [5200, 14]
##spacecrafts['TianZhou'] = [6500, 15]
##spacecrafts['Dragon'] = [3400, 42]

## insert data into cargolist dictionary
with open('/Users/jenniferbuur1/Documents/universiteit/UvAAEO/MinorProgrammeren/Heuristieken/Heuristieken/CargoLists/CargoList1.txt', 'rU') as f:
    for line in f:
            split = line.split()
            if len(split) == 3:
                split[2] = split[2].replace(",", ".")
                cargolist[split[0]] = [float(split[1]), float(split[2])]

## add ratios to cargolist
for key in cargolist:
    ratio = cargolist[key][0]/cargolist[key][1]
    cargolist[key].append(ratio)

## add ratios to spacecrafts
for key in spacecrafts:
    ratio = spacecrafts[key][0]/spacecrafts[key][1]
    spacecrafts[key].append(ratio)

## initiate total counters for all spacecrafts
total_cargo_kg = 0
total_cargo_m3 = 0
total_counter = 0

## loop over all spacecrafts
for spacecraft in range (len(spacecrafts)):

    ## sort cargolist and spacecrafts by ratio
    cargolist_sorted = sorted(cargolist.items(), key=lambda i: i[1][2])
    spacecrafts_sorted = sorted(spacecrafts.items(), key=lambda i: i[1][2])

    ## initiate max. values for spacecraft
    spacecraft_kg = spacecrafts_sorted[spacecraft][1][0]
    spacecraft_m3 = spacecrafts_sorted[spacecraft][1][1]
    spacecraft_ratio = spacecrafts_sorted[spacecraft][1][2]
    print("Spacecraft: " + str(spacecrafts_sorted[spacecraft][0]))
    print("Available KG: " + str(spacecraft_kg))
    print("Available M3: " + str(spacecraft_m3))
    print("Ratio: " + str(spacecraft_ratio))

    ## initiate empty spacecraft
    cargo_kg = 0
    cargo_m3 = 0
    counter = 0
    cargos = []

    ## add items from cargolist untill one of spacecraft limits is reached
    while cargo_kg + cargolist_sorted[counter][1][0] < spacecraft_kg and cargo_m3 + cargolist_sorted[counter][1][1] < spacecraft_m3:
        cargos.append(cargolist_sorted[counter][0])
        cargo_kg = cargo_kg + cargolist_sorted[counter][1][0]
        cargo_m3 = cargo_m3 + cargolist_sorted[counter][1][1]
        counter += 1

    ## print results of filled spacecraft
    if cargo_kg / cargo_m3 > spacecraft_ratio:
        print_advice = ['higher', 'high', 'lower']
    else:
        print_advice = ['lower', 'low', 'higher']
    print("Spacecraft " + str(spacecrafts_sorted[spacecraft][0]) + " is filled with " + str(counter) + " cargos. "  + "The total Weight is: " + str(cargo_kg) + "KG. The total volume is: " + str(cargo_m3) + " M3")
    print("The following cargos are packed: " + str(cargos))
    print("The ratio KG/M3 of this filled spacecraft is: " + str(cargo_kg / cargo_m3) + " This ratio is " + print_advice[0] + " then the spacecrafts ratio: " + str(spacecraft_ratio) + ". It is recommended to remove cargos with a " + print_advice[1] + " ratio and add cargos with a " + print_advice[2] + " ratio, to optimize usage of space/weight.")

    # sum packed cargos to total packed cargos
    total_cargo_kg += cargo_kg
    total_cargo_m3 += cargo_m3
    total_counter += counter

    ## remove cargos from cargolist when used
    for placedcargos in cargos:
        cargolist.pop(placedcargos, None)

## print list of cargos which are not loaded into spacecraft
cargolist_sorted = sorted(cargolist.items(), key=lambda i: i[1][2])
print("Cargos left:" + str(cargolist_sorted))

print ("Total KG: " + str(total_cargo_kg))
print("Total M3: " + str(total_cargo_m3))
print("Total Cargos: " + str(total_counter))
