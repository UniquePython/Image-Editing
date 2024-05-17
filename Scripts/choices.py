from colorama import init, Fore, Style

init(autoreset=True)

def choices():
    print(Fore.BLUE + "What do you want to do?" + Style.RESET_ALL)
    print(Fore.CYAN + "1. Blur" + Style.RESET_ALL)
    print(Fore.CYAN + "2. Contour" + Style.RESET_ALL)
    print(Fore.CYAN + "3. Detail" + Style.RESET_ALL)
    print(Fore.CYAN + "4. Edge" + Style.RESET_ALL)
    print(Fore.CYAN + "5. Extra Edge" + Style.RESET_ALL)
    print(Fore.CYAN + "6. Emboss" + Style.RESET_ALL)
    print(Fore.CYAN + "7. Find Edges" + Style.RESET_ALL)
    print(Fore.CYAN + "8. Sharpen" + Style.RESET_ALL)
    print(Fore.CYAN + "9. Smooth" + Style.RESET_ALL)
    print(Fore.CYAN + "10. Extra Smooth" + Style.RESET_ALL)
