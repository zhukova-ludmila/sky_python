def fizz_buzz(n):
    for x in range(1, n):
        if x % 3 == 0:
            print("Fizz")
        if x % 5 == 0:
            print("Buzz")
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        else:
            print(x)
fizz_buzz(17)
