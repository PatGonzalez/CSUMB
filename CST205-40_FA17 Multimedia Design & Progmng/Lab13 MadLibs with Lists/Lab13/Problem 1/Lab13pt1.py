#Christopher Holmes
#Patrick Gonzalez
#Lab 13 Problem 1

#Original text of the news story
try:
    fin = open('Mario_NewsArticle.txt')
except:
    print("Something went wrong opening the file.")
    
#Madlibbed file to be written to
try:
    fout = open('MadLibbed_Mario_NewsArticle.txt', 'w')
except:
    print("Something went wrong opening the file.")

#Read in the file    
originalParagraph = fin.read()


#List to hold each individual word from the paragraph
words = originalParagraph.split()

#Lists to hold the answers the user gives and the questions provided to the user    
userAnswers = []
questions = ["adjective","noun","flavor","flavor","flavor","adjective","adjective","adverb","adjective","plural noun","noun"]

#Loop to get answer to each question
for question in questions:    
    userAnswers.append(raw_input("Enter a %s: "%question))

#Loop to insert the user supplied answers over original word. The index of the word being replaced is hard coded, and the userAnswer is pulled from the list
for i, word in enumerate(words):
    if i == 20:
        words[i] = userAnswers[0]
    elif i == 33:
        words[i] = userAnswers[1]
    elif i == 55:
        words[i] = userAnswers[2]
    elif i == 59:
        words[i] = userAnswers[3]
    elif i == 67:
        words[i] = userAnswers[4]
    elif i == 68:
        words[i] = userAnswers[5]
    elif i == 108:
        words[i] = userAnswers[6]
    elif i == 130:
        words[i] = userAnswers[7]
    elif i == 160:
        words[i] = userAnswers[8]
    elif i == 171:
        words[i] = userAnswers[9]
    elif i == 213:
        words[i] = userAnswers[10]
    

#Write out the finished Madlid to the file that was opened in the begining
for word in words:
    fout.write(word+" ")
    
#Close both of the files that we opened at the begining
fout.close()
fin.close()
    
#Loop to get the index number of each of the words in the paragraph
#for i, word in enumerate(words):
#    print "Index: %s Word: %s"%(i,word)