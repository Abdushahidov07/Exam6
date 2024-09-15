# ### 1 Question
# Create a class Employee with a public attribute name, a protected attribute _salary, and a private attribute __id. Demonstrate how these are accessed and restricted.

# Создайте класс Employee с публичным атрибутом name, защищенным атрибутом _salary и закрытым атрибутом __id. Покажите, как они доступны и ограничены.

# class Employ:
#     def __init__(self, name, salary, id):
#         self.name = name
#         self._salary=salary
#         self.__id=id

# obj1=Employ(input(),input(),input())

# print(obj1.name) # он доступен всем классам и методом
# print(obj1._salary) # его используют только для самого класса и его подкаласса но он не будет выводит ошибку при выводе 
# print(obj1.__id) # он закрыт для всех класов кроме класса котором он создан и будет выводит ошибку при прямом запросе его данных

# ### 2 Question
# Create a class BankAccount with private attributes _balance and __pin.
# Initialize the values in the constructor.
# Access the _balance directly and see what happens when you try to access __pin.

# Создайте класс BankAccount с приватными атрибутами _balance и __pin.
# Инициализируйте значения в конструкторе.
# Получите доступ к _balance напрямую и посмотрите, что произойдет, когда вы попытаетесь получить доступ к __pin.


# class BankAccount:
#     def __init__(self, balance, pin):
#         self._balance = balance
#         self.__pin=pin
#     def show(self):
#         print("Твой баланс:", self._balance)
#         print("Tвой пинко:", self.__pin)
# objc1 = BankAccount(int(input()), int(input()))

# objc1.show()


# ### 3 Question
# a) In the same BankAccount class, define a setter method to update the private attribute _balance.
# Ensure that balance can’t be negative by checking in the setter.
# В том же классе BankAccount определите метод-сеттер для обновления частного атрибута _balance.
# Убедитесь, что баланс не может быть отрицательным, проверив в сеттере.

# b) Create a class Employee with an instance attribute name and a class attribute company.
# Create two objects and modify the company class attribute. Print the result to observe the behavior.
# Создайте класс Employee с атрибутом экземпляра name и атрибутом класса company.
# Создайте два объекта и измените атрибут класса company. Распечатайте результат, чтобы понаблюдать за поведением.
# a) 
# class BankAccount:
#     def __init__(self, balance, pin):
#         self._balance = balance
#         self.__pin=pin
#     def show(self):
#         print("Твой баланс:", self._balance)
#         print("Tвой пинко:", self.__pin)
#     def changebalnce(self, balance):
#         self._balance+=balance # тут мы используем метод сеттер
#         print(self._balance)

# objc1 = BankAccount(int(input()), int(input()))
# objc1.show()
# objc1.changebalnce(int(input()))
# objc1.show()

# b) 

# class Employe:
#     company="SoftClub"
#     def __init__(self, name):
#         self.name=name
#     def show(self):
#         print(f"Your name: {self.name}")
#         print(f"Your Work in:  {Employe.company}")
#     @classmethod
#     def editcompany(cls, new_namecompany):
#         cls.company=new_namecompany

# obj1 = Employe(input())
# obj1.show()
# obj2 = Employe(input())
# obj2.editcompany(input("Write your new compny: "))
# obj2.show()        




# ### 4 Question
# Create a base class Animal with a method speak().
# Create a derived class Dog that overrides speak().
# Further, derive a class Puppy from Dog and override the speak() method again.
# Call the speak() method from a Puppy object.

# Создайте базовый класс Animal с методом speak().
# Создайте производный класс Dog, который переопределяет speak().
# Далее, выведите класс Puppy из Dog и снова переопределите метод speak().
# Вызовите метод speak() из объекта Puppy.

# class Animal:
#     def __init__(self):
#         pass
#     def speak(self):
#         print("Speak")
# class Dog(Animal):
#     def speak(self):
#         print("Woof")
# class Puppy(Dog):
#     def speak(self):
#         print("Wooof")
    
# puppy = Puppy()

# puppy.speak()


# ### 5 Question
# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age. Use incapsulation methods as well. / Напишите программу на Python для создания класса человека. Включите такие атрибуты, как имя, страна и дата рождения. Реализуйте метод определения возраста человека. Также используйте методы инкапсуляции.

# from datetime import datetime, timedelta

# class Person:
#     def __init__(self, name, country, birthday):
#         self.name=name 
#         self.country=country
#         self.__birthday=birthday
#     def show(self):
#         print(f"Name: {self.name}\nCountry: {self.country}\nBirthday: {self.__birthday}")
#     def found_age(self):
#         if self.name == "Abdullo":
#             f = datetime.now()
#             print("Your Age:",f.year-self.__birthday)
#         else:
#             print("У ТЕБЯ НЕТ ПРАВ ЗНАТЬ ВОЗРАСТЬ ПОЛЬЗОВАТЕЛЯ !!")


# objct = Person(input("Name: "), input("Write your country: "),int(input("Write your birthday: ")))
# objct.show()
# objct.found_age()
    

# ### 6 Question
# Build a Nobel class. An instance is already created for you and instance attributes are included inside the print. Take those clues and try to reverse engineer the class.  Implement string representation of a class object using str method inside the class.

# Создайте Nobel класс. Экземпляр уже создан для вас, и атрибуты экземпляра включены в результат print. Воспользуйтесь этими подсказками и попытайтесь спроектировать класс. Реализуйте строковое представление объекта класса, используя метод str внутри класса.
# ```
# class Nobel:
#     pass

# np2005=Nobel("Peace", 2005, "Muhammad Yunus")
# print(np2005.category, np2005.year, np2005.winner)


# class Nobel:
#     def __init__(self, category, year, winner):
#         self.category:str=category
#         self.year=year
#         self.winner:str=winner
# np2005=Nobel("Peace", 2005, "Muhammad Yunus")
# print(np2005.category, np2005.year, np2005.winner)


# ### 7 Question
# Create a function which returns "upper" if all the letters in a word are uppercase, "lower" if lowercase and "mixed" for any mix of the two.
# Создайте функцию, которая возвращает «верхнюю», если все буквы в слове прописные, «нижнюю», если строчные, и «смешанную» для любого сочетания   этих двух букв.

# getCase("whisper...") ➞ "lower"

# getCase("SHOUT!") ➞ "upper"

# def lowupmix (n):
#     if n.isupper():
#         print("upper")
#     elif n.islower():
#         print("lower")
#     else:
#         print("mixed")
# lowupmix(input())

# ### 8 Question
# The Fibonacci sequence is defined as follows: φ0=1, φ1=1, φn=φn-1+φn-2 for n>1. The beginning of the Fibonacci series looks like this: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Write a function int phi(int n) (C/C++), function phi (n:integer ): integer, (Pascal), which, given a natural number n, returns φn.

# Последовательность Фибоначчи определена следующим образом: φ0=1, φ1=1, φn=φn-1+φn-2 при n>1. Начало ряда Фибоначчи выглядит следующим образом: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Напишите функцию int phi(int n) (C/C++), function phi (n:integer): integer, (Pascal), которая по данному натуральному n возвращает φn.

# # input 
# 3
# # output
# 3

# n = int(input())
# f1 = 1
# f2 = 1
# f3 = 0
# lict = [1, 1]
# if n > 1:
#     for i in range(0,n+1):
#         f3=f1+f2
#         f1=f2
#         f2=f3
#         lict.append(f3)
#     print(lict[n])
    


# ### 9 Question
# Print the following pattern.(Распечатайте следующий шаблон.)
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6
# 7 7 7
# 8 8
# 9


# n = int(input())
# k = n//2
# for i in range(1, n+1):
#     if i <= n//2+1:
#         for j in range(i):
#             print(i, end="")
#         print()
#     else:
#         for f in range(k):
#             print(i, end="")
#         print()
#         k-=1
    




# ### 10
# Create a function which takes a list of objects from the class IceCream and returns the sweetness value of the sweetest ice cream. Note that there is a class provided for you in the Tests tab.
# Each sprinkle has a sweetness value of 1
# Check below for the sweetness values of the different flavors.
# Создайте функцию, которая берет список объектов класса IceCream и возвращает значение сладости самого сладкого мороженого. Обратите внимание, что на вкладке «Тесты» вам предоставлен класс.
# Каждая посыпка имеет показатель сладости 1.
# Ниже приведены значения сладости различных вкусов.
 
#   class IceCream:
#           def __init__(self, flavor, num_sprinkles):
#               self.flavor = flavor
#               self.num_sprinkles = num_sprinkles

#  Flavors	        |Sweetness Value      |
#  -------------------|-------------------|
#  Plain	          |   0             |
#  Vanilla	          |   5             |
#  ChocolateChip	  |   5             |
#  Strawberry         |   10            |
#  Chocolate	      |   10            |   
#  ---------------------------------------|
 
# ice1 = IceCream("Chocolate", 13)         # value of 23
# ice2 = IceCream("Vanilla", 0)           # value of 5

# sweetest_icecream([ice1, ice2, ice3, ice4, ice5]) ➞ 23
# sweetest_icecream([ice3, ice1]) ➞ 23


# class IceCream:
#         def __init__(self, flavor, num_sprinkles):
#             self.flavor = flavor
#             self.num_sprinkles = num_sprinkles
#         def foundsweet():
              
