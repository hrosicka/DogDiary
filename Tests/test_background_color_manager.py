"""
Unit tests for the BackgroundColorManager module.
Tests color management functionality.
"""

import os
import sys
import pytest
from unittest.mock import MagicMock, patch

# Dynamically add the parent directory to sys.path BEFORE importing local modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from BackgroundColorManager import BackgroundColorManager


class TestBackgroundColorManager:
    """Tests for BackgroundColorManager class."""
    
    @pytest.fixture
    def mock_widget(self):
        """Create a mock widget for testing."""
        widget = MagicMock()
        widget.wisdom_label = MagicMock()
        widget.button_frame = MagicMock()
        widget.image_frame = MagicMock()
        widget.wisdom_frame = MagicMock()
        return widget
    
    def test_initialization(self, mock_widget):
        """Test BackgroundColorManager initialization."""
        manager = BackgroundColorManager(mock_widget)
        
        assert manager.widget == mock_widget
        assert manager.current_color == "Light Gray"
        assert len(manager.available_colors) == 4
    
    def test_available_colors_exist(self, mock_widget):
        """Test that all available colors are defined."""
        manager = BackgroundColorManager(mock_widget)
        
        colors = ["Light Gray", "Light Ivory", "Sky Blue", "Peach"]
        for color in colors:
            assert color in manager.available_colors
    
    def test_set_color_valid(self, mock_widget):
        """Test setting a valid color."""
        manager = BackgroundColorManager(mock_widget)
        
        manager.set_color("Sky Blue")
        
        assert manager.current_color == "Sky Blue"
        mock_widget.configure.assert_called()
    
    def test_set_color_invalid(self, mock_widget, capsys):
        """Test setting an invalid color."""
        manager = BackgroundColorManager(mock_widget)
        
        manager.set_color("InvalidColor")
        
        captured = capsys.readouterr()
        assert "Invalid Color" in captured.out
    
    def test_get_current_color(self, mock_widget):
        """Test getting current color."""
        manager = BackgroundColorManager(mock_widget)
        manager.current_color = "Peach"
        
        result = manager.get_current_color()
        
        assert result == "Peach"
    
    def test_get_available_colors(self, mock_widget):
        """Test getting list of available colors."""
        manager = BackgroundColorManager(mock_widget)
        
        colors = manager.get_available_colors()
        
        assert isinstance(colors, list)
        assert len(colors) == 4
        assert "Light Gray" in colors
        assert "Peach" in colors
    
    def test_change_widget_colors(self, mock_widget):
        """Test changing widget colors."""
        manager = BackgroundColorManager(mock_widget)
        
        manager.change_widget_colors("#FFFFFF")
        
        mock_widget.wisdom_label.configure.assert_called()
        mock_widget.button_frame.configure.assert_called()
        mock_widget.image_frame.configure.assert_called()
        mock_widget.wisdom_frame.configure.assert_called()
    
    def test_color_hex_values(self, mock_widget):
        """Test that color hex values are valid."""
        manager = BackgroundColorManager(mock_widget)
        
        for color_name, hex_value in manager.available_colors.items():
            assert hex_value.startswith("#")
            assert len(hex_value) == 7  # #RRGGBB
            # Check valid hex characters
            try:
                int(hex_value[1:], 16)
            except ValueError:
                pytest.fail(f"Invalid hex color: {hex_value}")
