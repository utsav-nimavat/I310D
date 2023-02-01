import math
def calculate_volume_of_sphere(radius):
	pi = math.pi
	volume = (4/3) * pi * (radius ** 3)
	return volume

radius1 = 30
radius2 = 40
print("The area of the sphere with radius " + str(radius1) + " is " + str(calculate_volume_of_sphere(radius1)))
print("The area of the sphere with radius " + str(radius2) + " is " + str(calculate_volume_of_sphere(radius2)))
