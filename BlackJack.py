import random
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
cards_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



def check(player, computer):
    if player > 21 or player < computer:
        print("You loss")
    elif computer > 21 or player > computer:
        print("You win")
    else:
        print("Draw")


def card_sum(player):
    A_check = False
    card_sum = 0

    for i in player:
        if i == 'A':
            A_check = True
        else:
            card_sum += cards_value[cards.index(i)]
    if A_check:
        if (card_sum + 11) > 21:
            card_sum += 1
        else:
            card_sum += 11

    return card_sum



yes = True
def main():
    global yes
    while yes:
        player_cards = random.sample(cards, 2)
        computer_cards = random.sample(cards, 2)
        # print()

        print(f"Your cards: {player_cards}")
        print(f"Computer's first card: {computer_cards[0]}")

        another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if another_card == 'y':
            player_cards.append(random.choice(cards))

        player_card_sum = card_sum(player_cards)
        computer_card_sum = card_sum(computer_cards)
        print(f"player_cards: {player_cards}")
        print(f"computer_cards: {computer_cards}")
        check(player_card_sum, computer_card_sum)

        response = input("Do you want to play a game of Blackjack type 'y' or 'n' : ").lower()
        if response == 'n':
            yes = False
        else:
            print("\n" * 20)


main()





