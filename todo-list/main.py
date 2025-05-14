import tkinter as tk

#main window
window = tk.Tk()
window.title("Shaun's To-Do List")

#Frame
input_frame = tk.Frame(window)
input_frame.pack(pady=10)

#boxes for tasks
task_entry = tk.Entry(input_frame, width=30)
task_entry.pack(side=tk.LEFT, padx=5)

#task list display
tasks_frame = tk.Frame(window)
tasks_frame.pack(pady=10)

#functions
def add_task():
  task_text = task_entry.get()
  if task_text:
    label = tk.Label(tasks_frame, text=task_text, font=("Arial", 12), anchor="w")
    label.pack(fill="x")
    task_entry.delete(0, tk.END)

#button
add_button = tk.Button(input_frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

window.mainloop()
