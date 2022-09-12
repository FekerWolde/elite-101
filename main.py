import random

name = input("What is your name? ")
print("Hi " + name + "! ")

while True:
  intro = input("How may I assist you: joke, calc, or convo? (To quit at anytime type q)  ")
  if intro == "q":
    break
  
  jokes = ["What's the best thing about Switzerland?...I don't know, but the flag is a big plus.", "Where do you learn to make a banana split?...Sundae school.", "I don't trust those trees.... They seem kind of shady.", "I don't trust stairs... They're always up to something.", "What do you call someone with no body and no nose? Nobody knows."]

  def calculator():
    first = input('First val:')
    second = input('Second val:')
    first = float(first)
    second= float(second)
    print(first + second)
  def conversation():
    feel = input("How are you feeling today? good, bad or eh? ")
    if feel == "good" :
      print("I am glad to here that I feel good aswell")
      good = input("Can I make your day better by telling a joke? yes or no ")
      if good == "yes" :
        print(random.choice(jokes))
      else :
        print("Ok" )
    elif feel == "bad" :
      print("I understand everyone has bad days. ")
      bad = input("Can I make your day better by telling a joke? yes or no ")
      if bad == "yes": 
        print(random.choice(jokes))
      else :
        print("Ok" )   
    else : 
      print("Same. ")
      eh = input("Can I make your day less eh by telling a joke? yes or no ")
      if eh == "yes": 
        print(random.choice(jokes))
      else :
        print("Ok" )   
    
  def choice():
    if intro == "joke":
      print(random.choice(jokes))
    elif intro == "calc":
      calculator()
    elif intro == "convo":
      conversation()
    
      
    
  
   
  
  
    
  
    
    
  
  
  if intro == "joke":
    print(random.choice(jokes))
  elif intro == "calc":
    calculator()
  else :
    conversation()
    

