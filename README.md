# Contact Manager

## Project Overview

Contact Manager is a command-line Python application for managing a simple contact list. It allows users to add contacts, look up phone numbers, delete contacts, and exit the program. The project focuses on reliable error handling and unit testing.

## Features

- Add a contact with a name and phone number.
- Find a contact and display the phone number.
- Delete a contact.
- Reject duplicate contact names using a custom `DuplicateContactError` exception.
- Handle attempts to find or delete contacts that do not exist.
- Validate menu input and recover when the user enters a non-integer choice.
- Run automated unit tests with Python's built-in `unittest` framework.

## Files

- `buggy_contacts.py` — the original starter program supplied with the assignment.
- `contact_manager.py` — the corrected contact manager application.
- `test_contact_manager.py` — unit tests for the application's behavior.
- `README.md` — project overview and instructions.

## Requirements

- Python 3.7 or newer.

## How to Run

1. Download or clone the repository.
2. Open a terminal in the project folder.
3. Click run in your preferred code-editor
4. Follow the on-screen menu.


## How to Run the Tests

From the project folder, run:

```bash
python -m unittest test_contact_manager.py
```

The tests check adding a contact, finding an existing contact, handling a missing contact, deleting an existing contact, handling deletion of a missing contact, rejecting duplicate contacts, and handling non-integer menu input.

## Updated Design

### 1. Invalid menu input

The original program did not convert menu input to an integer. The new program uses `try/except ValueError` to display a message to continue the loop.

### 2. Missing contacts during lookup

The original `find_contact()` accessed the dictionary directly, which could raise a `KeyError`. The corrected function catches that error, prints `Contact not found.`, and returns `None` when the contact does not exist.

### 3. Missing contacts during deletion

The original `delete_contact()` could raise a `KeyError` when a name was absent. The corrected function catches the error, prints `Contact not found.`, and returns `False`. It returns `True` after a successful deletion.

### 4. Duplicate contacts

The corrected program defines `DuplicateContactError`. The `add_contact()` function raises this exception if the name already exists, and `main()` catches it to show the error without terminating the application.

### 5. Automated tests

`test_contact_manager.py` uses `unittest.TestCase` to test expected behavior. Each test starts with an empty contact dictionary so that results do not depend on earlier tests.

### Screencast

**Screencast link:** Replace this line with your video URL after uploading your 3–5 minute recording.

```