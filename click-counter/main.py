import tkinter as tk

#main window
window = tk.Tk()
window.title("🖱️ Click Counter")


#variables
count = 0
is_dark = False

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

def toggle_theme():
  global is_dark
  is_dark = not is_dark

  if is_dark:
    bg_color = "#222"
    fg_color = "white"
    btn_color = "#444"
  else:
    bg_color = "white"
    fg_color = "black"
    btn_color = "#f0f0f0"
  #for the window and widgets
  window.config(bg=bg_color)
  label.config(bg=bg_color, fg=fg_color)
  status_label.config(bg=bg_color, fg=fg_color)
  button.config(bg=btn_color, fg=fg_color)
  decrement_button.config(bg=btn_color, fg=fg_color)
  reset_button.config(bg=btn_color, fg=fg_color)
  theme_button.config(bg=btn_color, fg=fg_color)

label = tk.Label(window, text="Count: 0", font=("Arial", 16))
label.pack(pady=10)
status_label = tk.Label(window, text="", font=("Arial", 12))
status_label.pack(pady=5)

#click me button!
button = tk.Button(window, text="Click Me", command=increment, font=("Arial", 14))
button.pack(pady=5)
#decrease button
decrement_button = tk.Button(window, text="Decrement", command=decrement, font=("Arial", 14))
decrement_button.pack(pady=5)
#for the reset button
reset_button = tk.Button(window, text="Reset", command=reset, font=("Arial", 14))
reset_button.pack(pady=5)
#theme button
theme_button = tk.Button(window, text="Toggle Theme", command=toggle_theme, font=("Arial", 14))
theme_button.pack(pady=5)

#run
window.mainloop()
window.iconbitmap("mouse.ico")
