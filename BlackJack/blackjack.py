import pygame
from random import shuffle
import time

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption('Blackjack')
#font = pygame.font.Font('C:\\WINDOWS\\FONTS\\ARIALBD.TTF', 32)
dt = 0
BACKSIDE = 'backside'
CARD_SCALE = 0.25

hit_rect = pygame.Rect(300, 250, 200, 50)
stand_rect = pygame.Rect(550, 250, 200, 50)
double_rect = pygame.Rect(800, 250, 200, 50)

font = pygame.font.SysFont(None, 30)
hit_text_surface = font.render('Hit', True, 'black')
stand_text_surface = font.render('Stand', True, 'black')
double_text_surface = font.render('Double', True, 'black')
hit_text_rec = hit_text_surface.get_rect(center=hit_rect.center)
stand_text_rec = stand_text_surface.get_rect(center=stand_rect.center)
double_text_rec = double_text_surface.get_rect(center=double_rect.center)


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

        #draw buttons
        draw_action_buttons()
        
        while True:
            # player's turn
            # wait for them to click a button
            # determine which button was clicked
            # evaluate between each hit
            # go until we bust, stand, or double
            
            # dealer's turn
            # if < 17, hit until >= 17
            # evaluate between each hit
            ...
        

        time.sleep(20)
        dt = clock.tick(60)

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
    if show_dealer_hand:
        #show both cards
        #update score
        display_cards(d, 'dealer')
    else:
        #2nd card is face down
        #update score, but dealer = ???
        display_cards([BACKSIDE] + d[1:], 'dealer')
        
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
        if card != 'BACKSIDE' and card != 'backside':
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
            
            filename = 'Blackjack/assets/' + rank + '_of_' + suit + '.png' 
        else:
            filename = 'Blackjack/assets/backside.png'
                       
        if player_hand:
            y_pos = 565
        else:
            y_pos = 100
        card_img = pygame.image.load(filename).convert_alpha()
        new_width = card_img.get_width() * CARD_SCALE
        new_height = card_img.get_width() * CARD_SCALE
        card_img = pygame.transform.scale(card_img, (int(new_width), int(new_height)))
        image_rect = card_img.get_rect()
        image_rect.center = (365 + image_rect.width * card_num, y_pos)
        card_num += 1       
        screen.blit(card_img, image_rect)
        pygame.display.flip()
        
def draw_action_buttons():
    pygame.draw.rect(screen, 'gray', hit_rect, 200)
    pygame.draw.rect(screen, 'gray', stand_rect, 200)
    pygame.draw.rect(screen, 'gray', double_rect, 200)
    screen.blit(hit_text_surface, hit_text_rec)
    screen.blit(stand_text_surface, stand_text_rec)
    screen.blit(double_text_surface, double_text_rec)
    pygame.display.flip()

def get_hand_value(hand):
    # gets the value of the hand passed
    
    aces = 0 #check our aces later, they'll be 1 and then at the end we'll see if they can be 10
    value = 0 #initialize hand value
    
    for card in hand:
        rank = card[0]
        if rank == 'A':
            aces += 1
        elif rank in ["J", "Q", "K"]:
            value += 10
        else:
            value += int(rank)
    
    # now add 1 for each ace
    value += aces
    
    for i in range(aces):
        if value + 10 <= 21:
            value += 10
    
    return value    
    
if __name__ == '__main__':
    main()