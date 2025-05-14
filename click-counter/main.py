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

label = tk.Label(window, text="Count: 0", font=("Arial", 16))
label.pack(pady=10)

#button!
button = tk.Button(window, text="Click Me", command=increment, font=("Arial", 14))
button.pack(pady=5)

#run
window.mainloop()
