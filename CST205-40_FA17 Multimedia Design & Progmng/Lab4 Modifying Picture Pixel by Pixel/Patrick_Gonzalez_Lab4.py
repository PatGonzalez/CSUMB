# Patrick Gonzalez
# CST 205 Fall B '17
# Lab #4 Modifying Pictures Pixels by Pixels
#
#
#This Function allows user to selcet an file and makes it a usable image in JES
def get_pic():
  return makePicture(pickAFile())
  
# This function prints to screen an images that is passed to it
def print2screen(pic):
  show(pic)

#Problem 1
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
  repaint(pic)
  writePictureTo(pic, "C://Users/Patri/Desktop//mirrorXresult.jpg") 
  
# This function mirrors an image down the middle along the x-axis top-to-bottom
def mirrorX():
  pic = get_pic()
  
  #This loop copies the top half of the image to the bottom half
  for x in range(0,getWidth(pic)):
    for y in range(0,getHeight(pic)/2):
      pU = getPixel(pic,x,y)  #get pixel object on the upper half
      cc = getColor(pU)  #copy the color of pixels on the upper half
      pL = getPixel(pic,x,(getHeight(pic)-y-1)) #get pixel object on the bottom half
      setColor(pL,cc)   # set pixel object on the upper half to the color of pixel object on the bottom half
  repaint(pic)
  writePictureTo(pic, "C://Users/Patri/Desktop//mirrorYresult.jpg")
  
# This function mirrors an image down the middle along the x-axis bottom-to-top
def mirrorX2():
  pic = get_pic()
  
  #This loop copies the bottom half of the image to the top half
  for x in range(0,getWidth(pic)):
    for y in range(getHeight(pic)/2, getHeight(pic)):
      pL = getPixel(pic,x,y)  #get pixel object on the bottom half
      cc = getColor(pL)  #copy the color of pixels on the bottom half
      pU = getPixel(pic,x,(getHeight(pic)-y-1)) #get pixel object on the top half
      setColor(pU,cc)   # set pixel object on the upper half to the color of pixel object on the bottom half
  repaint(pic)
  writePictureTo(pic, "C://Users/Patri/Desktop//mirrorX2result.jpg")
  
#This function mirrors an image down the middle along the y-axis left-to-right and then along the x-axis
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
  repaint(pic)
  writePictureTo(pic, "C://Users/Patri/Desktop//QuadMirrorResult.jpg")
  
# Problem 2
def simplePic():
  mypic = makeEmptyPicture(100,100)
  for x in range(0, getWidth(mypic)):
    for y in range(0, getHeight(mypic)):
      setColor(getPixel(mypic,x,y),blue)
  show(mypic)
  return mypic
  
  
    
# This functions takes a picture as a parameter,
# creates a new blank picture and copies the picture into it. 
# Then returns the new picture
def simpleCopy(oldPic):
  newPic = makeEmptyPicture(getWidth(oldPic), getHeight(oldPic))
  for x in range(0, getWidth(newPic)): 
    for y in range(0, getHeight(newPic)):
      setColor(getPixel(newPic,x,y),getColor(getPixel(oldPic,x,y)))
  show(newPic)
  writePictureTo(newPic, "C://Users/Patri/Desktop//simpleCopyResults.jpg") 
  return newPic
  
  
  
# Problem 3
#This function will create a copy of a picture,
# then rotate it 90 degrees to the left,
# and return the rotated picture from the function
def rotatePic(): 
  print"Choose a picture file: "
  oldPic = get_pic()
  
  newPic = makeEmptyPicture(getHeight(oldPic),getWidth(oldPic))
  for x in range(0, getWidth(newPic)): 
    for y in range(0, getHeight(newPic)): 
      setColor(getPixel(newPic,x,y),getColor(getPixel(oldPic,getWidth(oldPic)-y-1,x)))
  print2screen(newPic)
  writePictureTo(newPic, "C://Users/Patri/Desktop//rotatePicResults.jpg") 
  return newPic
  
  
  
# Problem 4
#This functions Makes a copy of a picturethat is hald as big as the original.
def shrink():
  print"Choose a picture file: "
  OGPic = get_pic()
  
  smlPic = makeEmptyPicture(getWidth(OGPic)/2,getHeight(OGPic)/2)
  
  for x in range(0, getWidth(OGPic),2):
    for y in range(0,getHeight(OGPic),2):
      p = getPixel(smlPic,x/2,y/2)    #points to the pixel of the smaller frame
      #Divides x,y by 2 to point to composate for incrementing by 2
      c = getColor(getPixel(OGPic,x,y))  #points to the color of the pixel of the original image
      setColor(p,c)
  print2screen(smlPic)
  writePictureTo(smlPic, "C://Users/Patri/Desktop//shrinkResult.jpg") 
  return smlPic
  
  
  
  
  
  
  
  
  
  
  
  
  
  