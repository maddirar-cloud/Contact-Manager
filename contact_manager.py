"""A fault-tolerant command-line contact manager."""


class DuplicateContactError(Exception):
    """Raised when a contact name already exists."""


contacts = {}


def add_contact(name, phone):
    """Add a contact, raising DuplicateContactError for duplicate names."""
    if name in contacts:
        raise DuplicateContactError(f"Contact '{name}' already exists.")
    contacts[name] = phone
    print(f"Added {name} to contacts.")
    return phone


def find_contact(name):
    """Return a contact's phone number, or None if the contact is missing."""
    try:
        phone = contacts[name]
    except KeyError:
        print("Contact not found.")
        return None

    print(phone)
    return phone


def delete_contact(name):
    """Delete a contact and return True, or return False if it is missing."""
    try:
        del contacts[name]
    except KeyError:
        print("Contact not found.")
        return False

    print(f"Deleted {name}.")
    return True


def main():
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. Find Contact")
        print("3. Delete Contact")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Enter a number from 1 to 4.")
            continue

        if choice == 1:
            name = input("Enter contact name: ").strip()
            phone = input("Enter phone number: ").strip()
            try:
                add_contact(name, phone)
            except DuplicateContactError as error:
                print(error)
        elif choice == 2:
            name = input("Enter name to find: ").strip()
            find_contact(name)
        elif choice == 3:
            name = input("Enter name to delete: ").strip()
            delete_contact(name)
        elif choice == 4:
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
