import itertools
import Spacecrafts as sc

class Spacefreight(object):
    ## fill spacecrafts with cargo by putting item in spacecrafts with the same ratio as the average ratio of the cargo together
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

    # fill spacecrafts with cargo regarding only weight
    def weight(spacecrafts, cargolist, items):
