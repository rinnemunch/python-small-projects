import random

print("Welcome to Guess the Number!")

while True:
  print("Choose a difficulty: Easy (1), Medium (2), Hard (3)")

  difficulty = input("Enter 1, 2, or 3: ")

  if difficulty == "1":
    max_num = 50
    max_attempts = 15
  elif difficulty == "2":
    max_num = 100
    max_attempts = 10
  elif difficulty == "3":
    max_num = 500
    max_attempts = 5
  else:
    print("Invalid choice. Defaulting to Medium.")
    max_num = 100
    max_attempts = 10


  number = random.randint(1, max_num)
  attempts = 0

  while True:
      try:
        guess = int(input(f"Enter your guess (1-{max_num}): "))
      except ValueError:
        print("That is not a number. Try again.")
        continue

      attempts += 1

      if guess == number:
        print(f"You got it in {attempts} tries!")
        break
      elif guess < number:
        print("Too low!")
      else:
        print("Too high!")

      if attempts >= max_attempts:
        print(f"Out of tries! The number was {number}.")
        break


  play_again = input("Play again? (y/n): ").lower()
  if play_again != "y":
    print("Thanks for playing!")
    break
