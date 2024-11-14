import unittest
import sys
from unittest.mock import patch

# Setting the path to the module to be tested
sys.path.append('../DogDiary')
from BackgroundColorManager import BackgroundColorManager

from unittest.mock import MagicMock

# Creating a mock widget to simulate the real widget's behavior
class MockWidget:
    def __init__(self):
        self.configure = MagicMock()
        self.wisdom_label = MagicMock()
        self.button_frame = MagicMock()
        self.image_frame = MagicMock()
        self.wisdom_frame = MagicMock()

# Test class for the BackgroundColorManager
class TestBackgroundColorManager(unittest.TestCase):

    def setUp(self):
        # Create a mock widget and initialize the manager
        self.widget = MockWidget()
        self.manager = BackgroundColorManager(self.widget)

    def test_set_valid_color(self):
        # Test setting a valid color
        self.manager.set_color("Light Gray")
        self.widget.configure.assert_called_with(bg="#F2F2F2")
        self.widget.wisdom_label.configure.assert_called_with(bg_color="#F2F2F2")

    def test_set_invalid_color(self):
        # Test setting an invalid color
        with patch('builtins.print') as mock_print:
            self.manager.set_color("InvalidColor")
            mock_print.assert_called_with("Invalid Color: InvalidColor")

    def test_get_current_color(self):
        # Test getting the current color
        self.manager.set_color("Sky Blue")
        self.assertEqual(self.manager.get_current_color(), "Sky Blue")

    def test_get_available_colors(self):
        # Test getting the list of available colors
        expected_colors = ["Light Gray", "Light Ivory", "Sky Blue", "Peach"]
        self.assertEqual(self.manager.get_available_colors(), expected_colors)

if __name__ == '__main__':
    unittest.main()