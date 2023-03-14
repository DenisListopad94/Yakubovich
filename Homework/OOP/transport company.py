from geopy.distance import geodesic


class TransportAgency(object):

    def __init__(self, name):
        self.name = name

    def count(self, coordinates: tuple, coordinates2: tuple):
        distance = geodesic(coordinates, coordinates2).kilometers
        print(int(distance))


EuroMall = TransportAgency("EuroMall")
EuroMall.count((52.093754, 23.685107), (53.902735, 27.555696))
# Брест - 52.093754, 23.685107, Минск - 53.902735, 27.555696, Лунинец - 52.245833, 26.800940
# я постараюсь доделать, пока не обращайте внимания на эту задачу
