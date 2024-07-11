class Person:
    def __init__(self, full_name, phone_number, email_address, home_address):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email_address = email_address
        self.home_address = home_address

    def __str__(self):
        return f"Name: {self.full_name}, Phone: {self.phone_number}, Email: {self.email_address}, Address: {self.home_address}"

class AddressBook:
    def __init__(self):
        self.entries = []

    def add_entry(self, person):
        self.entries.append(person)
        print("Contact successfully added!")

    def display_entries(self):
        if self.entries:
            for idx, person in enumerate(self.entries, 1):
                print(f"{idx}. {person.full_name} - {person.phone_number}")
        else:
            print("No contacts available.")

    def find_entry(self, query):
        results = [person for person in self.entries if query.lower() in person.full_name.lower() or query in person.phone_number]
        if results:
            for person in results:
                print(person)
        else:
            print("No contacts found matching that query.")

    def modify_entry(self, search_name):
        for person in self.entries:
            if person.full_name.lower() == search_name.lower():
                person.full_name = input("Enter new full name: ")
                person.phone_number = input("Enter new phone number: ")
                person.email_address = input("Enter new email address: ")
                person.home_address = input("Enter new home address: ")
                print("Contact successfully updated!")
                return
        print("Contact not found.")

    def remove_entry(self, search_name):
        for person in self.entries:
            if person.full_name.lower() == search_name.lower():
                self.entries.remove(person)
                print("Contact successfully deleted!")
                return
        print("Contact not found.")

def menu():
    address_book = AddressBook()

    while True:
        print("\nAddress Book Menu")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        option = input("Choose an option: ")

        if option == '1':
            full_name = input("Enter full name: ")
            phone_number = input("Enter phone number: ")
            email_address = input("Enter email address: ")
            home_address = input("Enter home address: ")
            person = Person(full_name, phone_number, email_address, home_address)
            address_book.add_entry(person)
        elif option == '2':
            address_book.display_entries()
        elif option == '3':
            query = input("Enter name or phone number to search: ")
            address_book.find_entry(query)
        elif option == '4':
            search_name = input("Enter the full name of the contact to update: ")
            address_book.modify_entry(search_name)
        elif option == '5':
            search_name = input("Enter the full name of the contact to delete: ")
            address_book.remove_entry(search_name)
        elif option == '6':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    menu()
