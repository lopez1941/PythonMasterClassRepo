# so your challenge here ow is to change the blackjack module to include a function called play that's a responsible
# ultimately for allowing or running the code that starts the game so you want to test that the play function can be
# used to start the game when the module is imported so again change the blackjack module itself to include a function
# play and that function should be responsible for actually running the code that starts the game then test the play
# function can be used to start the game when the module is imported that your way of knowing that things are working
# as they should so go away and city and see if you can figure that out and when you ready to come back ou can come
# back and check our solutions so pause the video now....
# ok so moving on now the challenge and its going to be quite a simple one the challenges is to add a new button to
# the program with the text new game now the button should call a function that clears the cards from the screen it
# resets the players and dealers hands and then starts a new game now the easiest way to clear the contents of a frame
# is to destroy the frame and create a new one with the same name and in fact that's why the program has a player_card_
# frame and dealer_card_frame inside the card frame itself so that's it go away and create a new button with the text
# new game and again the functionality clear the cards from the Screen reset the player and dealers hands and then
# start a new game so pause the video go away and see if you can come up with a solution and when you're ready to see
# our version of it come back and and I'll go through that with you pause the video now.....

import tkinter
import random


def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']

    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'

    # for each suit, retrieve the image for the cards
    for suit in suits:
        for card in range(1, 11):
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image))

    # face cards
    for card in face_cards:
        name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
        image = tkinter.PhotoImage(file=name)
        card_images.append((10, image))


def _deal_card(frame):
    # pop card off top of deck
    next_card = deck.pop(0)
    # add that card to the bottom of the deck
    deck.append(next_card)
    # add the image to a label and display the label
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')  # using pack since it's perfect to stack cards next to each other
    # now return the card's face value
    return next_card


def score_hand(hand):
    # calculate score, only one ace can be 11, goes to 1 if the hand busts
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_dealer():
    dealer_score = score_hand(dealer_hand)

    while 0 < dealer_score < 17:
        dealer_hand.append(_deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)

    if player_score > 21:
        result_text.set("Dealer Wins!")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player Wins!")
    elif dealer_score > player_score:
        result_text.set("Dealer Wins!")
    else:
        result_text.set("Draw!")


def deal_player():
    player_hand.append(_deal_card(player_card_frame))
    player_score = score_hand(player_hand)
    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Wins!")


def create_card_frames():
    global dealer_card_frame
    global player_card_frame
    global player_score_label
    # embedded frame for card images
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

    player_score_label = tkinter.IntVar()

    tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
    tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)

    # embedded frame for card images
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)


def init_hands():
    global player_hand
    global dealer_hand
    player_hand = []
    dealer_hand = []


def new_game():

    player_card_frame.destroy()
    dealer_card_frame.destroy()

    create_card_frames()
    result_text.set("")
    initial_deal()


def initial_deal():
    init_hands()
    deal_player()
    dealer_hand.append(_deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()


def shuffle_cards():
    global deck
    random.shuffle(deck)


def play():
    initial_deal()
    mainWindow.mainloop()


mainWindow = tkinter.Tk()

# set up the screen and frames for the dealer and player
mainWindow.title("Black Jack")
mainWindow.geometry("640x480")
mainWindow.configure(background='green')

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief='sunken', borderwidth=1, background='green')
card_frame.grid(row=1, column=0, stick='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

# embedded frame for card images
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

player_score_label = tkinter.IntVar()

tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)

# embedded frame for card images
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, sticky='w')

# remember with 'command' you have to assign a function, you can't pass a parameter when calling the function from \
# command or you're actually assigning the result, not the function itself
dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="Player", command=deal_player)
player_button.grid(row=0, column=1)

reset_button = tkinter.Button(button_frame, text="New Game", command=new_game)
reset_button.grid(row=0, column=2)

shuffle_button = tkinter.Button(button_frame, text="Shuffle", command=shuffle_cards)
shuffle_button.grid(row=0, column=3)

# load cards
cards = []
load_images(cards)
print(cards)


# create a new deck of cards and shuffle them
deck = list(cards)
print(deck)
shuffle_cards()


player_hand = []
dealer_hand = []

if __name__ == "__main__":
    play()

