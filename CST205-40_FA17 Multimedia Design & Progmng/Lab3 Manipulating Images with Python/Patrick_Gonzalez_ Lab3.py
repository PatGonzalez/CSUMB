# Patrick Gonzalez
# CST 205 Fall '17
# Lab 3
#############################################################################
# Warm UP

def get_pic(): 
  return makePicture(pickAFile())
  
def halfRed():
  # pic = get_pic()
   #pixels = getPixels(pic)
   
   lessRed(50)
   
   #for p in pixels:
    # r = getRed(p)
     #setRed(p, r*0.5)
   #repaint(pic)
  
def noBlue():
   pic = get_pic()
   pixels = getPixels(pic)
   
   for p in pixels:
     #b = getBlue(p)
     setBlue(p, 0)  #sets the value of blue pixels(p) to the given value of 0
   repaint(pic)
 

########################################################################################
   
# Problem 1

def lessRed(lR):
   pic = get_pic()
   pixels = getPixels(pic)    # gets all the pixels and returns an array contatining all the 
                              # pixels of the pic and assigns it to the variable pixels 
   
   for p in pixels:
     r = getRed(p)            # takes the value of Red pixel(p) to the variable r
     FlR = float(lR) / 100    # turns the integer lR into a float and then into a percentage
     setRed(p, r*FlR)        # sets the value of pixel(p) to the value of (red pixel value(r) * the specified value of FlR)
   repaint(pic)
   print "Reduced red pixels by %s" %FlR
   writePictureTo(pic, "C://Users/Patri/Desktop//lessRedResults_P1.jpg") 
  
########################################################################################
 
# Problem 2
def moreRed(mR):
   pic = get_pic()
   pixels = getPixels(pic)    # gets all the pixels and returns an array contatining all the 
                              # pixels of the pic and assigns it to the variable pixels 
   
   for p in pixels:
     r = getRed(p)            # takes the value of Red pixel(p) to the variable r
     FmR = float(mR) / 100    # turns the integer FmR into a float and then into a percentage
     R = r + r*FmR             #take the original pixel value and increases the value by a cetain percentage(FmR)
     setRed(p, R)        # sets the value of pixel(p) to the value of (red pixel value(r) * the specified value of FlR)
   repaint(pic)
   print "Incresead red pixels %s" %(FmR)
   writePictureTo(pic, "C://Users/Patri/Desktop//moreRedResults_P2.jpg") 
 
########################################################################################
  
# Problem 3
# This program manipulates the RGB components of each
# pixel to make the image look pink.
# RGB value for pink = R255, G102, B255

def roseGlass():
  pic = get_pic()
  pixels = getPixels(pic)
  
  pink_color = makeColor(255,102,255)   # creates the color pink
  
  for p in pixels:
    orig_color = getColor(p)  
    setColor(p, orig_color + pink_color)    #adds the color pink ontop of each original pixel colors
  writePictureTo(pic, "C://Users/Patri/Desktop//roseGlassResults_P3.jpg") 
  return pic
  #repaint(pic)
    
########################################################################################
   
# Problem 4
# This program lights the color of a pic pixel by pixel
def lightenUp():
  pic = get_pic()
  pixels = getPixels(pic)
 
  for p in pixels:
    oldColor = getColor(p)
    newColor = makeLighter(oldColor)
      
    setColor(p, newColor)    
  repaint(pic)
  writePictureTo(pic, "C://Users/Patri/Desktop//lightenUpResults_P4.jpg") 
       
########################################################################################
    
#Problem 5
# This program creates the opposite value for red, green, and blue of each pixel on the range of (0,255)
def makeNegative():
  pic = get_pic()
  pixels = getPixels(pic)
  
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    
    newR = abs(r-255)
    newG = abs(g-255)
    newB = abs(b-255)
    
    setRed(p, newR)
    setGreen(p, newG)
    setBlue(p,newB)
  writePictureTo(pic, "C://Users/Patri/Desktop//makeNegativeResults_P5.jpg") 
  return pic
  #repaint(pic)
    
########################################################################################
     
# PRoblem 6
# This program converts a colored image into black and white
# Covert each pixel to gray-scale by computing the average of the RGB values for each pixel
#       and then using that average as the new RBG values for that pixel.

def BnW():
  pic = get_pic()
  pixels = getPixels(pic)
  
  for p in pixels:
    newColor = makeColor(((getRed(p) + getGreen(p) + getBlue(p)))/3)
    setColor(p, newColor)
    
  repaint(pic)
  writePictureTo(pic, "C://Users/Patri/Desktop//BnWResults_P6_1.jpg") 

def betterBnW():
  pic = get_pic()
  pixels = getPixels(pic)
  
  for p in pixels:
    newColor = makeColor((getRed(p)*0.299 + getGreen(p)*0.587 + getBlue(p)*0.144))
    setColor(p, newColor)
  writePictureTo(pic, "C://Users/Patri/Desktop//betterBnWResults_P6_2.jpg") 
  return pic  
  #repaint(pic)