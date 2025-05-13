import os

os.system("cls" if os.name == "nt" else "clear")

print("Simple Calculator")

history = []

while True:
  os.system("cls" if os.name == "nt" else "clear")

  while True:
    try:
      num1 = float(input("Enter first number: "))
      break
    except ValueError:
      print("That is not a valid number. Try again.")

  valid_operators = ["+", "-", "*", "/", "%", "**"]
  while True:
    op = input("Enter operator (+, -, *, /, %, **): ")
    if op in valid_operators:
      break
    else:
      print("Invalid operator. Please chosse from +, -, *, /.")

  while True:
    try:
      num2 = float(input("Enter second number: "))
      if op in ["/", "%"] and num2 == 0:
        print("You can't divide or modulo by zero. Try a different number.")
        continue
      break
    except ValueError:
      print("That is not a valid number. Try again.")

  if op == "+":
    result = num1 + num2
  elif op == "-":
    result = num1 - num2
  elif op == "*":
    result = num1 * num2
  elif op == "/":
    result = num1 / num2
  elif op == "%":
    result = num1 % num2
  elif op == "**":
    result = num1 ** num2

  print(f"Result: {result}")
  history.append(f"{num1} {op} {num2} = {result}")


  again = input("Do you want another calculation? (y/n): ").lower()
  if again != "y":
    print("See ya later!")

    if history:
      print("\nCalculation History:")
      for item in history:
        print(item)

    break
