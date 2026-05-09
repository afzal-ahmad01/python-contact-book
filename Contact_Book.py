contacts = {}

while True:
    print("\n--- CONTACT BOOK MENU ---")
    print("1. Add Contact Number")
    print("2. Search Contact Number")
    print("3. Exit")

    choice = input("Enter 1/2/3: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")

        contacts[name] = phone

        print("Done! Your number has been saved.")

    elif choice == "2":
        search = input("Enter Name You Want To Search: ")

        if search in contacts:
            print(f"We found {search}. Contact Number: {contacts[search]}")
        else:
            print("Sorry, this contact is not in the list.")

    elif choice == "3":
        print("Program Closed. Goodbye!")
        break

    else:
        print("Invalid Option! Please choose 1, 2, or 3.")
















