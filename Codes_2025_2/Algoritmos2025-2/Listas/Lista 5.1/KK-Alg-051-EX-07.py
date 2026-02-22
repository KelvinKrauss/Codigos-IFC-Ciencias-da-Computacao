def sorteia_dado():
    import random
    x = random.randint(1, 6)
    return x

a,b,c,d,e,f = 0, 0, 0, 0, 0 ,0
for i in range (1000000):
    dado = sorteia_dado()
    if dado == 1:
        a = a + 1
    elif dado == 2:
        b = b + 1
    elif dado == 3:
        c = c + 1
    elif dado == 4:
        d = d + 1
    elif dado == 5:
        e = e + 1
    else:
        f = f + 1
    
print(f"O 1 saiu: {a} vezes \nO 2 saiu: {b} vezes\nO 3 saiu: {c}vezes\nO 4 saiu: {d} vezes\nO 5 saiu: {e} vezes\nO 6 saiu: {f} vezes")
