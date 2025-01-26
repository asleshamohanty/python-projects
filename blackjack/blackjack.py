import random
import os

def dealcards():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
  
def blackjack():
  if sum(computer_cards) == 21:
    print("Computers score is: ", sum(computer_cards), "\n")
    print("You lose!")
  elif sum(user_cards) == 21:
    print("You win!")

def changevalue(cards):
  if 11 in cards:
    if sum(cards) > 21:
      cards.remove(11)
      cards.append(1)

def over21(cards):
   if sum(cards) > 21:
      print("You lose!")

continue_game = True

while continue_game:

    print("Get ready to play BlackJack!!")
    option = input("Do you want to start? (y/n): ")

    if option == "y":
        
        user_cards = []
        computer_cards = []
        for i in range(2):
            user_cards.append(dealcards())
            computer_cards.append(dealcards())
        print("Your cards are: ", user_cards, "\n")
        print("Computers first card is: ", computer_cards[0], "\n")
        blackjack()
        changevalue(user_cards)
        changevalue(computer_cards)
        blackjack()

        more = True
        while more:
            draw_more = input("Do you want to draw another card? Type 'y' or 'n': ")
            if draw_more == "y":
                user_cards.append(dealcards())
                print("Your cards are: ", user_cards, "\n")
                blackjack()
                if sum(user_cards) > 21:
                    print("You went over 21, You lose!!")

            else:
                while sum(computer_cards) < 16:
                    computer_cards.append(dealcards())
                    if sum(computer_cards) > 21:
                        print("Computer went over 21, You win!!")
            more = False

        if sum(user_cards) != 21:
            if sum(user_cards) > sum(computer_cards):
                print("Computers score is: ", sum(computer_cards), "\n")
                print("Your score is: ", sum(user_cards), ", You win!!\n")
            elif sum(user_cards) < sum(computer_cards):
                print("Computers score is: ", sum(computer_cards), "\n")
                print("Your score is: ", sum(user_cards), ", You lose!!\n")
            else:
                print("Its a draw!!")
        

        replay = input("Do you want to play again? (y/n):")
        if replay == "y":
            os.system('cls')
            continue_game = True
        elif replay == "n":
            continue_game = False