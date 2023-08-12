from flask import Flask, render_template, request, redirect, url_for, session, g
import sqlite3
import bcrypt

app = Flask(__name__)
app.secret_key = 'YfeItpdUsWnmgfQ'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('db_clinica')
    return g.db


@app.route('/', methods=["GET"])
def index():
    return render_template('login.html')

@app.route('/login', methods=["POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        db = get_db()
        user_data = db.execute("SELECT * FROM USER_DATA WHERE USERNAME = ?", (username,)).fetchone()
        # aqui quiero codificar la contraseña, estaba viendo videos sobre bcryp
        # si alguien lo sabe usar o tiene conocimiento sobre otra libreria similar, se le agradece
        if user_data:
            stored_password = user_data[2]
            if password == stored_password:
                session['username'] = username
                return redirect(url_for('dashboard'))
            return 'CREDENCIALES INVALIDAS'
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

@app.route('/patient', methods=["GET"])
def patient_form():
    return render_template('patient.html')

@app.route('/patient/search', methods=["POST"])
def search_patient():
    pass


@app.route('/patient/add', methods=["GET", "POST"])
def add_patient():
    pass




# esto de aqui es para tirartodo, no es necesario descomentarlo
# @app.teardown_appcontext
# def close_db(exception):
#     db = g.pop('db', None)
#     if db is not None:
#         db.close()

if __name__ == '__main__':
    app.run(debug=True)




