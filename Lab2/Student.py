class Student:
    licznik = 0

    def __init__(self, imie, nazwisko, __numer_indeksu, kierunek):
        Student.licznik += 1
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_indeksu = __numer_indeksu
        self.kierunek = kierunek

    def __str__(self):
        return f'Imię : {self.imie}, Nazwisko :  {self.nazwisko}, Numer indeksu : {self.numer_indeksu}, ' \
               f'Kierunek : {self.kierunek} '

    def getLicznik(self):
        return Student.licznik


class StudentInformatyki(Student):

    def __init__(self, imie, nazwisko, __numer_indeksu, kierunek, specjalnosc):
        super().__init__(imie, nazwisko, __numer_indeksu, kierunek)
        self.kierunek = 'IIS'
        self.specjalnosc = specjalnosc

    def __str__(self):
        return f'Imię : {self.imie}, Nazwisko :  {self.nazwisko}, Numer indeksu : {self.numer_indeksu}, ' \
               f'Kierunek : {self.kierunek} Specjalnośc : {self.specjalnosc} '
