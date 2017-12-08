#Lab 13 Problem 2
#Patrick Gonzalez
#Christopher Holmes

import sys 
####################################################
#Global Variables

#Array holding possible direction commands
directions = ['fd','bk','lt','rt','pu','it','op','use','vw','yes','y','no','n','exit', 'help']
directionsList = ['Move Forward', 'Move Back', 'Move Left', 'Move Right', 'Pick Up', 'Interact', 'Open', 'Use', 'View', 'Yes', 'Yes', 'No', 'No', 'Exit', 'Help']

#Help Function
def helpMenu():
    printNow("This is the help menu.")
    printNow("Available choices are: ")
    #print(directions, sep=' ', end='.', flush=True)
    for i, d in enumerate(directions):
        if i == len(directions)-1:
            printNow("%s = %s."%(d,directionsList[i]))
        else:
            printNow("%s = %s, "%(d,directionsList[i]),)
  
################################################################################3
#function for entering the game
def enter():
    enterhouse = requestString("Do you want to play a game %s?  Great rewards lie inside! - press 'y' to continue: " %userName)
    if (enterhouse.lower() == "yes" or enterhouse.lower() == "y"):
        roomone()
    else:
        showInformation("Ok, bye")
####################################################################################
#Win function        
def leftHouse():
  showInformation("You made it out alive. Congrats!")

#######################################################################3
#Room 1 function by Chris Buckey
def roomone():
  #test test
  printNow ("------Main Lobby------")
  
  exitFlag = false
  
  while true:
    direction = requestString("Please choose a room (lt) will take you to The Room of The Deep, (fd) will take you to the Room of Questionnaire,\n (rt) will take you to the Locker Room, (bk) will take you back the way you entered the game, or (vw) to view the object in the center of the room: ")
    if direction == "rt":
      room2()
      break
      
    elif direction == "fd":
      room4()
      break
    elif direction == "lt":
      roomthree(1)
      break
    elif direction == "vw":
      showInformation ("Moving toward the object, you see that there is a box with a sign next to it.  The sign says IT IS DANGEROUS TO GO ALONE, TAKE ONE OF THESE!  The box is empty.")
    elif direction == 'help':
      helpMenu()
    elif direction == "bk":
      showInformation ("I am afraid you can't go back.  You must move forward")
    elif direction == "exit":
      showInformation("Exiting without finishing the game?!\n")
      exitFlag = true
      break
    else:
      showInformation ("That is not a direction, insolent fool!")
  #end while
    
  if exitFlag:
    callQuit()

  return -1
#end roomone
##########################################################################333
#Room 2 By Chrsi Holmes
def room2():
    #Tell the user about the room
    printNow("------The Locker Room------")
    printNow("This room has one door which is behind you and there is also a locker in front of you.")
    
    #Get what the user wants to do
    userActivity = requestString("Would you like to leave the way you came? ").lower()
    
    #Check the input from the user
    loopControl = true
    
    while loopControl:
        #Check to see if the user wanted the help menu printed
        if userActivity == 'help':
            helpMenu()
            userActivity = requestString("Would you like to inspect the locker further or leave the way you came? ")
        #Checks to see if the user entered a valid choice, if not, asks for another choice
        elif userActivity not in directions:
            showInformation("I'm sorry %s I can not do that"%userName)
            userActivity = requestString("Would you like to inspect the locker further or leave the way you came? ")
        #If a valid choice was entered, loopControl is set to false to break out of the loop
        else:
            if userActivity == 'help':
                break
            else:
                loopControl = false
            
    #Section to check to see which choice the user made
    #Checks if the user chose to exist the room with bk
    if userActivity == 'bk':
        #insert function call to room1 here to return to main lobby
        roomone()
    #checks to see if the user entered exit to end the game
    elif userActivity == 'exit':
        showInformation("Death is your only escape!")
        callQuit()
    elif userActivity == 'yes' or userActivity == 'y':
        showInformation("What to do now?")
        return roomone()
########################################################################################        
#Room 3 by John Seals
def roomthree(room):
  printNow("------Room of the Deep------")
  printNow("There is a poster on the left wall,  it's caption says CSUMBERIZED.\n There are also some windows to the right which look out into deep space. You can clearly distinguish several halloween decorations, obviously 2 or 3 years old.\n You see two vending machines along the left wall, a sink, a microwave and a referidgerator.  \nIt looks like some sort of intergalactic break room. There is something suspicious about the microwave, you get the feeling that it is making fun of you somehow.""")
  #Test to find out which room the player just came from
  if room == 1:
    x = 1
    y = 0
  if room == 5:
    x = 1
    y = 4
    
  p = 0
  nextRoom = 0
  userInput = ""
  hasCoin = false
  hasScrewdriver = false
  while userInput != 'exit':
    #userInput = requestString("Enter command: ") 
    userInput = requestString("Enter command - fd, lt, rt, bk, op: ")
    
    #move commands
    if userInput == "fd":
      if y < 4:
        y = y + 1
        printNow("You move forward one space. ")
      elif y == 4:
        printNow("You can't move any further in that direction.  ")
  
    elif userInput == "bk":
      if y > 0:
        y = y - 1
        printNow("You move backward one space. ")
      elif y == 0:
        printNow("You can't move any further in that direction. ")  
    
    elif userInput == "lt":
      if x > 0:
        x = x - 1
        printNow("You move left one space. ")
      elif x == 0:
        printNow("You can't move any further in that direction. ")  
      
    elif userInput == "rt":
      if x < 2:
        x = x + 1
        printNow("You move right one space. ")
      elif x == 2:
        printNow("You can't move any further in that direction.  ")
    
    elif userInput == "lb":
      if p < 2:
        printNow("There is nothing behind you. ")
      elif 2 <= p and p < 4:
        printNow("Nobody's following you. ")
      elif p >= 4:
        printNow("You're PARANOID %s! "%userName)
      p = p + 1  
    
    #pick up commands
    elif userInput == "pu":
      if x == 2 and y == 4:
        printNow("You pick up a handful of coins thinking smugly, these will come in handy later. ")
        hasCoin = true
      if x == 2 and y == 3:
        printNow("You wonder how someone could leave a useful tool such as this behind, you pick it up and wield it carefully.")
      else:
        printNow("There is nothing to pick up here. ")
    
    #open commands, used only for opening doors
    elif userInput == "op":
      if x == 1 and y == 4:
        showInformation("You have opened the door to a room that looks like a shrine. ")#take you to room 5
        #reply = requestString("Do you wish to walk through the door? ")
        reply = requestString('Do you wish to walk through the door? ')
        if reply == 'yes' or reply == 'y':
          #nextRoom = 5
          room5()
          #break
      elif x == 1 and y == 0:
        showInformation("You have opened the door to the Main Lobby. ")#take you to room 1
        #reply = requestString("Do you wish to walk through the door? ")
        reply = requestString('Do you wish to walk through the door? ')
        if reply == 'yes' or reply == 'y':
          #nextRoom = 1
          roomone()
          #break
      else:
        showInformation("I'm sorry %s I can not do that"%userName)
    
    #interact commands    
    elif userInput == "it":
      if x == 0 and y == 2:
        printNow("There is nothing in the referidgerator, although there are several colorful magnets and a post it note that says 'feed me'. ")
      if x == 2 and y <= 1:
        printNow("In the bottom corner of the room there is a pinball machine, you can just make out the lettering on the faded backboard, it says 'Dirty Harry'.  You would love to play the game but it looks like it's out of order.")
      if x == 2 and y >= 3:
        printNow("There is a table in the upper right corner of the room surrounded by chairs, some of which have been tipped over. The table is barren, except for a small pile of change near the top edge of the table and a screwdriver laying on it's side towards the bottom end of the table.")
      if x == 0 and y == 1:
        printNow("There is a change machine here. It accepts $1 and $5 bills. ")
      if x == 0 and y == 4:
        printNow("The soda machine looks to be in good working condition.  On the front, in big bold letters it says 'Enjoy Flavo-Bev Cola Today!'. Unfortunately, all the flavors are sold out...with the exception of diet, caffeine free cola.  The dollar bill acceptor is severly damaged, it looks as if someone has mangled it with some sort of hand held tool.")  
      if x == 0 and y == 3:
        printNow("The snacks look overpriced, and not very healthy, better just get something to drink instead.")
      if ((x == 0 and y == 0) or x == 1) or (x == 2 and y == 2):
        printNow("I'm sorry %s I can not do that"%userName)
      if x == 2 and y == 2:
        printNow("There is a comfortable looking couch here. ")  
    
    #use commands    
    elif userInput == "use":
      if x == 2 and y <= 1:
        printNow("You would love to play the pinball machine, but it appears to be out of order. ")
      if x == 2 and y == 2:
        printNow("You lay on the couch, somehow you feel much better about everything. ")
      if x == 0 and y == 1:
        printNow("You put a dollar into the change machine but nothing changes. ")
      if x == 0 and y == 4:
        if hasCoin == true and hasScrewdriver == true:
          printNow("You cram the screwdriver into the bill acceptor, it looks like this has been done several times before.You then put a coin into the machine and twist the screwdriver...there is a sound, like some kind of horrible malfunction... then you look below you...oh dear, instead of diet crappy flavor soda, a small, solid gold otter pops out from the machine, Eureka! YOU'RE RICH! Wait, it's only gold foil...as it turns out, this is a chocolate otter wrapped in gold foil.  Mmmm tasty chocolate.")
        if hasCoin == true and hasScrewdriver == false:
          printNow("You put several coins into the machine. There is a muffled bang...you look below you to find a nice, cold can of soda.  It tastes terrible.  ")
        if hasCoin == false:
          printNow("You don't have any change.")
      if (x == 0 and y == 0) or (x == 0 and (y == 2 or y == 3)) or x == 1 or (x == 2 and (y == 3 or y == 4)):   
        printNow("There is nothing to use here. ")
    
    #give the player a hint      
    elif userInput == "hint":
      showInformation("If you're thirsty, have a drink.  There is a pile of coins on the table.  Rumor has it that strange treasures are known to come out of the soda machine, with a little help...")          
    
    #display the list of commands that pertain to this specific room 
    elif userInput == "help":
      printNow("Here is the list of commands: To pick up type 'pu', To interact/look type 'it', To open door type 'op', To use something type 'use', To exit type 'exit'. ")
    
    #display the map
    elif userInput == "map":
      map(x,y)
      
    #error message
    else:
      showInformation("I'm sorry %s I can not do that"%userName)
  #exit to another room
  return 0

#display the current location in room 3, only used during development process   
def display(x,y):
  printNow("x =", x, "y = ", y)
  
#display a map which shows where the user is in room 3
def map(a,b):
  w = 5
  h = 3
  
  #Initialize the map matrix array and fill it with '_' characters
  mapMatrix = [['_' for x in range(h)] for y in range(w)]
 
  #display the doors as Ds on the map
  mapMatrix[0][1] = "D"
  mapMatrix[4][1] = "D"
  
  #Set an X to the player's current location
  mapMatrix[b][a] = "X"  #reversed because in order for the map to display correctly, we have to reverse it during the print function, this means we have to reverse the x and y coordinates
  
  #print the map
  printNow ("* * * * * *")  #print a * border around the top of the map
  for row in reversed(mapMatrix):
    printNow (" ".join(["*"]+row+["*"]))  #add *'s on the sides of the map
  printNow ("* * * * * *")  #print a * border around the bottom of the map
###################################################################################################################
#Room 4 By Patrick Gonzalez
def room4():
  d = direction()#Holds the array of all possible commands
  
  #Intro to the room
  printNow("------The Room of Questionnaire------")
  printNow ("There are no other doors in the room except the one behind you, but there is a strange mirror..")

  # Ask for user activity
  activity = ""
  activity = requestString("Do you want to inspect the mirror further or head back the way you came? ").lower()
  #Test the input from the user

  while true:
    #Check if the input is a letter
    if activity.isalpha() == False:
      activity = requestString("Do you want to inspect the mirror further or head back the way you came? ").lower()

    #Check if the guess asked for help
    if activity == 'help':
      helpMenu()
      activity = requestString("Do you want to inspect the mirror further or head back the way you came? ").lower()

    #Check if the user entered a proper command
    if activity not in d:
        showInformation("I'm sorry %s I can not do that."%userName)
        activity = requestString("Do you want to inspect the mirror further or head back the way you came? ").lower()

    #If they did input a proper command then move on to what they want to do 
    if activity in d:
      #print("Flag: activity in d")
      break

  # Once you have checked if the user input a proper command move on to the next step 
  if activity == 'bk':
    roomone() #input the function definition call to room 1

  elif activity == 'exit':
    showInformation("Death is your only escape! \m/")
    callQuit()
        
  elif activity == 'yes' or activity =='y':
    #print("Flag: They said yes inspect the mirror")
    #The player gets the chance to solve the mysterious quote
    mystery = hangMan() #If they pass the hangMan function it will return 'solved' otherwise it return 'incorrect'

    #If they solved the quote correctly they have the choice to enter the secret room or not
    if mystery == 'solved':  
      showInformation("You you solved the mysterious quote The mirror swings open leading to another room")
      decision = requestString("Do you enter the room? (y/n) ").lower()
      
      while true:
      #Check if the input is a letter
        if decision.isalpha() == False:
          decision = requestString("Do you enter the room? (y/n) ").lower

        #If they said yes to entering the room take them to secretRoom function
        if decision == 'yes' or decision =='y':
          #print "Flag: Yes enter the secret room"
          return secretRoom()
          
        #If they said no to entering the room take them to the begining of room4 function
        if decision == 'no' or decision =='n':
          # print "Flag: No do not enter the secret room"
          return room4()
        else:
          showInformation("You didnt enter yes or no")
          decision = requestString("Do you enter the room? (y/n) ").lower

    elif mystery == 'incorrect':
      showInformation("You failed to solve the puzzle.  Your life is over!!!\n")
      # test test
      callQuit()

  elif activity == 'no' or activity =='n':
    showInformation("What to do...?")
    return room4()
    
#an array to hold all the direction to check if the user entered a proper commmand  
def direction():
  d = ['fd','bk','lt','rt','pu','it','op','use','yes','y','no','n','exit']
  return d
########################################################################################################################  
#function for the secret room

def secretRoom():
  printNow("------Secret Room------")
  printNow ("You have entered the secret room and were teleported out of this hell hole. Congrats!")
  #sys.exit()
  callQuit()
  
####################################
# This ask the user to solve the blank in the mirror
#The rules are the same as hangman with 6 tries
#return 'solved' if they answer correctly
#return 'incorrect' if they answere wrong
def hangMan():
  showInformation ("Upon further inspection of the mirror you see a quote: \"What dosn't kill you only makes you stronger, except for ______, they will definitly kill you.\" What do you suppose will definitly kill you?")

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
    printNow ("You have %s guesses" %attempts)
    printNow ("Here is what you got so far:")
    printNow (blankWord)

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
            printNow ("interesting... it says, What dosn't kill you only makes you stronger, except for \"sharks\", they will definitly kill you.")
            return 'solved'

    #When the user guess the letter wrong:
    #  attach the incorrect guessed letter to the incorrect array
    #  decrease attempt to let the user know how many attempts they have left 
    else:
        incorrect.append(guess)
        attempts -=1
        printNow ("You guessed: ")
        printNow (incorrect)
  return 'incorrect'
########################################################################################333
#Room 5 By Mike Loeser
def room5():
  # user enters the room
  printNow("--- You have entered The Shrine ---")
  printNow("This is a dark room with no furniture.")
  printNow("On one wall is a curious looking painting.")
  
  userAction = requestString("What do you want to do? - type 'help' for a list of actions. ")
  
  while userAction.lower() != "exit":
    if userAction.lower() == 'help':
      helpMenu()
    elif userAction.lower() == 'vw':
      showView()
    elif userAction.lower() == 'bk':
      showExit()
    else:
      showInformation("I'm sorry %s I can not do that"%userName)
      
    userAction = requestString("What do you want to do? - type 'help' for a list of actions. ")


#Show View
def showView():
  printNow("you are in a darkened empty room")
  printNow("there are no windows")
  printNow("you see a large painting, at least 3 feet wide")
  printNow("it depicts a scene of a great white shark")
  printNow("cresting the water in an attack.")

 
#Show Exit
def showExit():
  printNow("you have exited the room")
  roomthree(5)
  # the exit will call room 3 function
  
  
def callQuit():
  showInformation("Good Bye %s." %userName)
  sys.exit()
  #raise SystemExit
  #return 0

#######################################################################################            
#Begin Main part of program where everything is called
#Print the intro to the scenario of the game
showInformation("It's a lovely day in Monterey.  You're walking down the hall at your favorite college. You're looking forward to a delicious lunch in your favorite cafeteria, but first you have to attend your last class of the day, the CST 205 lecture. Seems like another normal day at CSUMB. Nothing sinister could happen, could it?...could it?...OR COULD IT? You reach the classroom door, funny though...the window on the door is all black and there is a hand written note on the door that says 'Do you want to play a game?' You figure the lights are just off and the room is dark.  Suddenly, and without warning the door opens by itself and you walk through... BANG! The door slams shut and you're stuck!  What strange manner of room is this? Wherever you are, one thing is certain, you can't go back the way you came in...")
userName = requestString("Before we start what shall I call you? ")
#Call the enter function
enter()   
                                                                                                                                                                                                                                                                                                                                                                                           