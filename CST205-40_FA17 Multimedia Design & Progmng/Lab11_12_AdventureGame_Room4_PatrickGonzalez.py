#room 4 
#The room of questionnaire
#By Patrick Gonzalez

########################################################################### 
#Enter room 4 function
#######################################################################
def room4():
  d = direction()#Holds the array of all possible commands
  #Intro to the room
  printNow("------The Room of Questionnaire------")
  printNow ("There are no other doors in the room except the one behind you, but there is a strange mirror..")
  # Ask for user activity
  activity = ""
  activity = raw_input("Do you want to inspect the mirror further or head back the way you came?").lower()
  #Test the input from the user
  while true:
    #Check if the input is a letter
    if activity.isalpha() == False:
      activity = raw_input("Do you want to inspect the mirror further or head back the way you came?").lower()
    #Check if the guess asked for help
    if activity == 'help':
      helpMenu()
      activity = raw_input("Do you want to inspect the mirror further or head back the way you came?").lower()
    #Check if the user entered a proper command
    if activity not in d:
        print("That wasn't what I was expecting.")
        activity = raw_input("Do you want to inspect the mirror further or head back the way you came?").lower()
    #If they did input a proper command then move on to what they want to do 
    if activity in d:
      #print("Flag: activity in d")
      break
      
  # Once you have checked if the user input a proper command move on to the next step 
  if activity == 'bk':
    room1()  #input the function definition call to room 1
  elif activity == 'exit':
        print("Death is your only escape! \m/")
  elif activity == 'yes' or activity =='y':
      #print("Flag: They said yes inspect the mirror")
      #The player gets the chance to solve the mysterious quote
      mystery = hangMan() #If they pass the hangMan function it will return 'solved' otherwise it return 'incorrect'
      #If they solved the quote correctly they have the choice to enter the secret room or not
      if mystery == 'solved':  
        printNow("You you solved the mysterious quote")
        printNow("The mirror swings open leading to another room")
        decision = raw_input("Do you enter the room? (y/n)").lower()
        while true:
          #Check if the input is a letter
          if decision.isalpha() == False:
            decision = raw_input("Do you enter the room? (y/n)").lower
          #If they said yes to entering the room take them to secretRoom function
          if decision == 'yes' or decision =='y':
            #print "Flag: Yes enter the secret room"
            return secretRoom()
          #If they said no to entering the room take them to the begining of room4 function
          if decision == 'no' or decision =='n':
           # print "Flag: No do not enter the secret room"
            return room4()
          else:
            printNow("You didnt enter yes or no")
            decision = raw_input("Do you enter the room? (y/n)").lower
      elif mystery == 'incorrect':
        printNow("You didnt solve the mysterious quote, lets start over.")
        return room4()    
  elif activity == 'no' or activity =='n':
    printNow("What to do...?")
    return room4()
#######################################################################
#All other function
#############################################
#Help Menu
def helpMenu():
  printNow("This is the help menu")
  
  
#an array to hold all the direction to check if the user entered a proper commmand  
def direction():
  d = ['fd','bk','lt','rt','pu','it','op','use','yes','y','no','n','exit']
  return d


#to check if the room4 function calls to room 1 properly
def room1():
  return printNow("You made it back to room 1")

#function for the secret room
def secretRoom():
  print "You have entered the secret room"

####################################
# This ask the user to solve the blank in the mirror
#The rules are the same as hangman with 6 tries
#return 'solved' if they answer correctly
#return 'inccorect' if they answere wrong
  
def hangMan():
  print "Upon further inspection of the mirror you see a quote:"
  print "What dosn't kill you only makes you stronger, except for ______, they will definitly kill you."
  print "What do you suppose will definitly kill you?"
  
  
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
            print "interesting... it says, What dosn't kill you only makes you stronger, except for sharks, they will definitly kill you."
            return 'solved'
    #When the user guess the letter wrong:
    #  attach the incorrect guessed letter to the incorrect array
    #  decrease attempt to let the user know how many attempts they have left 
    else:
        incorrect.append(guess)
        attempts -=1
        print "You guessed: "
        print incorrect      
  return 'incorrect'