import random
computer_number=random.randint(1,50)

tries=0
while tries<=5 :
    player_number=int(input("Enter your guessed number : "))
    tries+=1

    if player_number<computer_number:
        print("missed!\nYou are too low")
    elif player_number>computer_number:
        print("missed!\nYou are too high")
    else:
        print("You win!\nYou guessed right.")
        break
print()

print("the secret number was",computer_number)
    
