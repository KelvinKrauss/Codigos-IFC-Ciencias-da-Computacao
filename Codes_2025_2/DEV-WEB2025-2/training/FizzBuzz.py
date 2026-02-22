n = 0
while n <= 999999:
    n = n + 1
    if n % 3==0 and n % 5==0:
        print ("FizzBuzz")
    elif n % 3==0:
        print ("Fizz")
    elif n % 5==0:
        print ("Buzz")
    elif n % 7==0:
        print ("Bazz")
    else:
        print(n)