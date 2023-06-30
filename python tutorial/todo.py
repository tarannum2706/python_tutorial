tasks = []

# Function to add a task to the list
def add_task():
  task = input("Enter a task: ")
  tasks.append(task)
  print("Task added successfully!")

# Function to remove a task from the list
def remove_task():
  task = input("Enter the task to remove: ")
  if task in tasks:
   tasks.remove(task)
   print("Task removed successfully!")
  else:
   print("Task not found!")

# Function to display all tasks
def show_tasks():
 if len(tasks) == 0:
  print("No tasks found!")
 else:
  print("Tasks:")
 for index, task in enumerate(tasks):
  print(f"{index+1}. {task}")

# Main loop
while True:
 print("\nMenu:")
 print("1. Add task")
 print("2. Remove task")
 print("3. Show tasks")
 print("4. Quit")
 choice = input("Enter your choice (1-4): ")

 if choice == "1":
  add_task()
 elif choice == "2":
  remove_task()
 elif choice == "3":
  show_tasks()
 elif choice == "4":
  print("Goodbye!")
  break
 else:
  print("Invalid choice!")