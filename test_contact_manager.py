import unittest
from unittest.mock import patch

import contact_manager


class TestContactManager(unittest.TestCase):
    """Test contact creation, lookup, deletion, and error handling."""

    def setUp(self):
        """Start each test with an empty contact list."""
        contact_manager.contacts.clear()

    def test_add_new_contact(self):
        """Adding a new contact stores its phone number."""
        contact_manager.add_contact("Alice", "555-0100")
        self.assertEqual(contact_manager.contacts["Alice"], "555-0100")

    def test_find_existing_contact(self):
        """Finding an existing contact returns its phone number."""
        contact_manager.contacts["Alice"] = "555-0100"
        with patch("builtins.print"):
            result = contact_manager.find_contact("Alice")
        self.assertEqual(result, "555-0100")

    def test_find_nonexistent_contact(self):
        """Finding a missing contact returns None without crashing."""
        with patch("builtins.print") as mock_print:
            result = contact_manager.find_contact("Missing")
        self.assertIsNone(result)
        mock_print.assert_called_with("Contact not found.")

    def test_delete_existing_contact(self):
        """Deleting an existing contact removes it from the dictionary."""
        contact_manager.contacts["Alice"] = "555-0100"
        with patch("builtins.print"):
            result = contact_manager.delete_contact("Alice")
        self.assertTrue(result)
        self.assertNotIn("Alice", contact_manager.contacts)

    def test_delete_nonexistent_contact(self):
        """Deleting a missing contact returns False without crashing."""
        with patch("builtins.print") as mock_print:
            result = contact_manager.delete_contact("Missing")
        self.assertFalse(result)
        mock_print.assert_called_with("Contact not found.")

    def test_add_duplicate_contact_raises_error(self):
        """Adding an existing name raises DuplicateContactError."""
        contact_manager.contacts["Alice"] = "555-0100"
        with self.assertRaises(contact_manager.DuplicateContactError):
            contact_manager.add_contact("Alice", "555-9999")

    def test_menu_rejects_non_integer_input(self):
        """A non-integer menu choice is handled and the loop continues."""
        with patch("builtins.input", side_effect=["letter", "4"]), patch(
            "builtins.print"
        ) as mock_print:
            contact_manager.main()
        mock_print.assert_any_call(
            "Invalid input. Enter a number from 1 to 4."
        )


if __name__ == "__main__":
    unittest.main()
