from flask import Flask, render_template, url_for, request, redirect, session
# import MySQLdb
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
    cursor = db.connection.cursor()
    cursor2 = db.connection.cursor()
    cursor.execute('SELECT program, count(distinct clgcode) FROM clglist group by program')
    details = cursor.fetchall()
    sno=len(details)

    cursor2.execute('SELECT COUNT(distinct clgcode) from clglist')
    clgCount=cursor2.fetchall()[0][0]

    return render_template('home.html',sno=sno,details=details,clgCount=clgCount)
    

@app.route('/program', methods=['POST', 'GET'])
def program():
    course = str(request.args.get('course'))
    cursor = db.connection.cursor()
    query = 'SELECT distinct clgcode, clgname, address FROM clglist WHERE program="{}"'.format(course)
    cursor.execute(query)
    details = cursor.fetchall()
    sno = len(details)
    return render_template('program.html',sno=sno, details=details,course=course)

@app.route('/college')
def college():
    course = str(request.args.get('course'))
    clgcode = int(request.args.get('clgcode'))
    cursor = db.connection.cursor()
    query = 'SELECT clgname,course,subcourse,intake FROM clglist WHERE program="{}" and clgcode={}'.format(course,clgcode)
    cursor.execute(query)
    details = cursor.fetchall()
    sno = len(details)
    return render_template('college.html', sno=sno, details=details, course=course,clgcode=clgcode)

if __name__ == '__main__':
    app.run(debug=True)