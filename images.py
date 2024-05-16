from tkinter import filedialog as fd
from PIL import Image, ImageFilter
from os import path

def blur(img, img_name):
    blur_img = img.filter(ImageFilter.BLUR)
    blur_img.save(f'{img_name}_blur.png', 'png')

def contour(img, img_name):
    contour_img = img.filter(ImageFilter.CONTOUR)
    contour_img.save(f'{img_name}_contour.png', 'png')

def detail(img, img_name):
    detail_img = img.filter(ImageFilter.DETAIL)
    detail_img.save(f'{img_name}_detail.png', 'png')

def edge(img, img_name):
    edge_img = img.filter(ImageFilter.EDGE_ENHANCE)
    edge_img.save(f'{img_name}_edgeenhance.png', 'png')

def xedge(img, img_name):
    xedge_img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    xedge_img.save(f'{img_name}_xedgeenhance.png', 'png')

def emboss(img, img_name):
    emboss_img = img.filter(ImageFilter.EMBOSS)
    emboss_img.save(f'{img_name}_emboss.png', 'png')

def sharp(img, img_name):
    sharp_img = img.filter(ImageFilter.SHARPEN)
    sharp_img.save(f'{img_name}_sharp.png', 'png')

def fedge(img, img_name):
    fedge_img = img.filter(ImageFilter.FIND_EDGES)
    fedge_img.save(f'{img_name}_fedge.png', 'png')

def smooth(img, img_name):
    smooth_img = img.filter(ImageFilter.SMOOTH)
    smooth_img.save(f'{img_name}_smooth.png', 'png')

def xsmooth(img, img_name):
    xsmooth_img = img.filter(ImageFilter.SMOOTH_MORE)
    xsmooth_img.save(f'{img_name}_xsmooth.png', 'png')

def open_image_and_process():
    file_path = fd.askopenfilename()

    if file_path:
        img = Image.open(file_path)
        img_name = path.basename(file_path) 

        blur(img, img_name)
        contour(img, img_name)
        detail(img, img_name)
        edge(img, img_name)
        xedge(img, img_name)
        emboss(img, img_name)
        fedge(img, img_name)
        sharp(img, img_name)
        smooth(img, img_name)
        xsmooth(img, img_name)
    else:
        raise FileNotFoundError("The file you are trying to access does not exist. Please try again.")

if __name__ == '__main__':
    open_image_and_process()
