from PIL import Image
from multiprocessing import Process
import glob, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def number_of_strides(dim):
    """
    Returns the number times the window will move in a particular axis
    """
    return int(dim/128)

def cut_photo(photo):
    original = Image.open(photo)
    file, ext = os.path.splitext(photo)
    width, height = original.size

    # coordinates of top left corner
    left = 0
    top = 0
    # coordinates of bottom right corner
    bottom = 128
    right = 128

    cropped_counter = 1

    for y in range(0,number_of_strides(height)):
        for x in range(0, number_of_strides(width)):
            cropped_photo = original.crop((left, top, right, bottom))
            cropped_photo.save(BASE_DIR+'\\processed\\'+file[6:]+'_'+str(x)+'_'+str(y)+'___'+str(cropped_counter)+".jpg", "JPEG")
            print("("+ str(left) + "," + str(top) + ")"+","+"("+ str(right) + "," + str(bottom) + ")"+" number "+ str(cropped_counter))
            right += 128
            left += 128
            cropped_counter += 1
        left = 0
        right = 128
        top += 128
        bottom += 128


def cut_photos():
    photos = glob.glob("./raw/*.jpg")
    # number_of_photos = len(photos)
    counter = 1
    for photo in photos:
        p = Process(target = cut_photo, args = (photo,))
        p.start()
        # p.join()
        counter += 1
        print("Photo " + str(counter))

if __name__ == "__main__":
    cut_photos()
