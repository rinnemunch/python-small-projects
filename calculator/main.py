print("Simple Calculator")

while True:

  while True:
    try:
      num1 = float(input("Enter first number: "))
      break
    except ValueError:
      print("That is not a valid number. Try again.")

  op = input("Enter operator (+, -, *, /): ")

  while True:
    try:
      num2 = float(input("Enter second number: "))
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
  else:
    print("Invalid operator.")

  again = input("Do you want another calculation? (y/n): ").lower()
  if again != "y":
    print("See ya later!")
    break
