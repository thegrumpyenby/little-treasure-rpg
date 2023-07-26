import time

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# enter here
print("> Welcome to the Treasure Dungeon.")
print("> Your mission is to find the treasure.") 
start = input("Type 'start' and hit 'enter' when you’re ready.\n")
if start.lower() == "start":
  print("\n\n> You enter the dungeon and walk down a long corridor.")
time.sleep(3)
print("> Eventually you arrive at a fork — a pitch dark corridor to the left. A slightly lighter corridor to the right.")
time.sleep(3)

# Choose a path
choose_left = input("> Which one do you choose? Left or right?\n")

if choose_left.lower() == "left" or choose_left.lower() == "l":
  print("\n\n> Good choice!")
else:
  time.sleep(3)
  print("\n\n> You fell into a hole.")
  print("> Game over!")
  exit()
time.sleep(2)
print("> Another corridor! You continue walking forward.")
time.sleep(2)

# choose to climb or swim
choose_swim = input("> You arrive at a dead end. In the dark, you can sort of make out a large body of water. Around the 'lake' is a rock-like formation with a very small ledge that can maybe, possibly fit your toes. Behind you, you hear an ominous and menacing growl. Quickly! What do you do? Climb the ledge or brave the lake? Climb or swim?\n")

if choose_swim.lower() == "swim" or choose_swim.lower() == "s":
  time.sleep(2)
  print("\n\n> Just as you enter the creepy looking water, a huge, scary-looking feline comes up behind you. It shies away from the water, and you use your chance to make your escape.")
else:
  time.sleep(3)
  print("\n\n> You scramble up onto the ledge and shimmy along, when a huge, scary-looking feline comes out of the corridor and swiftly climbs the rocks and pounces on you.")
  print("> Yer dead. In case that wasn’t clear yet.")
  print("> Game over!")
  exit()

time.sleep(2)
print("> You climb out of the water on the other side drenched. Shivering, you look back to the other side of the lake where the feline angrily growls and paces along the edge of the water. Phew!")

time.sleep(2)
print("> You’re really cold now that you’re wet, but you notice a hairdryer, miraculously plugged into a socket in the wall nearby.")
time.sleep(2)

# choose wet or dry
choose_no = input("> Do you want to try using the hairdryer on your clothes? Y/N \n")

if choose_no.lower() == "n" or choose_no.lower() == "no":
  time.sleep(2)
  print("\n\n> That’s right, a little discomfort never hurt anybody. You trudge on, still shivering, leaving a trail of water drops behind you. You’re pretty unhappy. But at least you’re alive.")
else:
  time.sleep(3)
  print("\n\n> Really? You thought that would work? Well, you electrocuted yourself! Didn’t they teach you not to use hair dryers near bodies of water?")
  print("> Game over!")
  exit()

time.sleep(2)
print("> You have no idea what horrible fate you just avoided!")
time.sleep(2)
print("> Probably better this way.")
time.sleep(3)
print("> You keep following yet another corridor. Put one foot in front of the other, starting with your left one.")

# choose to put one foot in front of the other
# Can I turn this into a while loop or solve it with a predefined function later on?
step1 = input("> Which foot are you starting with again?\n")
if step1.lower() == "left" or step1.lower() == "l":
  print("\n> Good!")
else:
  time.sleep(1)
  print("\n> Oh, for fuck’s sake!")
  step1_2 = input("> You wanna try that again?\n")
  
  if step1_2.lower() == "left" or step1_2.lower() == "l":
    print("\n> Good. Finally.")
  else:
    time.sleep(1)
    print("\n> I said, 'start with the left one', and you couldn’t even get that right.")
    print("Game over!")
    exit()

step2 = input("> Now the other foot.\n")
if step2.lower() == "right" or step2.lower() == "r":
  print("\n> You’re getting the hang of this!")
else:
  time.sleep(1)
  print("\n> Oh, for fuck’s sake!")
  print("> Game over!")
  exit()

step3 = input("> Continue.\n")
if step3.lower() == "left" or step3.lower() == "l":
  print("\n> Well done!")
else:
  time.sleep(2)
  print("\n> Oh, for fuck’s sake!")
  print("> Game over!")
  exit()

step4 = input("> And now?\n")
if step4.lower() == "right" or step4.lower() == "r":
  print("\n> Okay, I think you got the rest on your own. Just keep walking.")
  time.sleep(2)
  print("> Is that your normal walk? Oh, okay…")
else:
  print("\n> Oh, for fuck’s sake!")
  print("> Game over!")
  exit()

time.sleep(3)

print("> Alright. You did good. I’m real proud of you.")
time.sleep(2)
print("> No, no. I really do mean it. You put one foot in front of the other like a pro.")
time.sleep(3)
print("\n\n> Finally, the corridor opens up into a little room.")
time.sleep(3)
print("> You look around and find that there are three doors leading from the room.")
time.sleep(3)
print("> There’s a red door to your left. No, you can’t paint it black. Sorry.")

time.sleep(3)
print("> A blue door to your right.")
time.sleep(3)
print("> A green door in front of you.")
time.sleep(3)

choose_door = input("> Which door do you choose? R, B, or G?\n")

if choose_door.lower() == "green" or choose_door.lower() == "g":
  time.sleep(3)
  print("\n\n> You carefully pry open the door")
  time.sleep(3)
  print("> What’s that?")
  time.sleep(2)
  print("> It looks like daylight?")
  time.sleep(1)
  print("> OMG it is daylight!")
  time.sleep(3)
  print("\n\n> Congratuations! You’ve made it out of the dungeon!")
  time.sleep(2)
  print("> Unfortunately, you were so focused on making the right choice that you entirely forgot to find the treasure. You emerge from the dungeon none the richer but instead wetter and slightly worse for the wear than you went in.")
  time.sleep(2)
  print("> But at least you had an adventure. And capitalism can’t take that from.\n\n")
  time.sleep(2)
  print("> This game is now over if you hadn’t noticed. Thank you for playing.")
  exit()
elif choose_door.lower() == "red" or choose_door.lower() == "r":
  time.sleep(3)
  print("\n\n> Congratulations, you just burned to death in the fire behind the red door.")
  print("> Game over.")
  exit()

elif choose_door.lower() == "blue" or choose_door.lower() == "b":
  time.sleep(3)
  print("\n\n> Oh look, it’s your feline friend again! Meow!")
  print("> Game over.")
  exit()
else:
  print("\n\n> You should really be more diligent when typing. Game over.")
  exit()