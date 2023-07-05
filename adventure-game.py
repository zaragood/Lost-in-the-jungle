print('''
   _                   _
  (_)                 | |     
   _ _   _ _ __   __ _| | ___ 
  | | | | | '_ \ / _` | |/ _ |
  | | |_| | | | | (_| | |  __/
  | |\__,_|_| |_|\__, |_|\___|
 _/ |             __/ |       
 |__/            |___ /               _            
                                     ..:::::;'|
             __   ___             / \:::::;'  ;
           ,::::`'::,`.          :   ___     /
          :_ `,`.::::)|          | ,'SSt`.  /
          |(` :\)):::`;          |:::::::| :
          : \ ,`'`:::::`.        |:::::::| |
           \ \  ,' `:::::`.      :\::::::; |
            \ `.  ,' ` ,--.)     : `----'  |
             :  `-.._,'__.'      :   ____  |
             |     |              :,'::::\ |
             :  _  |              :::::::::|
             ;     :              |:::::::||
            :      |              |:::::::;|
            :  __  :              |\:::::; |
            |      |              | _____  |
            |      :              |':::::\ |
            : .--  |\             |::::::::|
            :      :.\            |:::::::;|
             :      \:\           |::::::/ |
              \ .-'  \'`.         ;`----' /;
               \      \|::-...__,'._     //
                `.  ,' `:::/ |::::::`. ,'/
                  `.     `-._;:::::::.','
                    `-..__,   ``--'' ,'
                          ``---....-'
''')
print("WELCOME TO THE LOST IN THE JUNGLE ADVENTURE GAME!")
print("=================================================\n")

print('''
Oh no you are lost in this mysterios jungle, surrounded by wildlifes.
Your mission is to navigate your way through the jungle, overcome 
obstacles to find your way back to civilation.
      
Be cautious you never know what awaits you.
''')
print("LET THE FUN BEGIN\n")

print("Ther are two path to choose from, the Narror path with tall thick trees and the Wide path with short tress.")
user_first_choice = input("Wide / Narror? ").lower()

#first lane that you have to make it across
if user_first_choice == "narrow":
    print("hew! you made it out of the thick trees, now lets move on.\n")
    
    #Second lane that you have to survive
    user_second_choice = input("Do you want to climb up the hill or swim accross the river? hill/swim: ").lower()
    if user_second_choice == "hill":
        print("You made it down the hill. now let move one")
        
        #third lane that you have to survive
        print("Do you want to walk through the mud or through the cave?")
        user_third_choice = input("choose wisely. Mud / Cave? ").lower()
        if user_third_choice == "mud":
            print("you are almost there! keep going\n!")
            
            #fourth lane that you have to survive
            print("The path by your left is dark and creepy but their there seem to be a burning flame by the rigth!")
            user_fourth_choice = input("which way would you go? right/ left: ").lower()
            if user_fourth_choice == "left":
                print("woohoo! you made to the high way, keep pushing\n!")
                
                #fift lane that you have to survive
                print("Do you want to take a break or walk down the highway?")
                user_fift_choice = input("choice wisely! wait / walk? ").lower()
                if user_fift_choice == "walk":
                    print("CONGRATULATION! You made it out of the jungle!\n")
                elif user_fift_choice == "wait":
                    print("sorry you got attacked by a cheetah!\nGAME OVER!")
                else:
                    print("Invalide response! try again!")
                    
            elif user_fourth_choice == "right":
                print("The flame lead you into the den of carnibals!\nGAME OVER!")
            else:
                print("invalide response! try agin!")
                
        elif user_third_choice == "cave":
            print("This is a dead end!\nGame over!")
        else:
            print("invalide response, try again!")

            
    elif user_second_choice == "swim":
        print("OMG! You just became a snack for the crocodile!")
    else:
        print("invalide respond, try again!")

elif user_first_choice == "wide":
    print("OOPS! You step into a quick sand.\nGAME OVER!")
else:
    print("Invalid response, try again")
