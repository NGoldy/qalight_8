class Human:
    favorite_drink = 'beer'
    def __init__(self, age: int):
        self.age = age
        if self.age < 18:
            self.favorite_drink = 'juce'

    def drink(self):
        class_name = self.__class__.__name__
        fav_drink = self.favorite_drink
        print(f' {class_name} likes drink {fav_drink}. He is {self.age} years old.')

class Worker(Human):

    def __init__(self, age, salary):
        super().__init__(age)
        self.salary = salary
        if self.age > 18 and self.salary > 1000:
            self.favorite_drink = 'wiskey'


man1 = Human(17)
man2 = Human(28)

man1.drink()
man2.drink()

w1 = Worker(15, 1000)
w1.drink()
w2 = Worker(43, 1000)
w2.drink()
w3 = Worker(37, 2000)
w3.drink()





