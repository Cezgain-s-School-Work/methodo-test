import unittest
from unittest.mock import patch
from io import StringIO
from main import is_palindrome, process_user_input, process_console


class TestPalindrome(unittest.TestCase):
    def test_palindrome_true(self):
        self.assertTrue(is_palindrome("Radar"))
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_palindrome_false(self):
        self.assertFalse(is_palindrome("Hello"))
        self.assertFalse(is_palindrome("Python"))


class TestProcessUserInput(unittest.TestCase):
    @patch("builtins.input", return_value="Radar")
    @patch("sys.stdout", new_callable=StringIO)
    def test_palindrome_input(self, mock_stdout, _):
        process_user_input()
        self.assertIn("Bien dit !", mock_stdout.getvalue())

    @patch("builtins.input", return_value="Hello")
    @patch("sys.stdout", new_callable=StringIO)
    def test_non_palindrome_input(self, mock_stdout, _):
        process_user_input()
        self.assertIn("Hello", mock_stdout.getvalue())


class TestProcessConsole(unittest.TestCase):
    @patch("builtins.input", side_effect=["Radar", KeyboardInterrupt])
    @patch("sys.stdout", new_callable=StringIO)
    def test_console_flow(self, mock_stdout, _):
        process_console()
        output = mock_stdout.getvalue()
        self.assertIn("Bonjour !", output)
        self.assertIn("Bien dit !", output)
        self.assertIn("Au revoir !", output)


if __name__ == "__main__":
    unittest.main()
