
"""Name(s): Dev Arora and Sean Kaloudis
Name of Project: Adventure Game Final Project"""

def enter():
    print ("Congrats, you have entered the game! You are faced with your first challenge. You see a ")
    

def start():
  print("Welcome to Tower Defense. You are a ruthless commander whose only objective is to defend your own tower and crush your enemy.")
  choice = input("Enter A or a to enter game: ")
  if choice in ("A","a"): 
    enter()
  else:
    print ("You are banished. If you can't even type in A you are not worthy of being a commander in the legendary Tower Defense. Please restart the game or accept your defeat. ")

