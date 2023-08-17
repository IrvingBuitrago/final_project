from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3 as sql
import bcrypt

app = Flask(__name__)
app.secret_key = 'YfeItpdUsWnmgfQ'

@app.route('/', methods=["GET"])
def index():
    return render_template('login.html')

@app.route('/login', methods=["POST"])
def login():
    if request.method == "POST":
        try:
            username = request.form['username']
            password_hash = request.form['password_hash']

            with sql.connect('db_clinica') as con:
                cur = con.cursor()
                review = cur.execute('SELECT * FROM USER_DATA WHERE USERNAME = ? AND PASSWORD_HASH = ?', (username, password_hash)).fetchone()
                if review:
                    return redirect(url_for('dashboard'))
                else:
                    return render_template('login.html', error='credenciales invalidas')
        except Exception as e:
            return render_template('login.html', error= str(e))
    return render_template('login.html')


@app.route('/dash', methods=["GET", "POST"])
def dashboard():
    if request.method == "POST":
        opcion = int(request.form['opcion'])
        if opcion == 1:
            return render_template('dashboard.html')
        elif opcion == 2:
            return render_template('appointment.html')
        elif opcion == 3:
            return render_template('patient.html')
        else:
            return render_template('dashboard.html')
    return render_template('dashboard.html')

@app.route('/patient', methods=["GET", "POST"])
def patient_form():
    return render_template('patient.html')

@app.route('/patient/search', methods=["GET", "POST"])
def search_patient():
    if request.method == 'POST':
        try:
            name_last_name = request.form['name_last_name']
            name, last_name = name_last_name.split()

            with sql.connect('db_clinica') as con:
                cur = con.cursor()
                review = cur.execute('SELECT * FROM PATIENT WHERE NAME = ? AND LAST_NAME = ?', (name,last_name)).fetchone()
                if review:
                    return render_template('patient.html', review=review)
                else:
                    return render_template('patient.html', error='paciente no encontrado')
        except Exception as e:
            return render_template('patient.html', error=str(e))
    return render_template('patient.html')


@app.route('/patient/add', methods=["GET", "POST"])
def add_patient():
    if request.method == 'POST':
        try:
            name = request.form['name']
            last_name = request.form['last_name']
            id_pat = request.form['id_pat']
            birthdate = request.form['birthdate']
            address = request.form['address']

            with sql.connect('db_clinica') as con:
                cur = con.cursor()
                review = cur.execute('SELECT * FROM PATIENT WHERE ID_PAT = ?', (id_pat,)).fetchone()
                if review:
                    return render_template('add_patient.html', error='registrado anteriormente')
                else:
                    insert = cur.execute('INSERT INTO PATIENT (name, last_name, id_pat, birthdate, address) VALUES (?, ?, ?, ?, ?)', (name, last_name, id_pat, birthdate, address))
                    con.commit()
                    return render_template('patient.html', msg='paciente registrado con exito')
        except Exception as e:
            return str(e)
    return render_template('add_patient.html')


@app.route('/patient/edit', methods=["GET", "POST"])
def edit_palabra():
    if request.method == 'POST':
        try:
            column_update = request.form['column_update']
            new_data = request.form['new_data']
            name = request.form['name']
            last_name = request.form['last_name']
            birthdate = request.form['birthdate']
            id_pat = request.form['id_pat']
            address = request.form['address']

            with sql.connect('db_clinica') as con:
                cur = con.cursor()
                update = cur.execute(f'UPDATE PATIENT SET {column_update} = ? WHERE NAME = ? AND LAST_NAME = ? AND BIRTHDATE = ? AND ID_PAT = ? AND ADDRESS = ?', (new_data, name, last_name, birthdate, id_pat, address))
                con.commit()
                return render_template('patient.html', update=update)
        except Exception as e:
            return render_template('patient.html', error=str(e))
    return render_template('patient.html')

@app.route('/patient/delete', methods=['POST'])
def delete_patient():
    try:
        name = request.form['name']
        last_name = request.form['last_name']

        with sql.connect('db_clinica') as con:
            cur = con.cursor()
            delete = con.execute('DELETE FROM PATIENT WHERE NAME = ? AND LAST_NAME = ?', (name, last_name))
            con.commit()
        return render_template('patient.html')
    except Exception as e:
        return render_template('patient.html', error=str(e))
    
# ...

@app.route('/appointment', methods=["GET"])
def appointment_form():
    return render_template('add_appointment.html')

@app.route('/appointment/add', methods=["POST"])
def add_appointment():
    if request.method == 'POST':
        try:
            appo_date = request.form['appo_date']
            time = request.form['time']
            reason = request.form['reason']

            with sql.connect('db_clinica') as con:
                cur = con.cursor()
                insert = cur.execute('INSERT INTO APPOINTMENT (APPO_DATE, TIME, REASON) VALUES (?, ?, ?)', (appo_date, time, reason))
                con.commit()
                return render_template('add_appointment.html', msg='Cita agregada con éxito')
        except Exception as e:
            return str(e)
    return render_template('add_appointment.html')

# ...

# ...

@app.route('/appointment/search', methods=["GET", "POST"])
def search_appointment():
    if request.method == 'POST':
        try:
            name_last_name = request.form['name_last_name']
            name, last_name = name_last_name.split()

            with sql.connect('db_clinica') as con:
                cur = con.cursor()
                review = cur.execute('SELECT * FROM PATIENT_APPOINTMENT WHERE NAME = ? AND LAST_NAME = ?', (name, last_name)).fetchone()
                if review:
                    return render_template('search_appointment.html', review=review)
                else:
                    return render_template('search_appointment.html', error='Cita no encontrada')
        except Exception as e:
            return render_template('search_appointment.html', error=str(e))
    return render_template('search_appointment.html')

# ...





if __name__ == '__main__':
    app.run(debug=True)




