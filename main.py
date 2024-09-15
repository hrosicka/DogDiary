from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

import tkinter as tk
import customtkinter
from CTkMessagebox import CTkMessagebox
import requests
from PIL import Image, ImageTk
import os  # Import the 'os' module for file path manipulation
import pyperclip


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

        self.current_image = None  # Define current_image as a class variable

        self.title("Dog Diary")
        self.resizable(False, False) 
        self.geometry("580x580")

        self.button_frame = tk.Frame(self)
        self.image_frame = tk.Frame(self)
        self.wisdom_frame = tk.Frame(self)

        self.button = customtkinter.CTkButton(master=self.button_frame,
                                text="What am I thinking about cats?",
                                command=self.show_dog_and_wisdom,
                                width=300,
                                text_color="white",
                                fg_color="#2D1E2F",
                                hover_color="#F15946")
        self.button.grid(row=1, column=1, columnspan=2, padx=10, pady=5)

        self.save_button = customtkinter.CTkButton(master=self.button_frame,
                                                   text="Save Image",
                                                   command=self.save_image,
                                                   width=150,
                                                   text_color="white",
                                                   fg_color="#2D1E2F",
                                                   hover_color="#F15946")
        self.save_button.grid(row=2, column=1, columnspan=2, padx=10, pady=5)

        self.copy_button = customtkinter.CTkButton(
            master=self.button_frame,
            text="Copy Wisdom",
            command=self.copy_wisdom_to_clipboard,
            width=150,
            text_color="white",
            fg_color="#2D1E2F",
            hover_color="#F15946",
        )
        self.copy_button.grid(row=3, column=1, columnspan=2, padx=10, pady=5)

        
        self.dog_image_label = customtkinter.CTkLabel(self.image_frame, text='')
        self.dog_image_label.grid(row=1, column=1, columnspan=3, padx=30, pady=10)


        self.wisdom_label = customtkinter.CTkLabel(self.wisdom_frame, wraplength=400, text='')
        self.wisdom_label.grid(row=2, column=1, columnspan=3, padx=30, pady=10)


        self.button_frame.pack(side=tk.TOP, padx=10, pady=10)
        self.image_frame.pack(side=tk.TOP, padx=10, pady=10)
        self.wisdom_frame.pack(side=tk.TOP, padx=10, pady=10)

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
        Resizes the image while maintaining its aspect ratio and handles potential download errors during image processing.

        Args:
            image_url (str): The URL of the dog image to download.
        """
        image_response = requests.get(image_url, stream=True)

        if image_response.status_code == 200:
            try:
                image = Image.open(image_response.raw)
                self.current_image = image  # Assign the processed image to current_image

                # Calculate the new dimensions to maintain aspect ratio
                label_width, label_height = 300, 200  # Target dimensions for the label

                image_width, image_height = image.size

                # Determine the scaling factor based on the limiting dimension
                scale_factor = min(label_width / image_width, label_height / image_height)

                # Resize the image while maintaining aspect ratio
                new_width = int(image_width * scale_factor)
                new_height = int(image_height * scale_factor)
                image = image.resize((new_width, new_height))

                image_tk = customtkinter.CTkImage(light_image=image, size=(new_width , new_height))
                self.dog_image_label.configure(image=image_tk)
                self.dog_image_label.image = image_tk

            except Exception as e:
                print(f"Error processing image: {e}")
                self.dog_image_label.configure(text="Error displaying image")
        else:
            print(f"Error downloading image: {image_response.status_code}")
            self.dog_image_label.configure(text="Error downloading image")

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
        self.wisdom_label.configure(text="\n".join(lines))

    def save_image(self):
        """
        Saves the currently displayed dog image to the disk.

        If no image is currently loaded, a warning message is displayed.
        """

        if not self.current_image:
            CTkMessagebox(title="Error", message="No image to save.")
            return

        # Get the file path where the image will be saved (using a file dialog)
        file_path = tk.filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG image", "*.png")])

        if file_path:
            try:
                # Save the image using the PIL library
                self.current_image.save(file_path)
                CTkMessagebox(title="Success", message="Image saved successfully.")
            except Exception as e:
                CTkMessagebox(title="Error", message=f"An error occurred while saving the image: {str(e)}")

    def copy_wisdom_to_clipboard(self):
        """Copies the current wisdom text to the clipboard."""
        wisdom_text = self.wisdom_label.cget("text")

        if wisdom_text == "":
            CTkMessagebox(title="Error", message="No text to copy.")
            return
        
        pyperclip.copy(wisdom_text)
        CTkMessagebox(title="Success", message="Text has been copied to the clipboard.")

       

# Run the main application loop if this script is executed directly
if __name__ == "__main__":
    app = DogImageApp()
    app.mainloop()