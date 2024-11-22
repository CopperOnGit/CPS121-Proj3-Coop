# CPS121 Project 3
# Written: <date> <fullname> <email>
# 
# <Include description of program here>
##
# Change each occurrence of "_" in the list below to be "Y" or "N" to indicate
# whether or not the given transformation is implemented in your program.
#
#   Can be done using just getPixels()
#   Y Altering colors of the image
#   Y Grayscale
#   Y Making darker or lighter
#   Y Sepia-toned
#   _ Posterized
#   Need nested loops
#   _ Mirrorizing
#   Y Edge detection
#   N Chromakey (change background)
#   N Blurring
#   Need nested loops and alter size or shape
#   _ Rotation
#   _ Cropping
#   _ Shifting
#   Other transformations
#   _ <description of transformation>
#   _ <description of transformation>
#   _ <description of transformation>
# ============================================================================

import GCPictureTools as pgt
import pygame as pg
import os, sys
import traceback
from GCPictureTools import Picture

# ============================================================================
# ================ Start making changes after this comment ===================
# ============================================================================

# ---- SUPPORTING FUNCTIONS SHOULD GO HERE ----
def edge(picture):
   edgedPicture = Picture(picture.getWidth(), picture.getHeight())
   for p in picture.getPixels():   
      red = p.getRed()
      green = p.getGreen()
      blue = p.getBlue()
      x = p.getX()
      y = p.getY()
      p1=  pgt.Pixel(p.getPicture(), p.getX()+1, p.getY()+1)
      if y < (picture.getHeight()-1) and x < (picture.getWidth()-1):
         sum = red+green+blue
         sum2 = p1.getRed()+p1.getGreen() + p1.getBlue() 
         diff = min(255, abs(sum2-sum))
         edgedPicture.setColor(p.getX(),p.getY(), (diff, diff, diff))
   return edgedPicture
         
def blueify(picture): # turn the blue colors more blue
   bluey = Picture(picture.getWidth(), picture.getHeight())
   for col in range(picture.getWidth()):
      for row in range(picture.getHeight()):
         pixel = picture.getPixel(col, row)
         red = pixel.getRed()
         green = pixel.getGreen()
         blue = pixel.getBlue()
         bluey.setColor(col, row, pg.Color(red, green, blue))
         if blue > red and blue > green:
            bluey.setBlue(col, row, 255)
   return bluey

def redy(picture): # turn the red colors more red
   redy = Picture(picture.getWidth(), picture.getHeight())
   for col in range(picture.getWidth()):
      for row in range(picture.getHeight()):
         pixel = picture.getPixel(col, row)
         red = pixel.getRed()
         green = pixel.getGreen()
         blue = pixel.getBlue()
         redy.setColor(col, row, pg.Color(red, green, blue))
         if red > blue and red > green:
            redy.setRed(col, row, 255)
   return redy

def darken(picture): # make the picture look darker
    darkerPicture = Picture(picture.getWidth(), picture.getHeight())
    for x in range(0, picture.getWidth()):
        for y in range(0, picture.getHeight()):
            darkerPicture.setGreen(x, y, picture.getGreen(x,y)*0.6)
            darkerPicture.setRed(x, y, picture.getRed(x,y)*0.5)
            darkerPicture.setBlue(x, y, picture.getBlue(x,y)*1.0)
    return darkerPicture
    
def monochrome(picture): # make the picture black and white
    blackWhite = Picture(picture.getWidth(), picture.getHeight())
    for x in range(0, picture.getWidth()):
        for y in range(0, picture.getHeight()):
            value = (picture.getRed(x,y) + picture.getGreen(x,y) +
            blackWhite.getBlue(x,y))/3
            blackWhite.setRed(x, y, value)
            blackWhite.setGreen(x, y, value)
            blackWhite.setBlue(x, y, value)
    return blackWhite

def alien(picture): # make the picture look like it is very old
    vintageStock = Picture(picture.getWidth(), picture.getHeight())
    for x in range(0,picture.getWidth()):
        for y in range(0, picture.getHeight()):
            red = picture.getRed(x,y)
            blue = picture.getBlue(x,y)
            if (red < 63):
                red = red*1.1
            blue = blue*0.9
            if (red > 62 and red < 192):
                red = red*1.15
            blue = blue*0.85
            if (red > 191):
                red = red*1.08
            if (red > 255):
                red = 225
            blue = blue*0.93
            vintageStock.setBlue(x, y, blue)
            vintageStock.setRed(x, y, red)
    return vintageStock

def mirrorPicture(picture): # mirror the image
    mirrorPicture = Picture(picture.getWidth(), picture.getHeight())
    for x in range(picture.getWidth()):
        for y in range(picture.getHeight()):
            mirrorPicture.setColor(picture.getWidth() - 1 - x, y, picture.getColor(x,y))
    return mirrorPicture

def flippedPicture(picture): # flip the image upside down
    flippedPicture = Picture(picture.getWidth(), picture.getHeight())
    for x in range(picture.getWidth()):
        for y in range(picture.getHeight()):
            flippedPicture.setColor(x, picture.getHeight() - 1 - y, picture.getColor(x,y))
    return flippedPicture

def createCollage():

    """Create a collage.
 
    Returns
    -------
    Picture
        the collage.
    """
    # create "canvas" on which to make a collage.  You may exchange the
    # width and height values if you prefer a landscape orientation.
    collage = pgt.Picture(700, 950)

    # ---- YOUR CODE TO BUILD THE COLLAGE GOES HERE ----
    # Notice that this is **inside** the createCollage() function.  Because
    # createCollage() should be a "one-and-only-one-thing" function, you
    # should use supporting functions to do transformations, etc.  These
    # supporting functions should be defined below, after the code for this
    # function.
    pic = pgt.Picture('image.png')
    edgedPicture = edge(pic)
    bluey = blueify(pic)
    darkImage = darken(pic)
    blackWhite = monochrome(pic)
    dangThatsOld = alien(pic)
    mirrorAhhPic = mirrorPicture(pic)
    RED = redy(pic)
    flippedAhhPic = flippedPicture(pic)

    edgedPicture.copyInto(collage, 100, 100)
    bluey.copyInto(collage, 100, 300)
    darkImage.copyInto(collage, 100, 500)
    blackWhite.copyInto(collage, 250, 100)
    dangThatsOld.copyInto(collage, 250, 300)
    mirrorAhhPic.copyInto(collage, 250, 500)
    RED.copyInto(collage, 400, 100)
    flippedAhhPic.copyInto(collage, 400, 300)
    pic.copyInto(collage, 400, 500)
    
    collage.save("swag.png")
    
    return collage

def createWebPage(imageFile, webPageFile):
    """Create web page that contains the collage.
    Parameter: imageFile - the image file name 
    Parameter: webPageFile - the finename of the output web page 
    Returns
    -------
    nothing
    """

    htmlFile = open(webPageFile, "wt")

    # ---- YOUR CODE TO BUILD THE Webpage with the COLLAGE GOES HERE ----
    # Matthew gave the idea for this part in writing out what the html file's code would be
    htmlCreation = f"""
    <DOCTYPE!>
    <html>
    <title>Cooper's Image Manipulator</title>
    <body>
    <h1>Cooper's image changer of his 2001 Dodge Dakota</h1>
    <img src="swag.png" alt= "Cooper's Collage should go here"></body>
    </html>
    """
    with open(webPageFile, "w") as file:
        file.write(htmlCreation)
    
if __name__ == "__main__":
    artFile = createCollage()
    createWebPage(artFile, "CooperArt.html")







# ============================================================================
# ============== Do NOT make any changes below this comment ==================
# ============================================================================

if __name__ == '__main__':

    # first command line argument, if any, is name of image file for output
    # second command line argument, if any, is name of the output html file name
    collageFile = None
    htmlFileName = "webpage.html"  #Default name

    if len(sys.argv) > 1:
        collageFile = sys.argv[1]
    if len(sys.argv) > 2:
        htmlFile = sys.argv[2]    

    # temporarily set media path to project directory
    scriptDir = os.path.dirname(os.path.realpath(sys.argv[0]))

    # create the collage
    
    collage = createCollage()
    #collage.display()

    try:
        # either show collage on screen or write it to file
        if collageFile is None:
            collage.display()
            input('Press Enter to quit...')
        else:
            print(f'Saving collage to {collageFile}')
            collage.save(collageFile)
            createWebPage(collageFile, htmlFileName)
    except:
        print('Could not show or save picture')

