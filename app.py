from flask import Flask, render_template, url_for, request, redirect, session
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = 'auditcell'

app.config['MYSQL_HOST'] = '127.0.0.1' # use when in linux distros
# app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '' # for no password
# app.config['MYSQL_PASSWORD'] = '12345678' # for password
app.config['MYSQL_DB'] = 'auditcell'

db = MySQL(app)

@app.route('/',methods=['POST','GET'])
def home():
    cursor = db.connection.cursor()
    cursor2 = db.connection.cursor()
    cursor.execute('SELECT program, count(distinct clgcode) FROM clglist group by program')
    details = cursor.fetchall()
    sno=len(details)

    cursor2.execute('SELECT COUNT(distinct clgcode) from clglist')
    clgCount=cursor2.fetchall()[0][0]
    
    return render_template('home.html',sno=sno,details=details,clgCount=clgCount)
    

@app.route('/login', methods=['POST', 'GET'])
def login():
    msg = ''
    if request.method == 'POST':
        if 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']
            cursor = db.connection.cursor()
            cursor.execute(
                'SELECT * FROM logincred WHERE username=%s AND password=%s', (username, password))
            info = cursor.fetchone()
        if info is not None:
            if username == info[0] and password == info[1]:
                session['loggedin'] = True
                session['username'] = info[0]
                session['password'] = info[1]
                return redirect(url_for('home'))
            msg = "Invalid username/password"
        else:
            msg = "Invalid username/password"

    return render_template("login.html", msg=msg)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    return redirect(url_for('home'))

@app.route('/program', methods=['POST', 'GET'])
def program():
    prgrm = str(request.args.get('prgrm'))
    
    cursor = db.connection.cursor()
    query = 'SELECT distinct clgcode, clgname, address FROM clglist WHERE program="{}"'.format(prgrm)
    cursor.execute(query)
    details = cursor.fetchall()
    sno = len(details)

    query2 = 'select course,subcourse from clglist where program="{}" group by concat(course,subcourse)'.format(prgrm)
    cursor.execute(query2)
    courseDetails = cursor.fetchall()
    courseCount=len(courseDetails)
    
    if request.args.get('subcourse'):
        subcourse=str(request.args.get('subcourse'))
        query3 = 'SELECT distinct clgcode, clgname, address,course,subcourse,intake FROM clglist WHERE program="{}" and subcourse="{}"'.format(prgrm,subcourse)
        cursor.execute(query3)
        details= cursor.fetchall()
        sno=len(details)
        return render_template('program.html',sno=sno,prgrm=prgrm, courseDetails=courseDetails,details=details,subcourse=subcourse)
    
    return render_template('program.html',sno=sno, details=details,prgrm=prgrm, courseDetails=courseDetails,courseCount=courseCount)

@app.route('/search')
def search():
     cursor = db.connection.cursor()
     query = 'SELECT program,course,subcourse,clgcode,clgname,address FROM clglist'
     cursor.execute(query)
     details = cursor.fetchall()
     sno = len(details)
     clgCount = set()
     for i in range(sno):
        clgCount.add(details[i][3])
     return render_template('searchClg.html', sno=sno, clgCount=len(clgCount), details=details)

@app.route('/college')
def college():
    prgrm = str(request.args.get('prgrm'))
    clgcode = int(request.args.get('clgcode'))
    cursor = db.connection.cursor()
    query = 'SELECT clgname,course,subcourse,intake FROM clglist WHERE program="{}" and clgcode={}'.format(prgrm,clgcode)
    cursor.execute(query)
    details = cursor.fetchall()
    sno = len(details)
    return render_template('college.html', sno=sno, details=details, prgrm=prgrm,clgcode=clgcode)

if __name__ == '__main__':
    app.run(debug=True)