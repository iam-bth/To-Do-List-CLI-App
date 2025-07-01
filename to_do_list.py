#importing JSON
import json
import os

#always save or load in the same folder as my .py file
base_dir = os.path.dirname(os.path.abspath(__file__))
tasks_file = os.path.join(base_dir, "tasks.json")

#defining function to load tasks
def load_tasks():
    if os.path.exists(tasks_file):
        with open(tasks_file, mode = "r") as file:
            return json.load(file)
    else:
        return []
    
#Empty task
tasks = load_tasks()

#defining function to show menu
def show_menu():
    print('\n===== TO-DO-LIST =====')
    print('1. Show tasks')
    print('2. Add tasks')
    print('3. Mark a task as done')
    print('4. Delete a task')
    print('5. Exit') 
    
#defining function to save task in json
def save_tasks():
    with open(tasks_file, "w") as file:
        json.dump(tasks, file, indent = 4)
        print("Tasks saved to tasks.json")
        
#defining function to display tasks
def display_tasks():
    if not tasks:
        print('No tasks added.')
    else:
        for i, task in enumerate(tasks, start = 1):
            status = '[✔️]' if task["done"] else "[]"
            print(f'{i}. {status} {task["title"]}')
            
#main loop
while True:
    show_menu()
    choice = input("Enter a choice 1-5: ").strip()
    
    if choice == "1":
        print("\n Your tasks:")
        display_tasks()
    
    elif choice == "2":
        title = input("Enter your new task: ").strip()
        tasks.append({"title" : title, "done" : False})
        print("Task added.")
        
    elif choice == "3":
        if not tasks:
            print("No tasks to mark as done.")
        else:
            display_tasks()
            try:
                num = int(input("Enter task number to mark as done: "))
                if 1 <= num <= len(tasks):
                    tasks[num - 1] ["done"] = True
                    print("Task marked as done.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
                
    elif choice == "4":
        if not tasks:
            print("No tasks to delete.")
        else:
            display_tasks()
            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    deleted = tasks.pop(num - 1)
                    print(f"Deleted: {deleted["title"]}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
            
                
    elif choice == "5":
        save_tasks()
        print("Have a Good Day!..")
        break
    
    else:
        print("Inavlid choice. Please enter 1 to 5.")