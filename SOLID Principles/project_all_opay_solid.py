# Single Responsibility Principle (SRP) - Each class should have only one reason to change

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class FlyingAnimal(Animal):  # Open/Closed Principle (OCP) - Open for extension, closed for modification
    def fly(self):
        pass

class SwimmingAnimal(Animal):  # Open/Closed Principle (OCP)
    def swim(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Bird(FlyingAnimal):  # Liskov Substitution Principle (LSP) - Derived types must be substitutable for their base types
    def make_sound(self):
        return "Chirp!"

    def fly(self):
        return "I'm flying!"

class Fish(SwimmingAnimal):  # Liskov Substitution Principle (LSP)
    def make_sound(self):
        return "Blub blub!"

    def swim(self):
        return "I'm swimming!"

# Interface Segregation Principle (ISP) - Clients should not be forced to depend on interfaces they do not use

class SoundMaker:
    def make_sound(self):
        pass

class FlyingCreature:
    def fly(self):
        pass

class SwimmingCreature:
    def swim(self):
        pass

class Dog(SoundMaker):
    def make_sound(self):
        return "Woof!"

class Bird(SoundMaker, FlyingCreature):
    def make_sound(self):
        return "Chirp!"

    def fly(self):
        return "I'm flying!"

class Fish(SoundMaker, SwimmingCreature):
    def make_sound(self):
        return "Blub blub!"

    def swim(self):
        return "I'm swimming!"

# Dependency Inversion Principle (DIP) - High-level modules should not depend on low-level modules, both should depend on abstractions

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class SoundMaker:
    def make_sound(self):
        pass

class FlyingCreature:
    def fly(self):
        pass

class SwimmingCreature:
    def swim(self):
        pass

class Dog(SoundMaker):
    def make_sound(self):
        return "Woof!"

class Bird(SoundMaker, FlyingCreature):
    def make_sound(self):
        return "Chirp!"

    def fly(self):
        return "I'm flying!"

class Fish(SoundMaker, SwimmingCreature):
    def make_sound(self):
        return "Blub blub!"

    def swim(self):
        return "I'm swimming!"

def main():
    animals = [Dog("Buddy"), Bird("Tweety"), Fish("Nemo")]

    for animal in animals:
        print(f"{animal.name} says: {animal.make_sound()}")
        if isinstance(animal, FlyingCreature):
            print(animal.fly())
        elif isinstance(animal, SwimmingCreature):
            print(animal.swim())

if __name__ == "__main__":
    main()
