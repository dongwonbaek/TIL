a = int(input())
b = int(input())
def rectangle(a, b):
    return a * b, (a + b)*2
print(rectangle(a, b), type(rectangle(a, b)))