def add(a, b):
    return a + b

def subtract(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divid(a, b):
    if b == 0:
        return "Cannot divide by zero."
    return a / b

def main():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number123: "))

    print("Addition:", add(a, b))
    print("Subtraction:", subtract(a, b))
    print("Multiplication:", multiply(a, b))
    print("Division:", divid(a, b))

if __name__ == "__main__":
    main()