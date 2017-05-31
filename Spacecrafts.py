class Spacecrafts(object):

    """
    In this class the variables for the spacecrafts are initiated
    and several functions that are neccessary for main.py
    """

    def __init__(self, sc_id, weight, volume, country):
        self.sc_id =  sc_id
        self.weight = weight
        self.volume = volume
        self.density = weight/volume
        self.country = country
        self.wastedweight = weight
        self.wastedspace = volume
        self.cargocount = 0
        self.meancargoratio = 0
        self.cargolist = []

    """
    This function checks whether a cargo item fits in an spacecraft
    """
    def check_craft(self, cargoweight, cargospace):
        if cargoweight <= self.wastedweight and cargospace <= self.wastedspace:
            return True
        else:
            return False

    """
    This function loads a cargo item into an spacecraft
    """
    def load_cargo(self, cargoratio, cargoweight, cargospace, cargo_id):
        self.cargocount += 1
        self.meancargoratio = self.density - (self.cargocount * self.meancargoratio + cargoratio) / (self.cargocount + 1)
        self.wastedweight -= cargoweight
        self.wastedspace -= cargospace
        self.cargolist.append(cargo_id)

    """
    This function sets the variables neccessary to the original state of init
    """
    def set_original(self):
        self.cargocount = 0
        self.meancargoratio = 0
        self.wastedweight = self.weight
        self.wastedspace = self.volume
        self.cargolist = []
