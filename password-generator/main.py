import random
import string

def generate_password(length=12):
  chars = string.ascii_letters + string.digits + string.punctuation
  return ''.join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
  try:
    length = int(input("Enter desired password length: "))
    if length < 4:
      print("Password too short. Must be at least 4 characters.")
    else:
      password = generate_password(length)
      print(f"\n 🔒 Your password ({length} characters):\n{password}")
  except ValueError:
    print("Please enter a valid number.")
