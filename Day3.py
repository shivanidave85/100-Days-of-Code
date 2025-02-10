print('''_
| |          
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ 
| __| '__/ _ \/ _` / __| | | | '__/ _ \  
| |_| | |  __/ (_| \__ \ |_| | | |  __/ 
 \__|_|  \___|\__,_|___/\__,_|_|  \___| 
 ''')

print("Welcome to Treasure Island \n Your mission is to find the treasure \n")

direction = input("Your're at cross road where do you want to go ? \n Type Left or Right \n")

if direction == "Left":
     swim = input("Your're at lake.Do you want to swim or wait for the boat to go to island ? \n Type swim or wait \n")

     if swim == "wait":
      door = input("Your're at door which door will you choose ? \n Red, Blue or Yellow \n")

      if door == "Blue":
       print("Eaten by beasts Game Over")
      elif door == "Red":
       print("Burned by Fire Game Over")
      elif door == "Yellow":
       print("You Win")
      else:
       print("Game Over")

     else:
       print("Attacked by pirates")
else:
    print("Game over")
