#Simple arithmetic calculator
op = ["+","-","*","/"]

#Functions for each operator
def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    return a/b

print(">>>>> Simple Arithmetic Calculator <<<<<")
def main():
    a = int(input("\n" "First Number: "))
    b = int(input("Second Number: "))
    c = input("Operation: ")

    if c == "+":
        print( add(a, b))
        main()
    elif c == "-":
        print(sub(a, b))
        main()
    elif c == "*":
        print(mul(a, b))
        main()
    elif c == "/":
        print (div(a, b))
        main()
    else:
        print("You entered an invalid operator")
        print("Please only use \"+\", \"-\", \"*\" or \"/\".")
        main()
main()
