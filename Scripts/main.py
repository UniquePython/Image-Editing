from tkinter import filedialog as fd
from PIL import Image
from os import path, name, startfile, system
from sys import platform
from colorama import init, Fore, Style
from filters import filter_functions, save_image_with_filter
from choices import choices
import time

for filter_name, filter_func in filter_functions.items():
    globals()[filter_name] = filter_func

def select_image():
    try:
        print(Fore.YELLOW + "Please select the image you want to process." + Style.RESET_ALL + "\n")
        return fd.askopenfilename(title="Select image")
    except Exception as e:
        print(Fore.RED + "An error occurred while selecting the image:", str(e) + Style.RESET_ALL)
        return None

def process_image(img_path):
    if not img_path:
        print(Fore.RED + "No file selected. Exiting the program." + Style.RESET_ALL)
        return

    try:
        img = Image.open(img_path)
        img_name = path.basename(img_path)
        img_base_name = path.splitext(img_name)[0]
        print(Fore.GREEN + f"You have selected the file: {img_name}" + Style.RESET_ALL)
        print(Fore.CYAN + f"File path: {img_path}" + Style.RESET_ALL + "\n")

        output_path = fd.askdirectory(title="Select Output folder")
        print(Fore.GREEN + f"You have selected the folder: {output_path}" + Style.RESET_ALL + "\n")

        while True:
            try:
                choices()

                user_choice = int(input(Fore.YELLOW + "Enter your choice: " + Style.RESET_ALL))
                if user_choice in range(1, 11):
                    start_time = time.time()
                    output_img_path = apply_filter(img, img_base_name, output_path, user_choice)
                    end_time = time.time()
                    processing_time = end_time - start_time
                    print(Fore.GREEN + f"Processing completed in {processing_time:.2f} seconds." + Style.RESET_ALL)
                    open_image(output_img_path)
                    break
                else:
                    print(Fore.RED + "Invalid Input. Please enter a number between 1 and 10." + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Invalid Input. Please enter a valid number." + Style.RESET_ALL)
    except (FileNotFoundError, IOError, Exception) as e:
        print(Fore.RED + "An error occurred while processing the image:", str(e) + Style.RESET_ALL)

def apply_filter(img, img_base_name, output_path, user_choice):
    filter_function = list(filter_functions.values())[user_choice - 1]
    output_file_path = save_image_with_filter(img, filter_function, img_base_name, output_path)
    return output_file_path

def open_image(file_path):
    if file_path:
        if name == 'nt':
            startfile(file_path)
        elif name == 'posix':
            opener = 'open' if platform == 'darwin' else 'xdg-open'
            system(f"{opener} {file_path}")

if __name__ == '__main__':
    init(autoreset=True)
    img_path = select_image()
    process_image(img_path)
