import math
def my_sqrt(a):
    epsilon = 0.0000001
    x = a
    while True:
        y = (x + a/x)/2.0
        if abs(y - x) < epsilon:
            break
        x = y
    return y
def test_sqrt():
    a = 1
    while a<26:
        diff = my_sqrt(a) - math.sqrt(a)
        print('a=', a, '|my_sqrt(a=)', my_sqrt(a), '|math.sqrt(a)=', math.sqrt(a), '|diff=', abs(diff))
        a = a + 1

test_sqrt()
