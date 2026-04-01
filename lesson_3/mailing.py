from adress import Adress


class Mailing:
    def __init__(self, to_adress, from_adress, cost, track):
        self.to_adress = to_adress
        self.from_adress = from_adress
        self.cost = cost
        self.track = track

    def get_to_adress(self):
        return str(Adress)

    def get_from_adress(self):
        return str(Adress)

    def get_cost(self):
        return self.cost

    def get_track(self):
        return self.track
