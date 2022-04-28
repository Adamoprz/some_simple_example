class Prostokat:
    def __init__(self, bok1_: float, bok2_: float) -> None:
        self.bok1 = bok1_
        self.bok2 = bok2_
    def oblicz_pole(self) -> float:
        return self.bok1 * self.bok2
    def oblicz_obwod(self) -> float:
        return 2*self.bok1 + 2*self.bok2

def main():
    prostokat = Prostokat(20.0,10.0)
    print(prostokat.oblicz_pole())
    print(prostokat.oblicz_obwod())

if __name__ == "__main__":
    main()