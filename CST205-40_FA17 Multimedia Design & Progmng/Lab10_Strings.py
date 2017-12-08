#Lab 10
#Chris Holmes
#Chris Buckey
#Patrick Gonzalez

def WarmUp():
  name = requestString("What is your name?")
  print name
  
  while True:
    string = requestString("Enter a string:")
    if string == "stop":
      break
    print string
#####################################################################    
    
def hangMan():
  print "Lets Play Hangman"
  print "There is a secert word you have to guess."
  print "You have 6 chances to guess one of the letters in the seceret word."
  print "Good Luck!"
  
  
  #This array holds all the guessed letters
  incorrect = []
  #This variable counts the number of attempts
  attempts = 6
  
  #The secret word to be guessed
  theWord = "sharks"
 
  #An array of blank Spaces
  # That will show the correct guesses
  #blankWord = [u'\u005F']*len(theWord)
  blankWord = ['_']*len(theWord)
  
  #This loop asks the user for the guessed letter
  # keeps looping until the user has reached the alloted number of guess attempts
  while attempts > 0:
    print "You have %s guesses" %attempts
    print"Here is what you got so far:"
    print blankWord
    
    #Ask for a guessed letter from the user 
    guess = requestString("Guess a letter: ").lower()
    while true:
       #Check if the guess is a letter
       if guess.isalpha() == False:
           guess = requestString("Letters only.  Please try again: ").lower()
       #Check if the guess has been guessed already
       if guess in incorrect:
         guess = requestString("You guessed that already.  Please try again: ").lower()
       #Check if the user enters one letter at a time
       if len(guess) !=1:
         guess = requestString("Only one at a time.  Please try again: ").lower()
       else:
         break
    
    #Is the guess letter in the seceret word
    if guess in theWord:
      #Then find the index of the correct guess in the seceret word
      for i, correct in enumerate(theWord):
        #When you find the index of where the guess letter belongs in the secerte word
        if guess == correct:
          #Then assign the guessed letter to the matching index of the secerte word to 
          #  that of the blankWord array to show to the user what they have guessed correctly 
          blankWord[i] = guess 
          #Turns the array of charecters into a string to check agaisnt the secret word
          temp = ''.join(blankWord)
          #Checks to see if the user has guessed all the letters so far
          if temp == theWord:
            return "That is right, the seceret word is %s!" %(temp)
    #When the user guess the letter wrong:
    #  attach the incorrect guessed letter to the incorrect array
    #  decrease attempt to let the user know how many attempts they have left 
    else:
        incorrect.append(guess)
        attempts -=1
        print "You guessed: "
        print incorrect
  print "HangMan!"
   
        
         
        
  
  
