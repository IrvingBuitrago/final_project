import sqlite3

conn = sqlite3.connect('db_clinica')

# conn.execute('''CREATE TABLE IF NOT EXISTS USER_DATA
#                 (USERNAME TEXT PRIMARY KEY NOT NULL,
#                 EMAIL TEXT NOT NULL,
#                 PASSWORD_HASH TEXT NOT NULL);''')
#
# conn.execute('''CREATE TABLE IF NOT EXISTS DENTIST
#                 (ID_DEN INTEGER PRIMARY KEY NOT NULL,
#                 NAME TEXT NOT NULL,
#                 LAST_NAME TEXT NOT NULL);''')
#
# conn.execute('''CREATE TABLE IF NOT EXISTS PATIENT
#                 (ID_PAT INTEGER PRIMARY KEY NOT NULL,
#                 NAME TEXT NOT NULL,
#                 LAST_NAME TEXT NOT NULL,
#                 BIRTHDATE DATE NOT NULL,
#                 ADDRESS TEXT NOT NULL);''')
#
# conn.execute('''CREATE TABLE IF NOT EXISTS APPOINTMENT
#                 (ID_APPO INTEGER PRIMARY KEY AUTOINCREMENT,
#                 APPO_DATE DATE NOT NULL,
#                 TIME TEXT NOT NULL,
#                 REASON TEXT NOT NULL);''')
# print('exito')
#
# conn.execute('''CREATE TABLE IF NOT EXISTS DENTIST_APPOINTMENT
#                 (ID_DEN INTEGER NOT NULL,
#                 ID_APPO INTEGER,
#                 PRIMARY KEY (ID_DEN, ID_APPO),
#                 FOREIGN KEY (ID_DEN) REFERENCES DENTIST(ID_DEN),
#                 FOREIGN KEY (ID_APPO) REFERENCES APPOINTMENT(ID_APPO));''')
#
# conn.execute('''CREATE TABLE IF NOT EXISTS PATIENT_APPOINTMENT
#                 (ID_PAT INTEGER NOT NULL,
#                 ID_APPO INTEGER,
#                 PRIMARY KEY (ID_PAT, ID_APPO),
#                 FOREIGN KEY (ID_PAT) REFERENCES PATIENT(ID_PAT),
#                 FOREIGN KEY (ID_APPO) REFERENCES APPOINTMENT(ID_APPO));''')
# print('exito')

conn.execute('''CREATE TABLE IF NOT EXISTS APPOINTMENT
                (ID_APPO INTEGER PRIMARY KEY AUTOINCREMENT,
                APPO_DATE DATE NOT NULL,
                TIME TEXT NOT NULL,
                REASON TEXT NOT NULL);''')




# conn.execute("INSERT INTO PATIENT (name, last_name, birthdate, id_pat, address) VALUES (?, ?, ?, ?, ?)",
#              ('Irving', 'Buitrago', '2000-11-25', '321', 'mi casa'))
# conn.commit()

# conn.execute('DELETE FROM PATIENT WHERE id_pat = ?', ('',))
# conn.commit()


# conn.execute('DROP TABLE IF EXISTS PATIENT_APPOINTMENT')
# print('listo')

