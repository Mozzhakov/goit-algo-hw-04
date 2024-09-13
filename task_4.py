def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def error_handler(function):
    def func_wrap(args, contacts):
        try:
            return function(args, contacts)
        except ValueError:
            print('Wrong amount of args.')
    return func_wrap

def add_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        contacts[name.capitalize()] = phone
        return "Contact added."
    return 'Contact already exists.'
    
def change_contact(args, contacts):
    name, phone = args
    name = name.capitalize()
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return 'Contact not found.'

def show_phone(args, contacts):
    name = args[0].capitalize()
    if name in contacts:
        return contacts[name]
    return 'Contact not found.'

def show_all(contacts):
    for name, phone in contacts.items():
        print(f'{name}: {phone}')

add_contact = error_handler(add_contact)
change_contact = error_handler(change_contact)
show_phone = error_handler(show_phone)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case 'exit' | 'close':
                print("Good bye!")
                break
            case 'hello':
                print("How can I help you?")
            case 'add': 
                print(add_contact(args, contacts))
            case 'change':
                print(change_contact(args, contacts))
            case 'phone':
                print(show_phone(args, contacts))
            case "all":
                show_all(contacts)
            case _:
                print("Invalid command.")
    
if __name__ == "__main__":
    main()

