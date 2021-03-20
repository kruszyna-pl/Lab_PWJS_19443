from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/list")
def list():
    connector = sql.connect("employees.db")
    connector.row_factory = sql.Row
    cursor = connector.cursor()
    cursor.execute('select * from emp order by name')
    row = cursor.fetchall()
    return render_template('list.html', row=row)


@app.route('/addemp', methods=['POST','GET'])
def method_add_emp():
    if request.method == 'POST':
        try:
            emp_number = request.form['emp_number']
            name = request.form['name']
            surname = request.form['surname']
            address = request.form['address']

            with sql.connect("employees.db") as connector:
                cursor = connector.cursor()
                cursor.execute("insert into emp (emp_number,name,surname,address) values (?,?,?,?)",
                               (emp_number, name, surname, address))

                connector.commit()
                msg = "Rekord zapisany"

        except:
            connector.rollback()
            msg = "Nie udało się zapisać rekordu"

        finally:
            return render_template('result.html', msg=msg)


@app.route("/add")
def new_student():
    return render_template('add.html')


if __name__ == "__main__":
    app.run()
