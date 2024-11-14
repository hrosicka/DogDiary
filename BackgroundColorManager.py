class BackgroundColorManager:
    """
    Manages the background color of a given widget and its child widgets.

    Args:
        widget: The main widget whose background color will be managed.

    Attributes:
        widget: The main widget.
        available_colors: A dictionary of available color names and their corresponding hex codes.
        current_color: The currently set background color.
    """
    def __init__(self, widget):
        self.widget = widget
        # Define a dictionary to store background colors with descriptive names
        self.available_colors = {
            "Light Gray": "#F2F2F2",
            "Light Ivory": "#FFFAFA",
            "Sky Blue": "#F0FFFF",
            "Peach": "#FFE4B5"
        }
        self.current_color = "Light Gray"  # Default color

    def set_color(self, color):
        """
        Sets the background color of the widget and its child widgets.

        Args:
            color: The desired color name.
        """
        if color in self.available_colors:
            self.widget.configure(bg=self.available_colors[color])
            self.current_color = color
            self.change_widget_colors(self.available_colors[color])
        else:
            print(f"Invalid Color: {color}")

    def change_widget_colors(self, color):
        """
        Changes the background color of specific child widgets.

        Args:
            color: The desired color.
        """
        self.widget.wisdom_label.configure(bg_color=color)
        self.widget.button_frame.configure(bg=color)
        self.widget.image_frame.configure(bg=color)
        self.widget.wisdom_frame.configure(bg=color)

    def get_current_color(self):
        """
        Returns the currently set background color.

        Returns:
            The current background color.
        """
        return self.current_color

    def get_available_colors(self):
        """
        Returns a list of available color names.

        Returns:
            A list of color names.
        """
        return list(self.available_colors.keys())