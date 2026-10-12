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

### Screencast

**Screencast link:** Replace this line with your video URL after uploading your 3–5 minute recording.

```
