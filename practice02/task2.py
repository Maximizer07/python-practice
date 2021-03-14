def f22(x):
    e = x & 0x80000000
    d = x & 0x7f000000
    c = x & 0x00ffff00
    b = x & 0x000000fc
    a = x & 0x00000003

    c = c << 8
    b = b << 8
    d = d >> 21
    a = a << 1
    e = e >> 31

    x = c + b + d + a + e
    return x


print(f'{f22(0x72de182a):#x}')
print(f'{f22(0xf0f36aca):#x}')
