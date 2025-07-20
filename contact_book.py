import json
import os

CONTACTS_FILE = "contacts.json"

# Load from JSON file
def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r") as file:
        return json.load(file)

# Save to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    save_contacts(contacts)
    print("✅ Contact added!")

def view_contacts(contacts):
    if not contacts:
        print("📭 No contacts found.")
        return
    print("\n📒 Contact List:")
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact(contacts):
    key = input("Enter name or phone to search: ").lower()
    results = [c for c in contacts if key in c["name"].lower() or key in c["phone"]]
    if results:
        print("\n🔎 Search Results:")
        for c in results:
            print(f"{c['name']} | {c['phone']} | {c['email']} | {c['address']}")
    else:
        print("❌ No contact found.")

def update_contact(contacts):
    view_contacts(contacts)
    try:
        idx = int(input("Enter contact number to update: ")) - 1
        contact = contacts[idx]
        print("Leave blank to keep current value.")
        name = input(f"Name [{contact['name']}]: ") or contact['name']
        phone = input(f"Phone [{contact['phone']}]: ") or contact['phone']
        email = input(f"Email [{contact['email']}]: ") or contact['email']
        address = input(f"Address [{contact['address']}]: ") or contact['address']
        contacts[idx] = {"name": name, "phone": phone, "email": email, "address": address}
        save_contacts(contacts)
        print("✅ Contact updated.")
    except (ValueError, IndexError):
        print("⚠️ Invalid contact number.")

def delete_contact(contacts):
    view_contacts(contacts)
    try:
        idx = int(input("Enter contact number to delete: ")) - 1
        removed = contacts.pop(idx)
        save_contacts(contacts)
        print(f"🗑️ Contact '{removed['name']}' deleted.")
    except (ValueError, IndexError):
        print("⚠️ Invalid number.")

def contact_menu():
    contacts = load_contacts()
    while True:
        print("\n📱 CONTACT BOOK MENU")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("👋 Exiting Contact Book.")
            break
        else:
            print("❌ Invalid choice. Try again.")

# Start the contact book
if __name__ == "__main__":
    contact_menu()
