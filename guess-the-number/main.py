import random

print("Welcome to Guess the Number!")
number = random.randint(1, 100)

while True:
  guess = int(input("Enter your guess (1-100): "))
  if guess == number:
    print("You got it!")
    break
  elif guess < number:
    print("Too low!")
  else:
    print("Too high!")
