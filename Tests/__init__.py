"""Test suite for DogDiary application."""

import os
import pytest

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    test_file = os.path.join(current_dir, "test_background_color_manager.py")
    pytest.main([test_file])
