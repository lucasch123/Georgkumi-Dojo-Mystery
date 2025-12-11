#Intro of the game#
#Some lines will have the type ignore as it recommended it, if it claimed to have an error when it didn't#
import random


print("The sharp glare of the sun wakes you up on the grassy field in front of Georgkumi dojo.") # type: ignore
print("You hear your classmate shout for you.\n") # type: ignore

#Gather the players username and then introduce Fencer who is your friend#
character = input("What would you like to be called on this adventure? ")
print(f"Ahh {character} where have you been, did you doze off? We got some new teachings from the dojo master: Fencer\n")
input("Press enter to continue...\n")

#Intro to some "world building" to build up what hpapens in the game
print("Welcome in students: Dojo Master")
print("Hello master: Students")
print(f"Let's get started on our basic training, {character} and Spencer why don't you guys start off by sparring: Dojo Master")
input("Press enter to continue...\n")

print(f"Heya {character} no hard feelings when I beat you right? Hahaha: Spencer(Fencer)")
print(f"Of course not, except I'm the one who will beat you: {character}")
print(f"{character} pulls out their pata, a sword like glove and Spencer pulls out his foil")
print("3... 2... 1... Begin!")
input("Press enter to continue...\n")

#Creating the stats and the battle system
def fencer_stats():
    return {
        "Health": 100,
        "Stamina": 100,
        "Skill": 10,
    }

def character_stats():
    return {
        "Health": 100,
        "Stamina": 100,
        "Skill": 10,
    }
#The stats for the battle system
def character_attack(character_player, enemy_player):
    if character_player["Stamina"] >= 10:
        damage = random.randint(character_player["Skill"] - 3, character_player["Skill"] + 5)
        enemy_player["Health"] -= damage
        character_player["Stamina"] -= 10
        print(f"{character} attacked the enemy for {damage} damage!")
    else:
        print(f"{character} is too tired and needs a turn to recharge")
        character_player["Stamina"] += 25

def enemy_attack(enemy_player, character_player):
    if enemy_player["Stamina"] >= 10:
        damage = random.randint(enemy_player["Skill"] - 3, enemy_player["Skill"] + 5)
        character_player["Health"] -= damage
        enemy_player["Stamina"] -= 10
        print(f"The enemy attacked {character} for {damage} damage!")
    else:
        print("The enemy is too tired and needs a turn to recharge")
        enemy_player["Stamina"] += 25
#Creating the actual turn based combat

def battle_system():
    character_player = character_stats()
    enemy_player = fencer_stats()
    print("Doododooooo dun dun dun dun battle begins!")
    
    while character_player["Health"] > 0 and enemy_player["Health"] > 0:
        print(f"Your HP: {character_player['Health']} Stamina: {character_player['Stamina']}")
        print(f"Enemy HP: {enemy_player['Health']} Stamina: {enemy_player['Stamina']}")
        
        print("\nChoose your action:")
        print("1. Attack")
        print("2. Rest (+10 stamina +7 HP)")
        
        choice = input("> ")

        if choice == "1":
            character_attack(character_player, enemy_player)
        elif choice == "2":
            character_player["Stamina"] += 10
            character_player["Health"] += 7
            print("You rest and recover 10 stamina and 7 health.")
        else:
            print("You messed up your punishment is losing your turn.")

      
        if enemy_player["Health"] <= 0:
            print(f"\n{character} defeated the fencer!")
            return "Win", character_player

        enemy_attack(enemy_player, character_player)

        
        if character_player["Health"] <= 0:
            print("\nYou were defeated...")
            return "Lose", character_player

    print("\nBattle Complete")
result, stats=battle_system()

if result == "Win":
    print(f"Well that was great battle wasn't it :{character}")
    print(f"Yeah I guess so {character} just wish I could win: Spencer")
    print(f"{character} gained 5 skill points")
    stats["Skill"] += 5

elif result == "Lose":
    print(f"Hahaha still need to improve some {character} : Spencer")
    print(f"I'm not done just yet let's keep going until I win one : {character}")
    print(f"{character} gained 5 skill points after countless battles until victory")
    stats["Skill"] += 5

print(stats)

input("Press enter to continue...\n")

print(f"\nNow i'll be able to do more damage in a battle with my new skills!:{character}")
print(f"Well done {character} I can tell you've been improving your skill with the pata, it could become a great weapon for you one day: Dojo Master")
print(f"Should I go to my room to rest or keep going with my training?: {character}")
print("\n1. Rest for max HP\n2. Progress with current HP")
def chapter_1():
    chapter_choice = input("\n>")
    if chapter_choice == "1":
        print("You have rested up and now your healthy again for more battles")
        stats["Health"] = 100
        print(stats)
        return
    elif chapter_choice == "2":
        print("You decide to keep going with the risk of having lower health")
        return
    else:
        print("Please select a valid input")
        return chapter_1()
chapter_1()

#Start of new section of the game
print("Chapter 1: Introduction to Georgkumi Dojo complete")
input("Press enter to continue to chapter 2...")

print(f"Ahhhh yare yare what a training session, I wonder what the others are up to:{character}")

print(f"\n{character} walks around the dojo and see's Spencer with someone holding a spear")
print("Yeah so I'm trying to get in but I feel vulnerable when I get close with my foil, any tips Zoe?: Spencer")
print("I reccomend trying to change your stance when you go in to keep your foil close to you: Zoe")
input("Press enter to continue...")

print(f"\nHey guy's what's up! That's a cool spear you got there: {character}")
print("Oh yeah thanks, you look kinda weak how about we fight: Zoe")
print(f"RIGHT NOW?? You know what sure..: {character}")
input("Press enter to continue...")


#Zoe's battle system, just minor tweaks
def spear_stats():
    return{
        "Health": 100,
        "Stamina": 100,
        "Skill": 20,
    }
def character_stats():
    return{
        "Health": 100,
        "Stamina": 100,
        "Skill": 15,
    }    
def battle_system():
    character_player = character_stats()
    enemy_player = spear_stats()
    print("\nDoododooooo dun dun dun dun battle begins!")
    
    while character_player["Health"] > 0 and enemy_player["Health"] > 0:
        print(f"Your HP: {character_player['Health']} Stamina: {character_player['Stamina']}")
        print(f"Enemy HP: {enemy_player['Health']} Stamina: {enemy_player['Stamina']}")
        
        print("\nChoose your action:")
        print("1. Attack")
        print("2. Rest (+10 stamina +7 HP)")
        
        choice = input("> ")

        if choice == "1":
            character_attack(character_player, enemy_player)
        elif choice == "2":
            character_player["Stamina"] += 10
            character_player["Health"] += 7
            print("You rest and recover 10 stamina and 7 health.")
        else:
            print("You messed up your punishment is losing your turn.")

      
        if enemy_player["Health"] <= 0:
            print(f"\n{character} defeated the fencer!")
            return "Win", character_player

        enemy_attack(enemy_player, character_player)

        
        if character_player["Health"] <= 0:
            print("\nYou were defeated...")
            return "Lose", character_player

    print("\nBattle Complete")
result, stats=battle_system()

if result == "Win":
    print(f"Who's really weak:{character}")
    print("Im.. im.. IMPOSSIBLE: Zoe")
    print(f"{character} gained 5 skill points")
    stats["Skill"] += 5

elif result == "Lose":
    print(f"Makes sense, you still have a lower skill {character} : Zoe")
    print(f"I'll get back at you just watch: {character}")
    print(f"{character} gained 5 skill points after fighting some randoms\n")
    stats["Skill"] += 5

print(stats)

input("Press enter to continue...\n")
#Dialouge and story building
print("Hey I wonder what the dojo master is up to, lets go check him out: Spencer")
print("The group goes to the dojo masters room but can't find him, but they see a faint glow coming out of the bookshelf")
print("\nThey inspect and see a big spirit in front of the dojo master as he bows down")
print("The group gets noticed slightly and the dojo master and spirit yell so the kids bolt")
print("They manage to hide and not get found")
print(f"What in the world was that: {character}")
print("Idk but whatever it is I know that it's not up to any good: Spencer")
input("Press enter to continue...")

print("Maybe lets look around for anything to help us get in: Zoe")


def explore():
    while True: 
        room_select = input("\nChoose where to go! :\n1. Storage\n2. Kitchen\n3. Suspicious room\n> ")
        
        if room_select == "1":
            print("Let's check out the storage to find anything that could help us get in that room")
            print("\nLooks like nothings here just some dusty shelves")
        
        elif room_select =="2":
            print("Let's check the kitchen for anything")
            print("\nJust some old beans and cookware")
        
        elif room_select == "3":
            print("Let's check the obviously suspicious room")
            print("Look's like theres a key to get in!")
            return
        else:
            print("Select a valid input")
explore()

print(f"\nNow that we have the key let's try to sneak in at midnight on the dot!: {character} ")
print("\nSome time passes until it's reached midnight!")
print("Now that time has passed it allowed you to regain all your health!")

def character_stats():
    return{
        "Health": 100,
        "Stamina": 100,
        "Skill": 20,
    }
stats["Health"] = 100
print(f"These are your current stats!\n{stats}")

print("Chapter 2: What evil? has finished\n Chapter 3: Finale starts")
input("Press enter to continue...")

print("\nAlright let's go in and check if he's there: Spencer")
print("Everything seems to be okay until...\n WHAT ARE YOU GUYS DOING HERE: Dojo Master")
print(f"Dojo master challenges {character} to a fight")


def master_stats():
    return{
        "Health": 100,
        "Stamina": 100,
        "Skill": 30,
    }
def character_stats():
    return{
        "Health": 100,
        "Stamina": 100,
        "Skill": 20,
    }    
def battle_system():
    character_player = character_stats()
    enemy_player = master_stats()
    print("\nDoododooooo dun dun dun dun battle begins!")
    
    while character_player["Health"] > 0 and enemy_player["Health"] > 0:
        print(f"Your HP: {character_player['Health']} Stamina: {character_player['Stamina']}")
        print(f"Enemy HP: {enemy_player['Health']} Stamina: {enemy_player['Stamina']}")
        
        print("\nChoose your action:")
        print("1. Attack")
        print("2. Rest (+10 stamina +7 HP)")
        
        choice = input("> ")

        if choice == "1":
            character_attack(character_player, enemy_player)
        elif choice == "2":
            character_player["Stamina"] += 10
            character_player["Health"] += 7
            print("You rest and recover 10 stamina and 7 health.")
        else:
            print("You messed up your punishment is losing your turn.")

      
        if enemy_player["Health"] <= 0:
            print(f"\n{character} defeated the Dojo Master! IMPOSSIBLE")
            return "Win", character_player

        enemy_attack(enemy_player, character_player)

        
        if character_player["Health"] <= 0:
            print("\nYou were defeated...")
            return "Lose", character_player

    print("\nBattle Complete")
result, stats=battle_system()

if result == "Win":
    print(f"We did it guys!:{character}")
    print("Im.. im.. IMPOSSIBLE: Dojo Master")
    print(f"{character} gained 5 skill points")
    stats["Skill"] += 5

elif result == "Lose":
    print(f"This isn't over:{character}")
    print("You're still too weak: Dojo Master")
    print(f"{character} gained 5 skill points after fighting some randoms\n")
    stats["Skill"] += 5

print(stats)

input("Press enter to continue...\n")

print("The group gets together to jump him which still defeats the Dojo Master")
print("You guys are cheap for that: Dojo Master")

print("\nThe group opens the shelf to find a evil spirit waiting for them")
input("Press enter to continue...\n")

print(f"The evil spirit offers {character} power")
print("Do you take it?")

def evil_offer():
    evil_choice = input("Do you take the offer? \n1.Yes \n2.No \n>")
    
    if evil_choice == "1":
        print(f"{character} betrays everyone and destroy's the dojo")
        exit()
    elif evil_choice =="2":
        print(f"{character}'s pata glows gold from the defience, {character} charges at the evil spirit and slays it saving the dojo")
        print("\nYou're declared a hero and the ultimate Pata user")
        exit()
    else:
        print("C'mon just choose something")
evil_offer()

print("The end")

