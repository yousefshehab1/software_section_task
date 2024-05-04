class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass

    def fly(self):
        pass

    def swim(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Bird(Animal):
    def make_sound(self):
        return "Chirp!"

    def fly(self):
        return "I'm flying!"

class Fish(Animal):
    def make_sound(self):
        return "Blub blub!"

    def swim(self):
        return "I'm swimming!"

def main():
    animals = [Dog("Buddy", "Dog"), Bird("Tweety", "Bird"), Fish("Nemo", "Fish")]

    for animal in animals:
        print(f"{animal.name} says: {animal.make_sound()}")
        if isinstance(animal, Bird):
            print(animal.fly())
        elif isinstance(animal, Fish):
            print(animal.swim())

if __name__ == "__main__":
    main()
