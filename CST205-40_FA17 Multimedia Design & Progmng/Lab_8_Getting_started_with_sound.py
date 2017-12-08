#Lab 8
#Chris Holmes
#Chris Buckey
#Patrick Gonzalez

#sound = makeSound(pickAFile())

def increaseVolume(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value * 2)
    
#Decreases the volume of a sound by half
def decreaseVolume(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value / 2)
    
#Takes in two parameters, sound and change
#Sound is the sound file that you want to change the volume on
#Change is the amount you want to change by. Use fraction to decrease, whole numbers to increase
def changeVolume(sound, change):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value * change)
  
#Finds the largest sample in a sound and returns it
#sets the variable max to the sample value at the first sample
#Loops through all samples, comparing to the value in max. 
#If the value in the loop is larger than max, new value of max is value in loop
def maxSample():
  sound = makeSound(pickAFile())
  samples = getSamples(sound)
  max = getSampleValue(samples[0])
  for x in range(1, len(samples)-1):
    if getSampleValue(samples[x]) > max:
      max = getSampleValue(samples[x])
  return max
  
#Sets any sample value that is greater than 0 to the max, 32767
#Sets any sample value that is less than 0 to the max negative, -32767
def goToEleven(sound):
  for sample in getSamples(sound):
    if getSampleValue(sample) > 0:
      setSampleValue(sample, 32767)
    elif getSampleValue(sample) < 0:
      setSampleValue(sample, -32767)


