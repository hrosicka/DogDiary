# Dog Diary

<div align="center">

  <a href="https://github.com/hrosicka/DogDiary/actions/workflows/tests.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/hrosicka/DogDiary/tests.yml?style=for-the-badge&color=4F8EF7&label=Tests&logo=githubactions&logoColor=white" alt="Tests" />
  </a>
  <a href="https://github.com/hrosicka/DogDiary/stargazers">
    <img src="https://img.shields.io/github/stars/hrosicka/DogDiary?style=for-the-badge&color=4F8EF7&logo=starship&logoColor=white" alt="Stars" />
  </a>
  <a href="https://github.com/hrosicka/DogDiary/network/members">
    <img src="https://img.shields.io/github/forks/hrosicka/DogDiary?style=for-the-badge&color=4F8EF7&logo=git&logoColor=white" alt="Forks" />
  </a>
  <a href="https://github.com/hrosicka/DogDiary/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/hrosicka/DogDiary?style=for-the-badge&color=4F8EF7&logo=github&logoColor=white" alt="Contributors" />
  </a>
  <a href="https://github.com/hrosicka/DogDiary/commits/master">
    <img src="https://img.shields.io/github/last-commit/hrosicka/DogDiary?style=for-the-badge&color=6366F1&logo=githubactions&logoColor=white" alt="Last Commit" />
  </a>
  <a href="https://github.com/hrosicka/DogDiary/issues">
    <img src="https://img.shields.io/github/issues/hrosicka/DogDiary?style=for-the-badge&color=F59E0B&logo=github&logoColor=white" alt="Issues" />
  </a>
  <br/>

  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=FFE873" alt="Python" />
  </a>
  <img src="https://img.shields.io/badge/Made%20With-Tkinter-0EA5E9?style=for-the-badge&logo=python&logoColor=white" alt="Made with Tkinter" />
  <a href="https://dog.ceo/">
    <img src="https://img.shields.io/badge/API-dog.ceo-F97316?style=for-the-badge&logo=fastapi&logoColor=white" alt="Random Dog API" />
  </a>
  <a href="https://catfact.ninja/">
    <img src="https://img.shields.io/badge/API-catfact.ninja-8B5CF6?style=for-the-badge&logo=fastapi&logoColor=white" alt="Catfact Ninja" />
  </a>
  <img src="https://img.shields.io/github/repo-size/hrosicka/DogDiary?style=for-the-badge&color=3B82F6&logo=files&logoColor=white" alt="Repo Size" />
  <br/>

  <img src="https://img.shields.io/badge/%F0%9F%90%BE-Paw--some%20Project-F97316?style=for-the-badge" alt="Paw-some Project" />
  <img src="https://img.shields.io/badge/Dog-Approved-22C55E?style=for-the-badge&logo=sparkles&logoColor=white" alt="Dog Approved" />
  <img src="https://img.shields.io/badge/Cat%20Facts-100%25-8B5CF6?style=for-the-badge&logo=sparkles&logoColor=white" alt="Cat Facts Inside" />
  <a href="https://github.com/hrosicka/DogDiary/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-10B981?style=for-the-badge&logo=opensourceinitiative&logoColor=white" alt="License: MIT" />
  </a>

</div>


Woof! This app 🐶🐾🐶 is a paw-some way to see adorable doggos and discover fun facts about their feline friends.
Based on Cat Facts API: https://catfact.ninja/fact and on Dog API: https://dog.ceo/api/breeds/image/random

## Introduction
The "Dog Diary"  application is a fun and simple app designed for dog and cat lovers 💕💘. It combines adorable dog images with interesting cat facts. The app utilizes two publicly available APIs:

- dog.ceo: This API provides random images of various dog breeds.
- catfact.ninja: This API offers a database of interesting and lesser-known facts about cats.

## Who is this for?
- Animal lovers: If you can't get enough of dogs and cats, this app is for you.
- Mood boosters: Need a quick pick-me-up? Our app is guaranteed to put a smile on your face.
- Anyone who loves fun: If you're looking for a fun and easy way to pass the time, look no further!

## Functionality
- Displays random dog images: Clicking the "What am I thinking about cats?" button will display a random image of a dog.

  ![](https://github.com/hrosicka/DogDiary/blob/master/doc/DogDiary.png)

- Displays cat facts: Along with the dog image, a fun fact about cats is presented.

  ![](https://github.com/hrosicka/DogDiary/blob/master/doc/DogDiary2.png)
  
- Saves images: Users can save their favorite dog images to their local device.

  ![](https://github.com/hrosicka/DogDiary/blob/master/doc/SaveImage.png)



## How to Change the Background Color

- Locate the "Background Color" label and the adjacent dropdown menu in the button section of the application.
- Click on the dropdown menu to reveal the list of available colors.
- Select your desired color from the list. The application's background will immediately update to reflect your choice.

   ![](https://github.com/hrosicka/DogDiary/blob/master/doc/ChangeBackgroundColor.png)


## Handling Empty Content for Buttons

The application handles situations where the user clicks buttons for working with images or text before any content (dog image or cat fact) has been loaded. In these cases, an information message box is displayed with a warning. Specifically:

- **"I'll Think Again"** - If the user clicks this button before the first cat fact is displayed (i.e., when wisdom_label is empty), a message box appears saying, "Thinking about cats again? Perhaps a new doggo will inspire you! Press the button 'What am I thinking about cats?' first!"

  ![](https://github.com/hrosicka/DogDiary/blob/master/doc/ThinkAgainMessageBox.png)
  
- **"Not My Idea" Button** - If the user clicks this button before the first cat fact is displayed (i.e., when wisdom_label is empty), a message box appears saying, "Press the button 'What am I thinking about cats?' first!"

  ![](https://github.com/hrosicka/DogDiary/blob/master/doc/NotMyIdeaMessageBox.png)


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

## Author
Lovingly crafted by [Hanka Robovska](https://github.com/hrosicka)

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details. Free to use, modify, and distribute as needed.
