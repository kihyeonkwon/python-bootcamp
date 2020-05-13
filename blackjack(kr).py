import random
import time

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}


class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self): return self.rank + " of "+self.suit


class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has : " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips():

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:

        try:
            chips.bet = int(input("How many chips to bet?"))
        except:
            print("Please provide an integer")
        else:
            if chips.bet > chips.total:
                print("Not enough chips")
            else:
                break


def hit(deck, hand):
    new_card = deck.deal()
    hand.add_card(new_card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing
    while True:
        a = input("Hit or Stand?")
        if a.upper() == 'HIT':
            hit(deck, hand)
            print("player draws a new card!! ")
            time.sleep(2)
            print("it's...")
            time.sleep(2)
            print(f'Player draws {player_hand.cards[2]}!!!')
            time.sleep(2)
            print(f"player's score is {player_hand.value}")
            time.sleep(2)
            if player_hand.value > 21:
                print("BUST!!!!")
                break
            else:
                continue

        elif a.upper() == 'STAND':
            print("Player stands! Dealer's turn")
            time.sleep(3)
            playing = False
            break

        else:
            print("please type 'hit' or 'stand'.")
            continue


def show_some(player, dealer):
    print("******************************")
    print("Dealer's card is {}".format(dealer.cards[0]))
    time.sleep(2)
    print("dealer's card is hidden")

    time.sleep(2)

    for card in player.cards:
        print(f"Player's card is {card}")
        time.sleep(2)
    print(f"player's score is {player_hand.value}")
    print("******************************")
    time.sleep(2)


def show_all(player, dealer):
    print("******************************")
    for card in player.cards:
        print(f"Player's card is {card}")
        time.sleep(1)
    print(f"Player's score is {player_hand.value}")

    if player_hand.value == 21:
        print("BLACKJACK!!!")
    time.sleep(3)

    for card in dealer.cards:
        print(f"Dealer's card is {card}")
        time.sleep(2)
    time.sleep(1)
    print(f"Dealer's score is {dealer_hand.value}")
    if dealer_hand.value == 21:
        print("BLACKJACK!!!")
    time.sleep(3)

    print("******************************")


def player_busts(player, dealer, chips):
    print("Bust player!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print('Win player!')
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Player wins! Dealer busted!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print('Dealer wins!!')
    chips.lose_bet()


def push(player, dealer):
    print('Dealer and player tie! PUSH')


print("나는 지금 강원랜드의 블랙잭 테이블에 앉아있다")
time.sleep(3)
player_chips = Chips(500)
print("좆되버린 인생.. 마지막 남은 전재산을 털어 500칩으로 바꿨다..")
highest_chip = player_chips.total
time.sleep(3)
print("마지막으로 좋은 시간이라도 보내고 가자 :)")
time.sleep(2)
print("10,000칩 이상 따면 빚을 갚고 새인생을 시작할 수 있어!!!")
time.sleep(2)
print("'당신의 운명은?:)'")
time.sleep(3)

sexslave = 0

while True:

    deck = Deck()
    deck.shuffle()
    print("딜러가 카드를 섞는다...")
    time.sleep(3)

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    print("카드 두장을 받았다!")
    time.sleep(2)

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    print("딜러가 카드 두장을 받았다!")
    time.sleep(2)
    dealer_hand.add_card(deck.deal())
    print(f"나한테는 {player_chips.total} 칩이 있다..")

    take_bet(player_chips)

    playing = True
    show_some(player_hand, dealer_hand)

    while playing:
        hit_or_stand(deck, player_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

        if player_hand.value <= 21:
            print("딜러가 패를 공개한다")
            time.sleep(2)

            for card in dealer.cards:
                print(f"Dealer's card is {card}")
                time.sleep(2)
                print(f"Dealer's score is {dealer_hand.value}")
                if dealer_hand.value == 21:
                    print("BLACKJACK!!!")
                    time.sleep(3)

            while dealer_hand.value < 17:
                print("딜러가 고민중이다...")
                time.sleep(6)
                print("딜러가 히트한다!")
                time.sleep(3)
                hit(deck, dealer_hand)
                print(f"딜러는  {dealer_hand.cards[-1]}를 뽑는다!")
                if dealer_hand.value > player_hand.value:
                    break
                else:
                    continue

            print("딜러가 고민중이다...")
            time.sleep(5)
            print("딜러가 웨이브한다! 카드를 깔 시간이다")
            time.sleep(1)

            show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
            if player_chips.total == 21:
                print("You win double for BLACKJACK!")
                player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)
        break

    time.sleep(3)
    print('\n Player total chips are at: {}'.format(player_chips.total))
    if player_chips.total > highest_chip:
        highest_chip = player_chips.total
        print(f"New record! You have {highest_chip} chips!")

    if player_chips.total > 10000:
        print("WOW! You have driven our casino to bankruptcy!")
        time.sleep(2)
        print("The next 216 digits is the secret of the universe. Congratulations!")
        time.sleep(2)
        print("94143243431512659321054872390486828512913474876027671959234602385829583047250165232525929692572765536436346272718401201264314754632945012784726484107562234789626728592858295347502772262646456217613984829519475412398501")

    elif player_chips.total == 0:
        print("You have fucked up! You are broke and now your life belongs to us!")
        time.sleep(2)
        print("Would you like to become a sexslave?")
        time.sleep(2)
        answer = input("Yes or No?")
        if answer[0].lower() == 'y':
            sexslave += 1
            print("You work as a sexslave for the rest of the night")
            print(f"You are now sexslave level {sexslave}")
            time.sleep(3)
            player_chips = Chips(sexslave * 100)
            print(sexslave*100+" chips received as a tip!")
            time.sleep(3)
            print("Let's go again!")

        else:
            print("Hahahahahahahaha")
            time.sleep(3)
            print("You thought you had an option?")
            time.sleep(2)
            print("Very funny!!!")
            time.sleep(2)
            print("You will become a sexslave for the rest of your life.")
            time.sleep(2)
            print("GAME OVER")
            time.sleep(2)
            print("GAMBLING IS AN ADDICTION. National Gambling Helpline (0808 8020 133)")

    else:
        time.sleep(1)
        new_game = input("Play again?")
        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            print("Thank you for playing!")
            print(f"Your highest chips are {highest_chip} chips!")
            if sexslave != 0:
                print(f"You worked as a sexslave for {sexslave} nights!")
            time.sleep(2)
            print("We will be waiting for you again! :)")
            break
