print("Simple Calculator")

while True:
  num1 = float(input("Enter first number: "))
  op = input("Enter operator (+, -, *, /): ")
  num2 = float(input("Enter second number: "))

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
