
# TASK 2 CALCULATOR

while True:
   print("\n---  simple Calculator---")
   num1 = float(input("enter the first number:"))
   num2 = float(input("enter the second number:"))

   print("Select operation")

   print("1.Additon(+)")
   print("2.Subtraction(-)")
   print("3.Multiplication(*)")
   print("4.Division(/)") 
   print("5.Exit")

   choice = input("Enter choice (+, -, *, /,5): ")

   if choice  ==  '+':
    result = num1 + num2
    print(f"The addition of {num1} + {num2} = {result}")
   elif choice  ==  '-':
    result = num1 - num2
    print(f"The subtraction of {num1} - {num2} = {result}")
   elif choice  ==  '*':
    result = num1 * num2
    print(f"The multiplication of {num1} * {num2} = {result}")
   elif choice  ==  '/':
       if num2!=0:
             result = num1 / num2
             print(f"The division of {num1} / {num2} = {result}")
       else:
            print("Error! Division by zero is not allowed.")
   elif choice == '5':
       print("Exiting the calculator.Goodbye!")
       break
   else:
    print("Invalid operation choice!")