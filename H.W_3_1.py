# задаємо умову  цілого числа
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
# задаємо дію над числами
operation = input("Enter operation: ")
if operation == "+":
    result = first_number + second_number
elif operation == "-":
    result = first_number - second_number
elif operation == "*":
    result = first_number * second_number
# робимо перевірку, задаючи умову,що друге число дорівнює 0
elif operation == "/":
    if second_number == 0:
        result = None
        print("cannot divide by zero")
    else:
        result = first_number / second_number
        print(result)
else:
    result = None
    print("no valid data")

print(result)


