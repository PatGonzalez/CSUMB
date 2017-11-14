#Patrick Gonzalez
#Midterm CSUMBy filter

def CSUMBy():
  #CSUMB logo Image
  logo =  makePicture(pickAFile())
  #Selfie Image
  selfie =  makePicture(pickAFile())
  
  # Blue tint glasses
  #Glasses = makeColor(240,255,255)
  #for p in getPixels(selfie):
  #  origPic = getColor(p)
   # setColor(p,origPic+Glasses)
    
  #replace the background of the logo with that of the selfie
  #bkColor = makeColor(0,0,0)
  for x in range(0, getWidth(logo)):
    for y in range(0, getHeight(logo)):
      px = getPixel(logo, x, y)
      pxBG = getPixel(selfie, x, y)
      color = getColor(px)
      colorBG = getColor(pxBG)
      if distance(color, white) < 200.0:
        setColor(px, colorBG) 
  
  #replace the right coroner of the selfie with the new logo 
  for x in range(0, getWidth(logo)):
    for y in range(0,getHeight(logo)):
      c = getColor(getPixel(logo,x,y)) #copies the color of the pixel of the logo
      p = getPixel(selfie,x,y) #points to the location of the selfie
      setColor(p,c)
      
  #add a golden backdrop for the graduation year
  color = makeColor(115,102,55)
  x = getWidth(selfie)-155
  y = getHeight(selfie)-155
  addOvalFilled(selfie, x, y, 150, 150, color)
  
  #Add the graduating year to the bottom right corner
  x = getWidth(selfie)-120
  y = getHeight(selfie)-60
  message = "'19"
  FontColor = makeColor(0,25,50)
  import java.awt.Font as Font
  custFont = makeStyle("Sarif", Font.BOLD, 80)
  addTextWithStyle(selfie,x,y,message,custFont,FontColor)
  
  explore(selfie)
  #show(selfie)