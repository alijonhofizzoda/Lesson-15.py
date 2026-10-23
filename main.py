# OOP  чорто принсип дорад:
# 1) INHERITENS 
# 2) PALYMORPHISM   ВАҚТЕ 
# 3) ABSTRACTION
# 4) ENCAPSULATION


# class Owner():
#     def owner(self):
#         print("Animal has owner")


# class Animal(Owner):
#     def sound(self):
#         print("Animal can make a sound")


# class Speed():
#     def speed(self):
#         print("This is fast")

# class Dog(Animal, Speed):
#     def hello(self):
#         print("This is dog")


# d=Dog()
# d.hello()
# d.sound()
# d.speed()
# d.owner()


# class Cat(Animal):
#     def hello(self):
#         print('This is cat')


# c=Cat()
# c.hello()
# c.sound()
# c.owner()

# class Library:
#     def init(self,name,shelf):
#         self.name=name
#         self.shelf=shelf

#     def info(self):
#         print(f'{self.name} -- {self.shelf}')

# l=Library('Kitobxonai milli',12345)
# l.info()

# class Department(Library):
#     def __init__(self, name, shelf,department_name):
#         super().__init__(name, shelf)
#         self.department_name=department_name

#     def malumot(self):
#         print(f'{self.name} -- {self.shelf} -- {self.department_name}')

# d1=Department('Kitobxonai milli',12345,'Classic')

# d1.info()
# d1.malumot()

# class Cat:
#     def hello(self):
#         print('This is cat')


# class Dog(Cat):
#     def hello(self):
#         print('This is Dog')


# class Parrot(Dog):
#     def hello(self):
#         print('This is parrot')

# d=Dog()
# d.hello()

# p=Parrot()
# p.hello()













# 1
# class Vehicle():
#     def move():
#         print("Нақлиёт ҳаракат мекунад")

# class Car(Vehicle):
#     def honk():
#         print("Би-би!")


# my_car=Car
# my_car.move()
# my_car.honk()
# 2
# class Employee():
#     def work(self):
#         print("Корманд кор мекунад")

# class Programmer(Employee):
#     def work(self):
#         print("Код менависад")

# class Teacher(Employee):
#     def work(self):
#         print("Дарс мегузаронад")

# emp=Employee()
# prog=Programmer()
# teach=Teacher()

# emp.work()
# prog.work()
# teach.work()
# 3
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Student(Person):
#     def __init__(self, name, age, group):
#         super().__init__(name, age)
#         self.group = group

#     def info(self):
#         print(f"Студент: {self.name}, {19} лет, группа {self.group}")

# s=Student("Али", 19, "Python-1")
# s.info()
# 4
# class Animal():
#     def speak(self): 
#         print("Ҳайвон овоз мебарорад")

# class Cat(Animal):
#     def speak(self):
#         super().speak()
#         print("Миёв")

# my_cat = Cat()
# my_cat.speak()
# 5
# class Device:
#     def power_on(self):
#         print("Устройство включено")

# class Phone(Device):
#     def call(self, number):
#         print(f"Звоню на номер {number}")

# class Smartphone(Phone):
#     def take_photo(self):
#         print("Фото сделано")

# my_smartphone = Smartphone()
# my_smartphone.power_on()
# my_smartphone.call("+992900000000")
# my_smartphone.take_photo()
# 6
# class Flyer:
#     def fly(self):
#         print("Лечу")

# class Swimmer:
#     def swim(self):
#         print("Плыву")

# class Duck(Flyer, Swimmer):
#     def quack(self):
#         print("Кря!")

# duck = Duck()
# duck.fly()
# duck.swim()
# duck.quack()
# print(Duck.__mro__)
# 7
# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email

#     def get_info(self):
#         return f"Имя: {self.name}, Email: {self.email}"

# class Admin(User):
#     def __init__(self, name, email, level):
#         super().__init__(name, email)
#         self.level = level

#     def get_info(self):
#         return f"{super().get_info()}, Уровень: {self.level}"

# class Customer(User):
#     def __init__(self, name, email, balance):
#         super().__init__(name, email)
#         self.balance = balance

# class Guest(User):
#     pass

# print(Admin("Али", "ali@mail.tj", 3).get_info())
# 8











