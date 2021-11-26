from flask import Flask, render_template, request, redirect, url_for
from dbhandler import Mysqlhandler#, Mysqlhandler2

app = Flask(__name__)

PHONE = 0

@app.route('/')
def index():
    return redirect(url_for('create_user'))

@app.route('/user_or_not')
def create_user() -> 'html':
    return render_template('entry.html',
    the_title='Are you a user already?')

@app.route('/user/buy_or_sell', methods=['POST'])
def buy_or_sell() -> str:
    #handleMe = sqlhandler()
    #Mysqlhandler.initial(handleMe)

    if request.method == 'POST':
        if request.form['submit_button'] == 'Signup':
            return render_template('signup.html', the_title='Signup as:')
        elif request.form['submit_button'] == 'Login':
            return render_template('login.html', the_title='Login as:')

@app.route('/user/signup', methods=['POST'])
def c_or_v() -> str:
    #handleMe = sqlhandler()
    #Mysqlhandler.initial(handleMe)

    if request.method == 'POST':
        if request.form['submit_button'] == 'Customer':
            return render_template('csign.html',)
        elif request.form['submit_button'] == 'Vendor':
            return render_template('vsign.html',)

    # elif request.method == 'GET':
    #     return render_template('contact.html', form=form)

    # name = request.form['name']
    # phno = request.form['phno']
    # dob = request.form['dob']
    # PHONE = phno
    # handleMe2 = Mysqlhandler()
    # Mysqlhandler.add_user(handleMe2, name, phno, dob)
    # return render_template('results.html',
    # the_name=name,
    # the_phno=phno,
    # the_dob=dob,
    # )

@app.route('/user/update', methods=['POST'])
def update_user() -> str:
    return render_template('update.html',
    the_title='Enter the updated details!')

@app.route('/user/login', methods=['POST'])
def v_l() -> str:
    # return render_template('done2.html',
    # )
    if request.method == 'POST':
        if request.form['submit_button'] == 'Customer':
            return render_template('clogin.html')
        elif request.form['submit_button'] == 'Vendor':
            return render_template('vlogin.html')

    # uname = request.form['uname']
    # pwd = request.form['pwd']
    # handleMe = sqlhandler()
    # sqlhandler.login(handleMe, uname, pwd)
    # return render_template('results2.html',
    # the_name=name,
    # the_phno = phno,
    # the_dob=dob,
    # )

@app.route('/user/delete', methods=['POST'])
def delete_user() -> str:
    #phno = request.form['phno']
    #handleMe = Mysqlhandler()
    #Mysqlhandler.delete_user(handleMe, phno)
    return render_template('delete.html',
    )

@app.route('/user/done', methods=['POST'])
def done() -> str:
    phno = request.form['phno']
    # handleMe = sqlhandler()
    # Mysqlhandler.delete_user(handleMe, phno)
    return render_template('done.html',
    )

@app.route('/user/sign_form', methods=['POST'])
def sign_form() -> str:
    # handleMe = sqlhandler()
    #Mysqlhandler.initial(handleMe)

    # name = request.form['name']
    # phno = request.form['phno']
    uname = request.form['uname']
    pwd = request.form['pwd']
    #PHONE = phno

    # handleMe2 = Mysqlhandler2()
    # var1 = Mysqlhandler2.signup(handleMe2, uname, pwd)
    handleMe = Mysqlhandler()
    var1 = Mysqlhandler.signup(handleMe, uname, pwd)
    str1 = "Signed up and auto-Logged in as:" + uname
    #str1 = "You are logged in as " + uname
    str2 = "ERROR: USERNAME TAKEN"


    if(var1 == 1):
        return render_template('results.html',
        the_username=uname, string=str1
        )
    else :
        return render_template('results.html',
        the_username=uname, string=str2
        )

@app.route('/user/login_form', methods=['POST'])
def login_form() -> str:
    # handleMe = sqlhandler()
    # Mysqlhandler.login(handleMe)

    uname = request.form['uname']
    pwd = request.form['pwd']
    #PHONE = phno
    handleMe2 = Mysqlhandler()
    var1 = Mysqlhandler.login(handleMe2, uname, pwd)
    str1 = "You are logged in as " + uname
    str2 = "Invalid credentials/User doesn't exist"

    if(var1 == 1):
        return render_template('results2.html',
        the_username=uname, string=str1
        )
    else :
        return render_template('results2.html',
        the_username=uname, string=str2
        )


app.run(host = "127.0.0.1", port = 5000, debug = True)
