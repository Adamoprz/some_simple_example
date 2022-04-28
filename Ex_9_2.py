class Pojazd:
    def __init__(self, max_predkosc_:int, przebieg_:float) -> None:
        self.max_predkosc = max_predkosc_
        self.przebieg = przebieg_
    def zwieksz_przebieg(self, wartosc:float) -> float:
        self.przebieg = self.przebieg + wartosc

def main():
    opel = Pojazd(205, 150_000)
    print("podaj o ile zwiekszyc przebieg: ")
    opel.zwieksz_przebieg(float(input()))
    print("nowy przebieg wynosi " + str(opel.przebieg))

if __name__ == "__main__":
    main()