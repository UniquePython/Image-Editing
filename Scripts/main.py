# Import necessary modules
from tkinter import filedialog as fd
from PIL import Image
from os import path, name, startfile, system
from sys import platform
from colorama import init, Fore, Style
from filters import *
from choices import *
import time
import os  # Importing os module to get file size

def select_image():
    """
    Prompt the user to select an image file.

    Returns:
    str: The file path of the selected image.
    """
    try:
        # Prompt user to select an image file
        print(Fore.YELLOW + "Please select the image you want to process." + Style.RESET_ALL)
        print()
        file_path = fd.askopenfilename(title="Select image")
        
        return file_path
    except Exception as e:
        print(Fore.RED + "An error occurred while selecting the image:", str(e) + Style.RESET_ALL)
        return None

def process_image(img_path):
    """
    Process the selected image based on the chosen filter.

    Parameters:
    img_path (str): The file path of the selected image.
    """
    if img_path:
        try:
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
            
            # Input validation loop
            while True:
                try:
                    # Prompt user to enter their choice of filter
                    user_choice = int(input(Fore.YELLOW + "Enter your choice: " + Style.RESET_ALL))

                    if user_choice in range(1, 11):
                        # Start timing the image processing
                        start_time = time.time()

                        # Apply the selected filter to the image
                        output_img_path = apply_filter(img, img_base_name, output_path, user_choice)

                        # End timing the image processing
                        end_time = time.time()
                        
                        # Calculate and display the processing time
                        processing_time = end_time - start_time
                        print(Fore.GREEN + f"Processing completed in {processing_time:.2f} seconds." + Style.RESET_ALL)
                        
                        # Open the image
                        open_image(output_img_path)
                        break  # Exit the loop if input is valid
                    else:
                        # Handle invalid input for filter choice
                        print(Fore.RED + "Invalid Input. Please enter a number between 1 and 10." + Style.RESET_ALL)
                except ValueError:
                    # Handle invalid input type
                    print(Fore.RED + "Invalid Input. Please enter a valid number." + Style.RESET_ALL)
        except FileNotFoundError as e:
            print(e)
        except IOError as e:
            print(Fore.RED + "An error occurred while opening the image file:", str(e) + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + "An error occurred while processing the image:", str(e) + Style.RESET_ALL)
    else:
        # Handle case when no file is selected
        print(Fore.RED + "No file selected. Exiting the program." + Style.RESET_ALL)

def apply_filter(img, img_base_name, output_path, user_choice):
    filter_functions = [blur, contour, detail, edge, xedge, emboss, fedge, sharp, smooth, xsmooth]
    selected_filter = filter_functions[user_choice - 1]
    return selected_filter(img, img_base_name, output_path)

def open_image(file_path):
    if file_path:
        if name == 'nt':
            startfile(file_path)
        elif name == 'posix':
            opener = 'open' if platform == 'darwin' else 'xdg-open'
            system(f"{opener} {file_path}")


if __name__ == '__main__':
    # Call functions to select and process the image
    init(autoreset=True)
    img_path = select_image()
    process_image(img_path)
