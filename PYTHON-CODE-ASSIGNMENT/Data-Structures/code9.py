def phonebook_program():
    phonebook = {}
    while True:
        print("\n1. Add Contact\n2. View Contact\n3. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            name = input("Name: ")
            number = input("Phone Number: ")
            phonebook[name] = number
        elif choice == '2':
            name = input("Enter name to look up: ")
            print("Number:", phonebook.get(name, "Not found"))
        elif choice == '3':
            break
        else:
            print("Invalid choice")


phonebook_program()