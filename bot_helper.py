def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    if len(args) != 2:
        return "Error: Only 2 parameters were expected. Please try again. Example usage: add [name] [phone number]"
    else:
        name, phone = args
        if not (name in contacts):
            contacts[name] = phone
            return "Contact added."
        else:
            return f"Contact {name} is already in contacts. Please use change command to update existing contact."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Error: Only 2 parameters were expected. Please try again. Example usage: change [name] [phone number]"
    else:
        name, phone = args
        if not (name in contacts):
            return f"Contact {name} is not in contacts. Please use add command to add a new contact."
        contacts[name] = phone
        return "Contact updated."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Error: Only 1 parameter was expected. Please try again. Example usage: phone [name]"
    else:
        name = args[0]
        if not (name in contacts):
            return f"Contact {name} is not in contacts. Please use add command to add a new contact."
    return contacts[name]


def show_all(args, contacts):
    if len(args) > 0:
        print("Error: No parameters was expected. Please try again. Example usage: all")
    for k in contacts:
        print(f"{k}: {contacts[k]}")


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            show_all(args, contacts)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
