from replit import clear
import art


def calculate(first_number, second_number, operation):
  if operation == "+":
      return first_number + second_number
  if operation == "-":
      return first_number - second_number
  if operation == "*":
      return first_number * second_number
  if operation == "/":
      return first_number / second_number

print(art.logo)
redo = True
first_number = float(input("What's the first number?: "))
print("+\n-\n*\n/\n")
while redo:
  operation = input("Pick an operation: ")
  second_number = float(input("What's the next number?: "))
  result = calculate(first_number, second_number, operation)
  print(f"{first_number} {operation} {second_number} = {result}")
  pick = input(f"Type 'y' to continue calculatin with {result}, type 'n' to start a new calculation or type anything else to close the calculator: ")
  if pick == "y":
    first_number = result
  elif pick == "n":
    clear()
    first_number = float(input("What's the first number?: "))
  else:
    redo = False
    
  
