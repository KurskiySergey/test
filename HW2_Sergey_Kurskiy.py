# --------------------------------------------------------task1

print("\n task 1\n")

n = [2 , "string" , [3  , False] , 34.5 ]
print("n has a type of " , type(n))
print("\n")
for i in range(len(n)):
    t_pe = str(type(n[i]))
    print(n[i] , " - this element has a type of " , t_pe , "\n")
    if (t_pe == "<class 'list'>"):
        for j in range(len(n[i])):
            print("In the list ", n[i] , " element " , n[i][j] , "has a type of " , type(n[i][j]) , "\n")



# -------------------------------------------------------task2

print("\n task2\n")

newListLength = int(input("Enter the length of the list\n"))
newList = []
answer = input("Do you want to enter values yourself? Y/N\n")
answer.lower()
if ((answer == "y") or (answer == 'yes')):
    for i in range(newListLength):
        value = input("Element {}\n".format(i))
        newList.insert(i , value)
else :
    for i in range(newListLength):
        newList.append(i)


print("Before: " , newList , "\n")
cicleLength = newListLength - (newListLength % 2)
for i in range(cicleLength):
    if (i % 2 == 0):
        tmp = newList[i+1]
        newList[i+1] = newList[i]
        newList[i] = tmp

print("After: " , newList , "\n")

# --------------------------------------------------------task 3

print("\n task3\n")

number = int(input("Enter a number\n"))

month_list = ["winter" , "spring" , "summer" , "autumn" , "winter"]
month_dict = {1 : "winter" , 2 : "winter" , 3 : "spring" , 4 : "spring" , 5 : "spring" , 6 : "summer" , 7 : "summer" , 8 : "summer" , 9 : "autumn" , 10 : "autumn" , 11 : "autumn" , 12 : "winter"}
month_dict_Ver2 = {"winter" : [12 , 1 , 2] , "spring" : [3 , 4 , 5] , "summer" : [6 , 7 , 8] , "autumn" : [9 , 10 , 11] }


for i in range(len(month_dict_Ver2)):
    season = month_dict_Ver2.get(month_list[i])
    for j in range(len(season)):
        if (season[j] == number):
            season = month_list[i]
            break
    if (season == month_list[i]):
        break

print("List = " , month_list[number // 3] , "\n" , "Dict = " , month_dict.get(number) , "\n" ,  "Dict_Ver2 = " , season , "\n" )


# --------------------------------------------------------task 4

print("\n task4\n")

sentence = input("Write your sentence: \n")

words = sentence.split(" ")

for i in range(len(words)):
    print("{}) {}\n".format(i+1 , words[i][:10]))



# --------------------------------------------------------task 5

print("\n task5\n")

rang_list = [7 , 5 , 3 , 3 , 2]
exit = False

while (exit != True):

    print("Your rand list = ", rang_list, "\n")
    answer = input("Enter number , or print Q for exit\n")
    if (answer.lower() == "q"):
        exit = True;
    else :
        answer = int(answer)
        for i in range(len(rang_list)):
            max = rang_list[i]
            if (answer >= max):
                count = 0
                if ( answer == max):
                    count = rang_list.count(max)
                rang_list.insert(i + count , answer)
                break
            else:
                if (i == len(rang_list) - 1):
                    rang_list.append(answer)
                    break


# ----------------------------------------------------task 6

print("\n task6\n")

print("Prepearing structure...\n\n")
exit = False

database = [] # Создаем базу данных
count = 1
while ( exit != True ):
    answer = input("If you want to exit enter Q, otherwise enter W\n")
    if (answer.lower() == "q"):
        exit = True
    else:
        name = input("Enter the nname of your product\n")
        price = int(input("Enter a price of your product\n"))
        amount = int(input("Enter an amount of your product\n"))
        measure = input("Enter measure of your product (kg , boxes , items ,etc.)\n")

        tmp_info =(count ,  { "name" : name , "price" : price , "amount" : amount , "measure" : measure})
        database.append(tmp_info)
        count = count + 1


print("Your database = " , database)


products_info = {} # Создаем информацию о продуктах

keys = str(database[0][1].keys())[11:-2].split(", ") # Находим значения ключей из базы

array = [] # Создаем массив значений по ключу
for i in range(len(keys)):
    tmp = []
    array.append(tmp)

for i in range(len(database)): # Заполняем массив
    for j in range(len(keys)):
        array[j].append(database[i][1].get(keys[j][1:-1]))


for i in range(len(keys)): # Загружаем в словарь
    tmp_info = { keys[i][1:-1] : array[i]}
    products_info.update(tmp_info)

print("\n Your product info\n")

print(products_info)
