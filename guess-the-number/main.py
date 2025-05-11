import random

print("Welcome to Guess the Number!")
number = random.randint(1, 100)
attempts = 0

while True:
  guess = int(input("Enter your guess (1-100): "))
  attempts += 1

  if guess == number:
    print(f"You got it in {attempts} tries!")
    break
  elif guess < number:
    print("Too low!")
  else:
    print("Too high!")
