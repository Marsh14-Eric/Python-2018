import random
import time

#getting user name
name = input("Hello there! What is your name? ")

#setting up responses
response_1 = "Yes"
response_2 = "No"
response_3 = "Not Sure"
response_4 = "Probably"
response_5 = "You will find out soon"
response_6 = "Most Definitly"

#randoms
answers = [response_1, response_2, response_3, response_4, response_5, response_6]

while True:
    #questions
    input("What is your question ")
    
    #give a answers
    print( name + " the answer is " + random.choice(answers))

    #close
    cmd = input("Would you like to [c]ontinue or e[x]it? " )
    if cmd == "x":
        print("Thanks for playing Magic 8 Ball! ")
        break
    elif cmd == "c":
        continue
    else:
        print("Thanks for playing Magic 8 Ball! ")
        break
