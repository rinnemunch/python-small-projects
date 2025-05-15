import time
import random

def tell_joke():
  jokes = [
    ("Why don't programmers like nature?", "It has too many bugs!"),
    ("Why do Python devs wear glasses?", "Because they can't C!"),
    ("What's a programmer's favorite hangout place?", "The Foo Bar."),
    ("Why did the developer go broke?", "Because he used up all his cache!"),
    ("How many programmers does it take to change a light bulb?", "None, that's a hardware problem!")
  ]

  setup, punchline = random.choice(jokes)

  print("Here's a joke for you...\n")
  time.sleep(1.5)
  print(setup)
  time.sleep(2)
  print(punchline + "\n")

#Starting the joke
if __name__ == "__main__":
  count = 0

  while True:
    user_input = input("Press Enter to hear a joke (or type 'q' to quit): ")
    if user_input.lower() == "q":
      print(f"\nYou heard {count} cringy ass joke(s) today. See ya!")
      break
    tell_joke()
    count += 1
