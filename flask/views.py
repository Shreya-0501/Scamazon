from flask import Flask, render_template, request, redirect, url_for
from dbhandler import Mysqlhandler

app = Flask(__name__)

PHONE = 0

@app.route('/')                                     #for redirecting to the main page
def index():
    return redirect(url_for('create_user'))

@app.route('/user_or_not')                          #redirects to signup/login based on what is chosen
def create_user() -> 'html':
    return render_template('entry.html',
    the_title='Are you a user already?')


@app.route('/user/buy_or_sell', methods=['POST'])   #redirects to login or signup 
def buy_or_sell() -> 'html':

    if request.method == 'POST':
        if request.form['submit_button'] == 'Signup':
            return render_template('signup.html', the_title='Signup as:')
        elif request.form['submit_button'] == 'Login':
            return render_template('login.html', the_title='Login as:')


@app.route('/user/signup', methods=['POST'])        #redirects to customer/vendor signup page
def c_or_v() -> 'html':

    if request.method == 'POST':
        if request.form['submit_button'] == 'Customer':
            return render_template('csign.html',)
        elif request.form['submit_button'] == 'Vendor':
            return render_template('vsign.html',)



@app.route('/user/update', methods=['POST'])        #
def update_user() -> 'html':
    return render_template('update.html',
    the_title='Enter the updated details!')


@app.route('/user/login', methods=['POST'])         #redirects to customer/vendor login page
def v_l() -> 'html':

    if request.method == 'POST':
        if request.form['submit_button'] == 'Customer':
            return render_template('clogin.html')
        elif request.form['submit_button'] == 'Vendor':
            return render_template('vlogin.html')



@app.route('/user/delete', methods=['POST'])        #
def delete_user() -> 'html':

    return render_template('delete.html',
    )

@app.route('/user/done', methods=['POST'])          #
def done() -> 'html':
    phno = request.form['phno']

    return render_template('done.html',
    )

@app.route('/user/sign_form', methods=['POST'])     # for buyer -> customer signup
def sign_form() -> 'html':

    uname = request.form['uname']
    pwd = request.form['pwd']

    handleMe = Mysqlhandler()
    var1 = Mysqlhandler.signup(handleMe, uname, pwd, 1)
    str1 = "Signed up and auto-Logged in as:" + uname
    str2 = "ERROR: USERNAME TAKEN"


    if(var1 == 1):
        return render_template('results.html',
        the_username=uname, string=str1
        )
    else :
        return render_template('results.html',
        the_username=uname, string=str2
        )

@app.route('/user/sign_form2', methods=['POST'])    #for vendor signup
def sign_form2() -> 'html':

    uname = request.form['uname']
    pwd = request.form['pwd']

    handleMe = Mysqlhandler()
    var1 = Mysqlhandler.signup(handleMe, uname, pwd, 2)
    str1 = "Signed up and auto-Logged in as:" + uname
    str2 = "ERROR: USERNAME TAKEN"


    if(var1 == 1):
        return render_template('results.html',
        the_username=uname, string=str1
        )
    else :
        return render_template('results.html',
        the_username=uname, string=str2
        )

@app.route('/user/login_form', methods=['POST'])    #for buyer->customer login
def login_form() -> 'html':

    uname = request.form['uname']
    pwd = request.form['pwd']

    handleMe2 = Mysqlhandler()
    var1 = Mysqlhandler.login(handleMe2, uname, pwd, 1)
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

@app.route('/user/login_form2', methods=['POST'])   #for vendor login
def login_form2() -> 'html':

    uname = request.form['uname']
    pwd = request.form['pwd']

    handleMe2 = Mysqlhandler()
    var1 = Mysqlhandler.login(handleMe2, uname, pwd, 2)
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
@app.route('/user/prod', methods=['POST', 'GET'])   #for products
def prod() -> 'html':

    msg = ''
    var1 = []

    handleMe2 = Mysqlhandler()
    var1 = Mysqlhandler.product(handleMe2)                  #all products are stored in list

    return render_template('prod2.html', products=var1)


@app.route('/user/search', methods=['POST', 'GET'])   #for products
def search():
    search_req = request.form['search_in']
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(search_req)

    handleMe2 = Mysqlhandler()
    records = Mysqlhandler.search(handleMe2, search_req)
    print("tftftftftftftftftfftttft")
    print(records)
    return render_template('prod2.html', products=records)
app.run(host = "127.0.0.1", port = 5000, debug = True)
