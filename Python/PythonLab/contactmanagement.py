def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    with open("contacts.txt", "a") as file:
        file.write(f"{name},{phone},{email}\n")
    print("Contact added successfully.")
    
def view_contacts():
    with open("contacts.txt", "r") as file:
        for line in file:
            name, phone, email = line.strip().split(",")
            print(f"Name: {name}, Phone: {phone}, Email: {email}")