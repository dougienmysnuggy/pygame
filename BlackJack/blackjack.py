'''
Trying a blackjack game using pygame
'''

'''
- Draw background
- deal cards
    dealer cards at top of screen
    player cards at bottom
- player turn
    draw hit, stand, double, split buttons
    get input from user
    draw card, evaluate, keep getting user input until stand or bust
    each hit deals 1 new card and draws it on screen
- if no bust, dealer turn
    reveal face down card
    if <= 16 hit, else stand
    evaluate, determine winner
    if win, pay
- rinse, repeat until user quits or money = 0
'''


import pygame
from random import shuffle
import time

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption('Blackjack')
font = pygame.font.Font('C:\\WINDOWS\\FONTS\\ARIALBD.TTF', 32)
dt = 0
BACKSIDE = 'backside'
CARD_SCALE = 0.25


def main():
    running = True
    #generate a brand new deck (only 1 deck for now)
    deck = build_deck()
    
    # Main Loop
    while running:
        shuffle(deck) # eventually we'll add a card shoe for multiple decks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill('green')
        pygame.display.flip()
        
        #deal cards
        player_hand = []
        dealer_hand = []
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())
        display_hand(dealer_hand, player_hand, False)
        time.sleep(20)
        dt = clock.tick(60) / 1000

    pygame.quit() 
    
def build_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['c', 'd', 'h', 's']
    d = []
    
    for rank in ranks:
        for suit in suits:
            d.append((rank, suit))
    return d

def display_hand(d, p, show_dealer_hand):
    #show dealer's hand
    #if show_dealer_hand:
        #show both cards
        #update score
    display_cards(d, 'dealer')
    #else:
        #2nd card is face down
        #update score, but dealer = ???
    #    display_cards([BACKSIDE] + d[1:])
        
    #show player's hand
    #print('Player:', get_hand_value(p))
    display_cards(p, 'player')
    
def display_cards(hand, turn):
    '''
    get filename
    load img = filename
    rect for img
    show card image
    '''
    card_num = 1
    for card in hand:
        if turn == 'player':
            player_hand = True
        else:
            player_hand = False
        #build file name
        if card[0] == 'J':
            rank = 'jack'
        elif card[0] == 'Q':
            rank = 'queen'
        elif card[0] == 'K':
            rank = 'king'
        elif card[0] == 'A':
            rank = 'ace'  
        else:
            rank = str(card[0])
        
        if card[1] == 'c':
            suit = 'clubs'
        elif card[1] == 's':
            suit = 'spades'
        elif card[1] == 'h':
            suit = 'hearts'
        elif card[1] == 'd':
            suit = 'diamonds'
        if player_hand:
            y_pos = 565
        else:
            y_pos = 100
            
        filename = 'blackjack\\assets\\' + rank + '_of_' + suit + '.png'
        card_img = pygame.image.load(filename).convert_alpha()
        new_width = card_img.get_width() * CARD_SCALE
        new_height = card_img.get_width() * CARD_SCALE
        card_img = pygame.transform.scale(card_img, (int(new_width), int(new_height)))
        image_rect = card_img.get_rect()
        image_rect.center = (365 + image_rect.width * card_num, y_pos)
        card_num += 1       
        screen.blit(card_img, image_rect)
        pygame.display.flip()

def get_hand_value(hand):
    ...
    
if __name__ == '__main__':
    main()