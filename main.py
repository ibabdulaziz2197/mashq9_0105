# 3
class Animal:
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type

    def eat(self):
        return f"{self.name} ovqat yeyapti"


class Dog(Animal):
    def __init__(self, name, age, type, breed, color):
        super().__init__(name, age, type)
        self.breed = breed
        self.color = color

    def eat(self):
        parent_text = super().eat()
        return parent_text + " va tez yeyapti"

    def bark(self):
        return "It hurmoqda"

d = Dog("Rex", 3, "sut emizuvchi", "Ovcharka", "qora")

print(d.eat())
print(d.bark())
