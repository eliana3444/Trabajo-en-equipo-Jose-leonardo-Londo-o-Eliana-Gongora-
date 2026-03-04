def operaSumaMult(func):
    def wrapper(a,b):
        return func(a, b) * 5
    return wrapper

def restar5(func):
    def wrapper(a, b):
        return func(a, b) - 5
    return wrapper

@restar5
def suma(a, b):
    return a + b

print(suma(10, 7))  

    