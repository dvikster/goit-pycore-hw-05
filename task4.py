import re 

# Декоратор для обробки помилок
def input_error(func):
    def inner(*args, **kwargs):
        try:
            # Для функцій, які додають або змінюють контакт додаю додаткову перевірку на кількість аргументів add_contact та change_contact
            if func.__name__ in ["add_contact", "change_contact"]:
                if len(args[0]) < 2:
                    # Перевірка на кількість аргументів
                    raise ValueError("Give me name and phone please.")
                phone = args[0][1]
                # Перевірка формату номера телефону
                if not re.match(r'^[\d\+\-\(\)]+$', phone):
                    return "Phone number can contain only digits and symbols (+, -, (, ))."

            # Для show_all перевіряємо, чи є контакти
            if func.__name__ == "show_all" and not kwargs.get("contacts"):
                return "No contacts added yet"

            # Виклик основної функції
            return func(*args, **kwargs)
        
        except IndexError:
            return "Give me name please" #ця помилка буде спрацьовувати для функції show_phone, коли не додане ім'я, бо попереду є перевірка на два аргумента для інших функцій
        except KeyError:
            return "Contact not found." #ця помилка буде спрацьовувати для функції show_phone коли не знайдено контакт з введеним іменем
        except ValueError as e:
            return str(e)
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args, contacts):
    name, phone = args[0], args[1]
    contacts[name] = phone
    return f"Contact {name} added."

@input_error
def change_contact(args, contacts):
    name, phone = args[0], args[1]
    contacts[name] = phone
    return f"Contact {name} updated."

@input_error
def show_phone(args, contacts):
    name = args[0]
    return f"{name}'s phone number: {contacts[name]}"

@input_error
def show_all(args, contacts):
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip()

        if not user_input: #додала перевірку на пустий enter
            print("Error: Please enter a command.")
            continue

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts=contacts))
        elif command == "change":
            print(change_contact(args, contacts=contacts))
        elif command == "phone":
            print(show_phone(args, contacts=contacts))
        elif command == "all":
            print(show_all(args, contacts=contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
