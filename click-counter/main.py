import tkinter as tk

#main window
window = tk.Tk()
window.title("Click Counter")

#variables
count = 0

#increase & decrease
def increment():
  global count
  count += 1
  label.config(text=f"Count: {count}")

  #milestone messages
  if count == 10:
    status_label.config(text="🔥 10 clicks! You're on fire!")
  elif count == 50:
    status_label.config(text="😲 50? Ight chill.")
  elif count == 100:
    status_label.config(text="🚀 100! You're unstoppable and a bit crazy!")
  else:
    status_label.config(text="")

def decrement():
  global count
  count -= 1
  label.config(text=f"Count: {count}")

def reset():
  global count
  count = 0
  label.config(text=f"Count: {count}")

label = tk.Label(window, text="Count: 0", font=("Arial", 16))
label.pack(pady=10)
status_label = tk.Label(window, text="", font=("Arial", 12))
status_label.pack(pady=5)

#button!
button = tk.Button(window, text="Click Me", command=increment, font=("Arial", 14))
button.pack(pady=5)
#decrease button
decrement_button = tk.Button(window, text="Decrement", command=decrement, font=("Arial", 14))
decrement_button.pack(pady=5)
#for the reset button
reset_button = tk.Button(window, text="Reset", command=reset, font=("Arial", 14))
reset_button.pack(pady=5)

#run
window.mainloop()
