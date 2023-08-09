class Human:
    favorite_drink = 'beer'
    def __init__(self, age: int):
        self.age = age
        if self.age < 18:
            self.favorite_drink = 'juce'

    def drink(self):
        class_name = self.__class__.__name__
        fav_drink = self.favorite_drink
        print(f' {class_name} likes drink {fav_drink}')

man1 = Human(17)
man2 = Human(28)

man1.drink()
man2.drink()






