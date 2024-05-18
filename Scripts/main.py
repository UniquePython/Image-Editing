# Import necessary modules
from tkinter import filedialog as fd
from PIL import Image
from os import path, name, startfile, system
from sys import platform
from colorama import init, Fore, Style
from filters import *
from choices import *

def select_image():
    """
    Prompt the user to select an image file.

    Returns:
    str: The file path of the selected image.
    """
    # Prompt user to select an image file
    print(Fore.YELLOW + "Please select the image you want to process." + Style.RESET_ALL)
    print()
    file_path = fd.askopenfilename(title="Select image")

    return file_path

def process_image(img_path):
    """
    Process the selected image based on the chosen filter.

    Parameters:
    img_path (str): The file path of the selected image.
    """
    if img_path:
        # Open the selected image file
        img = Image.open(img_path)
        img_name = path.basename(img_path) 
        img_base_name = path.splitext(img_name)[0]  # to handle file extensions properly

        # Display information about the selected image
        print(Fore.GREEN + "You have selected the file:", img_name + Style.RESET_ALL)
        print(Fore.CYAN + "File path:", img_path + Style.RESET_ALL)
        print()

        # Prompt user to enter the output directory path
        print(Fore.YELLOW + "Please select the output path: " + Style.RESET_ALL)

        output_path = fd.askdirectory(title="Select Output folder")

        print(Fore.GREEN + "You have selected the folder:", output_path + Style.RESET_ALL)
        print()

        # Create the output directory if it doesn't exist
        if not path.exists(output_path):
            raise FileNotFoundError(Fore.RED + "Path does not exist. Please try again." + Style.RESET_ALL)

        # Display available filter choices
        choices()
        
        try:
            # Prompt user to enter their choice of filter
            user_choice = int(input(Fore.YELLOW + "Enter your choice: " + Style.RESET_ALL))

            if user_choice in range(1, 11):
                # Apply the selected filter to the image
                apply_filter(img, img_base_name, output_path, user_choice)

                # Open the image
                open_image(output_path)
            else:
                # Handle invalid input for filter choice
                print(Fore.RED + "Invalid Input. Please enter a number between 1 and 10." + Style.RESET_ALL)
        except ValueError:
            # Handle invalid input type
            print(Fore.RED + "Invalid Input. Please enter a valid number." + Style.RESET_ALL)
    else:
        # Handle case when no file is selected
        print(Fore.RED + "No file selected. Exiting the program." + Style.RESET_ALL)

def apply_filter(img, img_base_name, output_path, user_choice):
    """
    Apply the selected filter to the image.

    Parameters:
    img (PIL.Image): The input image to be processed.
    img_base_name (str): The base name of the input image file.
    output_path (str): The directory where the processed image will be saved.
    user_choice (int): The user's choice of filter.
    """
    # Apply the selected filter to the image
    filter_functions = [blur, contour, detail, edge, xedge, emboss, fedge, sharp, smooth, xsmooth]
    selected_filter = filter_functions[user_choice - 1]
    selected_filter(img, img_base_name, output_path)  
    print(Fore.GREEN + "Processing Complete!" + Style.RESET_ALL)

def open_image(file_path):
    """
    Open the specified image file using the default image viewer.

    Parameters:
    file_path (str): The file path of the image to be opened.
    """
    if name == 'nt':  # For Windows
        startfile(file_path)
    elif name == 'posix':  # For macOS and Linux
        opener = 'open' if platform == 'darwin' else 'xdg-open'
        system(f"{opener} {file_path}")


if __name__ == '__main__':
    # Call functions to select and process the image
    init(autoreset=True)
    img_path = select_image()
    process_image(img_path)
