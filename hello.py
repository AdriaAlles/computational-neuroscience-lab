# Week 1: exponent rules, checked numerically
a = 2.0
m = 3
n = 4

lhs = a**m * a**n
rhs = a**(m + n)
print("a^m * a^n =", lhs)
print("a^(m+n)  =", rhs)
print("Equal?", lhs == rhs)

print("a^0 =", a**0)
print("a^-3 =", a**-3, " 1/a^3 =", 1 / a**3)