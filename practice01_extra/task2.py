def fast_pow(x,y):
    pow=1
    while y>0:
        if (y==1):
            return pow*x
        if (y%2==1):
            pow*=x
        x*=x
        y//=2
    return pow

def fast_pow_test():
    for x in range(1,101):
        for y in range(1,101):
            assert fast_pow(x, y) == x ** y
    print("Успешно")

fast_pow_test()