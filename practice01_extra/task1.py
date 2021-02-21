def fast_mul(x,y,mul=0):
    if (x==0 or y==0):
        return 0
    if (x==1):
        return mul+y
    if (x%2==1):
        mul+=y
    return fast_mul(x//2,y*2,mul)

def fast_mul_test():
    for x in range(1,101):
        for y in range(1,101):
            assert fast_mul(x, y) == x * y
    print("Успешно")

fast_mul_test()