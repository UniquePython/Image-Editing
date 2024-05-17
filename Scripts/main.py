from tkinter import filedialog as fd
from PIL import Image
from os import path
from colorama import init, Fore, Style
from filters import * 
from choices import *

def open_image_and_process():
    print(Fore.YELLOW + "Please select the image you want to process." + Style.RESET_ALL)
    print()
    file_path = fd.askopenfilename()

    if file_path:
        img = Image.open(file_path)
        img_name = path.basename(file_path) 

        print(Fore.GREEN + "You have selected the file:", img_name + Style.RESET_ALL)
        print(Fore.CYAN + "File path:", file_path + Style.RESET_ALL)
        print()

        choices()

        try:
            user_choice = int(input(Fore.YELLOW + "Enter your choice: " + Style.RESET_ALL))

            if user_choice in range(1, 11):
                if user_choice == 1:
                    blur(img, img_name)
                elif user_choice == 2:
                    contour(img, img_name)
                elif user_choice == 3:
                    detail(img, img_name)
                elif user_choice == 4:
                    edge(img, img_name)
                elif user_choice == 5:
                    xedge(img, img_name)
                elif user_choice == 6:
                    emboss(img, img_name)
                elif user_choice == 7:
                    fedge(img, img_name)
                elif user_choice == 8:
                    sharp(img, img_name)
                elif user_choice == 9:
                    smooth(img, img_name)
                elif user_choice == 10:
                    xsmooth(img, img_name)
                else:
                    print(Fore.RED + "Invalid Input" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Invalid Input" + Style.RESET_ALL)
            print(Fore.GREEN + "Processing Complete!" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Invalid Input. Please enter a number." + Style.RESET_ALL)
    else:
        raise FileNotFoundError

if __name__ == '__main__':
    try:
        open_image_and_process()
    except FileNotFoundError as _:
        print(Fore.RED + "Exiting the program since user cancelled the input." + Style.RESET_ALL)
