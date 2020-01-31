def hello(name="person"):
    print("Hello " + name)
hello("El")
hello("Pinche")
hello("Pastel")
hello()

def add(number1, number2):
    return number1+number2
print(add(1, 2))

add = lambda number1, number2: number1+number2
print(add(1, 2))