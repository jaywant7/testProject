def addition(num1,num2):
    return num1+num2
def subtraction(num1,num2):
    return num1-num2
def division(num1,num2):
    return num1/num2
def multiplication(num1,num2):
    return num1*num2
print("Select Operations")
print(
    "1. Addition\n"
    "2. Subtraction\n"
    "3. Multiplication\n"
    "4. Division\n")
operation = int(input("Enter choice of operation 1,2,3,4: "))
n1 = float(input("Enter the First Number: "))
n2 = float(input("Enter the Second Number: "))
if operation == 1:
    print (n1, "+", n2, "=", addition(n1, n2))

elif operation == 2:
    print (n1, "-", n2, "=", subtraction(n1, n2)) 

elif operation == 3:
    print (n1, "*", n2, "=", multiplication(n1, n2)) 
    
elif operation == 4:
    print (n1, "/", n2, "=", division(n1, n2)) 
    
else:
    print("Invalid Input")
