from math import *

while True:
    try:
        #Задаю значение переменной x
        x = int(input("x = "))

        if  ((cos(x-1/2*pi))*tan(1.5*pi + x)):
            print("Нет решения - один из знаменателей обращается в ноль")
        else:
            z1 = tan((x-pi/2) * cos(3*pi/2 + x) - pow(sin, 3)(3.5*pi - x)) / ((cos(x-1/2*pi))*tan(1.5*pi + x))
            z2 = pow(sin, 2)(x)

            print("z1 = ", f'{z1:}')
            print("z2 = ", f'{z2:}')
        break 
    except ValueError:
        print("x - это число")
        break
            
