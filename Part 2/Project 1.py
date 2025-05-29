# Persistent Contact Book
import time
import os
# File name to store contacts
file_name = "contacts.txt"

# Load Contacts from file into a dictionary
contacts = {}

# Load Contacts from file if it exist
if os.path.exists(file_name):
    with open(file_name,'r') as f:
        for line in f.readlines():
            name,phone = line.strip().split('|')
            contacts[name]=phone


def update_contact_file():
    with open(file_name,'w') as f:
        for name,phone in contacts.items():
            f.write(f"{name}|{phone}\n")

def add_contact():
    name = input("🔤 Enter name:")
    phone = input("📞 Enter phone number:")
    contacts[name] = phone
    update_contact_file()
    print("✅ Contact added Successfully!")

def delete_contact():
    global contacts
    name = input("❌ Enter a name to delete:")
    if name in contacts:
        del contacts[name]
        update_contact_file()
        print("🗑️ Contact Deleted")
    else:
        print("⚠️ Contact not found!")

def view_contacts():
    if contacts:
        print("\n--------🧾 All Contacts---------------")
        for name,phone in contacts.items():
            print(f"🤵 {name} => {phone}")
        print("\n---------------------------------------")
    else:
        print("⚠️ No Contacts Found!")

def search_contacts():
    search = input("Enter name to search: ").lower()
    found = False
    print("\n--------🧾 All Contacts---------------")
    for name,phone in contacts.items():
        if search in name.lower():
            print(f"🤵 {name} => {phone}")
            found = True
    if not found:
        print("😔 No matching contact found.")
    print("\n---------------------------------------")

while True:
    print("\n📔 Contact Book Menu:")
    print("1. Add Contact")
    print("2. View all contacts")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5):")
    print("\n")
    match choice:
        case '1':add_contact()
        case '2':view_contacts()
        case '3':delete_contact()
        case '4':search_contacts()
        case '5':break
        case _:print("⚠️ Invalid Input!")
    time.sleep(2)
