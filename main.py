from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

import tkinter as tk
import requests
from PIL import Image, ImageTk


class DogImageApp(tk.Tk):
    """
    This class represents the main application window for the Dog Image app.
    It creates the GUI elements, handles user interaction, and displays random dog
    images and cat facts.
    """

    def __init__(self):
        """
        Initializes the application window with its title, geometry, and widgets.

        - Sets the window title to "Dog Diary".
        - Disables resizing behavior for a fixed window size.
        - Sets the window size to 680x480 pixels.
        - Creates a label to display the dog image.
        - Creates a label to display the cat fact with automatic line wrapping.
        - Creates a button labeled "What am I thinking about cats?" that triggers
          the `show_dog_and_wisdom` method when clicked.
        """
        super().__init__()

        self.title("Dog Diary")
        self.resizable(False, False) 
        self.geometry("480x480")

        self.show_button = tk.Button(self, text="What am I thinking about cats?", command=self.show_dog_and_wisdom)
        self.show_button.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

        self.dog_image_label = tk.Label(self)
        self.dog_image_label.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

        self.wisdom_label = tk.Label(self, wraplength=400)
        self.wisdom_label.grid(row=2, column=1, columnspan=3, padx=10, pady=10)

    def show_dog_and_wisdom(self):
        """
        Fetches a random dog image and cat fact concurrently and displays them.
        Handles potential errors from both API requests.
        """
        try:
            dog_response = requests.get("https://dog.ceo/api/breeds/image/random")
            dog_data = dog_response.json()
            image_url = dog_data["message"]

            cat_response = requests.get("https://catfact.ninja/fact")
            cat_data = cat_response.json()
            wisdom_text = cat_data["fact"]

            self.show_dog_image(image_url)
            self.show_wisdom(wisdom_text)

        except Exception as e:
            print(f"An error occurred: {e}")
            self.dog_image_label.configure(text="Error fetching data")
            self.wisdom_label.configure(text="Failed to retrieve cat fact")

    def show_dog_image(self, image_url):
        """
        Downloads and displays the dog image at the given URL.
        Resizes the image and handles potential download errors during image processing.

        Args:
            image_url (str): The URL of the dog image to download.
        """
        image_response = requests.get(image_url, stream=True)

        if image_response.status_code == 200:
            try:
                image = Image.open(image_response.raw)
                image = image.resize((400, 300))
                image_tk = ImageTk.PhotoImage(image)

                self.dog_image_label.configure(image=image_tk)
                self.dog_image_label.image = image_tk
            except Exception as e:
                print(f"Error processing image: {e}")
                self.dog_image_label.configure(text="Error displaying image")  # Set error message for label

        else:
            print(f"Error downloading image: {image_response.status_code}")
            self.image_label.configure(text="Error downloading image")  # Set error message for label

    def show_wisdom(self, wisdom_text):
        """
        Fetches a random cat fact from the "https://catfact.ninja/fact" API,
        formats the text for better display in the `wisdom_label`, and updates the label.

        Args:
            wisdom_text (str): The raw cat fact retrieved from the API.
        """

        # No need to repeat the API call here, 
        # assume `wisdom_text` already contains the fact.

        lines = []  # List to store formatted lines with line breaks
        max_length = 68  # Maximum characters per line for better display

        for word in wisdom_text.split():
            # If lines is not empty (there's existing formatted text)
            if lines:
                # Check if the current line + new word exceeds max_length
                if len(" ".join(lines[-1:])) + len(word) > max_length:
                    lines.append("")  # Start a new line
            else:
                lines.append("")  # Initiate the first line

            # Append current word with a space to the last line in 'lines'
            lines[-1] += " " + word

        # Join formatted lines with newline characters and update the label
        self.wisdom_label.config(text="\n".join(lines))

# Run the main application loop if this script is executed directly
if __name__ == "__main__":
    app = DogImageApp()
    app.mainloop()