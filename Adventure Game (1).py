# This is an adventurous game
import random
import time

#This function is to show winners that they have won
def won ():
    return print("you have won!!!!!!!")

#This function is to show losers that they have lost
def lost():
    return print("you have lost, so sad")
    time.sleep(2)

#This function is to restart the main function again
def restarting ():
    restart = input("Do you want to start again? (yes/no)").lower().strip()
    return restart


#This is the major function
def main():
    import random
    import time
    #This is the first part of the game asking if they are interested
    answer = input("would you like to play? (yes/no)")
    
    #To confirm and convert the answer to lower case and remove whitespace
    if answer.lower().strip() == "yes":

        list_ = ["You have reached a crossroads, would you like to go right? (yes/no) ", "You see a boat and a bike.would you pick a boat? (yes/no)", "You have encountered a monster, would you like to run (yes/no)" ]
        rand_list = random.choice(list_)

        if rand_list == "You have reached a crossroads, would you like to go right? (yes/no) ":
            answer = input("You have reached a crossroads, would you like to go right? (yes/no) ").lower(). strip()
            if answer == "yes": 
                answer = input ("You have encountered a monster, would you like to run (yes/no)")
                if answer == "yes":
                    print ("This was a bad choice, you lost!")
                    time.sleep(2)
                    lost()
                elif answer == "no":
                    print ("This is a good choice, you made it away safely.")
                    time.sleep(2)
                    
            elif answer == "no":
                print ("Bad choice, you lost!!")
                time.sleep(2)
                lost()

        elif rand_list == "You have encountered a monster, would you like to run (yes/no)":
            answer = input("You have encountered a monster, would you like to run (yes/no)").lower(). strip()
            if answer == "no":
                print ("This was a bad choice, you lost!")
                time.sleep(2)
                lost()
            elif answer == "yes":
                answer = input("You see a boat and a bike.would you pick a boat? (yes/no)")
                if answer == "no":
                    print("you are dead now, Game Over!!!")
                    time.sleep(2) 
                    lost()
                elif answer == "yes":
                    print ("This is a good choice, you made it away safely.")
                    time.sleep(2)

        elif rand_list == "You see a boat and a bike.would you pick a boat? (yes/no)":
            answer = input("You see a boat and a bike.would you pick a boat? (yes/no)")
            if answer == "yes":
                print("Unfortunatelly you do not know how to paddle a canoe. Game Over!!!")
                time.sleep(2)
                lost()
            elif answer == "no":
                answer = input("You have reached a crossroads, would you like to go right? (yes/no) ")
                if answer == "no":
                    print ("This was a bad choice, you lost!")
                    time.sleep(2)
                    lost()
                elif answer == "yes":
                    print("This is a good choice, you made it away safely.") 
    
    else: 
        print ("That is bad")
        time.sleep(2)

    restart = restarting()
    if restart == "yes":
        main()
    
    else:
        exit()       
        
main()