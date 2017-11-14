#Lab 7
#Team Socal Betawares
#Patrick Gonzalez
def get_pic():
  return makePicture(pickAFile())
  
def snowMan(message, x, y):
  # get the picture
  pic = get_pic()
  
  # add the message to the picture
  import java.awt.Font as Font
  custFont = makeStyle("Arial", Font.BOLD, 40)
  addTextWithStyle(pic, x, y, message, custFont, white)
  
  # create the snowman - 3 ovals, filled with white
  # 2 black eyes, 1 orange nose
  # #1 - 60px, #2 - 80px, #3 - 100px - total height 240px, radius 50px 
  # #1 add the facial features
  # find the middle of the picture
  width = getWidth(pic)
  height = getHeight(pic)
  
  startX = width/2
  startY = height - 240
  
  addOvalFilled(pic, startX-30, startY, 60, 60, white)
  addOvalFilled(pic, startX-15, startY+20, 10, 10, black)
  addOvalFilled(pic, startX+5, startY+20, 10, 10, black)
  addOvalFilled(pic, startX-7, startY+30, 14, 14, orange)
  addOvalFilled(pic, startX-40, startY+60, 80, 80, white)
  addOvalFilled(pic, startX-50, startY+140, 100, 100, white)
  #addOvalFilled(pic, startX
  show(pic)


def shrink(picture):
  width = getWidth(picture)
  height = getHeight(picture)
  newwidth = width/2
  newheight = height/2
  
  newpic = makeEmptyPicture(newwidth, newheight)
  
  for x in range(0, width, 2):  # in increments of x+2
      for y in range(0, height, 2):  # in increments of y+2
          oldPixel = getPixel(picture, x,y)  # get the pixel from the original picture
          newPixel = getPixel(newpic, x/2, y/2)  # get the pixel from the new picture
          color = getColor(oldPixel)  # get the color of the old picture's pixel
          setColor(newPixel, color)  #insert the color from the old picture into the new picture
  return newpic   

def pyCopy(source, target, targetX, targetY):    
    width = getWidth(source)
    height = getHeight(source)
    for x in range(0, width):
        for y in range(0, height):
            pixel = getPixel(source, x, y)
            color = getColor(pixel)
            setColor(getPixel(target, targetX+x, targetY+y), color)  # copy the other picture, pixel by pixel
    return target
    
def message(pic, msg):
  import java.awt.Font as Font
  custFont = makeStyle("Magneto", Font.BOLD, 50)
  addTextWithStyle(pic, 0, 100, msg, custFont, white)

def ThanksGiving():
  print "Please select the turkey picture"
  pic =  makePicture(pickAFile())  #greenscreen picture
  #shrink(pic)
  print "Select your background"
  picBG =  makePicture(pickAFile())  # background
  print "Select your family photo"
  picFP = makePicture(pickAFile())  #family photo
  print "Select pet photo"
  picFP2 =  makePicture(pickAFile()) # Pets Photo
  
  pyCopy(picFP, picBG, (getWidth(pic)-getWidth(picFP)), 100)  # copy the family picture to the background
  pyCopy(picFP2, picBG, (getWidth(pic)-getWidth(picFP2)), 400) #copy the pet photo to the background+family
  
  for x in range(0, getWidth(pic)):  #green screen effect
    for y in range(0, getHeight(pic)):
      px = getPixel(pic, x, y)
      pxBG = getPixel(picBG, x, y)
      color = getColor(px)
      colorBG = getColor(pxBG)
      if distance(color, green) < 200.0:
        setColor(px, colorBG)
  
  message(pic,"Happy Thanksgiving") # print the message
  #explore(pic)
  show(pic)
  writePictureTo(pic, "C://Users/Patri/Desktop//ThanksGivingCard.jpg")


    