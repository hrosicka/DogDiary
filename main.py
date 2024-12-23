from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

import tkinter as tk
import customtkinter
from CTkMessagebox import CTkMessagebox
import requests
from PIL import Image, ImageTk
import os  # Import the 'os' module for file path manipulation
import pyperclip
import clipboard
import io
import base64
import win32clipboard
import win32con
from idlelib.tooltip import Hovertip
from BackgroundColorManager import BackgroundColorManager
from tkinter.messagebox import showinfo, showerror
from io import BytesIO

class DogImageApp(tk.Tk):
    """
    This class represents the main application window for the Dog Image App.
    It handles the graphical user interface (GUI), user interaction,
    and displays random dog images alongside corresponding cat facts.
    """

    def __init__(self):
        """
        Initializes the application window with its title, geometry, and widgets.

        - Sets the window title to "Dog Diary".
        - Disables resizing behavior for a fixed window size.
        - Sets the window size to 600x600 pixels.
        - Creates frames to organize the layout of UI elements.
        - Creates buttons for user interaction with descriptive text.
        - Creates labels to display dog images and cat facts.
        - Assigns tooltips to buttons using the Hovertip class.
        """
        super().__init__()

        self.current_image = None  # Stores the currently displayed image
        background_manager = BackgroundColorManager(self)

        self.title("Dog Diary")
        self.resizable(False, False) 
        self.geometry("600x700")

        dirname = os.path.dirname(__file__)
        #self.icon_path = os.path.join(dirname, 'IconUser.ico')  # Replace with your icon file path
        #self.iconbitmap(self.icon_path)  # Set the window icon
        self.warning_ico_path = os.path.join(dirname, 'warning.png') 

        self.button_frame = tk.Frame(self)
        self.image_frame = tk.Frame(self)
        self.wisdom_frame = tk.Frame(self)

        # "What am I thinking about cats?" button with tooltip
        self.button = customtkinter.CTkButton(master=self.button_frame,
                                text="What am I thinking about cats?",
                                command=self.show_dog_and_wisdom,
                                width=300,
                                text_color="white",
                                fg_color="#2D1E2F",
                                hover_color="#F15946")
        self.button.grid(row=1, column=1, columnspan=3, padx=2, pady=5)
        
        self.button_tooltip = (
            "Unleash the secrets of the feline mind...\n"
            "through a dog image and a cat fact!\n"
            "Generate a new dog image and cat fact.")
        Hovertip(self.button, self.button_tooltip)

        # Additional buttons with tooltips
        self.new_idea_button = customtkinter.CTkButton(master=self.button_frame,
                                                   text="I'll Think Again",
                                                   command=self.show_new_idea,
                                                   width=150,
                                                   text_color="white",
                                                   fg_color="#2D1E2F",
                                                   hover_color="#F15946")
        self.new_idea_button.grid(row=2, column=1, columnspan=1, padx=2, pady=5)

        # Additional buttons with tooltips
        self.copy_image_button = customtkinter.CTkButton(master=self.button_frame,
                                                   text="Copy Image",
                                                   command=self.copy_image_to_clipboard,
                                                   width=150,
                                                   text_color="white",
                                                   fg_color="#2D1E2F",
                                                   hover_color="#F15946")
        self.copy_image_button.grid(row=2, column=2, columnspan=1, padx=2, pady=5)
        

        self.new_doggo_button = customtkinter.CTkButton(master=self.button_frame,
                                       text="Not My Idea",
                                       command=self.show_new_doggo,
                                       width=150,
                                       text_color="white",
                                       fg_color="#2D1E2F",
                                       hover_color="#F15946")
        self.new_doggo_button.grid(row=2, column=3, columnspan=1, padx=2, pady=5)

        # Additional buttons with tooltips
        self.save_button = customtkinter.CTkButton(master=self.button_frame,
                                                   text="Save Image",
                                                   command=self.save_image,
                                                   width=150,
                                                   text_color="white",
                                                   fg_color="#2D1E2F",
                                                   hover_color="#F15946")
        self.save_button.grid(row=3, column=1, columnspan=1, padx=2, pady=5)

        self.save_button_tooltip = (
            "Because who doesn't need more adorable doggo in their life?\n"
            "Save the current image to a file.")
        Hovertip(self.save_button, self.save_button_tooltip)

        self.copy_button = customtkinter.CTkButton(
            master=self.button_frame,
            text="Copy Wisdom",
            command=self.copy_wisdom_to_clipboard,
            width=150,
            text_color="white",
            fg_color="#2D1E2F",
            hover_color="#F15946",
        )
        self.copy_button.grid(row=3, column=2, columnspan=1, padx=2, pady=5)

        self.copy_button_tooltip = (
            "Don't let these wise words go to the dogs!\n"
            "Save the cat fact to your clipboard.")
        Hovertip(self.copy_button, self.copy_button_tooltip)

        self.save_wisdom_button = customtkinter.CTkButton(
            master=self.button_frame,
            text="Save Wisdom",
            command=self.save_wisdom,
            width=150,
            text_color="white",
            fg_color="#2D1E2F",
            hover_color="#F15946",
        )
        self.save_wisdom_button.grid(row=3, column=3, columnspan=1, padx=2, pady=5)

        self.save_wisdom_button_tooltip = (
            "Don't let these wise words go to the dogs!\n"
            "Save the cat fact to a text file.")
        Hovertip(self.save_wisdom_button, self.save_wisdom_button_tooltip)


        self.color_label = customtkinter.CTkLabel(master=self.button_frame,
                                                   text="Background Color",
                                                   width=150,
                                                   text_color="#2D1E2F")
        self.color_label.grid(row=4, column=1, columnspan=1, padx=2, pady=5)

        # Create a dropdown menu for background colors
        self.color_menu = customtkinter.CTkComboBox(
            master=self.button_frame,
            values=list(background_manager.available_colors),
            command=lambda color: background_manager.set_color(color),
            text_color="white",
            fg_color="#2D1E2F",
            dropdown_hover_color="#F15946",
            button_hover_color="#F15946",
            dropdown_fg_color="#2D1E2F",
            dropdown_text_color="white",
        )
        self.color_menu.grid(row=4, column=2, columnspan=1, padx=2, pady=5)

        
        self.dog_image_label = customtkinter.CTkLabel(self.image_frame, text='')
        self.dog_image_label.grid(row=1, column=1, columnspan=3, padx=30, pady=10)


        self.wisdom_label = customtkinter.CTkLabel(self.wisdom_frame, wraplength=400, text='')
        self.wisdom_label.grid(row=2, column=1, columnspan=3, padx=30, pady=10)


        self.button_frame.pack(side=tk.TOP, padx=10, pady=10)
        self.image_frame.pack(side=tk.TOP, padx=10, pady=10)
        self.wisdom_frame.pack(side=tk.TOP, padx=10, pady=10)

    def show_new_idea(self):

        if not self.current_image:
            CTkMessagebox(title="Error",
                          message="Thinking about cats again? Perhaps a new doggo will inspire you! Press the button 'What am I thinking about cats?' first!",
                          icon=self.warning_ico_path,
                          icon_size=(100,100),
                          fg_color="#F2F2F2",
                          bg_color="light grey",
                          button_text_color="white",
                          button_width=80,
                          button_color="#2D1E2F",
                          button_hover_color="#F15946")
            return
        
        try:
            cat_response = requests.get("https://catfact.ninja/fact")
            cat_data = cat_response.json()
            wisdom_text = cat_data["fact"]

            self.show_wisdom(wisdom_text)

        except Exception as e:
            print(f"An error occurred: {e}")
            self.wisdom_label.configure(text="Failed to retrieve cat fact")


    def show_new_doggo(self):
        """
        Fetches a new random dog image and updates the display.

        This method:
        1. Fetches a new dog image URL from the dog.ceo API.
        2. Updates the displayed image by calling self.show_dog_image() 
        with the new URL.
        """
        wisdom_text = self.wisdom_label.cget("text")

        if wisdom_text == "":
            CTkMessagebox(title="Error",
                          message="Press the button 'What am I thinking about cats?' first!",
                          icon=self.warning_ico_path,
                          icon_size=(100,100),
                          fg_color="#F2F2F2",
                          bg_color="light grey",
                          button_text_color="white",
                          button_width=80,
                          button_color="#2D1E2F",
                          button_hover_color="#F15946")
            return
        
        try:
            dog_response = requests.get("https://dog.ceo/api/breeds/image/random")
            dog_data = dog_response.json()
            image_url = dog_data["message"]
            self.show_dog_image(image_url)
        except Exception as e:
            print(f"Error fetching new dog image: {e}")
            self.dog_image_label.configure(text="Error fetching new dog image")



    def show_dog_and_wisdom(self):
        """
        Fetches a random dog image and cat fact concurrently and displays them.
        Handles potential errors gracefully to provide informative messages to the user.

        This method performs the following steps:

        1. Initiates concurrent API requests:
            - Fetches a random dog image URL from the "dog.ceo" API.
            - Fetches a random cat fact from the "catfact.ninja" API.
        2. Parses the JSON responses from both APIs for data extraction.
        3. Extracts the dog image URL and cat fact text from the respective responses.
        4. Calls helper methods to display the retrieved dog image and cat fact.
            - `self.show_dog_image(image_url)`: Displays the downloaded dog image.
            - `self.show_wisdom(wisdom_text)`: Displays the retrieved cat fact.
        5. Implements error handling with a try-except block:
            - Catches any exceptions (e.g., network issues, API errors).
            - Logs the error message for debugging purposes.
            - Updates the dog image and wisdom labels with informative error messages.
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

        This method performs the following steps:

        1. Downloads the dog image from the provided URL using `requests.get(image_url, stream=True)`.
        2. Checks the HTTP status code of the response:
            - If successful (status code 200):
                - Opens the downloaded image data using `Image.open(image_response.raw)`.
                - Stores the processed image in the `self.current_image` attribute for potential future use.
                - Calculates the new dimensions to maintain the image's aspect ratio while fitting within the label frame.
                - Resizes the image using `image.resize((new_width, new_height))`.
                - Converts the PIL image to a format compatible with the CTkImage widget.
                - Updates the `dog_image_label` with the resized and converted image.
            - If download fails (non-200 status code):
                - Logs the error message for debugging purposes.
                - Updates the `dog_image_label` with an informative error message.

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
        Formats and displays the provided cat fact text in the `wisdom_label`.

        This method performs the following steps:

        1. Assumes `wisdom_text` already contains the retrieved cat fact.
        2. Initializes an empty list `lines` to store formatted text with line breaks.
        3. Defines `max_length` to control the maximum characters per line for better readability.
        4. Iterates through each word in the `wisdom_text`:
            - If `lines` is not empty (meaning there's existing formatted text):
                - Checks if adding the current word to the last line would exceed `max_length`.
                    - If exceeded, starts a new line by appending an empty string to `lines`.
            - Appends the current word with a space to the last line in `lines`.
        5. Joins the formatted lines with newline characters (`\n`) for proper multi-line display.
        6. Updates the `wisdom_label` with the formatted text.

        Args:
            wisdom_text (str): The raw cat fact text to be formatted and displayed.
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
        Saves the currently displayed dog image to the user's chosen location.

        This method performs the following steps:

        1. Checks if there's an image loaded (`self.current_image` is not None).
            - If no image is loaded, displays a warning message using `CTkMessagebox`.
            - If an image is loaded, proceeds with saving.
        2. Prompts the user to choose a file path and filename using `tk.filedialog.asksaveasfilename`.
            - Sets the default extension to ".png" and filters for PNG images.
        3. If the user selects a file path:
            - Attempts to save the loaded image (`self.current_image`) using the PIL library's `save` method.
                - On successful save, displays a success message using `CTkMessagebox`.
            - Catches potential exceptions during saving:
                - Logs the error message for debugging purposes (using `str(e)`).
                - Displays an error message to the user using `CTkMessagebox`.
        """

        if not self.current_image:
            CTkMessagebox(title="Error",
                          message="No image to save.",
                          icon=self.warning_ico_path,
                          icon_size=(100,100),
                          fg_color="#F2F2F2",
                          bg_color="light grey",
                          button_text_color="white",
                          button_width=80,
                          button_color="#2D1E2F",
                          button_hover_color="#F15946")
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
        """
        Copies the currently displayed wisdom text to the system clipboard.

        This method performs the following steps:

        1. Retrieves the text content from the `wisdom_label` using `cget("text")`.
        2. Checks if there's any text to copy:
            - If the `wisdom_text` is empty, displays a warning message using `CTkMessagebox`.
        3. If there's text to copy:
            - Copies the `wisdom_text` to the system clipboard using the `pyperclip.copy` function.
            - Displays a success message to inform the user using `CTkMessagebox`.
        """
        wisdom_text = self.wisdom_label.cget("text")

        if wisdom_text == "":
            CTkMessagebox(title="Error",
                          message="No wisdom text to copy.",
                          icon=self.warning_ico_path,
                          icon_size=(100,100),
                          fg_color="#F2F2F2",
                          bg_color="light grey",
                          button_text_color="white",
                          button_width=80,
                          button_color="#2D1E2F",
                          button_hover_color="#F15946")
            return
        
        pyperclip.copy(wisdom_text)
        CTkMessagebox(title="Success", message="Text has been copied to the clipboard.")

    def copy_image_to_clipboard(self):
        """Copies the current image to the clipboard in JPG format using win32clipboard.

        Args:
            self: An instance of the class containing the attribute self.current_image with the image.
        """

        if not self.current_image:
            CTkMessagebox(title="Error",
                          message="No image to copy.",
                          icon=self.warning_ico_path,
                          icon_size=(100,100),
                          fg_color="#F2F2F2",
                          bg_color="light grey",
                          button_text_color="white",
                          button_width=80,
                          button_color="#2D1E2F",
                          button_hover_color="#F15946")
            return

        # Uložení obrázku do paměti jako JPG
        with io.BytesIO() as output:
            self.current_image.save(output, format="BMP")
            data = output.getvalue()

        output = BytesIO()
        self.current_image.convert('RGB').save(output, 'BMP')
        data = output.getvalue()[14:]
        output.close()

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()


    def save_wisdom(self):
        """
        Saves the currently displayed wisdom text to a text file.

        This method performs the following steps:

        1. Retrieves the text content from the `wisdom_label` using `cget("text")`.
        2. Checks if there's any text to save:
            - If the `wisdom_text` is empty, displays a warning message using `CTkMessagebox`.
        3. If there's text to save:
            - Prompts the user to choose a file path and filename using `tk.filedialog.asksaveasfilename`.
                - Sets the default extension to ".txt" and filters for text files.
        4. If the user selects a file path:
            - Opens the file in write mode (`"w"`) for writing.
            - Writes the `wisdom_text` to the file.
            - Closes the file.
            - Displays a success message to inform the user using `CTkMessagebox`.
        5. Catches potential exceptions during file operations:
            - Logs the error message for debugging purposes (using `str(e)`).
            - Displays an error message to the user using `CTkMessagebox`.
        """

        wisdom_text = self.wisdom_label.cget("text")

        if wisdom_text == "":
            CTkMessagebox(title="Error",
                          message="No wisdom text to save.",
                          icon=self.warning_ico_path,
                          icon_size=(100,100),
                          fg_color="#F2F2F2",
                          bg_color="light grey",
                          button_text_color="white",
                          button_width=80,
                          button_color="#2D1E2F",
                          button_hover_color="#F15946")
            return

        # Get the file path where the text will be saved (using a file dialog)
        file_path = tk.filedialog.asksaveasfilename(
            defaultextension=".txt", filetypes=[("Text file", "*.txt")]
        )

        if file_path:
            try:
                # Open the file in write mode and write the wisdom text
                with open(file_path, "w") as f:
                    f.write(wisdom_text)

                CTkMessagebox(title="Success", message="Wisdom saved successfully.")
            except Exception as e:
                CTkMessagebox(title="Error",
                              message=f"An error occurred while saving: {str(e)}",
                              icon=self.warning_ico_path,
                              icon_size=(100,100),
                              fg_color="#F2F2F2",
                              bg_color="light grey",
                              button_text_color="white",
                              button_width=80,
                              button_color="#2D1E2F",
                              button_hover_color="#F15946")

       

# Run the main application loop if this script is executed directly
if __name__ == "__main__":
    app = DogImageApp()
    app.mainloop()