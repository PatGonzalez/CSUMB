#Patrick Gonzalez
#Midterm: CSUMBy filter

#This filter will take a selfie image and will replace the pixels in the top right to that of an image of the CSUMB logo. 
#Then replace the background of the logo with that of the selfie. 
#Then ask the user to type in their graduating year to write in the bottom of the image with a gold backdrop.  
def CSUMBy():
  #CSUMB logo Image
  logo =  makePicture(pickAFile())
  #Selfie Image
  selfie =  makePicture(pickAFile()) 
  
  #replace the background of the logo with that of the selfies right corner of the image
  newLogo = greenScreen(logo,selfie)
 
  #replace the right coroner of the selfie with the new logo that has the respective backdrop
  for x in range(0, getWidth(newLogo)):
    for y in range(0,getHeight(newLogo)):
      c = getColor(getPixel(newLogo,x,y)) #copies the color of the pixel of the logo
      p = getPixel(selfie,x,y) #points to the location of the selfie to replace
      setColor(p,c)
      
  #add a golden backdrop for the graduation year message to go over
  selfie = backDrop(selfie)
  
  #Input the graduating year message
  selfie = askNwriteQuestion(selfie)
 
  repaint(selfie)
  show(selfie)
  writePictureTo(selfie, "C://Users/Patri/Desktop//CSUMByReulst.jpg") 
  
  
  
#replace the background of the logo with that of the selfie
#Patameters: greenPic is the picture with the green backgraound that we are going to replace
#            picBkg is the background of the image the will take place of the green pixels in greenPic
def greenScreen(greenPic,picBkg):
   #bkColor = makeColor(0,0,0)
   for x in range(0, getWidth(greenPic)):
    for y in range(0, getHeight(greenPic)):
      px = getPixel(greenPic, x, y)
      pxBG = getPixel(picBkg, x, y)
      color = getColor(px)
      colorBG = getColor(pxBG)
      if distance(color, white) < 200.0:
        setColor(px, colorBG) 
   return greenPic
 
 
#ASk the user what is there graduating year
#  If they input anything but an integer ask the question again
#Then write the message on to the bottom of the pic  
#Parameters: pic is the pic that the message will be written on
def askNwriteQuestion(pic):
  #Question
  while True:
    try: 
      year = int(raw_input("Enter your graduating year:"))
    except ValueError:
      print "Sorry you didnt enter a graduating year."
    else:
      break
  #Write message    
  message = "Class of %s" %(year)
  FontColor = makeColor(0,25,50)
  import java.awt.Font as Font
  custFont = makeStyle("Georgia", Font.BOLD, 80)
  addTextWithStyle(pic,(getWidth(pic)-508)/2,getHeight(pic)-22,message,custFont,FontColor)
  
  return pic
  
#add a golden backdrop for the graduation year
def backDrop(pic):
  color = makeColor(115,102,55)
  addRectFilled(pic,0,getHeight(pic)-100,getWidth(pic),getHeight(pic),color)
  return pic