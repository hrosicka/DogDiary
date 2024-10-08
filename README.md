# Dog Diary
Woof! This app is a paw-some way to see adorable doggos and discover fun facts about their feline friends.
Based on Cat Facts API: https://catfact.ninja/fact and on Dog API: https://dog.ceo/api/breeds/image/random

## Introduction
The "Dog Diary" application is a fun and simple app designed for dog and cat lovers. It combines adorable dog images with interesting cat facts. The app utilizes two publicly available APIs:

- dog.ceo: This API provides random images of various dog breeds.
- catfact.ninja: This API offers a database of interesting and lesser-known facts about cats.

## Functionality
- Displays random dog images: Clicking the "What am I thinking about cats?" button will display a random image of a dog.

  ![](https://github.com/hrosicka/DogDiary/blob/master/doc/DogDiary.png)

- Displays cat facts: Along with the dog image, a fun fact about cats is presented.

  ![](https://github.com/hrosicka/DogDiary/blob/master/doc/DogDiary2.png)
  
- Saves images: Users can save their favorite dog images to their local device.

  ![](https://github.com/hrosicka/DogDiary/blob/master/doc/SaveImage.png)


## Code Breakdown:

1. Imports: Necessary libraries for GUI elements, network requests, image processing, and clipboard interaction are imported.
2. DogImageApp Class:
    -  init(): Initializes the application window with title, size, and disables resizing. Creates frames and buttons with descriptive text. Assigns tooltips to buttons using the Hovertip class.
    -  show_dog_and_wisdom(): Fetches a random dog image URL and cat fact concurrently using requests. Handles potential errors gracefully and updates labels with informative messages.
    -  show_dog_image(image_url): Downloads and displays the dog image at the given URL. Implements error handling for download failures.
    -  show_wisdom(wisdom_text): Formats and displays the provided cat fact text in the wisdom label.
    -  save_image(): Saves the currently displayed dog image to a user-chosen location. Handles potential saving errors.
    -  copy_wisdom_to_clipboard(): Copies the displayed cat fact text to the system clipboard.
    -  save_wisdom(): Saves the displayed cat fact to a user-chosen text file. Handles potential file operation errors.
4. Main Loop: If the script is executed directly, it creates an instance of the DogImageApp class and starts the main application loop (mainloop).
