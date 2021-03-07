class Student:
    licznik = 0

    def __init__(self, imie, nazwisko, numerIndeksu, kierunek):
        Student.licznik += 1
        self.imie = imie
        self.nazwisko = nazwisko
        self.__numerIndeksu = numerIndeksu
        self.kierunek = kierunek

    def __str__(self):
        return "Imię: %s Nazwisko: %s Kierunek: %s Indeks: %s" % (
            self.imie, self.nazwisko, self.kierunek, self.__numerIndeksu)

    def __eq__(self, other):
        if self.imie == other.imie and self.nazwisko == other.nazwisko:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.imie < other.imie and self.nazwisko < other.nazwisko:
            return True
        else:
            return False

    def getLicznik(self):
        return Student.licznik

    def rokDrugi(self):
        print(self.__str__() + ' Rok: 2')

    ## Usprawniona fukcja rok_drugi według mnie powinna przyjmować dodatkowy parametr
    # w tym wypoadku rok studiów
    # poprawiona funcja prezentuje się następująco
    # def rok_studiow(self, rokStudiow):
    #     print(self.__str__() + ' Rok:', rokStudiow)
    # funkcja rok drugi nie jest zła jednak, takie harcodowanie nie jest dobra praktyka
    # starajmy sie aby nasze rozwiązania były reużywalne oraz miały sens

class StudentInformatyki(Student):

    def __init__(self, imie, nazwisko, numerIndeksu, kierunek, specjalnosc):
        super().__init__(imie, nazwisko, numerIndeksu, kierunek)
        self.kierunek = 'IIS'
        self.specjalnosc = specjalnosc
