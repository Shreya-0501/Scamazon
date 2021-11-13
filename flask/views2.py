from flask import Flask, render_template, request
from dbhandler import Mysqlhandler


app = Flask(__name__)

PHONE = 0

@app.route('/user/register')
def create_user() -> 'html':
    return render_template('entry.html',
    the_title='Are you a user already?')

@app.route('/user/display', methods=['POST'])
def display_user() -> str:
    handleMe = Mysqlhandler()
    #Mysqlhandler.initial(handleMe)
    
    if request.method == 'POST':
        if request.form['submit_button'] == 'Customer':
            return render_template('clogin.html',)
        elif request.form['submit_button'] == 'Vendor':
            return render_template('vlogin.html',)

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

@app.route('/user/display2', methods=['POST'])
def display2_user() -> str:
    return render_template('done2.html',
    )
    # name = request.form['name']
    # dob = request.form['dob']
    # phno = request.form['phno']
    # handleMe = Mysqlhandler()
    # Mysqlhandler.update_user(handleMe, name, phno, dob)
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
    handleMe = Mysqlhandler()
    Mysqlhandler.delete_user(handleMe, phno)
    return render_template('done.html',
    )

@app.route('/user/login_form', methods=['POST'])
def login_form() -> str:
    handleMe = Mysqlhandler()
    #Mysqlhandler.initial(handleMe)

    name = request.form['name']
    phno = request.form['phno']
    uname = request.form['uname']
    pwd = request.form['pwd']
    #PHONE = phno
    # handleMe2 = Mysqlhandler()
    # Mysqlhandler.add_user(handleMe2, name, phno, dob)
    return render_template('results.html',
    the_name=name,
    the_phno=phno,
    the_username=uname,
    )

app.run(host = "127.0.0.1", port = 5000, debug = True)
