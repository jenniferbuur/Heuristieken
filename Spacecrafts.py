class Spacecrafts(self):

    __init__(self, weight, volume, sc_id):
        self.sc_id =  sc_id
        self.weight = weight
        self.volume = volume
        self.density = weight/float(volume)

# moeten we hier nou die algoritmes ook in zetten?

#    def load_spacecrafts(self, cargolist):
