class Spacecrafts(object):

    def __init__(self, sc_id, weight, volume):
        self.sc_id =  sc_id
        self.weight = weight
        self.volume = volume
        self.density = weight/volume
        self.wastedweight = weight
        self.wastedspace = volume
        self.cargocount = 0
        self.meancargoratio = 0
        self.cargolist = []

    def __str__(self):
        return self.sc_id + ", " + str(self.weight) + ", " + str(self.volume) + ", " + str(self.density)

    def check_craft(self, cargoweight, cargospace):
        if cargoweight <= self.wastedweight and cargospace <= self.wastedspace:
            return True
        else:
            return False

    def load_cargo(self, cargoratio, cargoweight, cargospace, cargo_id):
        self.cargocount += 1
        self.meancargoratio = self.density - (self.cargocount * self.meancargoratio + cargoratio) / (self.cargocount + 1)
        self.wastedweight -= cargoweight
        self.wastedspace -= cargospace
        self.cargolist.append(cargo_id)

    # def best_craft(self, craft, cargoratio):
    #     diff = abs(self.density - (self.cargocount * self.meancargoratio + cargoratio) / (self.cargocount + 1)
    #     return diff


# moeten we hier nou die algoritmes ook in zetten? NEEEEEEE!!!!

#    def load_spacecrafts(self, cargolist):