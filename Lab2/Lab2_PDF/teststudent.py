import Lab2.studencik as stud


def testy():
    student = stud.Studencik('Wojciech', 'Pietruszyński', 19443, 'Informatyka')
    print(student.getLicznik(), student)
    student1 = stud.StudentInformatyki('Jan', 'Kowalski', 12345, None, 'Programowanie')
    print(student1.getLicznik(), student1)
    student2 = stud.StudentInformatyki('Jan', 'Nowak', 12346, None, 'Programowanie')
    print(student2.getLicznik(), student2)


if __name__ == "__main__":
    testy()
