#Christopher Holmes
#Patrick Gonzalez
#

#Import the libraries needed to run this program.
#urllib required for getting the url
#os required to be able to output the file to the location that the script is running
import urllib
import os

#Function definition to make an HTML page that takes in one parameter, list
def makePage(list):
    #Path is the path to where the python script is being run from, with the file name at the end of it.
    #path = os.path.join(os.getcwd(), 'pythonWebPage-2.html')
    path='C:\Users\Patri\Desktop\CSUMB\CST205-40_FA17 Multimedia Design & Progmng\Lab16 URLs and HTML\pythonWebPage_Lab16.html'
    #Open the file with write permission
    file = open(path, "wt")
    #Begin the writting of the HTML file.
    file.write("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 
  Transition//EN" "http://www.w3.org/TR/html4/loose.dtd">
  
  <html>
  <head><title>I made this page with Python!</title>
  </head>
  <body>
  <h1>Patrick Gonzalez and Chris Holmes PYTHON PAGE!!!</h1>""")
    #Inject our specific headlines that we have that are passed in from the list
    for line in list:
        string = "<h2>%s<h2>"%line
        file.write(string)
    file.write("""</body>
  </html>""")
    file.close()
def scraping():
  #Link to where to get the HTML code from
  link = "https://news.google.com"
  #Open the link and store it in a variable
  f = urllib.urlopen(link)
  #Read the HTML line by line to be able to iterate over it
  myfile = f.readlines()
  #Count variable to see how many variables have been grabbed
  count = 0
  #List to store the headlines we find
  parsedlines=[]
  #Loop through each line of the HTML file
  for line in myfile:
      #Since we don't want every headline, we limit it to 20
      if count < 20:
          #Look for the word heading in the line because that was present in each line that had a headline
          if "heading" in line:
              #Add the line if it contains heading and increment the count by 1
              parsedlines.append(line)
              count += 1
            
  #List to store the parsed headlines in text form
  headlines = []
  #Iterate over each item in the parsedlines list
  for line in parsedlines:
      #Find the index of the line for where the text starts that we want to grab
      startIndex = line.rfind("aria-level=\"2\"")+16
      #Find the index of where to stop grabbing from the line
      endIndex = line.find("</a>", startIndex)
      #Grab the actual text using the headlines
      headline = line[startIndex:endIndex]
      #See if the two phrases are not in the line as they aren't true headlines, and if they aren't add to list
      if "jsname=" not in headline or "jsmodel" not in headline:
          headlines.append(headline)

  #Call the makePage function with the list passed in
  makePage(headlines)