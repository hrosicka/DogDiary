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
        self.geometry("680x480")

        self.dog_image_label = tk.Label(self)
        self.dog_image_label.pack()

        self.wisdom_label = tk.Label(self, wraplength=400)
        self.wisdom_label.pack()

        self.show_button = tk.Button(self, text="What am I thinking about cats?", command=self.show_dog_and_wisdom)
        self.show_button.pack()

    def show_dog_image(self):
        """
        Fetches a random dog image from the "https://dog.ceo/api/breeds/image/random" API,
        displays it in the `dog_image_label`, and handles potential errors.

        - Makes a GET request to the dog image API.
        - Parses the JSON response to extract the image URL.
        - Sends a GET request to download the image data in stream mode.
        - Checks the response status code.
        - If successful (status code 200):
            - Opens the image using Pillow's `Image.open` method.
            - Resizes the image to 400x300 pixels to fit the label better.
            - Converts the image to a format compatible with Tkinter's `ImageTk` class.
            - Updates the `dog_image_label` with the new image.
        - If unsuccessful:
            - Displays an error message in the `dog_image_label`.
        """
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        data = response.json()

        image_url = data["message"]
        image_response = requests.get(image_url, stream=True)

        if image_response.status_code == 200:
            image = Image.open(image_response.raw)
            image = image.resize((400, 300))
            image_tk = ImageTk.PhotoImage(image)

            self.dog_image_label.configure(image=image_tk)
            self.dog_image_label.image = image_tk
        else:
            self.dog_image_label.configure(text="Error downloading image")

    def show_wisdom(self):
        """
        Fetches a random cat fact from the "https://catfact.ninja/fact" API,
        formats the text for better display in the `wisdom_label`, and updates the label.

        - Makes a GET request to the cat fact API to retrieve a JSON response containing a random cat fact.
        - Parses the JSON response to extract the "fact" field, which holds the actual cat fact text.
        - Initializes an empty list `lines` to store the formatted text with line breaks.
        - Sets a `max_length` variable to define the maximum characters allowed per line for better display.
        - Iterates through each word in the `wisdom_text` split by whitespace:
            - If `lines` is not empty (meaning there's already existing formatted text):
                - Checks if the combined length of the current line (including spaces) and the new word exceeds the `max_length`.
                    - If it does, append an empty string to `lines` to start a new line.
            - Otherwise, append an empty string to `lines` to initiate the first line.
            - In both cases, append the current word with a space to the last element in `lines`.
        - Joins the formatted lines in `lines` with newline characters (`\n`) and updates the `wisdom_label` with the final text.
        """
        response = requests.get("https://catfact.ninja/fact")
        data = response.json()

        wisdom_text = data["fact"]
        lines = []
        max_length = 68

        for word in wisdom_text.split():
            if lines:
                if len(" ".join(lines[-1:])) + len(word) > max_length:
                    lines.append("")
            else:
                lines.append("")
            lines[-1] += " " + word

        self.wisdom_label.config(text="\n".join(lines))

    def show_dog_and_wisdom(self):
        """
        Calls the `show_dog_image` and `show_wisdom` methods sequentially to display a random dog image and a random cat fact.
        """
        self.show_dog_image()
        self.show_wisdom()


if __name__ == "__main__":
    app = DogImageApp()
    app.mainloop()