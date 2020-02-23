# task 1

print('\n task1\n')

integer = 5
float = 8.8
bool = True
string = 'Hello Python'

print(integer)
print(float)
print(bool)
print(string)

number = int(input('Put a number 1:  '))
var = int(input('Put a number 2:     '))
word = input('Print a string:    ')

print( 'number - {} var - {} word - {}'.format(number , var , word))



# task 2

print('\n task2\n')

seconds = int(input('Input time in seconds: '))

minutes = seconds // 60
hours = minutes // 60
min = minutes % 60
sec = seconds % 60
days = hours // 24
hour = minutes % 24

print('Current time dd:hh:mm::ss = {}:{}:{}:{}'.format(days ,hour , min , sec))

# task 3

print("\n task3\n")

n = input('Input a number n:    ')

nn = n + n
nnn = nn + n

sum = int(n) + int(nn) + int(nnn)

print("n + nn + nnn = " , sum)


# task 4

print("\n task4\n")

number = int(input("Input a digital and not signed number:  "))

max = 0

while ( (number // 10) != 0 ):
    mod = number % 10
    number = number // 10
    if (max < mod):
        max = mod

print("max number = " , max)

# task 5

print("\n task5\n")

revenue = int(input("Input your revenue: ="))
costs = int(input("Input your costs: ="))

profit = revenue - costs

if (profit > 0):
    print("You are in profit")
    rent = profit / revenue
    staff = int(input('Input number of employees: = '))
    profitPerPerson = profit / staff
    print("Profit = {} , rent = {} , staff - {} , profit per person - {}".format(profit , rent , staff , profitPerPerson))
else:
    print("You are in loss")


# task 6

print("\n task6\n")

a = int(input("Input number a = "))
b = int(input("Input number b = "))

dayCount = 1
print("1 day : {} km ".format(a))

while ( a < b):
    a = a + a*0.1
    dayCount = dayCount + 1
    print("{} day : {} km".format(dayCount , a))

print("Answer : After {} days sportsmen will achive a result - not less then {} km".format(dayCount , a))


