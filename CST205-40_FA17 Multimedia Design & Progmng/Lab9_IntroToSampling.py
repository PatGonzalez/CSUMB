#Lab 9
#Patrick Gonzalez

#Make a new sound variable
def sound():
  s = makeSound(pickAFile())
  return s
#Saves a sound to desktop 
def saveSound(sound):
   writeSoundTo(sound,"C://Users/Patri/Desktop//NewSoundResult.wav")
   
###############################################################################################
#Problem 1
#This Function:
  #Make a new empty sound.
  #Once we have our empty sound, we'll want to go 
    #through each index in our source sound in the range that starts at our beginning index and ends at our ending index.
      #For each sample, we want to get the value from the source at the given index
      #And copy it to the correct location in the target. 
        #We will need to have a separate variable for the targetIndex that starts at zero and that we 
          #increment every time we are done copying a sample from the source to the target 
  #return the target sound.
#Parameters:
   #Source is the longer sound that contains our clip
   #Start is the starting index of our clip
   #End is the ending index of our clip
def clip(source, start, end):
  newSound = makeEmptySound((end-start))
  
  for i in range(start,end):
    value = getSampleValueAt(source,i)
    setSampleValueAt(newSound,i-start,value)
    
  return newSound
  
################################################################################################
#Problem 2
#copy function that will let us splice our new sound into a bigger sound
#Parameters:
  #Source is the source sound (the short clip)
  #Target is the target sound (the sound that is being made from adding clips together)
  #Start is the index in the target sound where the copy of the source should begin 
def copy(source,target,start):
  lenSource = getLength(source)
  lenTarget = getLength(target)
  
  biggerSound = makeEmptySound(lenSource+lenTarget,44100)
  
  index = 0
  for i in range(0,lenSource):
    value = getSampleValueAt(source,i)
    setSampleValueAt(biggerSound,index, value)
    index +=1
  for i in range(0,lenTarget):
    value = getSampleValueAt(target,i+start)
    setSampleValueAt(biggerSound,index, value)
    index +=1
    
  return biggerSound
#############################################################################
#Problem 3
#collage
#Use the clip and copy functions to create a sound collage that combines at 
#   least five clips from other sounds into a new sound

def soundCollage():
   #creat sound one clip
   s1 = sound()
   explore(s1)
   start = int(raw_input("Enter starting index of sound to clip"))
   end = int(raw_input("Enter ending index of sound to clip"))
   s1 = clip(s1,start,end)
   
   #create sound two clip
   s2 = sound()
   explore(s2)
   start = int(raw_input("Enter starting index of sound to clip"))
   end = int(raw_input("Enter ending index of sound to clip"))
   s2 = clip(s2,start,end)
   
   #stich sound one and two together
   collage = copy(s1,s2,0)
   
   #create sound three clip
   s3 = sound()
   explore(s3)
   start = int(raw_input("Enter starting index of sound to clip"))
   end = int(raw_input("Enter ending index of sound to clip"))
   s3 = clip(s3,start,end)
   
   #stich sound three to the collage
   collage = copy(collage,s3,0)
   
   #create sound four clip
   s4 = sound()
   explore(s4)
   start = int(raw_input("Enter starting index of sound to clip"))
   end = int(raw_input("Enter ending index of sound to clip"))
   s4 = clip(s4,start,end)
   
   #stich sound four to collage
   collage =copy(collage,s4,0)
   
   #create sound five clip
   s5 = sound()
   explore(s5)
   start = int(raw_input("Enter starting index of sound to clip"))
   end = int(raw_input("Enter ending index of sound to clip"))
   s5 = clip(s5,start,end)
   #stich sound five to the collage
   collage = copy(collage,s5,0)
   
   #save the collage to file
   #saveSound(collage)
   
   return collage
   
################################################################   
#Problem 4
#returns the sound backwards  
def reverse(sound):
  lenSound = getLength(sound)
  newSound = makeEmptySound(lenSound)
  
  for i in range(0,lenSound):
    value = getSampleValueAt(sound,i)
    setSampleValueAt(newSound,lenSound-i-1,value)
    
  return newSound