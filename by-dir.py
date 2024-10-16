from os import listdir
from os.path import splitext

from PIL import Image

ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']
PIXEL_COLORS = {
    'R': (255, 0, 0),
    'O': (255, 165, 0),
    'Y': (255, 255, 0),
    'G': (0, 255, 0),
    'C': (0, 0, 255),
    'P': (128, 0, 128),
    'B': (0, 0, 0),
    'W': (255, 255, 255),
}
VALID_FILETYPES = [".jpg", ".jpeg", ".png"]

MAX_WIDTH = 64
COLOR_INDICATOR = '`'
NEWLINE_SYMBOL = '$'

def eucl_dist(firstVector, secondVector):
    return ((firstVector[0] - secondVector[0]) ** 2 +
            (firstVector[1] - secondVector[1]) ** 2 +
            (firstVector[2] - secondVector[2]) ** 2) ** 0.5

def resize_image(image):
    width, height = image.size
    ratio = height / width

    return image.resize((MAX_WIDTH, int(MAX_WIDTH * ratio)))

def get_colors(pixel):
    colors = []
    dists = []
    for color_name, color_rgb in PIXEL_COLORS.items():
        dist = eucl_dist(pixel, color_rgb)
        
        if len(dists) == 0:
            dists.append(dist)
            colors.append(color_name)
        else:
            for i, found_dist in enumerate(dists):
                if dist < found_dist:
                    dists.insert(i, dist)
                    colors.insert(i, color_name)
                    
                    break
            
            dists.append(dist)
            colors.append(color_name)
    
    return [colors[0], colors[1]]

def color_ascii(image):
    grayscale = image.convert('L')

    intensity_pixels = grayscale.getdata()
    color_pixels = image.getdata()

    ascii_image = ''
    for i, intensity_pixel in enumerate(intensity_pixels):
        intensity = intensity_pixel // 25
        
        color_pixel = color_pixels[i]
        colors = get_colors(list(color_pixel))
        
        foreground = colors[1].lower()
        background = colors[0].upper()

        ascii_image += COLOR_INDICATOR + foreground + background + str(ASCII_CHARS[intensity])

        if (i + 1) % MAX_WIDTH == 0 and i > 0:
            ascii_image += NEWLINE_SYMBOL

    return ascii_image

def main():
    path = input("Enter path to directory of images:\n")
    try:
        dirlist = listdir(path)
    except:
        print("Invalid path!")

        main()
        return
    
    for path in dirlist:
        file_name, file_extension = splitext(path)
        if not file_extension in VALID_FILETYPES: continue

        image = Image.open(path)
        new_image = resize_image(image)

        ascii_text = color_ascii(new_image)
        print("--", path, "ASCII --")
        print(ascii_text.encode("unicode_escape").decode() + '\n')
    
    main()

main()
