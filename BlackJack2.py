import random

def play_game():
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    game_is_over = False

    def card_picker():
        """This function will return a random card from the cards"""
        cards_value = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return random.choice(cards_value)

    def calculate_score(Player):
        """sum the cards of the players based on the condition"""
        if sum(Player) == 21 and len(Player):
            return 0
        while 11 in Player and sum(Player) > 21:
            Player.remove(11)
            Player.append(1)

        return sum(Player)

    def compare(u_score, c_score):
        if u_score == c_score:
            print("Draw 🙃")
        elif c_score == 0:
            print("Lose, opponent has BlackJack 😱")
        elif u_score == 0:
            print("Win with a BlackJack 🤩")
        elif u_score > 21:
            print("You went over. You lose 😭")
        elif c_score > 21:
            print("Opponent went over. You win 🤩")
        elif u_score > c_score:
            print("You win 🤩")
        else:
            print("You lose 😞")

    for i in range(2):
        user_cards.append(card_picker())
        computer_cards.append(card_picker())

    while not game_is_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your Cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score > 21 or user_score == 0 or computer_score == 0:
            game_is_over = True
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if another_card == 'y':
                user_cards.append(card_picker())
            else:
                game_is_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(card_picker())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand {user_cards}, final_score: {user_score}")
    print(f"Computer's final hand {computer_cards}, final_score: {computer_score}")
    compare(user_score, computer_score)



while input("Do you want to play a game of Blackjack type 'y' or 'n' : ").lower() == 'y':
    print("\n" * 20)
    play_game()
