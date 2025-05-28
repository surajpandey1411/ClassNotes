import csv

CONTACTS_FILE = 'contacts.csv'

def load_contacts():
    """Load contacts from the CSV file."""
    try:
        with open(CONTACTS_FILE, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    """Save contacts to the CSV file."""
    with open(CONTACTS_FILE, mode='w', newline='') as file:
        fieldnames = ['name', 'phone', 'email']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)

def add_contact():
    """Add a new contact."""
    contacts = load_contacts()
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts.append({'name': name, 'phone': phone, 'email': email})
    save_contacts(contacts)
    print(f"Contact '{name}' added.")

def view_contacts():
    """View all contacts."""
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
    else:
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def search_contact():
    """Search for a contact."""
    search_term = input("Enter name or phone number to search: ")
    contacts = load_contacts()
    results = [contact for contact in contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
    if results:
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("No matching contacts found.")

def update_contact():
    """Update an existing contact."""
    name = input("Enter the name of the contact to update: ")
    contacts = load_contacts()
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"Current details: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            contact['phone'] = input("Enter new phone number: ")
            contact['email'] = input("Enter new email address: ")
            save_contacts(contacts)
            print(f"Contact '{name}' updated.")
            return
    print("Contact not found.")

def delete_contact():
    """Delete a contact."""
    name = input("Enter the name of the contact to delete: ")
    contacts = load_contacts()
    for i, contact in enumerate(contacts):
        if contact['name'].lower() == name.lower():
            del contacts[i]
            save_contacts(contacts)
            print(f"Contact '{name}' deleted.")
            return
    print("Contact not found.")

def main():
    """Main menu for the contact management system."""
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
