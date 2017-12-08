#Lab 14 Files In Python
#Patrick Gonzalez


    
#########################################################################################################333    
#Problem 1
#Rumor has it that the literary classic Green Eggs and Ham was written because Dr. Seuss's publisher bet him he couldn't write a book using only 50 words.  
#Write a Python program that opens the file Eggs.txt (containing the entire text of Green Eggs and Ham) and verifies this urban legend by doing the following:
#Create a count of how many total words appear in Green Eggs and Ham
#Create a count of how often each of the words appears (note that Eggs eggs Eggs! eggs? and eggs, should all be counted as the same word).  
#Print out the total count and the count for each of the words. 
#Print out the most commonly occuring word in the book

def wordCount():
  #Open the file and throw an error if the file wasnt succesfully opened. 
  try:
    fin = open('C:\Users\Patri\Desktop\CSUMB\CST205-40_FA17 Multimedia Design & Progmng\eggs.txt','r')
  except:
    return "Unable to open given file."
  #Read the eggs.tx file into a variable
  book = fin.read()
  #creat a list of all the words in eggs.txt
  words = book.split()
  #close eggs.txt file
  fin.close()
  
  #count of how many total words appear in Green Eggs and Ham/eggs.txt
  count = 0
  for word in words:
    count+=1 
  
  #count of how often each of the words appears
  repeatedWords = dict()  #Creat an empty directory
  for word in words:  
    if word not in repeatedWords:  #If word not in the directory create a new item with key word and new value of 1
      repeatedWords[word]=1
    else:                          #If word does exist in the directory increment the key word
      repeatedWords[word]+=1
     
  #Print out the total count and the count for each of the words. 
  print ("There are a total of %s words in Green Eggs and Ham."%count)
  print ("\nHere is a list of the repetead words:")
  printDict(repeatedWords)
    
  #Print out the most commonly occuring word in the book
  inverse = invert_dict(repeatedWords) #Invert the dictionary so that the values are the keys and the keys are the values
  maxKey = max(inverse)  #Find larget key 
  maxKeyValue = inverse[max(inverse)] #Get the largets keys value
  #print("\nThe most commonly used word is: ")
  #print(maxValueKey,maxValue)
  print "\nThe word %s is the most commonly used word and was used %d times."%(maxKeyValue,maxKey)
##############################################################################################
#Print a dictionary
def printDict(d):
  for key in d:
    print (key,d[key])
#######################################################################################  
#Invert a Dictionary:
#Create an empty dictionary.
#Each time through the loop key gets a key from d and val gets the corresponding value.
#If val is not in inverse, that means we havnet seend it before, so we create a new item and intialize it with a singleton(a list that contains a single element).
#Otherwise we have seen this value before, so we append the corresponding key to the list.  
def invert_dict(d):
  inverse = dict() 
  for key in d:
    val = d[key]
    if val not in inverse:
      inverse[val] = [key]
    else:
      inverse[val].append(key)
  return inverse

################################################################################################################################
#Problem 2
#pull the headlines from the CSU news webpage: https://www2.calstate.edu/csu-system/news
#Then open the file in JES 
#Use string processing techniques to extract the headlines from the paper.
def html2txt():
  #Open the file and throw an error if the file wasnt succesfully opened. 
  try:
    fin = open('C:\Users\Patri\Desktop\CSUMB\CST205-40_FA17 Multimedia Design & Progmng\News.html','r')
  except:
    return "Unable to open given file."
    
  #Read each line of the file into a variable
  html = fin.readlines()
  
  #To hold the full story line in the html file
  storyLine = []
  
  #To hold just the headline text of the html from from the storyLine list
  headLines = []
  
  #close file
  fin.close()
  
  #Capture all the lines in the html that contain the key word story or press release
  for line in html:
    if "Story" in line or "Press Release" in line:
      storyLine.append(line)
  for line in storyLine:
    startIndex = line.rfind("<h2>")+4
    endIndex = line.find("</h2>")
    headLine = line[startIndex:endIndex]
    if "<div" not in headLine and "</a>" not in headLine and headLine not in headLines:
      headLines.append(headLine)
      
  print "-----CSU Breaking News!-----"
  for i in headLines:
    print i
  #print words
  
 