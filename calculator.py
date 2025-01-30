def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operation = { "+" : add, 
              "-" : subtract, 
              "*" : multiply, 
              "/" : divide
            }


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

for i in operation:
    print(i)
    
symbol = input("Enter operation to perform: ")
operation_cal = operation[symbol]
answer = operation_cal(num1, num2)
print(answer)
cont = "y"

while cont != "n":
    response = input(f"Type 'y' to continue with {answer}, or type 'n' to exit: ")
    if response == 'y':
        symbol = input("Enter operation to perform: ")
        num1 = answer
        num2 = int(input("Enter the second number: "))
        operation_cal = operation[symbol]
        answer = operation_cal(num1,num2)
        print(answer)
    else:
        cont == 'n'
        break
