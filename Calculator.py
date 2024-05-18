def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

print("1.addition")
print("2.subtraction")
print("3.multiplation")
print("dividing")

while True:
    choice = input("Enter choice:(1,2,3,4) ")

    if choice in ('1','2','3','4'):
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num2,num1))

        elif choice == '2':
            print(num2, "-", num1, "=", subtract(num2,num1))

        elif choice == '3':
            print(num2, "x", num1, "=", multiply(num2,num1))

        elif choice == '4':
            print(num2, "/", num1, "=", divide(num2,num1))

        next_calculation = input("Do you want to continue?(Y/N) ")

        if next_calculation == "N":
            break

    else:
        print("ERROR 404 NOT FOUND :)")



