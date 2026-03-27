import math
def square(x):
    square = x*x
    return (square)
x = float(input())
result = square(x)
end = math.ceil(result)
print(end)
