class Road:
    def __init__(self , length_in_meters , width_in_meters , material_density = 2400):

        self._length = length_in_meters
        self._width = width_in_meters
        self.__density = material_density
        # 2400 - примерная плотность асфальтобетона кг/ м^3


    def total_mass(self , thickness_in_centimeters):

        volume = self._length * self._width * thickness_in_centimeters / 100
        # в кубических метрах

        mass = round(volume * self.__density / 1000 , 2 )
        # в тоннах

        print(f"Примерная масса дороги = {mass} тонн")



def roads(length , width , thickness):

    example_road = Road(length , width)

    example_road.total_mass(thickness)



if __name__ == "__main__":

    example_road = Road(5000 , 10)

    example_road.total_mass(5)
