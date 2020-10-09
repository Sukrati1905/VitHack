from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL


app = Flask(__name__)



app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Chunmun@1905'
app.config['MYSQL_DB'] = 'sukrati'

mysql = MySQL(app)

@app.route('/profile', methods=['GET', 'POST'])
def login():
    msg = ' '
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:

        username = request.form['username']
        password = request.form['password']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM register WHERE username = %s AND password = %s', (username, password,))

        account = cursor.fetchone()

        if account:
            session['loggedin'] = True

            session['username'] = register['username']

            return redirect(url_for('home'))
        else:
            msg = 'Incorrect username/password!'

    return render_template('index.html', msg=msg)


@app.route('/logout',methods=['GET', 'POST'])
def logout():

   session.pop('loggedin', None)

   session.pop('username', None)

   return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        name = request.form['name']
        dob =request.form['dob']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(f"SELECT * FROM register WHERE username = '{username}';")
        account = cursor.fetchone()

        if account:
            msg = 'Account already exists!'

        else:
            cursor.execute('INSERT INTO register VALUES (%s, %s, %s, %s, %s)', (username, password, email, name, dob))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':

        msg = 'Please fill out the form!'
    return render_template('register.html', msg=msg)



@app.route('/',methods=['GET', 'POST'])
def home():
    if 'loggedin' in session:

        return render_template('home.html', username=session['username'])

    return redirect(url_for('login'))


@app.route('/pro',methods=['GET', 'POST'])
def profile():

    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM register WHERE username = %s', (session['username'],))
        account = cursor.fetchone()

        return render_template('profile.html', account=account)

    return redirect(url_for('login'))


if (__name__=='__main__'):
    app.run(debug=True)
