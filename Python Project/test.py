
while True:
    num1 = int(input("Enter number 01:"))
    operator = input("enter *,+,-,/ :")
    num2 = int(input("Enter number 02:"))

    if operator == '+':
        print(num1+num2)
    if operator == '-':
        print(num1-num2)
    if operator == '*':
        print(num1*num2)
    if operator == '/':
       print(num1/num2)
