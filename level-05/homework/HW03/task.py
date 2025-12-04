'''
1) დაწერეთ კოდი, სადაც მომხმარებელს მოთხოვთ ინფორმაციას მათ შესახებ: სახელი, გვარი,
ასაკი, შემდეგ ეს ინფორმაცია გამოიტანეთ როგორც რამე დოკუმენტი, მაგალითად პასპორტი
(თითქოს მთავრობის პროგრამაა)

მაგალითად:


======================
name: name
surname: surname
age: age
birth: დღე/თვე/წელი
======================

'''


name = input("Enter your name: ")
last_name = input("Enter your last name: ")
birth_day = input('Enter your birth day as "DD": ')
birth_month = input('Enter your birth month as "MM": ')
birth_year = int(input('Enter your birth year as "YYYY": '))

current_year = 2025
age = current_year - birth_year

print("======================")
print("name: " + name)
print("last name: " + last_name)
print("age: " + str(age))
print("birth: " + birth_day + "/" + birth_month + "/" + str(birth_year))
print("======================")
