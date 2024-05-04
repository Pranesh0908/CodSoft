import random

user_score=0
computer_score=0
option='yes'

while(option=='yes'):

    def winner(user_choice,computer_choice):

        global user_score
        global computer_score

        if (user_choice=='rock' and computer_choice=='scissors') or (user_choice=='paper' and computer_choice=='rock') or (user_choice=='scissors' and computer_choice=='paper'):
            print('\nYou win!')
            user_score=user_score+1
            
        elif(user_choice==computer_choice):
            print("\nIt's a tie")

        else:
            print('\nYou lose!')
            computer_score+=1
        
        print(f"\nScore - You:{user_score} Computer:{computer_score}")


    print("\nRock👊 Paper🖐️  Scissors✌️ !")
    user_choice=input("Choose rock,paper,scissors:").lower()

    option1=1
    while option1==1:

        if user_choice in ['rock','paper','scissors']:
            break
        else:
            print('Invalid choice. Please choose rock,paper,scissors.')
            user_choice=input('Choose rock,paper,scisoors:')
            
            if user_choice in ['rock','paper','scissors']:
                option1=0

    computer_choice=random.choice(['rock','paper','scissors'])

    print("\nYour choice:",user_choice)
    print("Computer choice:",computer_choice)
    winner(user_choice,computer_choice)
    option=input("Do you want to continue (yes or no):")

print("Thanks for playing!")