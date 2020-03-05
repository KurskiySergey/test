from sys import argv

script_name , work_hours , salary_per_hour , bonus = argv

def Salary (work_hours , salary_per_hour , bonus):
    try:
        salary = (int(work_hours) * int(salary_per_hour)) + int(bonus)
        print("Salary = " ,salary)
        return 0
    except:
        print(ValueError , "need type of int")
        return 1


Salary(work_hours , salary_per_hour , bonus)