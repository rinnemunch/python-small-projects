import random
import string

def generate_password(length=12):
  chars = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choice(chars) for _ in range(length))
  return password

if __name__ == "__main__":
  print("🔒 Generated Password:")
  print(generate_password())
