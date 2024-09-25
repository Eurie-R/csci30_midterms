# CSCI 30 Midterms Python Assignment

## Overview

This repository contains the Python assignment for the CSCI 30 Midterms. Please follow the instructions below to set up your development environment and get started with the assignment.

## Prerequisites

- **Python Version**: Make sure you have Python installed on your machine. The recommended version is Python 3.x.

## Setup Instructions

1. **IDE Setup**:
   - I use Visual Studio Code (VS Code) for this project. If you are using a different IDE, the setup process might vary slightly.

2. **Extensions**:
   - While the extensions listed below are not required, they are used in my setup to improve code readability:
     - [Better Comments](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments)
     - [Comment Anchors](https://marketplace.visualstudio.com/items?itemName=ExodiusStudios.comment-anchors)
   - So if you wonder why some of the comments look weird, its probably my extensions

3. **Clone the Repository**:
   - Clone this repository using the following command:
     ```powershell
     git clone <repository-url>
     ```
   
4. **Navigate to the Project Directory**:
   - Change to the project directory:
     ```powershell
     cd <\project-directory>
     ```

5. **Virtual Environment**:
   - Unfortunately, you will have to setup the Virtual Environment yourself.
   - In VS Code, you can automatically enter the virtual environment. Please refer to the clip for more details.
  ![VS Code Auto Venv Activate](venv.gif)
   - To activate the virtual environment manually, run the following command in a command prompt:
     ```bash
     .\.venv\Scripts\activate
     ```

7. **Dependancy Check**:
   - Check if everything has been properly installed:
     ```powershell
     .\project-directory> pip freeze
     ```
   
   - It should result in something like:
     ```powershell
     project-directory> pip freeze
     numpy==1.26.4      # note that the new specs mention that numpy 1.26.4 is the working version for this assignment
     pygame==2.6.0
     ```    

   - Install Missing Dependencies:
     - If it doenst match, run the following command while in while venv is enabled:
    ```powershell
    pip install -r requirements.txt
    ```

8. **Run Tests**:
   - Run ```stdaudio.py``` to check if everything was installed correctly. You should hear a sequence of notes playing.
   - Use `ringbuffer_tester.py` to run tests and ensure everything is functioning correctly.

10. **Project Structure**:
   - All files outside the `midterms` folder are used for testing purposes only. Feel free to add or remove files from this folder as needed, since these files are not required for submission.

11. **File Details**:
   - `ringbuffer.py`: This file is complete, but you can review and make edits if necessary.
   - `ringbuffer_tester.py`: Use this file to test any changes you make to `ringbuffer.py`.

## Contributing

Feel free to contribute by making changes or improvements to the code. Make sure to test your changes thoroughly.
