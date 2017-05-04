class Cargo(self):

    def __init__(self, weight, volume, cargo_id):
        self.weight = weight
        self.volume = volume.replace(",". ".")
        self.cargo_id = cargo_id #nodig?
        self.density = weight/float(volume)
        self.cargolist = []

    def load_cargo(self, cargo_nr):
        cargolist.append(cargo_nr)


    def sort_by_weight(self, cargolist):
        sorted(cargolist, key = lambda x: [cargolist[x][weight]])

    def sort_by_desnity(self. cargolist):
        sorted(cargolist, key = lambda x: [cargolist[x][ratio]])

    def return_loaded_cargo(self):
        return cargolist
