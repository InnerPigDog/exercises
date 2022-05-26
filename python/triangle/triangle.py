def equilateral(sides):
    return sides[0] == sides[1] == sides[2] != 0 and triangle_requierment(sides)

def isosceles(sides):
    return (sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]) and triangle_requierment(sides)

def scalene(sides):
    return not (isosceles(sides)) and triangle_requierment(sides)

def triangle_requierment(sides):
    return sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]