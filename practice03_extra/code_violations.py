# 1. whitespace before '('
for i in range (5):
    break
# 2. missing whitespace around operator.
x=0
# 3. missing whitespace after ','.
print('Hello','World')
# 4. unexpected spaces around keyword / parameter equals
print('Hello', end =' ')
# 5. expected 2 blank lines, found 1
def func1():
    pass

def func2():
    pass


# 6. multiple statements on one line (colon)
if x > 5: y = 10
# 7. multiple statements on one line (semicolon)
from math import factorial; x = factorial(5)
# 8. comparison to None should be 'if cond is None:'
# 9. comparison to True should be 'if cond is True:' or 'if cond:'
if x != True:
    print("var is not equal to True")
if x == None:
    print("var is equal to None")
