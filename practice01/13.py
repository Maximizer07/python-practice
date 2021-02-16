import math
def f13(n,m):
    a=0;
    b=0;
    for i in range(1,n+1):
        b+=i**6+math.tan(i)
        for j in range(1,m+1):
            a+=i**5-24*(j**8)
    return a-62*b
print(f'{f13(97,75):.2e}')
print(f'{f13(32,90):.2e}')