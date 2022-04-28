import random
# duck typing -- Interpreter sprawdza jakie funkcjonalnosci ma dany obiekt.


class Card:
    def __init__(self, value:str, figure:str) -> None:
        self.figure = figure
        self.value = value

    def __str__(self) -> str:
        return f"{self.value} - {self.figure}"


class Deck:
    def __init__(self, figures:list, values:list) -> None:
        self.card_ = []
        self.figures = figures
        self.values = values
        self.create_Deck()

    def __str__(self):
        return self.card_

    def create_Deck(self) -> None:
        for value in self.values:
            for figure in self.figures:
                t = Card(value, figure)
                self.add(t)

    def add(self, added_card: Card) -> None:
        self.card_.append(added_card)

    def shuffle(self) -> None:
        random.shuffle(self.card_)

    def deal(self) -> str:
        return self.card_.pop()

def main():
    figures = ["Diamond", "Clubs", "Heart", "Spade"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J" , "Q" , "K"]
    #Generate and create new deck
    deck_f = Deck(figures, values)
    #deck_f.create_Deck()
    #print all cards of the deck
    print(*deck_f.card_,sep = ', ')
    #shuffle deck
    deck_f.shuffle()
    #print shuffled deck
    print(*deck_f.card_,sep = ", ")
    print(len(deck_f.card_))

    #print last card from the shuffled deck and remove the last card from deck.
    print(deck_f.deal())
    #print deck (now it is reduced by one card
    print(deck_f.card_[0])
    #deck_f.card_[0]
    #jedna karta mniej
    print(len(deck_f.card_))

if __name__ == "__main__":
    main()