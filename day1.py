import json
import os

running = True
FILENAME = "tasks.json"
l_actions = ['Add Task', 'View Tasks', 'Mark Task as Done', 'Delete Task', 'Exit']


def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            try:
                data = json.load(f)
                if isinstance(data, list):
                    return data
            except json.JSONDecodeError:
                pass
    return []


def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task():
    tasks = load_tasks()
    name = input('📝 Enter task name: ')
    due_date = input('📅 Enter due date (e.g., 31-12-2025): ')

    task = {
        "id": len(tasks) + 1,
        "name": name,
        "due_date": due_date,
        "finished": False
    }

    tasks.append(task)
    save_tasks(tasks)
    print("\n✅ Task added successfully!\n---\n")


def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("\n📭 No tasks found.\n")
        return

    print("\n🗂️ Your Tasks:")
    for task in tasks:
        status = "✅ Done" if task["finished"] else "❌ Not done"
        print(f"[{task['id']}] {task['name']} — Due: {task['due_date']} — {status}")
    print("---\n")


def mark_task():
    tasks = load_tasks()
    if not tasks:
        print("\n📭 No tasks to mark.\n")
        return

    view_tasks()
    try:
        task_id = int(input("✔️ Enter task ID to mark as done: "))
        for task in tasks:
            if task["id"] == task_id:
                if task["finished"]:
                    print("🔁 Task is already marked as done.\n")
                else:
                    task["finished"] = True
                    save_tasks(tasks)
                    print("✅ Task marked as done!\n")
                return
        print("⚠️ Task ID not found.\n")
    except ValueError:
        print("⚠️ Please enter a valid number.\n")


def delete_task():
    tasks = load_tasks()
    if not tasks:
        print("\n📭 No tasks to delete.\n")
        return

    view_tasks()
    try:
        task_id = int(input("🗑️ Enter task ID to delete: "))
        new_tasks = [task for task in tasks if task["id"] != task_id]
        if len(new_tasks) == len(tasks):
            print("⚠️ Task ID not found.\n")
            return
        # Reassign IDs
        for i, task in enumerate(new_tasks, start=1):
            task["id"] = i
        save_tasks(new_tasks)
        print("🗑️ Task deleted successfully!\n")
    except ValueError:
        print("⚠️ Please enter a valid number.\n")


def exit_tasks():
    global running
    running = False
    print("👋 Goodbye, WooMann! Stay productive!\n")


menu_options = {
    "1": add_task,
    "2": view_tasks,
    "3": mark_task,
    "4": delete_task,
    "5": exit_tasks
}

while running:
    print("=== 🚀 WooMann's To-Do List ===")
    for i, action in enumerate(l_actions, 1):
        print(f"{i}. {action}")
    choice = input('Choose an option (1-5): ').strip()
    print()

    action = menu_options.get(choice)
    if action:
        action()
    else:
        print('⚠️ Invalid choice. Try again.\n')
