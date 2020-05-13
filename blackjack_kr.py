import random
import time
import sys

suits = ('하트', '다이아', '스페이드', '클로버')
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
            chips.bet = int(input("돈을 얼마나 걸까?"))
        except:
            print("정수를 입력해야지")
        else:
            if chips.bet > chips.total:
                print("돈이 모자란데")
            else:
                break


def hit(deck, hand):
    new_card = deck.deal()
    hand.add_card(new_card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing
    double = 0
    while True:
        a = input("히트 or 스탠드 or 더블다운 or 스플릿. 설명이 필요하면 '설명'을 입력해주세요. ")
        if a.upper() == '히트':
            double = 1
            hit(deck, hand)
            print("한장더!!! ")
            time.sleep(2)
            print("새 카드는...")
            time.sleep(2)
            print(f'{player_hand.cards[-1]}!!!')
            time.sleep(2)
            print(f"이제 내 점수는 {player_hand.value}..")
            time.sleep(1)
            if player_hand.value > 21:
                print("버스트?!!!!")
                break
            else:
                continue

        elif a.upper() == '스탠드':
            print("스탠드! 딜러 까보시지!!")
            time.sleep(3)
            playing = False
            break

        elif a.upper() == '더블다운':
            if double == 0 and player_chips.total >= 2*player_chips.bet:
                print("더블다운! 가즈아~!!")
                player_chips.bet = 2 * player_chips.bet
                time.sleep(2)
                print('판돈은 두배가 됐다.')
                time.sleep(2)
                player_hand.add_card(deck.deal())
                player_hand.adjust_for_ace()
                time.sleep(2)
                print("새 카드는...")
                time.sleep(2)
                print(f'{player_hand.cards[-1]}!!!')
                time.sleep(2)
                print(f"이제 내 점수는 {player_hand.value}..")
                time.sleep(1)
                if player_hand.value > 21:
                    print("버스트?!!!!!!")
                    break
                else:
                    pass

            else:
                print('이미 히트를 했거나 돈이 모자라서 할 수 없다.')
                time.sleep(2)

        elif a.upper() == '스플릿':
            if values[player_hand.cards[0].rank] == values[player_hand.cards[1].rank] and player_chips.total >= 2*player_chips.bet:
                print("스플릿!")
                time.sleep(2)
                player_chips.bet = 2 * player_chips.bet
                print('판돈은 두배가 됐다.')
                a = deck.deal()
                b = deck.deal()
                print('새로나온 카드는...')
                time.sleep(2)
                print(a)
                time.sleep(2)
                print(b)
                time.sleep(2)
                a = values[deck.deal().rank]
                b = values[deck.deal().rank]
                if a > b:
                    player_hand.value = player_hand.value/2 + a
                else:
                    player_hand.value = player_hand.value/2 + b
                print(f"이제 내 유리한 점수는 {player_hand.value}..")
                time.sleep(1)
            else:
                print("카드가 같지 않거나 돈이 부족하기 때문에 스플릿 할 수 없다.")
                continue

        elif a.upper() == '설명':
            print("'히트'는 카드를 한장 더 받게 됩니다. 21이 넘어가면 '버스트'하여 죽습니다. \n '스탠드'는 카드를 받지 않고 여기서 턴을 끝냅니다. \n '더블다운'은 판돈을 두배로 늘리고 카드를 한장만 더 받게됩니다. \n '스플릿'은 같은 카드 두장이 나왔을때 판돈을 두배로 걸고 새로 카드를 두장 더 뽑아 유리한쪽을 사용합니다. \n ")

        else:
            print("'히트' '스탠드' '더블다운' '스플릿' 중에서 골라주세요 ^~^")
            continue


def show_some(player, dealer):
    print("******************************")
    print("딜러의 카드는 \n{}".format(dealer.cards[0]))
    time.sleep(2)
    print("한장은 덮어져 있다.")

    time.sleep(2)
    print("내 카드는")
    for card in player.cards:
        print(f"{card}")
        time.sleep(2)
    print("이다..")
    time.sleep(0.5)
    print(f"내 점수는 {player_hand.value}이다...")
    print("******************************")
    time.sleep(2)


def show_all(player, dealer):
    print("******************************")
    print("내 카드는")
    for card in player.cards:
        print(f"{card}")
        time.sleep(2)
    print(f"내 점수는 {player_hand.value}이다...")

    if player_hand.value == 21:
        print("BLACKJACK!!!")
    time.sleep(3)
    print("딜러의 카드는")
    for card in dealer.cards:
        print(f"{card}")
        time.sleep(2)
    time.sleep(1)
    print(f"Dealer's score is {dealer_hand.value}")
    if dealer_hand.value == 21:
        print("BLACKJACK!!!")
    time.sleep(3)

    print("******************************")


def player_busts(player, dealer, chips):
    print("내가 버스트라니!!!!!!!!!!!")
    chips.lose_bet()


win = 0


def player_wins(player, dealer, chips):
    global win
    exclaim = ["이겼다!!!! 운명은 내 편이야!!!!!", "역시 나야!!! 다 알고한거야!!!!",
               "가즈아 가즈아 가즈아!!!!!", "진작에 카지노나 올껄!!!!!!"]
    print(exclaim[win % 4])
    win += 1
    time.sleep(0.5)
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("딜러가 버스트 당했어!!!! ㅋㅋㅋㅋㅋㅋ 븅신ㅋㅋㅋㅋ")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print('씨발.. 내 인생..')
    chips.lose_bet()


def push(player, dealer):
    print('아!!! 이점수에 동점?!?!')
    time.sleep(2)
    print("하아 아깝다.. 한끗만 더 나와주면 대박 터질것같다...")


def check_blackjack(player_hand, dealer_hand):
    global con
    if player_hand.value == 21 and dealer_hand.value != 21:
        print("블랙잭이다!!!!!!!!!!!!!!!!!!! 따블로 먹는다!!!!!!!")
        player_wins(player_hand, dealer_hand, player_chips)
        player_wins(player_hand, dealer_hand, player_chips)
        time.sleep(3)
        print("요시! 오늘밤 느낌 좋구여!!!")
        time.sleep(2)
        con = 1

    elif player_hand.value != 21 and dealer_hand.value == 21:

        time.sleep(3)
        print("딜러가 패를 공개한다")
        time.sleep(2)
        for card in dealer_hand.cards:
            print(f" {card} ")
            time.sleep(2)
        time.sleep(2)
        print("블랙잭이잖아!!!! 사기아냐?????")
        dealer_wins(player_hand, dealer_hand, player_chips)
        time.sleep(3)
        con = 1

    elif player_hand.value == 21 and dealer_hand.value == 21:
        print("오!!!!!!!!!!!블랙잭!!!!!!!!!!!! ")
        time.sleep(2)
        print("딜러가 패를 공개한다")
        for card in dealer_hand.cards:
            print(f" {card} ")
            time.sleep(2)
        print("딜러도 블랙잭이다!!!!")
        time.sleep(2)
        print("?????????????????")
        time.sleep(2)
        con = 1
    else:
        pass


reset = 0

while reset == 0:
    print("나는 지금 강원랜드의 블랙잭 테이블에 앉아있다")
    time.sleep(3)
    player_chips = Chips(500)
    print("좆되버린 인생.. ")
    highest_chip = player_chips.total
    time.sleep(3)
    print("창창하던 내인생은 이더리움과 신라젠으로 인해 구렁텅이로 빠지고 말았다. ")
    time.sleep(3)
    print("운전해온 차를 팔아서 생긴 마지막 남은 전재산인 500만원...")
    time.sleep(2)
    print("요시! 오늘 밤 5000만원 이상 따면 빚을 갚고 새인생을 시작할 수 있어!!!")
    time.sleep(3)
    print("그렇지만 돈을 다 잃으면 섬노예로 팔려간다는 소문도 있다..")
    time.sleep(3)
    print("천사들의 섬으로...")
    time.sleep(5)

    sexslave = 0
    sexslavetotal = 0

    while True:

        deck = Deck()
        deck.shuffle()
        print("딜러가 카드를 섞는다...")
        time.sleep(2)

        print(f"나한테는 {player_chips.total} 만원이 있다..")
        time.sleep(2)

        take_bet(player_chips)

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())
        print("카드 두장을 받았다!")
        time.sleep(1)

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        print("딜러가 카드 두장을 받았다!")
        time.sleep(1)
        dealer_hand.add_card(deck.deal())

        playing = True
        player_hand.adjust_for_ace()
        show_some(player_hand, dealer_hand)
        con = 0

        while playing:
            check_blackjack(player_hand, dealer_hand)

            if con == 1:

                break

            hit_or_stand(deck, player_hand)

            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                break

            if player_hand.value <= 21:
                print("딜러가 패를 공개한다")
                time.sleep(2)
                print("딜러는")

                for card in dealer_hand.cards:
                    print(f" {card} ")
                    time.sleep(2)
                print("를 갖고 있다.")
                time.sleep(1)
                print(f"딜러의 점수는 {dealer_hand.value}이다..")
                time.sleep(2)
                if dealer_hand.value == 21:
                    print("21이다!!!!")
                    time.sleep(2)

                while dealer_hand.value < 17:
                    print("딜러가 히트한다!")
                    time.sleep(2)
                    hit(deck, dealer_hand)
                    print(f"딜러는  {dealer_hand.cards[-1]}를 뽑는다!")
                    time.sleep(1)
                    print(f"딜러의 점수는 이제 {dealer_hand.value}이다...")
                    time.sleep(2)
                    if dealer_hand.value > player_hand.value:
                        break
                    else:
                        continue

                time.sleep(1)

            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
                if player_chips.total == 21:
                    print("21이다!!!")

            else:
                push(player_hand, dealer_hand)
            break
        time.sleep(3)
        print('\n 나의 돈은 현재: {}만원'.format(player_chips.total))
        if player_chips.total > highest_chip:
            highest_chip = player_chips.total
            print(f"떡상했다!!  {highest_chip} 만원이야!!")

        if player_chips.total >= 3000:
            print("돈 다 모았다!!!!!")
            break

        elif player_chips.total == 0:
            print("천사 : 안녕하세요")
            time.sleep(2)
            answer = input("섬노예로 일할래? (예/아니오)")
            if answer.lower() == 'y' or answer.lower() == '응' or answer.lower() == '네' or answer.lower() == '예' or answer.lower() == 'ㅇ':
                pass

            else:

                time.sleep(3)
                print("천사: 선택이 있는 줄 알았어?")
                time.sleep(2)

            sexslave += 10

            print("나는 섬노예로 팔려갔다.")
            time.sleep(1)
            print(f"나는 이제 섬노예다.")
            time.sleep(2)
            print(f"{sexslave}년간 뙤약볕에서 녹초가 되도록 나는 소금만 말렸다.")

            time.sleep(2)
            if sexslave > 30:
                while True:
                    print('앞이 갑자기 까맣다')
                    time.sleep(3)
                    print('총 60년이 넘는 세월동안 염전노예로 생활하며 쌓인 피로가 ')
                    time.sleep(3)
                    print('누적되버린것같다.')
                    time.sleep(2)
                    print(f"당신의 최고 기록은 {highest_chip} 만원입니다!")
                    print(f"당신은 {sexslavetotal}년동안 섬노예로 일했습니다!")
                    time.sleep(2)
                    print("소금 잘 먹을게요 :)")
                    sys.exit()

            time.sleep(2)
            print(f"주인님들의 눈초리를 피해 나는 조금씩조금씩 소금을 쌔벼두었다.")
            sexslavetotal = sexslavetotal + sexslave
            time.sleep(2)
            print(f"어느날 주인님들이 자는 틈을타 나는 육지로 도망쳐 나왔다.")
            time.sleep(2)
            player_chips = Chips(sexslave * 50)
            print("죽을 각오로 모은 소금을 팔아 "+str(sexslave*50) +
                  "만원을 구했다")
            time.sleep(2)
            if player_chips.total > highest_chip:
                highest_chip = player_chips.total
                print(f"{highest_chip} 만원.. 내가 평생 벌어본 가장 큰 돈이다!!!")
            time.sleep(2)
            print("다시는 이런일을 겪어서는 안될 것 같다... ")
            time.sleep(2)
            print("그러기 위해선 돈이 있어야돼...")
            time.sleep(2)
            print("본전 회복하러 강원랜드로 가즈아!!!!!")
            time.sleep(2)
            print("도박은 중독입니다. 도박문제 전화·온라인 상담(도박문제 헬프라인 1336(무료)/넷라인)")
            time.sleep(1)
            print(f"당신의 최고 기록은 {highest_chip} 만원입니다!")
            print(f"당신은 총 {sexslavetotal}년동안 섬노예로 일했습니다!")
            time.sleep(1)

        else:
            time.sleep(1)
            print("조금만 더 하면 빚을 갚을 수 있을 거 같다? 'ㅇ' \n 정신차리고 집으로 가자.. 'ㄴ'")
            new_game = input()
            if new_game[0].lower() == 'y' or new_game[0].lower() == '응' or new_game[0].lower() == 'd' or new_game[0].lower() == '예'or new_game[0].lower() == 'ㅇ':
                playing = True
                print("도박은 중독입니다. 도박문제 전화·온라인 상담(도박문제 헬프라인 1336(무료)/넷라인)")
                time.sleep(2)
                print(
                    f"최고기록 {highest_chip}, 섬노예로 보낸 기간 {sexslavetotal}년 ")
                continue
            else:
                print("와줘서 감사합니다!")
                print(f"당신의 최고 기록은 {highest_chip} 만원입니다!")
                if sexslave != 0:
                    print(f"당신은 {sexslavetotal}년동안 섬노예로 일했습니다!")
                time.sleep(2)
                print("다시 오세요~ ! :)\n win + shift + s 키로 스크린샷을 찍어 당신의 기록을 공유하세요!")
                time.sleep(3)
                print("나는 카지노를 나와 상쾌한 강원도의 공기를 마셨다.")
                time.sleep(2)
                print(
                    f"그래! {player_chips.total}만원? 이정도 돈으로 나온 내가 자랑스러워! 이제 다시 새로운 출발을 해보자!")
                time.sleep(3)
                print("나는 서울에 돌아오자마자 비트코인에 전재산을 때려박았다.")
                time.sleep(3)
                print("이틀만에 재산의 절반을 잃었고...")
                time.sleep(2)
                print("난 다시 강원도로 돌아왔다..")
                time.sleep(2)
                player_chips.total = int(player_chips.total / 2)
                print(f"잘못된 선택으로 반토막이 난 재산...{player_chips.total}만원... ")
                time.sleep(2)
                print("그렇지만..")
                time.sleep(3)
                print("왠지 오늘은 운이 좋을 것 같다. ")
                time.sleep(2)
                print(
                    "도박은 중독입니다. 도박문제 전화·온라인 상담(도박문제 헬프라인 1336(무료)/넷라인) \n 제작자 : https://github.com/kihyeonkwon")
                time.sleep(2)

    print("됐다!! 이 돈이면 빚을 다 갚고 새출발을 할 수 있어!!!")
    time.sleep(2)
    print("500만원으로 시작해서 5000만원까지 왔구나..")
    time.sleep(2)
    print("열배나 늘렸어!! 오늘같은 밤을 두번만 더하면 50억??!!! 한남동에 저택 사는거 아니야???")
    time.sleep(4)
    a = input("'한남동 대저택을 노린다' or '빚만 갚고 0원으로 돌아간다'. (엔딩이 나눠지게 됩니다)")
    while True:
        if a[0] == '한':
            time.sleep(3)
            print("빚을 모두 청산하고 한남동에 대저택만 사면 나는 정말 다 끝내고 손털거야")
            time.sleep(3)
            print("근데 하루만 더하면 50억이 500억 되는거 아닌가?ㅋㅋ 와...")
            time.sleep(3)
            print("500억 있으면 뭐하지...")
            time.sleep(3)
            print("은행이자만 받아도 이게 얼마지... 1프로만 해도 1년에 5억.... 아예 카지노를 하나 만들어도 되겠는데? ")
            time.sleep(4)
            print("그런 꿈을 갖고 나는 카지노에 들어갔고.......")
            time.sleep(5)
            print("세시간 뒤에는 다시 섬으로 가는 보트 안이였다.")
            time.sleep(5)
            print("무슨 일이 벌어진걸까")
            time.sleep(5)
            print("희망에 가득찼던 어렸을 적 내 모습이 생각난다.")
            time.sleep(5)
            print("설령 인터스텔라처럼 너와 얘기할 수 있다하더라도..")
            time.sleep(5)
            print(" 너가 이렇게 될것이라고는 부끄러워서 말해주지 못하겠구나. ")
            time.sleep(5)
            print("보트는 섬에 도착하겠지만 나는 그렇지 않을것이다.")
            time.sleep(5)
            break
        elif a[0] == '빚':
            time.sleep(3)
            print("나는 모든 빚을 청산하고 잔고 0원으로 돌아왔다.")
            time.sleep(3)
            print("통장은 비었지만 지금의 나는 누구보다도 충만한 기분이다.")
            time.sleep(3)
            print("비트코인, 주식, 카지노.. ")
            time.sleep(3)
            print("한방으로 뒤집어 평생 먹고놀려는 사람들의 욕심들... ")
            time.sleep(3)
            print("그리고 그 욕심들을 이용해 돈을 버는 사람들.. ")
            time.sleep(3)
            print("욕심과 욕심이 얽히고설켜 만들어진 기형적인 현대의 산물들일 뿐인 것이다. ")
            time.sleep(3)
            print("이제 나는 이 세계를 떠나겠어.. ")
            time.sleep(3)
            print(f"나는 그동안 {sexslavetotal}년간 섬에서 일했던 경력을 살려 작은 섬의 염전에 취직했다.")
            time.sleep(3)
            print("이곳에서 나는 도박에 빠져 정신을 못차리는 사람들에게 노동의 기쁨을 알려주며 살고 있다.")
            time.sleep(3)
            print("바뀐 인성덕분인지 사람들은 나를 천사라고 부른다. ")
            break
        else:
            continue
    print("이 게임을 진행하면서 한번이라도 섬에 간적이 있었나요?")
    time.sleep(2)
    print("게임을 하면서 섬이 있다는 사실이 얼마나 든든했나요")
    time.sleep(2)
    print("현실에서 섬은 존재하지 않습니다.")
    time.sleep(2)
    print("도박은 인생을 파멸시키는 길입니다.")
    time.sleep(5)
    print("도박문제 전화·온라인 상담(도박문제 헬프라인 1336(무료)/넷라인) \n 제작자 : https://github.com/kihyeonkwon")
