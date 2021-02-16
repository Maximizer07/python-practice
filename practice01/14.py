def f14(n):
    if n==0:
        return 7
    elif n==1:
        return 6
    else:
        return (1/78)*f14(n-2)**3+(abs(f14(n-1)))
print(f'{f14(2):.2e}')
print(f'{f14(7):.2e}')
