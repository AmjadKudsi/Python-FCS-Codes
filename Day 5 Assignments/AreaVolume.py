import math

print("New Cone details:")
r = float(input("Enter the radius of the cone: "))
h = float(input("Enter the height of the cone: "))


class cone():
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        volume = math.pi * self.radius * self.radius * self.height / 3

        print("The volume of the cone is: ", volume)

    def surface_area(self):
        base = math.pi * self.radius * self.radius
        print("Surface Area of the base is: ", base)

        x = self.radius * self.radius + self.height * self.height
        sq = math.sqrt(x)
        side = math.pi * self.radius * sq
        print("Surface Area of the base is: ", side)


c = cone(r, h)
c.volume()
c.surface_area()