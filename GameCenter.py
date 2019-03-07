import random
import time
#____________________________________________________MISC
armour_points = 0
health = 100

print("Welcome Choose Your Game!")
print("Option [1} is Sebetian's Ultimate Rock, Paper, Scissors.")
print("Option [2] is Juan's Tic Tac Toe. [CURRENTLY NOT AVALIABLE.]")
print("Option [3] is Roberth's Choose Your Own Adventure.")
game = input()
if game == '1':
    #variables for game
    user_score = 0
    computer_score = 0
    user_choice = ""
    computer_choice = ("rock", "paper", "scissors", "yeet", "dab", "t-pose", "default dance")
    #variables for game

    #rules

    print("Welcome to Rock, Paper, Scissors, Yeet, Dab, T-Pose, Default Dance.")
    game = input("Do you want to play?")

    print(" ")
    print("These are the rules:")
    print(" ")
    print("""Your choices are: rock, paper, scissors, yeet, dab, t-pose, and default dance.
    Keep your choice in lowercase.""")
    time.sleep(2)
    print(" ")
    print("Here is the list of what beats what:")
    time.sleep(2)
    print(" ")
    print("""rock will beat: scissors, dab, and t-pose.
    But rock will lose to: paper, yeet, default dance.""")
    time.sleep(4)
    print(" ")
    print("""paper will beat: rock, yeet, and default dance.
    But paper will lose to: scissors, dab, and t-pose.""")
    time.sleep(4)
    print(" ")
    print("""scissors will beat: paper, dab, and t-pose.
    But scissors will lose to: yeet, rock, and default dance.""")
    time.sleep(4)
    print(" ")
    print("""yeet will beat: rock scissors, and t-pose.
    But yeet will lose to: dab, paper, and default dance.""")
    time.sleep(4)
    print(" ")
    print("""dab will beat: yeet, rock, and default dance.
    But dab will lose to: t-pose, scissors, and rock.""")
    time.sleep(4)
    print(" ")
    print("""t-pose will beat: dab, paper, and default dance.
    But t-pose will lose to: yeet, rock, and scissors.""")
    time.sleep(4)
    print(" ")
    print("""default dance will beat: rock, scissors, and yeet.
    But default dance will lose to: paper, dab, and t-pose.""")
    time.sleep(4)
    print(" ")
    print("""Anything else typed other than these exact answers will result in point loss.
    Even capitalized. Spelling will count, so check it.
    There is a secret choice though that you will win with automatically. You have to find that out.""")
    time.sleep(4)
    print(" ")
    print("""If you need to see the list of what beats what again, just type "HELP"
    without the quotations and it will be reprinted. That or scroll up.""")
    time.sleep(2)
    print(" ")
    print("The first to 5 points wins.")

    print(" ")
    print("User score is: ", user_score)
    print("Computer score is: ", computer_score)
    print(" ")

    #rules

    #the game       
    while game == ("yes") or game == ("Yes") or game == ("yes.") or game == ("Yes.") or game == ("yea") or game == ("yea.") or game == ("yeah") or game == ("yeah.") or game == ("") or game == ("maybe") or game == ("Maybe") or game ==("maybe.") or game == ("Maybe.") or game == ("okay") or game == ("okay.") or game == ("Okay") or game == ("Okay.") or game == ("k") or game == ("K") or game == ("ok") or game == ("Ok") or game == ("Ok.") or game == ("ok.") or game == ("k.") or game == ("K.") or game == ("yeehaw"):
    
        user_choice = input("What is your choice User? Type HELP if you need help. ")
        print(" ")
        print("You chose ", user_choice)

        computer_choice = ("rock", "paper", "scissors", "yeet", "dab", "t-pose", "default dance")
        computer_choice = random.choice(computer_choice)
        print("Computer chose " ,computer_choice)


    #when user needs help
        if user_choice == "HELP":
            print(" ")
            print("""Your choices are: rock, paper, scissors, yeet, dab, t-pose, and default dance. Keep your choice in lowercase.""")
            time.sleep(2)
            print(" ")
            print("Here is the list of what beats what:")
            time.sleep(2)
            print(" ")
            print("""rock will beat: scissors, dab, and t-pose. But rock will lose to: paper, yeet, default dance.""")
            time.sleep(4)
            print(" ")
            print("""paper will beat: rock, yeet, and default dance. But paper will lose to: scissors, dab, and t-pose.""")
            time.sleep(4)
            print(" ")
            print("""scissors will beat: paper, dab, and t-pose. But scissors will lose to: yeet, rock, and default dance.""")
            time.sleep(4)
            print(" ")
            print("""yeet will beat: rock scissors, and t-pose. But yeet will lose to: dab, paper, and default dance.""")
            time.sleep(4)
            print(" ")
            print("""dab will beat: yeet, rock, and default dance. But dab will lose to: t-pose, scissors, and rock.""")
            time.sleep(4)
            print(" ")
            print("""t-pose will beat: dab, paper, and default dance. But t-pose will lose to: yeet, rock, and scissors.""")
            time.sleep(4)
            print(" ")
            print("""default dance will beat: rock, scissors, and yeet. But default dance will lose to: paper, dab, and t-pose.""")
            time.sleep(4)
            print(" ")
        
    #when the user needs help
        
    #when a tie happens between user + computer
        if user_choice == "rock" and computer_choice == "rock":
            print("A tie! No points for ties.")
            print("User score is: ", user_score)
            print("Computer score is: ", computer_score)
            print(" ")
    
        if user_choice == "paper" and computer_choice == "paper":
            print("A tie! No points for ties.")
            print("User score is: ", user_score)
            print("Computer score is: ", computer_score)
            print(" ")

        if user_choice == "scissors" and computer_choice == "scissors":
            print("A tie! No points for ties.")
            print("User score is: ", user_score)
            print("Computer score is: ", computer_score)
            print(" ")

        if user_choice == "yeet" and computer_choice == "yeet":
            print("A tie! No points for ties.")
            print("User score is: ", user_score)
            print("Computer score is: ", computer_score)
            print(" ")

        if user_choice == "dab" and computer_choice == "dab":
            print("A tie! No points for ties.")
            print("User score is: ", user_score)
            print("Computer score is: ", computer_score)
            print(" ")

        if user_choice == "t-pose" and computer_choice == "t-pose":
            print("A tie! No points for ties.")
            print("User score is: ", user_score)
            print("Computer score is: ", computer_score)
            print(" ")

        if user_choice == "default dance" and computer_choice == "default dance":
            print("A tie! No points for ties.")
            print("User score is: ", user_score)
            print("Computer score is: ", computer_score)
            print(" ")
    #when a tie happens between user + computer


        
    #when rock wins for user/computer      
        if user_choice == "rock" and computer_choice == "scissors":
            user_score = user_score+1
            print("rock beats scissors. User wins.")
            print("User score is: ", user_score)
            print("Computer score is: ", computer_score)
            print(" ")

        if user_choice == "rock" and computer_choice == "dab":
            user_score = user_score+1
            print("rock beats dab. User wins.")
            print("User score is: ", user_score)
            print("Computer score is: ", computer_score)
            print(" ")
        
        if user_choice == "rock" and computer_choice == "t-pose":
            user_score = user_score+1
            print("rock beats t-pose. User wins.")
            print("User score is: ", user_score)
            print("Computer score is: ", computer_score)
            print(" ")

    #computer wins now
        
        if user_choice == "scissors" and computer_choice == "rock":
            computer_score = computer_score+1
            print("rock beats scissors. Computer wins.")
            print("Computer score is: ", computer_score)
            print("User score is: ", user_score)
            print(" ")
        
        if user_choice == "dab" and computer_choice == "rock":
            computer_score = computer_score+1
            print("rock beats dab. Computer wins.")
            print("Computer score is: ", computer_score)
            print("User score is: ", user_score)
            print(" ")
        
        if user_choice == "t-pose" and computer_choice == "rock":
            computer_score = computer_score+1
            print("rock beats t-pose. Computer wins.")
            print("Computer score is: ", computer_score)
            print("User score is: ", user_score)
            print(" ")
    #when rock wins for user/computer



    #when paper wins for user/computer
        if user_choice == "paper" and computer_choice == "rock":
            user_score = user_score+1
            print("paper beats rock. User wins.")
            print("User score is: ", user_score)
            print("Computer score is: ", computer_score)
            print(" ")

        if user_choice == "paper" and computer_choice == "yeet":
            user_score = user_score+1
            print("paper beats yeet. User wins.")
            print("User score is: ", user_score)
            print("Computer score is: ", computer_score)
            print(" ")

        if user_choice == "paper" and computer_choice == "default dance":
            user_score = user_score+1
            print("paper beats default dance. User wins.")
            print("User score is: ", user_score)
            print("Computer score is: ", computer_score)
            print(" ")

    #computer wins now

        if user_choice == "rock" and computer_choice == "paper":
            computer_score = computer_score+1
            print("paper beats rock. Computer wins.")
            print("Computer score is: ", computer_score)
            print("User score is: ", user_score)
            print(" ")

        if user_choice == "yeet" and computer_choice == "paper":
            computer_score = computer_score+1
            print("paper beats yeet. Computer wins.")
            print("Computer score is: ", computer_score)
            print("User score is: ", user_score)
            print(" ")

        if user_choice == "default dance" and computer_choice == "paper":
            computer_score = computer_score+1
            print("paper beats default dance. Computer wins.")
            print("Computer score is: ", computer_score)
            print("User score is: ", user_score)
            print(" ")
    #when paper wins for user/computer


        
    #when scissors wins for user/computer
        if user_choice == "scissors" and computer_choice == "paper":
            user_score = user_score+1
            print("scissors beats paper. User wins.")
            print("User score is: ", user_score)
            print("Computer score is: ", computer_score)
            print(" ")

        if user_choice == "scissors" and computer_choice == "dab":
            user_score = user_score+1
            print("scissors beats dab. User wins.")
            print("User score is: ", user_score)
            print("Computer score is: ", computer_score)
            print(" ")

        if user_choice == "scissors" and computer_choice == "t-pose":
            user_score = user_score+1
            print("scissors beats t-pose. User wins.")
            print("User score is: ", user_score)
            print("Computer score is: ", computer_score)
            print(" ")

    #computer wins now

        if user_choice == "paper" and computer_choice == "scissors":
            computer_score = computer_score+1
            print("scissors beats paper. Computer wins.")
            print("Computer score is: ", computer_score)
            print("User score is: ", user_score)
            print(" ")
        
        if user_choice == "dab" and computer_choice == "scissors":
            computer_score = computer_score+1
            print("scissors beats dab. Computer wins.")
            print("Computer score is: ", computer_score)
            print("User score is: ", user_score)
            print(" ")

        if user_choice == "t-pose" and computer_choice == "scissors":
            computer_score = computer_score+1
            print("scissors beats t-pose. Computer wins.")
            print("Computer score is: ", computer_score)
            print("User score is: ", user_score)
            print(" ")
    #when scissors wins for user/computer


        
    #when yeet wins for user/computer
        if user_choice == "yeet" and computer_choice == "rock":
            user_score = user_score+1
            print("yeet beats rock. User wins.")
            print("User score is: ", user_score)
            print("Computer score is: ", computer_score)
            print(" ")

        if user_choice == "yeet" and computer_choice == "scissors":
            user_score = user_score+1
            print("yeet beats scissors. User wins.")
            print("User score is: ", user_score)
            print("Computer score is: ", computer_score)
            print(" ")

        if user_choice == "yeet" and computer_choice == "t-pose":
            user_score = user_score+1
            print("yeet beats t-pose. User wins.")
            print("User score is: ", user_score)
            print("Computer score is: ", computer_score)
            print(" ")

    #computer wins now

        if user_choice == "rock" and computer_choice == "yeet":
            computer_score = computer_score+1
            print("yeet beats rock. Computer wins.")
            print("Computer score is: ", computer_score)
            print("User score is: ", user_score)
            print(" ")

        if user_choice == "scissors" and computer_choice == "yeet":
            computer_score = computer_score+1
            print("yeet beats scissors. Computer wins.")
            print("Computer score is: ", computer_score)
            print("User score is: ", user_score)
            print(" ")

        if user_choice == "t-pose" and computer_choice == "yeet":
            computer_score = computer_score+1
            print("yeet beats t-pose. Computer wins.")
            print("Computer score is: ", computer_score)
            print("User score is: ", user_score)
            print(" ")
    #when yeet wins for user/computer



    #when dab wins for user/computer
        if user_choice == "dab" and computer_choice == "yeet":
            user_score = user_score+1
            print("dab beats yeet. User wins.")
            print("User score is: ", user_score)
            print("Computer score is: ", computer_score)
            print(" ")

        if user_choice == "dab" and computer_choice == "paper":
            user_score = user_score+1
            print("dab beats paper. User wins.")
            print("User score is: ", user_score)
            print("Computer score is: ", computer_score)
            print(" ")

        if user_choice == "dab" and computer_choice == "default dance":
            user_score = user_score+1
            print("dab beats default dance. User wins.")
            print("User score is: ", user_score)
            print("Computer score is: ", computer_score)
            print(" ")

    #computer wins now

        if user_choice == "yeet" and computer_choice == "dab":
            computer_score = computer_score+1
            print("dab beats yeet. Computer wins.")
            print("Computer score is: ", computer_score)
            print("User score is: ", user_score)
            print(" ")
        
        if user_choice == "paper" and computer_choice == "dab":
            computer_score = computer_score+1
            print("dab beats paper. Computer wins.")
            print("Computer score is: ", computer_score)
            print("User score is: ", user_score)
            print(" ")

        if user_choice == "default dance" and computer_choice == "dab":
            computer_score = computer_score+1
            print("dab beats default dance. Computer wins.")
            print("Computer score is: ", computer_score)
            print("User score is: ", user_score)
            print(" ")
    #when dab wins for user/computer



    #when t-pose wins for user/computer
        if user_choice == "t-pose" and computer_choice == "dab":
            user_score = user_score+1
            print("t-pose beats dab. User wins.")
            print("User score is: ", user_score)
            print("Computer score is: ", computer_score)
            print(" ")

        if user_choice == "t-pose" and computer_choice == "paper":
            user_score = user_score+1
            print("t-pose beats paper. User wins.")
            print("User score is: ", user_score)
            print("Computer score is: ", computer_score)
            print(" ")

        if user_choice == "t-pose" and computer_choice == "default dance":
            user_score = user_score+1
            print("t-pose beats default dance. User wins.")
            print("User score is: ", user_score)
            print("Computer score is: ", computer_score)
            print(" ")

    #computer wins now

        if user_choice == "dab" and computer_choice == "t-pose":
            computer_score = computer_score+1
            print("t-pose beats dab. Computer wins.")
            print("Computer score is: ", computer_score)
            print("User score is: ", user_score)
            print(" ")

        if user_choice == "paper" and computer_choice == "t-pose":
            computer_score = computer_score+1
            print("t-pose beats paper. Computer wins.")
            print("Computer score is: ", computer_score)
            print("User score is: ", user_score)
            print(" ")

        if user_choice == "default dance" and computer_choice == "t-pose":
            computer_score = computer_score+1
            print("t-pose beats default dance. Computer wins.")
            print("Computer score is: ", computer_score)
            print("User score is: ", user_score)
            print(" ")
    #when t-pose wins for user/computer



    #when default dance wins for user/computer
        if user_choice == "default dance" and computer_choice == "rock":
            user_score = user_score+1
            print("default dance beats rock. User wins.")
            print("User score is: ", user_score)
            print("Computer score is: ", computer_score)
            print(" ")

        if user_choice == "default dance" and computer_choice == "scissors":
            user_score = user_score+1
            print("default dance beats scissors. User wins.")
            print("User score is: ", user_score)
            print("Computer score is: ", computer_score)
            print(" ")

        if user_choice == "default dance" and computer_choice == "yeet":
            user_score = user_score+1
            print("default dance beats yeet. User wins.")
            print("User score is: ", user_score)
            print("Computer score is: ", computer_score)
            print(" ")

    #computer wins now

        if user_choice == "rock" and computer_choice == "default dance":
            computer_score = computer_score+1
            print("default dance beats rock. Computer wins.")
            print("Computer score is: ", computer_score)
            print("User score is: ", user_score)
            print(" ")

        if user_choice == "scissors" and computer_choice == "default dance":
            computer_score = computer_score+1
            print("default dance beats scissors. Computer wins.")
            print("Computer score is: ", computer_score)
            print("User score is: ", user_score)
            print(" ")

        if user_choice == "yeet" and computer_choice == "default dance":
            computer_score = computer_score+1
            print("default dance beats yeet. Computer wins.")
            print("Computer score is: ", computer_score)
            print("User score is: ", user_score)
            print(" ")
    #when default dance wins for user/computer



    #when player mispells an option
        if user_choice!= "rock" and user_choice!= "paper" and user_choice!= "scissors" and user_choice!= "yeet" and user_choice!= "dab" and user_choice!= "t-pose" and user_choice!= "default dance" and user_choice!= "HELP":    
            print("User mispelled one of the choices. A point is deducted.")
            user_score = user_score - 1
            print("User score is now" , user_score)
            print("Computer score is still" , computer_score)
            print(" ")


#when user or computer wins
        if user_choice == "ctrl+alt+del" or user_choice == "Ctrl+Alt+Del":
            print("You won the game User! You won with ", user_score, " and the computer had ", computer_score)
            print(" ")
            game = input("Do you want to play again?")
            print(" ")
            computer_score = 0
            user_score = 0


        if user_score == 5:
            print("You won the game User! You won with ", user_score, " and the computer had ", computer_score)
            print(" ")
            game = input("Do you want to play again?")
            print(" ")
            computer_score = 0
            user_score = 0

        if computer_score == 5:
            print("You lost the game User. The computer won with ", computer_score, " and you had ", user_score)
            print(" ")
            game = input("Do you want to play again?")
            print(" ")
            computer_score = 0
            user_score = 0
#____________________________________________________________________________
if game == '2':
    
#____________________________________________________________________________
if game == '3':
    print ("Welcome to Chuzyaown Adventura")
    print("----PRESS START----")
    input()
    choice_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
    random_ch = random.SystemRandom()
    choice = random.choice(choice_list)
    print("What is thy name?")
    name = input()
    #____________________________________________________
    print ("-You wake up in an silent, barren, humid cave by yourself.-")
    print ("-There are 2 passage ways, numbered 1 and 2-")
    print ("-Choose to go through one of them.-")
    passage = input()
    #____________________________________________________PASSAGE 1
    if passage == '1':
        print("-You go through passage 1 and the end of the tunnel you suddenly slip and bang your head. RIP-")
    #____________________________________________________PASSAGE 2
    elif passage == '2':
        print("-You walk through the tunnel you see a light, as you reach it you are blinded by the light, as your eyes adjust to the light. You are attacked by a small weak looking goblin. What will you do?-")
        print("--Fight--")
        print("--Talk--")
        print("--Run--")
        choice1 = input().lower()
    #____________________________________________________FIGHT
        if choice1 == "fight":
            print("-You decided to punch the goblin. I will now roll the die. You rolled a "+ choice +".-")
    #____________________________________________________DEATH
        if choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5' or choice == '6':
            print("-You failed!-")
            print("-The Goblin dodges your punch and pushes you.-")
            print("-You fall and bang your head-")
            print("-Ha. RIP-")
#--------------------------------------------------------------------------------------------------------------------

#____________________________________________________ok roll
            if choice == '7' or choice == '8' or choice =='9' or choice =='10' or choice == '11' or choice =='12':
                print("-You punch the Goblin.-")
                print("-But your punch was weak.-")
                print("-The Goblin attacks back taking 25 health points from you.-")
                health = health - 25
                print ('-Your health is now-')
                print(health)
                print("-Will you attack again?-")
                choice4 =input().lower()
                if choice4 == "yes":
                    print("-You decided to attack the goblin. I will now roll the die again. You rolled a "+ choice +".-")
                #____________________________________________________DEATH
                if choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5' or choice == '6':
                    print("-You failed!-")
                    print("-The Goblin dodges your punch and pushes you.-")
                    print("-You fall and bang your head-")
                    print("-Ha. RIP-")
                    #____________________________________________________ok roll
                if choice == '7' or choice == '8' or choice =='9' or choice =='10' or choice == '11' or choice =='12':
                    print("-You punch the Goblin.-")
                    print("-But your punch was weak.-")
                    print("-The Goblin attacks back taking 25 health points from you.-")
                    health = health - 25
                    print ('-Your health is now-')
                    #____________________________________________________good roll
                if choice == '13' or choice == '14' or choice == '15' or choice == '16':
                    print("-Success!-")
                    print("-Your punch knocked the Goblin out-")
                    print("-Will you loot the Goblin?-")
                    choice3 =input().lower()
                    if choice3 == "yes":
                        print("-You found a rusty key-")
                    if choice3 == "no":
                        print("-THE GOBLIN JUMPS BACK UP AND ATTACKS YOU!-")
                        print("-YOU CAN'T REACT-")
                        print("-IT TEARS OUT YOUR THOUT AND YOU DIE-")
                        print("--RIP--")
                        #____________________________________________________great roll
                if choice == '17' or choice == '18' or choice == '19' or choice == '20':
                    print("-SUCCESS! CRITIKAL HIT!-")
                    print("-ONE PUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUCH!-")
                    print("-Your punch obliterated the Goblin-")
                    print("-You recieved a rusty key-")
                    print("-With the newly recieved key-")
                    print("-You are teleported to a tresure chest with three key holes choose one key hole-")
                    choice6 = input().lower()
                    if choice6 == "1":
                        print("-Congrats You won the game OWO WOW-")
                    if choice6 == "2" or choice6 == "2":
                        print("-OOF RIP YOU DIED INSTANTLY-")
#--------------------------------------------------------------------------------------------------------------------
#____________________________________________________good roll
            if choice == '13' or choice == '14' or choice == '15' or choice == '16':
                print("-Success!-")
                print("-Your punch knocked the Goblin out-")
                print("-Will you loot the Goblin?-")
                choice3 =input().lower()
                if choice3 == "yes":
                    print("-You found a rusty key-")
                    print("-With the newly recieved key-")
                    print("-You are teleported to a tresure chest with three key holes choose one key hole-")
                    choice6 = input().lower()
                    if choice6 == "1":
                        print("-Congrats You won the game OWO WOW-")
                    if choice6 == "2" or choice6 == "2":
                        print("-OOF RIP YOU DIED INSTANTLY-")
                if choice3 == "no":
                    print("-THE GOBLIN JUMPS BACK UP AND ATTACKS YOU!-")
                    print("-YOU CAN'T REACT-")
                    print("-IT TEARS OUT YOUR THROUT AND YOU DIE-")
                    print("--RIP--")
#____________________________________________________great roll
            if choice == '17' or choice == '18' or choice == '19' or choice == '20':
                print("-SUCCESS! CRITIKAL HIT!-")
                print("-ONE PUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUCH!-")
                print("-Your punch obliterated the Goblin-")
                print("-You recieved a rusty key-")
                print("-With the newly recieved key-")
                print("-You are teleported to a tresure chest with three key holes choose one key hole-")
                choice6 = input().lower()
                if choice6 == "1":
                    print("-Congrats You won the game OWO WOW-")
                if choice6 == "2" or choice6 == "2":
                    print("-OOF RIP YOU DIED INSTANTLY-")
#____________________________________________________TALK
    elif choice1 == "talk":
            print("-You decieded to talk to the Goblin.-")
            print("-What will you say?-")
            print("--A)Hello there!--")
            print("--B)Oi. U fok wot m8?--")
            print("--C)I mean no harm!--")
            choice2 = input().lower()
            if choice2 == "a":
                print("-THE GOBLIN JUMPS ON YOU AND KILLS YOU!-")
                print("-RIP-")
            if choice2 == "b":
                print("-The Goblin responds, ""Oi. m8. hoW yA arE BlOke?""-")
                print("""I fOuND thIS tiNG HeRRE. IzzA keY""")
                print("YoU CaN haVE iT!")
                print("-You take the key-")
            if choice2 == "c":
                print("-The Goblin runs off and leaves a rusty key.-")
                print("-With the newly recieved key-")
                print("-You are teleported to a tresure chest with three key holes choose one key hole-")
                choice6 = input().lower()
                if choice6 == "1":
                    print("-Congrats You won the game OWO WOW-")
                if choice6 == "2" or choice6 == "2":
                    print("-OOF RIP YOU DIED INSTANTLY-")
                
#____________________________________________________RUN
    elif choice1 == "run":
            print("-You decided to run.-")
            print("-Aaanndd. You know what happens?-")
            print("-You slip.....-")
            print("-and you fall taking 99% health damage-")
            print("-Will you continue to run?-")
            choice5 = input().lower()
            if choice5 == "yes":
                print("-You keep running and slip again this time taking only 1% damage.-")
                print("Hey what luck you only... Oh yeah.")
                print("-YOU'RE DEAD. LOL. RIP-")
            if choice5 == "no":
                print("-You stopped running -")
                print("-you hear foot steps getting closer and closer.-")
                print("-IT'S THE GOBLIN AND HE'S HERE FOR YOU!-")
                print("-He jumps on you and defeats you. RIP Coward-")
#____________________________________________________CLOSING SCENE
