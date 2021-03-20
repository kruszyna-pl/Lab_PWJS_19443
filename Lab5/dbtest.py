import sqlite3


def all_operation_on_db():
    connector = sqlite3.connect('employees.db')
    print("employees.db is created")

    connector.execute('create table emp(name TEXT, surname TEXT, emp_number TEXT, address TEXT)')
    print("Table employees has been created")

    cursor = connector.cursor()
    cursor.execute("insert into emp ( name,surname,emp_number,address)values(?,?,?,?)",
                   ('Wojciech', 'Pietruszynski', '1', '82-300 Elbląg ul.Tajemnicza 5/4'))
    cursor.execute("insert into emp ( name,surname,emp_number,address)values(?,?,?,?)",
                   ('Jan', 'Kowalski', '2', '82-300 Elbląg ul.Zimna 511/9'))

    print(cursor.fetchall())

    connector.commit()
    connector.close()


if __name__ == '__main__':
    all_operation_on_db()
