from tkinter import filedialog as fd
from PIL import Image
from os import path, makedirs
from colorama import init, Fore, Style
from filters import *
from choices import *

def open_image_and_process():
    init(autoreset=True)
    print(Fore.YELLOW + "Please select the image you want to process." + Style.RESET_ALL)
    print()
    file_path = fd.askopenfilename()

    if file_path:
        img = Image.open(file_path)
        img_name = path.basename(file_path) 
        img_base_name = path.splitext(img_name)[0]  # to handle file extensions properly

        print(Fore.GREEN + "You have selected the file:", img_name + Style.RESET_ALL)
        print(Fore.CYAN + "File path:", file_path + Style.RESET_ALL)
        print()

        output_path = input(Fore.YELLOW + "Enter the directory where you want your output to be saved: " + Style.RESET_ALL)

        if not path.exists(output_path):
            makedirs(output_path)

        choices()
        try:
            user_choice = int(input(Fore.YELLOW + "Enter your choice: " + Style.RESET_ALL))

            if user_choice in range(1, 11):
                filter_functions = [blur, contour, detail, edge, xedge, emboss, fedge, sharp, smooth, xsmooth]
                selected_filter = filter_functions[user_choice - 1]
                selected_filter(img, img_base_name, output_path)  
                print(Fore.GREEN + "Processing Complete!" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Invalid Input. Please enter a number between 1 and 10." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Invalid Input. Please enter a valid number." + Style.RESET_ALL)
    else:
        print(Fore.RED + "No file selected. Exiting the program." + Style.RESET_ALL)

if __name__ == '__main__':
    open_image_and_process()
