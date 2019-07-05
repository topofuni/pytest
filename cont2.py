class Parent:
    house = "incheon"
    def __init__(self):
        self.money = 10000
        print("init")

class Child1(Parent):
    def __init__(self):
        super().__init__()
        pass

class Child2(Parent):
    def __init__(self):
        pass

child1 = Child1()
child2 = Child2()

#parent1 = Parent()

print(child1.money)

print(dir(child1))




