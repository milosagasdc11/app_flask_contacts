#Importamos flask, mariadb y render
import flask
from flask import render_template, request, redirect,  url_for, flash
import mariadb



#Creamos la app de flask
app = flask.Flask(__name__)
app.config["DEBUG"] = False

#Inicializamos la sesion
app.secret_key= 'mysecretkey'

# configuration used to connect to MariaDB
config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'milosagasdc11',
    'password': 'Milosqui11',
    'database': 'flask_contacts'
}

# metodos para el enrutamiento
@app.route('/')
def index(): 
    data = select_all_contacts()
    return render_template('index.html', contacts = data) #Direcciono al index y le envio los datos


@app.route('/add', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        insert_contact(fullname, phone, email)
        return redirect (url_for('index'))
        

@app.route('/edit/<id>')
def edit_contact(id):
    data = select_contact_byId(id)
    return render_template('edit_contact.html', contact = data[0])

@app.route('/delete/<id>')
def delete_contact(id):
    delete_contact_byId(id)
    return redirect(url_for('index'))


@app.route('/update/<id>', methods = ['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        update_contact(id,fullname, phone, email)
        return redirect(url_for('index'))


#mariadb contacts  
def insert_contact(fullname, phone, email):
    conn = mariadb.connect(**config)
    cur = conn.cursor()
    cur.execute("INSERT INTO contacts (fullname, phone, email) VALUES(%s, %s, %s)", 
    (fullname, phone, email))
    conn.commit()
    print('Contacto insertado')

def select_all_contacts():
    conn = mariadb.connect(**config)
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts")
    data = cur.fetchall()
    return data

def delete_contact_byId(id):
    conn = mariadb.connect(**config)
    cur = conn.cursor()
    cur.execute("DELETE FROM contacts where id = {0}".format(id))
    conn.commit()
    print('Contacto eliminado')

def select_contact_byId(id):
    conn = mariadb.connect(**config)
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts where id = {0}".format(id))
    data = cur.fetchall()
    return data

def update_contact(id, fullname, phone, email):
    conn = mariadb.connect(**config)
    cur = conn.cursor()
    cur.execute("UPDATE contacts SET fullname = %s, phone=%s, email = %s WHERE id = %s", 
    (fullname, phone, email, id))
    conn.commit()
    print('Actualizado con exito')


#run de appp
app.run()
    
