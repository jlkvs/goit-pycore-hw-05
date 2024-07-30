def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            if isinstance(e, KeyError):
                return "This contact does not exist."
            elif isinstance(e, ValueError):
                return "Give me name and phone please."
            elif isinstance(e, IndexError):
                return "Enter user name."
    return inner

@input_error
def add_contact(args, contacts):
    if len(args) < 2:
        raise ValueError
    name, phone = args[0], " ".join(args[1:])
    contacts[name] = phone
    return f"Contact {name} added with phone number {phone}."

@input_error
def change_contact(args, contacts):
    if len(args) < 2:
        raise ValueError
    name, phone = args[0], " ".join(args[1:])
    if name in contacts:
        contacts[name] = phone
        return f"Phone number for {name} updated to {phone}."
    else:
        raise KeyError

@input_error
def show_phone(args, contacts):
    if not args:
        raise IndexError
    name = args[0]
    if name in contacts:
        return f"{name}'s phone number is {contacts[name]}."
    else:
        raise KeyError

@input_error
def show_all_contacts(_, contacts):
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts available."

def parse_input(user_input):
    tokens = user_input.strip().split()
    cmd = tokens[0].lower() if tokens else ""
    args = tokens[1:]
    return cmd, args

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

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
        elif command == "show":
            print(show_all_contacts(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
