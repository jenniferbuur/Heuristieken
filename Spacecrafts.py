class Spacecrafts(self):

    __init__(self, weight, volume, sc_id):
        self.sc_id =  sc_id
        self.weight = weight
        self.volume = volume
        self.density = weight/float(volume)

    
