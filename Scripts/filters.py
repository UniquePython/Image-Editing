from PIL import ImageFilter
from os import path

def save_image_with_filter(img, img_name, output_path, filter_name, filter_func):
    filtered_img = img.filter(filter_func)
    output_file_path = path.join(output_path, f'{img_name}_{filter_name}.png')
    filtered_img.save(output_file_path, 'PNG')

def blur(img, img_name, output_path):
    save_image_with_filter(img, img_name, output_path, 'blur', ImageFilter.BLUR)

def contour(img, img_name, output_path):
    save_image_with_filter(img, img_name, output_path, 'contour', ImageFilter.CONTOUR)

def detail(img, img_name, output_path):
    save_image_with_filter(img, img_name, output_path, 'detail', ImageFilter.DETAIL)

def edge(img, img_name, output_path):
    save_image_with_filter(img, img_name, output_path, 'edgeenhance', ImageFilter.EDGE_ENHANCE)

def xedge(img, img_name, output_path):
    save_image_with_filter(img, img_name, output_path, 'xedgeenhance', ImageFilter.EDGE_ENHANCE_MORE)

def emboss(img, img_name, output_path):
    save_image_with_filter(img, img_name, output_path, 'emboss', ImageFilter.EMBOSS)

def sharp(img, img_name, output_path):
    save_image_with_filter(img, img_name, output_path, 'sharp', ImageFilter.SHARPEN)

def fedge(img, img_name, output_path):
    save_image_with_filter(img, img_name, output_path, 'fedge', ImageFilter.FIND_EDGES)

def smooth(img, img_name, output_path):
    save_image_with_filter(img, img_name, output_path, 'smooth', ImageFilter.SMOOTH)

def xsmooth(img, img_name, output_path):
    save_image_with_filter(img, img_name, output_path, 'xsmooth', ImageFilter.SMOOTH_MORE)
