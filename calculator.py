first_number = int(input("This is a small callculator for doing simple operations. Please enter first number: "))
second_number = int(input("Please enter second number: "))
operation = input("Please enter operation sign: ")

if operation == "+":
    outcome = int(first_number) + int(second_number)
    print(outcome)
elif operation == "-":
    outcome = int(first_number) - int(second_number)
    print(outcome)
elif operation == "*":
    outcome = int(first_number) * int(second_number)
    print(outcome)
elif operation == "/":
    outcome = int(first_number) / int(second_number)
    print(outcome)
else:
    print("You have entered a bad operation sign: ")
