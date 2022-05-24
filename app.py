from flask import Flask, render_template, url_for, request, redirect, session
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '' # for no password
# app.config['MYSQL_PASSWORD'] = '12345678' # for password
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
    prgrm = str(request.args.get('prgrm'))
    
    cursor = db.connection.cursor()
    query = 'SELECT distinct clgcode, clgname, address FROM clglist WHERE program="{}"'.format(prgrm)
    cursor.execute(query)
    details = cursor.fetchall()
    sno = len(details)

    #query2='SELECT distinct subcourse FROM clglist WHERE program="{}" ORDER BY subcourse'.format(prgrm)
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

# @app.route('/courseFilter')
# def courseFilter():
#         prgrm = str(request.args.get('prgrm'))
#         subcourse=str(request.args.get('subcourse'))
#         cursor = db.connection.cursor()
#         query = 'SELECT clgname,course,subcourse,intake FROM clglist WHERE program="{}" and subcourse={}'.format(prgrm,subcourse)
#         cursor.execute(query)
#         details = cursor.fetchall()


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