import math

eq = '4x^2 +4x +    (-8) =  0'

eq_parts = eq.replace(' ', '').split('x^2')
a = int(eq_parts[0])

eq_parts = eq_parts[1].split('x')
b = int(eq_parts[0])

eq_parts = eq_parts[1].split('=')
c = int(eq_parts[0].strip('+()'))

print(a, b, c)

sq = b**2 - 4*a*c

x1 = int((-b + math.sqrt(sq)) / (2*a))
x2 = int((-b - math.sqrt(sq)) / (2*a))

print(x1, x2)