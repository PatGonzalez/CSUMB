#Mini-Lab: Adding on to the HTML Lab
#Patrick GOnzalez

#########################################################################################################333    
# Green Eggs and Ham Word Count Problem from Lab 14
#Rumor has it that the literary classic Green Eggs and Ham was written because Dr. Seuss's publisher bet him he couldn't write a book using only 50 words.  
#Write a Python program that opens the file Eggs.txt (containing the entire text of Green Eggs and Ham) and verifies this urban legend by doing the following:
#Create a count of how many total words appear in Green Eggs and Ham
#Create a count of how often each of the words appears (note that Eggs eggs Eggs! eggs? and eggs, should all be counted as the same word).  
#Print out the total count and the count for each of the words. 
#Print out the most commonly occuring word in the book

def HtmlWordCount():
  #Open the file and throw an error if the file wasnt succesfully opened. 
  try:
    fin = open('C:\Users\Patri\Desktop\CSUMB\CST205-40_FA17 Multimedia Design & Progmng\eggs.txt','r')
  except:
    return "Unable to open given file."
  #Read the eggs.tx file into a variable
  book = fin.read()
  #creat a list of all the words in eggs.txt
  diffWords = book.split()
  #close eggs.txt file
  fin.close()
  
  #count of how many total words appear in Green Eggs and Ham/eggs.txt
  count= len(book.split())
  
  #Change all the word to lower case
  words=[]
  for i in diffWords:
    words.append(i.lower())
  
  #count of how often each of the words appears
  repeatedWords = dict()  #Creat an empty directory
  for word in words:  
    if word not in repeatedWords:  #If word not in the directory create a new item with key word and new value of 1
      repeatedWords[word]=1
    else:                          #If word does exist in the directory increment the key word
      repeatedWords[word]+=1
     
  #Print out the total count and the count for each of the words. 
  #print ("There are a total of %s words in Green Eggs and Ham."%count)
  #print ("\nHere is a list of the repetead words:")
  #printDict(repeatedWords)
    
  #Print out the most commonly occuring word in the book
  inverse = invert_dict(repeatedWords) #Invert the dictionary so that the values are the keys and the keys are the values
  maxKey = max(inverse)  #Find largest key 
  maxKeyValue = inverse[max(inverse)] #Get the largets keys value
  
  #invert again the dictionary again
  #inverse2nd = invert_dict(inverse)
  
  #print("\nThe most commonly used word is: ")
  #print(maxValueKey,maxValue)
  #print "\nThe word %s is the most commonly used word and was used %d times."%(maxKeyValue,maxKey)
  
  makePage(inverse,count,maxKeyValue,maxKey) 
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

#################################################################################################
#Function definition to make an HTML page that takes in one parameter, list
def makePage(d,count,maxKeyValue,maxKey):
    #Path is the path to where the python script is being run from, with the file name at the end of it.
    #path = os.path.join(os.getcwd(), 'pythonWebPage-2.html')
    path='C:\Users\Patri\Desktop\CSUMB\CST205-40_FA17 Multimedia Design & Progmng\GreenEggsAndHam_WebPage.html'
    #Open the file with write permission
    file = open(path, "wt")
    #Begin the writting of the HTML file.
    file.write("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 
  Transition//EN" "http://www.w3.org/TR/html4/loose.dtd">
  
  <html>
  <head><title>I made this page with Python!</title>
  </head>
  <body>
  <p style="color:#339900; font-size:50px; font-weight:bold">Green Eggs and Ham Word Count!</p>
  """)
    #Inject our specific headlines that we have that are passed in from the list
    file.write("<h2>There are a total of %s words in Green Eggs and Ham.<h2>"%count)
    file.write("<h1>Here is a list of the repetead words:<h1>")
    for key, value in d.items():
        if key<12:
          file.write("""<p style='color:#C4C431; font-size:10px; font-weight:normal'>%s</p>"""%','.join(value))
        elif key<24:
          file.write("""<p style='color:#29B3A9; font-size:30px; font-weight:bold'>%s</p>"""%','.join(value))
        elif key<48:
          file.write("""<p style='color:#B36E29; font-size:60px; font-weight:normal'>%s</p>"""%','.join(value))
        else:
          file.write("""<p style='color:#5EB329; font-size:90px; font-weight:bold'>%s</p>"""%','.join(value))
    #file.write("""</body>
    file.write("<h2>\nThe word %s is the most commonly used word and was used %d times.<h2>"%(maxKeyValue,maxKey))
    file.write("""</body></html>""")
    file.close()
#############################################################################################