import tkinter as tk

#main window
window = tk.Tk()
window.title("Shaun's To-Do List")
#styling
window.geometry("400x400")
window.configure(bg="#f4f4f4")

#Frame
input_frame = tk.Frame(window)
input_frame.pack(pady=10)

#boxes for tasks
task_entry = tk.Entry(input_frame, width=30, font=("Segoe UI", 11))
task_entry.pack(side=tk.LEFT, padx=5)

#task list display
tasks_frame = tk.Frame(window, bg="#f4f4f4", padx=10)
tasks_frame.pack(pady=10)

#functions
def add_task():
  task_text = task_entry.get()
  if task_text:
    #frame for each task row
    task_frame = tk.Frame(tasks_frame)
    task_frame.pack(fill="x", pady=2)

    #task label
    label = tk.Label(task_frame, text=task_text, font=("Segoe UI", 12), anchor="w", bg="white", padx=10)
    label.pack(side=tk.LEFT, fill="x", expand=True)

    #delete button
    delete_button = tk.Button(task_frame, text="❌", command=task_frame.destroy)
    delete_button.pack(side=tk.RIGHT)

    #clear box
    task_entry.delete(0, tk.END)


#button
add_button = tk.Button(input_frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

task_entry.bind("<Return>", lambda event: add_task()) #this is just the function to click enter to add another task

window.mainloop()
