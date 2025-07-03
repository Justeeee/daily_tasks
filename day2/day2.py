import json
import os

running = True
FILENAME = "passwords.json"
l_actions = ['Add password', 'View password', 'Change password', 'Delete password', 'Exit']


def load_passwords():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            try:
                data = json.load(f)
                if isinstance(data, list):
                    return data
            except json.JSONDecodeError:
                pass
    return []


def save_passwords(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=4)


def add_password():
    passwords = load_passwords()
    website = input('📝 Enter website address: ')
    password = input('📅 Enter password (e.g., abcdefg123): ')

    data = {
        "id": len(passwords) + 1,
        "website": website,
        "password": password,
    }

    passwords.append(data)
    save_passwords(passwords)
    print("\n✅ Password added successfully!\n---\n")


def view_passwords():
    passwords = load_passwords()
    if not passwords:
        print("\n📭 No passwords found.\n")
        return

    print("\n🗂️ Your passwords:")
    for password in passwords:
        print(f"[{password['id']}] {password['website']} — Password: {password['password']}")
    print("---\n")


def change_password():
    passwords = load_passwords()
    if not passwords:
        print("\n📭 No passwords to change.\n")
        return

    view_passwords()
    try:
        password_id = int(input("✔️ Enter password ID to change it: "))
        for password in passwords:
            if password["id"] == password_id:
                new_password = input('Please enter new password: ')
                password["password"] = new_password
                save_passwords(passwords)
                return
        print("⚠️ Password ID not found.\n")
    except ValueError:
        print("⚠️ Please enter a valid number.\n")


def delete_password():
    passwords = load_passwords()
    if not passwords:
        print("\n📭 No passwords to delete.\n")
        return

    view_passwords()
    try:
        password_id = int(input("🗑️ Enter password ID to delete: "))
        new_passwords = [password for password in passwords if password["id"] != password_id]
        if len(new_passwords) == len(passwords):
            print("⚠️ Password ID not found.\n")
            return
        # Reassign IDs
        for i, password in enumerate(new_passwords, start=1):
            password["id"] = i
        save_passwords(new_passwords)
        print("🗑️ Password deleted successfully!\n")
    except ValueError:
        print("⚠️ Please enter a valid number.\n")


def exit_passwords():
    global running
    running = False
    print("👋 Goodbye, WooMann! Stay productive!\n")


menu_options = {
    "1": add_password,
    "2": view_passwords,
    "3": change_password,
    "4": delete_password,
    "5": exit_passwords
}

while running:
    print("=== 🚀 WooMann's Password Saver ===")
    for i, action in enumerate(l_actions, 1):
        print(f"{i}. {action}")
    choice = input('Choose an option (1-5): ').strip()
    print()

    action = menu_options.get(choice)
    if action:
        action()
    else:
        print('⚠️ Invalid choice. Try again.\n')
