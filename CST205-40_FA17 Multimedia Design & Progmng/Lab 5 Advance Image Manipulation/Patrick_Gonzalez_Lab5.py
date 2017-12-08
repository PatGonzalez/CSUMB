#Patirck Gonzalez
#CST 205 Fall B '17
#Lab #5 Adanced Image Manipulation

#This Function allows user to selcet an file and makes it a usable image in JES
def get_pic():
  return makePicture(pickAFile())
  
# This function prints to screen an images that is passed to it
def print2screen(pic):
  show(pic)
  
#this function creates a new blank image
def canvas(x,y):
    newPic = makeEmptyPicture(x,y)
    return newPic
    
#Warm Up
# This function makes a copy of an image onto an empty image bigger than the orignal in the middle
def centerPic():
  OGPic = get_pic()
  
  #Create a new empty image x times larger than the original
  newPic = makeEmptyPicture(getWidth(OGPic)*2, getHeight(OGPic)*2)
  # two for loops (one for x in the source picture that goes from 0 to width 
  # and one for y in the source picture that goes from 0 to height) and to keep track of the
  # current location in the target picture with variables that you increment yourself.
  for x in range(0, getWidth(OGPic)):
    for y in range(0, getHeight(OGPic)):
      FindMidX =(getWidth(newPic)/4)
      FindMidY = (getHeight(newPic)/4)
      p = getPixel(newPic, x+FindMidX, y+FindMidY) #Points to the pixel of the new pic 
      c = getColor(getPixel(OGPic,x,y)) #Copies the color for a pixel in the original pic
      setColor(p,c)  #assigns the color of the original pic to a pixel location of the new pic
      
  print2screen(newPic)
  writePictureTo(newPic, "C://Users/Patri/Desktop//CenterPicResult.jpg")
  return newPic
  
# Problem 1
# This function makes a copy of an image onto an empty image bigger than the orignal in the middle
# Parameters:
#    source = original pic 
#    target = makeEmptyPicture(getWidth(source)*2, getHeight(source)*2)
#    targetX and targetY are the x, y locations in the target picture where the (0,0)
def pyCopy(source, target, targetX, targetY):
  for x in range(0, getWidth(source)):
    for y in range(0, getHeight(source)):
      c = getColor(getPixel(source,x,y))     #Copies the color for a pixel in the original pic
      p = getPixel(target, x+targetX, y+targetY)  #Points to the pixel of the new pic 
      setColor(p,c)     #assigns the color of the original pic to a pixel location of the new pic
  #show(target)
  writePictureTo(target, "C://Users/Patri/Desktop//pyCopyResult.jpg")
  return target
  
 
#functions to use with problem 2 collage
def QuadMirror():
  pic = get_pic()
  
  #This loop copies the left side of the image to the right side
  for x in range(0,getWidth(pic)/2):
    for y in range(0,getHeight(pic)):
      pL = getPixel(pic,x,y)  #get pixel object on the right
      cc = getColor(pL)  #copy the color of pixels on the right
      pR = getPixel(pic,(getWidth(pic)-x-1),y) #get pixel object on the left
      setColor(pR,cc)   # set pixel object on the right to the color of pixel object on the left
      
      pU = getPixel(pic,x,y)  #get pixel object on the upper half
      cc = getColor(pU)  #copy the color of pixels on the upper half
      pL = getPixel(pic,x,(getHeight(pic)-y-1)) #get pixel object on the bottom half
      setColor(pL,cc)   # set pixel object on the upper half to the color of pixel object on the bottom half
  return pic
  
#This function mirrors an image down the middle along the y-axis left-to-right
def mirrorY():
  pic = get_pic()
  
  #This loop copies the left side of the image to the right side
  for x in range(0,getWidth(pic)/2):
    for y in range(0,getHeight(pic)):
      pL = getPixel(pic,x,y)  #get pixel object on the right
      cc = getColor(pL)  #copy the color of pixels on the right
      pR = getPixel(pic,(getWidth(pic)-x-1),y) #get pixel object on the left
      setColor(pR,cc)   # set pixel object on the right to the color of pixel object on the left
  return pic
###############  
def betterBnW():
  pic = get_pic()
  pixels = getPixels(pic)
  
  for p in pixels:
    newColor = makeColor((getRed(p)*0.299 + getGreen(p)*0.587 + getBlue(p)*0.144))
    setColor(p, newColor)
  return pic
######################
def rotatePic(): 
  oldPic = get_pic()
  
  newPic = makeEmptyPicture(getHeight(oldPic),getWidth(oldPic))
  for x in range(0, getWidth(newPic)): 
    for y in range(0, getHeight(newPic)): 
      setColor(getPixel(newPic,x,y),getColor(getPixel(oldPic,getWidth(oldPic)-y-1,x)))
  #print2screen(newPic)
  #writePictureTo(newPic, "C://Users/Patri/Desktop//rotatePicResults.jpg") 
  return newPic
  
  ##############################
def roseGlass():
  pic = get_pic()
  pixels = getPixels(pic)
  
  pink_color = makeColor(255,102,255)   # creates the color pink
  
  for p in pixels:
    orig_color = getColor(p)  
    setColor(p, orig_color + pink_color)    #adds the color pink ontop of each original pixel colors
   # repaint(pic)
  return(pic)
 ######################################33
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
    
  #repaint(pic) 
  return(pic)

#Problem 2
#uses your copy function and your image manipulation functions from the last few labs to create a photo collage that fills your new blank image and:
#Contains at least 8 photos
#At least 5 of the photos should be modified in some way using some of your image manipulation functions from previous labs (black and white, rotated, lightened, you pick!)
#Fills the new image 

def makeCollage():
  collage = canvas(2550,3300)
  
  #picture 1
  print "Pic 1:"
  pic1 = betterBnW()
  pyCopy(pic1,collage,0,0)
  
  #picture 2
  print "Pic 2:"
  pic2= mirrorY()
  pyCopy(pic2,collage,850,0)
  
  #picture 3
  print "Pic 3:"
  pic3 = get_pic()
  pyCopy(pic3,collage,1700,0)
  
  #picture 4
  print "Pic 4:"
  pic4 = makeNegative()
  pyCopy(pic4,collage,0,1100)
  
  #picture 5
  print "Pic 5:"
  pic5 = get_pic()
  pyCopy(pic5,collage,850,1100)
  
  #picture 6
  print "Pic 6:"
  pic6 = QuadMirror()
  pyCopy(pic6,collage,1700,1100)
  
  #picture 7
  print "Pic 7:"
  pic7 = get_pic()
  pyCopy(pic7,collage,0,2200)
  
  #picture 8
  print "Pic 8:"
  pic8 = roseGlass()
  pyCopy(pic8,collage,850,2200)
  
  #picture 9
  print "Pic 9:"
  pic9 = rotatePic()
  pyCopy(pic9,collage,1700,2200)
  
  writePictureTo(collage, "C://Users/Patri/Desktop//CollageResult.jpg")
  return collage
  
  
  
  
  