import random

COLORS = ["Red", "Green", "Blue", "Yellow"]
VALUES = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Skip", "Reverse", "Draw Two"]
WILDS = ["Wild", "Wild Draw Four"]

print("                                   RULES    ")
print("The rules are simple in UNO you have to put the same colour card as the top card")

print("Your goal is to finish your cards")





def build_deck():
    deck = []
    for color in COLORS:
        deck.append((color, "0"))
        for val in VALUES[1:]:
            deck.extend([(color, val), (color, val)])
    for wild in WILDS:
        deck.extend([("Wild", wild)] * 4)
    random.shuffle(deck)
    return deck

def is_valid_play(card, top_card, current_color):
    c_color, c_val = card
    t_val = top_card
    return c_color == "Wild" or c_color == current_color or c_val == t_val

def format_card(card):
    return card[1] if card[0] == "Wild" else f"{card[0]} {card[1]}"

def play_uno():
    deck = build_deck()
    player_hand = [deck.pop() for _ in range(7)]
    bot_hand = [deck.pop() for _ in range(7)]
    
    # Ensure starting card is not a Wild Draw Four
    discard = [deck.pop()]
    while discard[-1][1] == "Wild Draw Four":
        deck.insert(0, discard.pop())
        discard.append(deck.pop())
        
    current_color = discard[-1][0] if discard[-1][0] != "Wild" else random.choice(COLORS)
    turn = 0  # 0 = Player, 1 = Bot

    while player_hand and bot_hand:
        if not deck:
            top = discard.pop()
            deck = discard[:]
            random.shuffle(deck)
            discard = [top]

        top_card = discard[-1]
        print(f"\nTop Card: {format_card(top_card)} (Active Color: {current_color})")

        if turn == 0:
            print("Your Hand:")
            for idx, card in enumerate(player_hand, 1):
                print(f"  {idx}. {format_card(card)}")
            
            choice = input("Enter card number to play, or 'd' to draw: ").strip().lower()
            if choice == 'd':
                drawn = deck.pop()
                print(f"You drew: {format_card(drawn)}")
                if is_valid_play(drawn, top_card, current_color):
                    player_hand.append(drawn)
                else:
                    player_hand.append(drawn)
                    turn = 1
                continue

            if not choice.isdigit() or not (1 <= int(choice) <= len(player_hand)):
                print("Invalid input. Try again.")
                continue

            chosen_card = player_hand[int(choice) - 1]
            if not is_valid_play(chosen_card, top_card, current_color):
                print("Invalid move! Card must match active color, value, or be Wild.")
                continue

            player_hand.pop(int(choice) - 1)
            discard.append(chosen_card)
            current_color = chosen_card[0]

            if chosen_card[0] == "Wild":
                while True:
                    new_col = input("Choose a color (Red, Green, Blue, Yellow): ").strip().capitalize()
                    if new_col in COLORS:
                        current_color = new_col
                        break
            if chosen_card[1] == "Wild Draw Four":
                bot_hand.extend([deck.pop() for _ in range(4)])
                print("Bot draws 4 cards and loses its turn!")
            elif chosen_card[1] == "Draw Two":
                bot_hand.extend([deck.pop() for _ in range(2)])
                print("Bot draws 2 cards and loses its turn!")
            elif chosen_card[1] in ("Skip", "Reverse"):
                print(f"Bot's turn is skipped ({chosen_card[1]})!")
            else:
                turn = 1

        else:
            print(f"Bot has {len(bot_hand)} cards.")
            valid_cards = [c for c in bot_hand if is_valid_play(c, top_card, current_color)]
            if valid_cards:
                chosen_card = valid_cards[0]
                bot_hand.remove(chosen_card)
                discard.append(chosen_card)
                print(f"Bot played: {format_card(chosen_card)}")
                current_color = chosen_card[0]

                if chosen_card[0] == "Wild":
                    current_color = random.choice(COLORS)
                    print(f"Bot changed color to {current_color}!")
                if chosen_card[1] == "Wild Draw Four":
                    player_hand.extend([deck.pop() for _ in range(4)])
                    print("You draw 4 cards and lose your turn!")
                elif chosen_card[1] == "Draw Two":
                    player_hand.extend([deck.pop() for _ in range(2)])
                    print("You draw 2 cards and lose your turn!")
                elif chosen_card[1] in ("Skip", "Reverse"):
                    print(f"Your turn is skipped ({chosen_card[1]})!")
                else:
                    turn = 0
            else:
                drawn = deck.pop()
                bot_hand.append(drawn)
                print("Bot had no playable cards and drew a card.")
                turn = 0
    print("\n You Win!" if not player_hand else "\n Bot Wins!")

if __name__ == "__main__": 
    play_uno()