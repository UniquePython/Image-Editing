from colorama import Fore, Style

def choices():
    options = [
        "Blur", "Contour", "Detail", "Edge", "Extra Edge",
        "Emboss", "Find Edges", "Sharpen", "Smooth", "Extra Smooth"
    ]
    print(Fore.BLUE + "What do you want to do?" + Style.RESET_ALL)
    for i, option in enumerate(options, start=1):
        print(Fore.CYAN + f"{i}. {option}" + Style.RESET_ALL)
