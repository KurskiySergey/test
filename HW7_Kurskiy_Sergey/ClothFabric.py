from abc import ABC , abstractclassmethod

class Fabric:

    suit_database = []
    coat_database = []

    @property
    def fabric_info(self):
        print(f"Number of suits - {len(self.suit_database)}\nNumber of coats - {len(self.coat_database)}\n")

    def total_consumption(self):
        suit_consumtion = 0
        coat_consumption = 0
        for suit in self.suit_database:
            suit_consumtion +=  2 * suit.height + 0.3

        for coat in self.coat_database:
            coat_consumption += coat.size/6.5 + 0.5

        print(f"Suit consumptions = {suit_consumtion}\nCoat consumptions = {coat_consumption}\nTotal consumptions = {suit_consumtion + coat_consumption}\n")

cloth_fabric = Fabric()


class Cloth(ABC):

    __name = ""
    @abstractclassmethod
    def consumption(self):
        pass

    @property
    def name(self):
        return f"The name of this cloth - {self.__name}\n"

    @name.setter
    def name(self , name):
        if self.__name == "":
            self.__name = name



class Coat(Cloth):

    def __init__(self , size):
        self.name = "Coat"
        self.size = size
        global  cloth_fabric
        cloth_fabric.coat_database.append(self)


    def consumption(self):
        result = self.size/6.5 + 0.5
        print(f"consumption - {result}\n")


class Suit(Cloth):

    def __init__(self , height):
        self.name = "Suit"
        self.height = height
        global cloth_fabric
        cloth_fabric.suit_database.append(self)

    def consumption(self):
        result = 2 * self.height + 0.3
        print(f"consumption - {result}\n")


if __name__ == "__main__":

    test = Coat(23)
    print(test.name)
    test.consumption()
    test.name = "Suit"
    print(test.name)

    suit = Suit(20)
    print(suit.name)
    suit.consumption()
    suit.name = "Coat"
    print(suit.name)

    cloth_fabric.fabric_info
    cloth_fabric.total_consumption()