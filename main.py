
"""Name(s): Dev Arora and Sean Kaloudis
Name of Project: Adventure Game Final Project"""
def fifteenwarriors():
  print("The warriors are quick and able to defeat the calvarymen, taking ¼ of your enemy’s tower.")
  tenbdragons()

def fiverarmoredwarriors():
  print("The dragon destroys the armored warriors because the armored warriors can’t attack the air. The dragon manages to reach the tower and destroys it. YOU DIE!")
  death()
  
def tendragons():
  print(" The 10 dragons manage to destroy the enemy dragons and reduce the opponent’s tower health by 1/4 .")
  finalcountdown()

def dragoncatapults():
  print("The catapults manage to destroy the dragon and reduce the opponent’s tower health by 1/4 .")
  tengiants()
def dragon():
  print("You see a dragon flying towards the tower. Do You: \n A: Send 5 armored warriors \n B: Send 10 dragons \n C: Fire catapults")
  choice = input("Do you:")
  if choice in ("A", "a"):
    fivearmoredwarriors()
  elif choice in ("B","b"): 
    tendragons()
  elif choice in ("C", "c"):
    dragoncatapults()

def calvary():
  print("Your enemy has sent 10 armored cavalrymen armed with heavy broadswords. Do you: \n A: Send in 10 heavily armed soldiers \n B: Send in 10 archers \n C: Send in 15 warriors")
  choice = input("Do you:")
  if choice in ("A", "a"):
    tenheavysoldiers()
  elif choice in ("B","b"): 
    tenarchers()
  elif choice in ("C", "c"):
    fifteenwarriors()
  
def firecatapults():
  print("Most of your catapults miss, and your tower loses ⅓ of its health, but you are able to escape with your life.")
  calvary()
def twoarchers():
  print("Your archers are barely able to defend but the balloons land one attack on your tower, lowering its health by ⅓.")
  calvary()
def shootcannons():
  print("You are barely able to shoot them down but you succeed!")
  calvary()

def fourwarriors():
  print("The archers shoot down the warriors before the warriors can even reach the archers. The archers shoot at your tower and reduce its health by 1/3.")
  dragon()


  

def skeletonarmy():
  print("BAD CHOICE! The frail skeletons barely manage to reach the archers and stop them but you have lost a lot of your troops. Winning will be difficult from here.")
  



  
def threearmoredwarriors():
  print("The arrows of the enemy archers bounce off the armor of the warriors. Your tower is not harmed and the heavily armed warriors continue and attack your opponents tower. Your opponent's tower health decreases by 1/4.") 
  dragon()
  
def archers():
  print("You get the news that your enemy has sent 5 archers.Do you: \n A: Send 4 warriors \n B: Send 50 skeletons \n C: Send 3 heavily armored soldiers")
  choice = input("Do you:")
  if choice in ("A", "a"):
    fourwarriors()
  elif choice in ("B","b"): 
    skeletonarmy()
  elif choice in ("C", "c"):
    threearmoredwarriors()


  
def balloons():
  print ("You now must defend your tower against the two hot air balloons. \n A: Fire catapults \n B: Send in 2 archers \n C: Try and shoot them down with cannons")
  choice = input("Do you:")
  if choice in ("A", "a"):
    firecatapults()
  elif choice in ("B","b"): 
    twoarchers()  
  elif choice in ("C", "c"):
    shootcannons()
    
def giant(): 
  print ("The giant is too tall and can’t see the warrior. The warrior manages to attack your tower and reduces your tower health by ⅓.")
  archers()

def fullbattalion():
  print(" Bad choice! The enemy sends in two hot air balloons that bomb your army and wipe out most of your troops, defeating them will be very difficult from here!")
  balloons()

def twowarriors():
  print("Good Job! The 2 warriors can easily defeat the lone warrior. Your tower is not harmed and the two lone warriors manage to reduce the health of your opponent’s tower health by 1/4.  However, your opponents get angry that they could not damage your tower.")
  archers()


def enter():
  print ("Congrats, you have entered the game! You are faced with your first challenge. You see a lone warrior charging towards your tower, do you send \n A: A giant \n B: A fully armed battalion \n C: 2 warriors")
  choice = input("Do you:")
  if choice in ("A", "a"):
    giant()
  elif choice in ("B","b"): 
    fullbattalion()
  elif choice in ("C", "c"):
    twowarriors()
    

def start():
  print("Welcome to Tower Defense. You are a ruthless commander whose only objective is to defend your own tower and crush your enemy.")
  begin = input("Enter A or a to enter game: ")
  if begin in ("A","a"): 
    enter()
  else:
    print ("You are banished. If you can't even type in A you are not worthy of being a commander in the legendary Tower Defense. Please restart the game or accept your defeat. ")
start()
