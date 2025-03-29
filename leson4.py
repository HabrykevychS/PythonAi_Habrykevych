class Human:
    height = 170

class Student(Human):
    satiety = 0

class Worker(Human):
    satiety = 100

h = Human()
s = Student
w = Worker()

print(h.height)
print("*"*20)
print(s.satiety)
print(s.height)
print("*"*20)
print (w.satiety)
print(w.height)
class Grandparent:
    hight = 170
    satiety = 100
    age = 60

class Parent(Grandparent):
    age = 40

class Child(Parent):
    height = 50



class Hello:
    def __init__(self):
        print('Hello')

class HelloWorld(Hello):
    def __init__(self):
        super().__init__()
        print("World")

hw = HelloWorld()



