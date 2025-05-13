print("Simple Calculator")

while True:

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
    print(f"Result: {num1 + num2}")
  elif op == "-":
    print(f"Result: {num1 - num2}")
  elif op == "*":
    print(f"Result: {num1 * num2}")
  elif op == "/":
    if num2 == 0:
      print("Error: Cannot divide by zero.")
    else:
      print(f"Result: {num1 / num2}")
  elif op == "%":
    if num2 == 0:
      print("Error: Cannot modulo by zero.")
    else:
      print(f"Result: {num1 % num2}")
  elif op == "**":
    print(f"Result: {num1 ** num2}")
  else:
    print("Invalid operator.")

  again = input("Do you want another calculation? (y/n): ").lower()
  if again != "y":
    print("See ya later!")
    break
