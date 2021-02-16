import math
def f12(x):
    if x<15:
        return x**3-x**8
    elif x<50:
        return math.sin(x**8)-x**3
    else:
        return 79*(math.sin(x)+59*(x**7))**3-math.tan(x)
print(f'{f12(107):.2e}')
print(f'{f12(98):.2e}')
