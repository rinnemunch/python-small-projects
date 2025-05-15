import time

def start_pomodoro():
  work_minutes = 25
  total_seconds = work_minutes * 60

  print("Pomodoro Started! Focus for 25 minutes.\n")

  while total_seconds:
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    print(f"{minutes:02d}", end="\r")
    time.sleep(1)
    total_seconds -= 1

  print("\nTime's up! Take a 5-minute break.")

if __name__ == "__main__":
  start_pomodoro()
