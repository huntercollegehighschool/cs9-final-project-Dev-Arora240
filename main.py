
"""Name(s): Dev Arora and Sean Kaloudis
Name of Project: Adventure Game Final Project"""
import os
def death():
  print("You have failed as a commander Mr. Cheng.\n Yes we know who you are.\n Press R to restart.")
  begin = input("Enter R or r to enter game: ")
  if begin in ("R","r"): 
    os.system('clear')
    start() 
  else:
    print ("You have failed to restart. You can no longer restart as you are not worthy to be a commander. ")
def tie():
  print("Both sides have stopped their attacks, no one wins or loses. Press R to restart")
  begin = input("Enter R or r to enter game: ")
  if begin in ("R","r"): 
    os.system('clear')
    start()
  else:
    print ("You have failed to restart. You can no longer restart as you are not worthy to be a commander. ")
def victory():
  print("Amazing Job Mr. Cheng. Not only are you a great teacher, but you are also a great commander. Please click the following link for a special prize \n https://www.youtube.com/watch?v=xfr64zoBTAQ&list=PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx&index=9 \n Press R to restart.")
  begin = input("Enter R or r to enter game: ")
  if begin in ("R","r"): 
    os.system('clear')
    start()
  else:
    print ("You have failed to restart. You can no longer restart as you are not worthy to be a commander. ")


def whiteflag():
  print("Your enemy sees your white flag, but proceeds to destroy your tower. YOU DIE")
  death()
  
def cannonsfire():
  print("Your cannons do little to no damage to the enemy army and your tower gets destroyed. YOU DIE")
  death()
def evacuateb():
  print("You narrowly escape your tower before it is destroyed and you run away to a nearby town. You have lost this game but you are still alive, maybe you will get your revenge some day? Press R to restart")
  begin = input("Enter R or r to enter game: ")
  if begin in ("R","r"): 
    start()
  else:
    print ("You have failed to restart. You can no longer restart as you are not worthy to be a commander. ")
def evacuate ():
  print (" You are unable to escape such chaos and you get caught by the enemy army. YOU DIE.")
  death()
def finalboss():
  print("Your enemy sends in 5 heavily armored soldiers, 3 dragons, and 5 flaming catapults. You have no troops left to defend. Do you: \n A: Raise your white flag \n B: Fire your cannons \n C: Evacuate your tower")
  choice = input("Do you:")
  if choice in ("A", "a"):
    whiteflag()
  elif choice in ("B","b"): 
    cannonsfire()
  elif choice in ("C", "c"):
    evacuateb()
def finalcountdown():
  print("Your enemy sends in 10 heavily armored soldiers, 10 calvarymen, and 15 dragons. You don’t have any dragons left to defend. Do you:\n A: Raise your white flag \n B: Fire your cannons \n C: Evacuate your tower.")
  choice = input("Do you:")
  if choice in ("A", "a"):
    whiteflag()
  elif choice in ("B","b"): 
    cannonsfire()
  elif choice in ("C", "c"):
    evacuate()
def firecannonsb2():
  print("Your cannons are ineffective against the dragons and they destroy your tower.")  
  death()
def fivearchersb2():
  print("The archers are unable to stop so many dragons and your tower is destroyed.")
  death()
def restofarmy():
  print("The rest of your army isn’t much, but is barely able to defend against the dragons.")
  finalboss()
def tendragonsb2():
  print("The enemy sends in 10 dragons, and you barely have any troops left to defend against them. Do you: \n A: Fire your cannons. \n B: Send in 5 archers \n C: Send in the rest of your entire army")
  choice = input("Do you:")
  if choice in ("A", "a"):
    firecannonsb2()
  elif choice in ("B","b"): 
    fivearchersb2()
  elif choice in ("C", "c"):
    restofarmy()
def firecannons():
  print("The cannons are ineffective against the dragons and the dragons destroy your tower.")
  death()
def thirtyarchers():
  print("The archer’s arrows do nothing to the dragons and they destroy your tower.")
  death()
def firebcatapult():
  print("Your catapults successfully destroy the dragons and take ¼ of the enemy’s health. However, both sides have depleted their resources from this long war and you come to an agreement to stop attacking each other.")
  tie()
def fivewarriors():
  print(" DEATH! \n Warriors don’t deal enough damage and the giants manage to reach your tower. Due to this your tower is destroyed.")
  death()

def fivegiants():
  print("DEATH! \n The Giants brawl it out, but after the brawl, 5 of your opponent's giants survive and reach your tower. Due to this your tower is destroyed.")
  death()

def twentydragons():
  print("Victory! \n The 20 dragons manage to melt the giants! Your dragons go unharmed as giants can’t attack flying troops. Your dragons manage to attack your opponent’s tower and completely destroy it!")
  victory()

def tengiants():
  print(" You see 10 giants slowly stomping their way to your tower. Do you: \n A: You send 5 warriors \n B: You send 5 giants at them \n C: You send 20 dragons")
  choice = input("Do you:")
  if choice in ("A", "a"):
    fivewarriors()
  elif choice in ("B","b"): 
    fivegiants()
  elif choice in ("C", "c"):
    twentydragons()

def tenbdragons():
  print("Your opponent sends in 10 dragons. Do you: \n A: Fire cannons \n B: Send 30 archers \n C: Fire catapults") 
  choice = input("Do you:")
  if choice in ("A", "a"):
    firecannons()
  elif choice in ("B","b"): 
    thirtyarchers()
  elif choice in ("C", "c"):
    firebcatapult()
  

def tenheavysoldiers():
  print("The warriors are quick and able to defeat the calvarymen, taking ¼ of your enemy’s tower.")
  tenbdragons()
def tenarchers():
  print("The archer’s arrows are ineffective against the armor of the calvarymen, your tower loses ⅓ of its health.")
  tenbdragons()
def fifteenwarriors():
  print("The warriors are quick and able to defeat the calvarymen, taking ¼ of your enemy’s tower.")
  tenbdragons()

def fivearmoredwarriors():
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
  tendragonsb2()
  



  
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
