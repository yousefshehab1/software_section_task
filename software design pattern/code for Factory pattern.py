class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing Circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing Rectangle")

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "rectangle":
            return Rectangle()
        else:
            raise ValueError("Invalid shape type")

# Example usage:
factory = ShapeFactory()
circle = factory.create_shape("circle")
rectangle = factory.create_shape("rectangle")

circle.draw()
rectangle.draw()
