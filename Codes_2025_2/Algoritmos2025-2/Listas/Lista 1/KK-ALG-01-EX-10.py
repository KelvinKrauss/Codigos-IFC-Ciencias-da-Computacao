import math

a = int(input("a: "))
b = int(input("b: "))
print(a + b)
print("diferenca (a - b): ", a - b)
print("produto: ", a * b)
if b != 0:
    print("quociente (a / b): ", a / b)
    print("resto (a % b): ", a % b)

if a > 0:
    print("log10(a): ", math.log10(a))

print("a elevado a b: ", a ** b)
