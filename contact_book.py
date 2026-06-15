# Code is main attempt at creating a contact book
# Lacked the time and creativity to visualize contact book
"""print("Contact Book")

# Use for loop?
contact = {}

def contact_menu():
    print("Contact Book")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def add_contact():
    contacts = {}
    name = input("Enter name: ")
    phone_number = int(input("Enter phone number: "))
    contacts[name] = phone_number
    print(contacts)

def view_contacts():
    print(contact)

def search_contacts():
    print(contact)

def del_contacts():
    print(contact)

def exit_contacts():
    print("Exiting Contact Book")

def action_book():

    contact_menu()
    
    choice = int(input("Select Option: "))

    if choice == 1:
        add_contact()

    if choice == 2:
        view_contacts()

    if choice == 3:
        search_contacts()

    if choice == 4:
        del_contacts()

    if choice == 5:
        exit_contacts()

    
action_book()"""

# All code below is AI assisted (ChatGPT).
def contact_book():
    contacts = {}
    running = True
    # Menu list
    def menu():
        print("\n=== Contact Book Menu ===")
        print("1. Add a New Contact")
        print("2. View All Contacts")
        print("3. Search for a Contact")
        print("4. Delete a Contact")
        print("5. Exit")
    # New contacts
    def new_contact():
        name = input("Enter contact name: ")
        number = input("Enter telephone number: ")
        contacts[name] = number
        print(f"Contact '{name}' added successfully.")
    # Viewing contacts
    def view_all_contacts():
        if not contacts:
            print("No contacts available.")
            return

        print("\n--- All Contacts ---")
        for name, number in contacts.items():
            print(f"Name: {name}, Number: {number}")
    # Search for specific contacct
    def search_contact():
        name = input("Enter name to search: ")
        if name in contacts:
            print(f"Found - Name: {name}, Number: {contacts[name]}")
        else:
            print("Contact not found.")
    # Delete contact
    def del_contact():
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact '{name}' deleted.")
        else:
            print("Contact not found.")
    # Leave contact book
    def exit():
        nonlocal running
        print("Exiting Contact Book...")
        running = False
    # Choose option in menu
    while running:
        menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            new_contact()
        elif choice == "2":
            view_all_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            del_contact()
        elif choice == "5":
            exit()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    contact_book()


"""I'm including the AI prompt for how I had visualized the program:
I need to create a python file of a Contact Book. It has 5 inputs: Add\n
a New Contact, View All Contacts, Search for a Contact, Delete a Contact, \n
and Exit. The first function is titled menu(). It contains a print out as \n
follows: 1. Add a New Contact 2. View All Contacts 3. Search for a Contact \n
4. Delete a Contact 5. Exit. The second function is titled new_contact().\n
The function takes inputs and puts them into a dictionary. The first input\n
is a name and is input into the key. The second input is the telephone number\n
and is input into the value. The number is stored into a dictionary for other\n
functions to access. The third function is titled view_all_contacts(). It\n
gives a view of all contacts stored into the dictionary so far. The fourth\n
function is titled search_contact(). It allows the user to search and check\n
if the name and telephone number are in the dictionary. The fifth function is\n
titled del_contact(). This function allows user to delete a key and value from\n
the dictionary. The sixth function is titled exit(). This function allows the\n
user to exit from the Contact Book. The seventh function is titled contact_book().\n
This function contains within it the first, second, third, fourth, fifth, and sixth\n
functions inside it."""