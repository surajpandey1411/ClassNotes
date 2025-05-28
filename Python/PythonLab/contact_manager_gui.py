import tkinter as tk
from tkinter import messagebox
import json

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    """Load contacts from the JSON file."""
    try:
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_contacts(contacts):
    """Save contacts to the JSON file."""
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    """Add a new contact."""
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    if name and phone:
        contacts = load_contacts()
        contacts.append({'name': name, 'phone': phone, 'email': email})
        save_contacts(contacts)
        update_contact_list()
        clear_entries()
        messagebox.showinfo("Success", "Contact added successfully.")
    else:
        messagebox.showerror("Error", "Name and phone number are required.")

def update_contact_list():
    """Update the listbox with all contacts."""
    contacts = load_contacts()
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def clear_entries():
    """Clear the input fields."""
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

def on_contact_select(event):
    """Populate the input fields with the selected contact's details."""
    try:
        selected_index = contact_listbox.curselection()[0]
        contacts = load_contacts()
        selected_contact = contacts[selected_index]
        name_entry.delete(0, tk.END)
        name_entry.insert(tk.END, selected_contact['name'])
        phone_entry.delete(0, tk.END)
        phone_entry.insert(tk.END, selected_contact['phone'])
        email_entry.delete(0, tk.END)
        email_entry.insert(tk.END, selected_contact['email'])
    except IndexError:
        pass

def delete_contact():
    """Delete the selected contact."""
    try:
        selected_index = contact_listbox.curselection()[0]
        contacts = load_contacts()
        del contacts[selected_index]
        save_contacts(contacts)
        update_contact_list()
        clear_entries()
        messagebox.showinfo("Success", "Contact deleted successfully.")
    except IndexError:
        messagebox.showerror("Error", "Please select a contact to delete.")

def search_contact():
    """Search for contacts by name."""
    search_term = search_entry.get().lower()
    contacts = load_contacts()
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        if search_term in contact['name'].lower():
            contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Set up the main window
root = tk.Tk()
root.title("Contact Manager")

# Create the input fields and labels
tk.Label(root, text="Name").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Phone").grid(row=1, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1)

tk.Label(root, text="Email").grid(row=2, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)

# Create the buttons
tk.Button(root, text="Add Contact", command=add_contact).grid(row=3, column=0)
tk.Button(root, text="Delete Contact", command=delete_contact).grid(row=3, column=1)
tk.Button(root, text="Search", command=search_contact).grid(row=4, column=0, columnspan=2)

# Create the search entry
search_entry = tk.Entry(root)
search_entry.grid(row=4, column=1)

# Create the listbox to display contacts
contact_listbox = tk.Listbox(root, height=10, width=50)
contact_listbox.grid(row=5, column=0, columnspan=2)
contact_listbox.bind('<<ListboxSelect>>', on_contact_select)

# Initialize the contact list
update_contact_list()

# Start the main loop
root.mainloop()
