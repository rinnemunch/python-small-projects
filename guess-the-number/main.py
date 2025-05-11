import random

print("Welcome to Guess the Number!")

while True:
  print("Choose a difficulty: Easy (1), Medium (2), Hard (3)")

  difficulty = input("Enter 1, 2, or 3: ")

  if difficulty == "1":
    max_num = 50
  elif difficulty == "2":
    max_num = 100
  elif difficulty == "3":
    max_num = 500
  else:
    print("Invalid choice. Defaulting to Medium.")
    max_num = 100


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


  play_again = input("Play again? (y/n): ").lower()
  if play_again != "y":
    print("Thanks for playing!")
    break
