import Lab2.Student as stud


def testy():
    print('Zadanie 1,Zadanie 3 ,Zadanie 4')
    s1 = stud.Student('Wojciech', 'Pietruszyński', 19443, 'Informatyka')
    # print(student.numer_indeksu) jeśli pole prywatne to wywołanie jest nie możliwe
    # przy obiekcie możemy się odwołać
    print(s1.getLicznik(), s1)
    s2 = stud.StudentInformatyki('Jan', 'Kowalski', 12345, None, 'Programowanie')
    print(s2.getLicznik(), s2.__str__(), 'Specjalnosc: ', s2.specjalnosc)
    s3 = stud.StudentInformatyki('Jan', 'Nowak', 12346, None, 'Programowanie')
    print(s3.getLicznik(), s3.__str__(), 'Specjalnosc: ', s3.specjalnosc)
    print('Zadanie 2')
    print(s1.imie, s1.nazwisko, "<", s2.imie, s2.nazwisko)
    print(s1.__lt__(s2))
    print(s1.imie, s1.nazwisko, "<", s3.imie, s3.nazwisko)
    print(s2.__lt__(s1))
    print()
    print(s1.imie, s1.nazwisko, "==", s2.imie, s2.nazwisko)
    print(s1.__eq__(s2))
    print(s1.imie, s1.nazwisko, "==", s3.imie, s3.nazwisko)
    print(s2.__eq__(s1))
    print(s1.imie, " ", s1.nazwisko, "==", s1.imie, s1.nazwisko)
    print(s1.__eq__(s1))

    print("Zadanie 5")
    stud.Student.rokDrugi(s1)

    print("Zadanie 5 poprawiona metoda")
    stud.Student.rok_studiow(s2, 4)


if __name__ == "__main__":
    testy()
