name = input("What is your name? ")
print("Welcome", name, "to this adventure. You are a traveler who reaches different paths. Each choise leads to a different adventure. Good luck!")

answer1 = input("You are at a crossroad. You can go left middle or right. Which way do you want to go?(left/middle/right) ").lower()

if answer1 == "left":
    answer2 = input("You just entered a dark and quiet path. Do you want to follow the lights or follow the sounds?(lights/sounds) ").lower()
    if answer2 == "lights":
        answer5 = input("You have just found a friendly village and may rest safely. Are you choosing to rest at an inn or talk to the villagers?(inn/villagers) ")
        if answer5 == "inn":
            print("You were able to rest and regain your strength as well as receive a map that leads to the Hidden Valley where you find herbs and become wealthy!")
            print("Congratulations", name, "you have completed the adventure!")
            quit()
        else:
            print("They warn about danger ahead but gives you supplies and lead you to Ancient Ruins. You discover lost knowledge and become a famous historian!")
        
    else:
        print("A wild animal appears and you have to run away!")
        print("Game Over")
        
elif answer1 == "middle":
    answer3 = input("You have just reached a fast and wide river. Do you swim across or build a raft?(swim/raft) ").lower()
    if answer3 == "swim":
        print("The current was too strong and you were swept away!")
        print("Game Over")
    else:
        answer6 = input("You successfully find supplies to build a raft and crossed the river! Across the river you find a fishing camp and gain food or you explore a mysterious cave?(fishing/cave) ")
        if answer6 == "fishing":
            print("You become a merchant fisherman and live happily ever after!")
            print("Congratulations", name, "you have completed the adventure!")
            quit()
        else:
            print("You continue travelling and found bandits who captured you!")
            print("Game Over")

elif answer1 == "right":
    answer4 = input("You have just entered a steep and cold mountain trail. Do you climb quickly or move carefully?(quickly/carefully) ").lower()
    if answer4 == "quickly":
        print("You slipped and fell down the mountain!")
        print("Game Over")
    else:
        answer7 = input("You safely reached the top and found a beautiful view and a treasure! You can either open the chest or leave it alone.(open/leave) ")
        if answer7 == "open":
            print("You found gold and precious gems! You are now rich!")
            print("Congratulations", name, "you have completed the adventure!")
            quit()
        else:
            print("You chose to leave the treasure and continue your adventure, valuing experiences over material wealth.")
else:
    print("Not a valid option. Game Over.")