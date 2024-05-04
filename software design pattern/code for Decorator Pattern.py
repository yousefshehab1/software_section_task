# Define a component interface
class Coffee:
    def cost(self):
        pass

# Define concrete component
class SimpleCoffee(Coffee):
    def cost(self):
        return 5

# Define decorator
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

# Define concrete decorators
class Milk(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2

class Sugar(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1

if __name__ == "__main__":
    my_coffee = SimpleCoffee()
    print("Cost of simple coffee:", my_coffee.cost())

    my_coffee_with_milk = Milk(my_coffee)
    print("Cost of coffee with milk:", my_coffee_with_milk.cost())

    my_coffee_with_milk_and_sugar = Sugar(my_coffee_with_milk)
    print("Cost of coffee with milk and sugar:", my_coffee_with_milk_and_sugar.cost())
