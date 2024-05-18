from PIL import ImageFilter
from os import path

def save_image_with_filter(img, img_name, output_path, filter_name, filter_func):
    """
    Apply a specified filter to an image and save the result.

    Parameters:
    - img (PIL.Image): The input image to be processed.
    - img_name (str): The base name of the input image file.
    - output_path (str): The directory where the processed image will be saved.
    - filter_name (str): The name of the filter being applied.
    - filter_func (function): The function representing the image filter to be applied.
    """
    # Apply the specified filter to the image
    filtered_img = img.filter(filter_func)

    # Construct the output file path
    output_file_path = path.join(output_path, f'{img_name}_{filter_name}.png')

    # Save the processed image
    filtered_img.save(output_file_path, 'PNG')

def blur(img, img_name, output_path):
    """
    Apply a blur filter to the image and save the result.

    Parameters:
    - img (PIL.Image): The input image to be processed.
    - img_name (str): The base name of the input image file.
    - output_path (str): The directory where the processed image will be saved.
    """
    save_image_with_filter(img, img_name, output_path, 'blur', ImageFilter.BLUR)

def contour(img, img_name, output_path):
    """
    Apply a contour filter to the image and save the result.

    Parameters:
    - img (PIL.Image): The input image to be processed.
    - img_name (str): The base name of the input image file.
    - output_path (str): The directory where the processed image will be saved.
    """
    save_image_with_filter(img, img_name, output_path, 'contour', ImageFilter.CONTOUR)

def detail(img, img_name, output_path):
    """
    Apply a detail filter to the image and save the result.

    Parameters:
    - img (PIL.Image): The input image to be processed.
    - img_name (str): The base name of the input image file.
    - output_path (str): The directory where the processed image will be saved.
    """
    save_image_with_filter(img, img_name, output_path, 'detail', ImageFilter.DETAIL)

def edge(img, img_name, output_path):
    """
    Apply an edge enhance filter to the image and save the result.

    Parameters:
    - img (PIL.Image): The input image to be processed.
    - img_name (str): The base name of the input image file.
    - output_path (str): The directory where the processed image will be saved.
    """
    save_image_with_filter(img, img_name, output_path, 'edgeenhance', ImageFilter.EDGE_ENHANCE)

def xedge(img, img_name, output_path):
    """
    Apply an edge enhance more filter to the image and save the result.

    Parameters:
    - img (PIL.Image): The input image to be processed.
    - img_name (str): The base name of the input image file.
    - output_path (str): The directory where the processed image will be saved.
    """
    save_image_with_filter(img, img_name, output_path, 'xedgeenhance', ImageFilter.EDGE_ENHANCE_MORE)

def emboss(img, img_name, output_path):
    """
    Apply an emboss filter to the image and save the result.

    Parameters:
    - img (PIL.Image): The input image to be processed.
    - img_name (str): The base name of the input image file.
    - output_path (str): The directory where the processed image will be saved.
    """
    save_image_with_filter(img, img_name, output_path, 'emboss', ImageFilter.EMBOSS)

def sharp(img, img_name, output_path):
    """
    Apply a sharpen filter to the image and save the result.

    Parameters:
    - img (PIL.Image): The input image to be processed.
    - img_name (str): The base name of the input image file.
    - output_path (str): The directory where the processed image will be saved.
    """
    save_image_with_filter(img, img_name, output_path, 'sharp', ImageFilter.SHARPEN)

def fedge(img, img_name, output_path):
    """
    Apply a find edge filter to the image and save the result.

    Parameters:
    - img (PIL.Image): The input image to be processed.
    - img_name (str): The base name of the input image file.
    - output_path (str): The directory where the processed image will be saved.
    """
    save_image_with_filter(img, img_name, output_path, 'fedge', ImageFilter.FIND_EDGES)

def smooth(img, img_name, output_path):
    """
    Apply a smooth filter to the image and save the result.

    Parameters:
    - img (PIL.Image): The input image to be processed.
    - img_name (str): The base name of the input image file.
    - output_path (str): The directory where the processed image will be saved.
    """
    save_image_with_filter(img, img_name, output_path, 'smooth', ImageFilter.SMOOTH)

def xsmooth(img, img_name, output_path):
    """
    Apply a smooth more filter to the image and save the result.

    Parameters:
    - img (PIL.Image): The input image to be processed.
    - img_name (str): The base name of the input image file.
    - output_path (str): The directory where the processed image will be saved.
    """
    save_image_with_filter(img, img_name, output_path, 'xsmooth', ImageFilter.SMOOTH_MORE)
