from ast import Mod
import cv2
import numpy as np

import os
from matplotlib import pyplot

def edit():
    #Read the image
    image = cv2.imread('Media/sample.jpg')

    #greyscale filter
    def greyscale(img):
        greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return greyscale

    # brightness adjustment
    def bright(img, beta_value ):
        img_bright = cv2.convertScaleAbs(img, beta=beta_value)
        return img_bright

    #sharp effect
    def sharpen(img):
        kernel = np.array([[-1, -1, -1], [-1, 9.5, -1], [-1, -1, -1]])
        img_sharpen = cv2.filter2D(img, -1, kernel)
        return img_sharpen

    #sepia effect
    def sepia(img):
        img_sepia = np.array(img, dtype=np.float64) # converting to float to prevent loss
        img_sepia = cv2.transform(img_sepia, np.matrix([[0.272, 0.534, 0.131],
                                        [0.349, 0.686, 0.168],
                                        [0.393, 0.769, 0.189]])) # multipying image with special sepia matrix
        img_sepia[np.where(img_sepia > 255)] = 255 # normalizing values greater than 255 to 255
        img_sepia = np.array(img_sepia, dtype=np.uint8)
        return img_sepia

    #grey pencil sketch effect
    def pencil_sketch_grey(img):
        #inbuilt function to create sketch effect in colour and greyscale
        sk_gray, sk_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.1) 
        return  sk_gray

    #colour pencil sketch effect
    def pencil_sketch_col(img):
        #inbuilt function to create sketch effect in colour and greyscale
        sk_gray, sk_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.1) 
        return  sk_color

    #HDR effect
    def HDR(img):
        hdr = cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)
        return  hdr

    # invert filter
    def invert(img):
        inv = cv2.bitwise_not(img)
        return inv

    #defining a function
    from scipy.interpolate import UnivariateSpline
    def LookupTable(x, y):
        spline = UnivariateSpline(x, y)
        return spline(range(256))

    #summer effect
    def Summer(img):
        increaseLookupTable = LookupTable([0, 64, 128, 256], [0, 80, 160, 256])
        decreaseLookupTable = LookupTable([0, 64, 128, 256], [0, 50, 100, 256])
        blue_channel, green_channel, red_channel  = cv2.split(img)
        red_channel = cv2.LUT(red_channel, increaseLookupTable).astype(np.uint8)
        blue_channel = cv2.LUT(blue_channel, decreaseLookupTable).astype(np.uint8)
        sum= cv2.merge((blue_channel, green_channel, red_channel ))
        return sum

    #winter effect
    def Winter(img):
        increaseLookupTable = LookupTable([0, 64, 128, 256], [0, 80, 160, 256])
        decreaseLookupTable = LookupTable([0, 64, 128, 256], [0, 50, 100, 256])
        blue_channel, green_channel, red_channel = cv2.split(img)
        red_channel = cv2.LUT(red_channel, decreaseLookupTable).astype(np.uint8)
        blue_channel = cv2.LUT(blue_channel, increaseLookupTable).astype(np.uint8)
        win= cv2.merge((blue_channel, green_channel, red_channel))
        return win


    #making the greyscale image
    a1 = greyscale(image)
    filename = 'greyscale.jpg'
    # Using cv2.imwrite() method
    # Saving the image
    cv2.imwrite(f'Edited/{filename}', a1)

    #making the  more bright image
    #positive beta value
    a2 = bright(image, 60)
    filename = 'more_bright.jpg'
    # Using cv2.imwrite() method
    # Saving the image
    cv2.imwrite(f'Edited/{filename}', a2)

    #making the  less bright image
    #negative beta value
    a3 = bright(image, -60)
    filename = 'less_bright.jpg'
    # Using cv2.imwrite() method
    # Saving the image
    cv2.imwrite(f'Edited/{filename}', a3)

    #making the sharp image
    a4 = sharpen(image)
    filename = 'sharpen.jpg'
    # Using cv2.imwrite() method
    # Saving the image
    cv2.imwrite(f'Edited/{filename}', a4)

    #making the sepia image
    a5 = sepia(image)
    filename = 'sepia.jpg'
    # Using cv2.imwrite() method
    # Saving the image
    cv2.imwrite(f'Edited/{filename}', a5)

    #making the grey pencil sketch
    a6 = pencil_sketch_grey(image)
    filename = 'pencil_grey.jpg'
    # Using cv2.imwrite() method
    # Saving the image
    cv2.imwrite(f'Edited/{filename}', a6)

    #making the colour pencil sketch
    a7 = pencil_sketch_col(image)
    filename = 'pencil_col.jpg'
    # Using cv2.imwrite() method
    # Saving the image
    cv2.imwrite(f'Edited/{filename}', a7)

    #making the hdr img
    a8 = HDR(image)
    filename = 'HDR.jpg'
    # Using cv2.imwrite() method
    # Saving the image
    cv2.imwrite(f'Edited/{filename}', a8)

    #making the invert img
    a9 = invert(image)
    filename = 'invert.jpg'
    # Using cv2.imwrite() method
    # Saving the image
    cv2.imwrite(f'Edited/{filename}', a9)

    #making the summer img
    a11 = Summer(image)
    filename = 'Summer.jpg'
    # Using cv2.imwrite() method
    # Saving the image
    cv2.imwrite(f'Edited/{filename}', a11)

    #making the winter img
    a10 = Winter(image)
    filename = 'Winter.jpg'
    # Using cv2.imwrite() method
    # Saving the image
    cv2.imwrite(f'Edited/{filename}', a10)

    os.startfile('Edited')