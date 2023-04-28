import math
w = int(input('What is the Width of the tire (milimeters)? '))
a = int(input('What is the Aspect Ratio of the tire? '))
d = int(input('What is the Diameter of the tire (inches)? '))
volume = ((math.pi * w**2 * a) * (w * a + 2540 * d)) / 10000000000
print(f'The approximate volume of the tire is {volume:.2f} liters.')