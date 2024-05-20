from PIL import ImageFilter
from os import path
from colorama import Fore, Style

def save_image_with_filter(img, filter_func, img_base_name, output_path):
    """
    Apply a specified filter to an image and save the result.

    Parameters:
    - img (PIL.Image): The input image to be processed.
    - filter_func (function): The function representing the image filter to be applied.
    - img_base_name (str): The base name of the input image file.
    - output_path (str): The directory where the processed image will be saved.
    """
    # Apply the specified filter to the image
    filtered_img = img.filter(filter_func)

    # Construct the output file path
    output_file_path = path.join(output_path, f"{img_base_name}_{filter_func.__name__}.png")

    # Save the processed image
    filtered_img.save(output_file_path, 'PNG')
    print(Fore.GREEN + f"Image saved as: {output_file_path}" + Style.RESET_ALL)
    print()
    return output_file_path

def blur(img, img_name, output_path):
    save_image_with_filter(img, ImageFilter.BLUR, img_name, output_path)

def contour(img, img_name, output_path):
    save_image_with_filter(img, ImageFilter.CONTOUR, img_name, output_path)

def detail(img, img_name, output_path):
    save_image_with_filter(img, ImageFilter.DETAIL, img_name, output_path)

def edge(img, img_name, output_path):
    save_image_with_filter(img, ImageFilter.EDGE_ENHANCE, img_name, output_path)

def xedge(img, img_name, output_path):
    save_image_with_filter(img, ImageFilter.EDGE_ENHANCE_MORE, img_name, output_path)

def emboss(img, img_name, output_path):
    save_image_with_filter(img, ImageFilter.EMBOSS, img_name, output_path)

def sharp(img, img_name, output_path):
    save_image_with_filter(img, ImageFilter.SHARPEN, img_name, output_path)

def fedge(img, img_name, output_path):
    save_image_with_filter(img, ImageFilter.FIND_EDGES, img_name, output_path)

def smooth(img, img_name, output_path):
    save_image_with_filter(img, ImageFilter.SMOOTH, img_name, output_path)

def xsmooth(img, img_name, output_path):
    save_image_with_filter(img, ImageFilter.SMOOTH_MORE, img_name, output_path)
