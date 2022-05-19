from flask import Flask, render_template, url_for, request, redirect, session
import MySQLdb
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'auditcell'

db = MySQL(app)

@app.route('/',methods=['POST','GET'])
def login():
    msg=''
    if request.method == 'POST':
        return redirect(url_for('home'))
    return render_template('login.html',msg=msg)

@app.route('/home',methods=['POST','GET'])
def home():
    return render_template('home.html')