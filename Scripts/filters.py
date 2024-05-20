from PIL import ImageFilter
from os import path
from colorama import Fore, Style
import time

def save_image_with_filter(img, filter_func, img_base_name, output_path):
    filtered_img = img.filter(filter_func)

    timestamp = str(int(time.time() * 1000))

    output_file_path = path.join(output_path, f"{img_base_name}_{filter_func.__name__}_{timestamp}.png")

    filtered_img.save(output_file_path, 'PNG')
    print(Fore.GREEN + f"Image saved as: {output_file_path}" + Style.RESET_ALL)
    print()
    return output_file_path

filter_functions = {
    "blur": ImageFilter.BLUR,
    "contour": ImageFilter.CONTOUR,
    "detail": ImageFilter.DETAIL,
    "edge": ImageFilter.EDGE_ENHANCE,
    "xedge": ImageFilter.EDGE_ENHANCE_MORE,
    "emboss": ImageFilter.EMBOSS,
    "sharp": ImageFilter.SHARPEN,
    "fedge": ImageFilter.FIND_EDGES,
    "smooth": ImageFilter.SMOOTH,
    "xsmooth": ImageFilter.SMOOTH_MORE
}

for filter_name, filter_func in filter_functions.items():
    globals()[filter_name] = lambda img, img_name, output_path, f=filter_func: save_image_with_filter(img, f, img_name, output_path)
