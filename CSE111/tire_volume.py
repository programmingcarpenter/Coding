import math
import datetime
time_now = datetime.datetime.now()
time_now = time_now.strftime('%Y-%m-%d')
w = int(input('What is the Width of the tire (milimeters)? '))
a = int(input('What is the Aspect Ratio of the tire? '))
d = int(input('What is the Diameter of the tire (inches)? '))
volume = ((math.pi * w**2 * a) * (w * a + 2540 * d)) / 10000000000
print(f'The approximate volume of the tire is {volume:.2f} liters.')
with open('volumes.txt', 'a') as text_file:
    text_file.write(f'{time_now}, {w}, {a}, {d}, {volume:.2f}')