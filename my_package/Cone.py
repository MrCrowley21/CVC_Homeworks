import math
def cone_volume(radius, height):
    return (1 / 3) * 3.14 * height * radius

def cone_total_area(radius, height):
    return 3.14 * radius * (radius + math.sqrt(radius ** 2 + height ** 2))
