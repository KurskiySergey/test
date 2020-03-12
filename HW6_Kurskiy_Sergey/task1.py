import time

class TrafficLight:

    def __init__( self ,__color , blink_sec = 3):

        self.__color = __color
        self.blink_sec = blink_sec
        if __color == "Red":
            self.__color_type = 41
        elif __color == "Yellow":
            self.__color_type = 43
        else:
            self.__color_type = 42

    def __blinks(self):
        count = 0
        while count < self.blink_sec:
            print("\b" * 20, end='')
            print(f"{self.__color} = \033[{self.__color_type}m{'    '}\033[0m", end='')
            time.sleep(0.5)
            print("\b" * 20, end='')
            print(f"{self.__color} = {' '}\033[0m", end='')
            time.sleep(0.5)
            count += 1

    def running(self , seconds):

        print(f"{self.__color} = \033[{self.__color_type}m{'    '}\033[0m" , end='')

        if seconds > self.blink_sec:
            time.sleep(seconds - self.blink_sec)
        else:
            time.sleep(0)

        self.__blinks()
        self.turn_off()

    def turn_off(self):
        print("\b" * 20, end='')




def Light(red_seconds = 7 , yellow_seconds = 5 , green_seconds = 6 , max_cicles = 5):

    Red = TrafficLight("Red")
    Yellow = TrafficLight("Yellow")
    Green = TrafficLight("Green")

    cicle_count = 0
    print("TrafficLight is working\n")
    while True:
        Red.running(red_seconds)
        Yellow.running(yellow_seconds)
        Green.running(green_seconds)
        if cicle_count == max_cicles-1:
            break
        cicle_count += 1

    print("TrafficLight is turned off")

if __name__ == "__main__":

    Light()
