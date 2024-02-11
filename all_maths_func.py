
def addition(a, b):
    c= a+b
    return c




def subtract(a, b):
    d= a - b
    return d




def multiply(a, b):
    e =a * b
    return e




def division(a, b):
    f= a / b
    return f




def find_modulo(a, b):
    c= a % b
    return c




def main_function():
    n1=int(input("enter digit"))
    n2=int(input("enter digit"))



    print(addition(n1, n2))
    print(subtract(n1, n2))
    print(division(n1, n2))
    print(multiply(n1, n2))
    print(find_modulo(n1, n2))

main_function()