from flask import Flask, url_for, redirect, render_template,request,flash
# import mysql.connector as msc
# msc.__version__
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy # use to create a connection with database

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@db:3306/my_db' #provide password and name of database

db = SQLAlchemy(app)

class User(db.Model):# name of table in data base
    id = db.Column(db.BigInteger, primary_key=True) # define column name and attributes
    name = db.Column(db.String(60), unique=True)
    course = db.Column(db.String(60), unique=True)
    branch = db.Column(db.String(500))
    rollno = db.Column(db.String(300), unique=True)
    email = db.Column(db.String(60), unique=True)
    about_us = db.Column(db.String(500))
    username = db.Column(db.String(300), unique=True)
    password = db.Column(db.String(300), unique=True)

    def __init__(self, id, name, course, branch, rollno,email,about_us,username,password):
        self.id = id
        self.name = name
        self.course = course
        self.branch = branch
        self.rollno = rollno
        self.email = email
        self.about_us = about_us,
        self.username = username
        self.password = password

    @property
    def serialize(self):
        context = {
            'id': self.id,
            'name': self.name,
            'course': self.course,
            'branch': self.branch,
            'rollno': self.rollno,
            'email': self.email,
            'about_us': self.about_us,
            'username': self.username,
            'password': self.password,
        }
        return context




@app.route('/', methods = ['GET','POST'])
def index():
    try:
        if request.method == 'POST':  # request method to use 'POST'
            print('request.methods')
            id = request.form['id']
            name = request.form['name']# syntax to use get() method &&&&DNS_PROBE_FINISHED_NO_INTERNET
            course = request.form['course']
            branch = request.form['branch']
            rollno = request.form['rollno']
            email = request.form['email']
            about_us = request.form['about_us']
            username = request.form['username']
            password=request.form['password']
            print(name, course)


            user = User(
                id=id,
                name=name,
                course=course,
                branch=branch,
                rollno = rollno,
                email = email,
                about_us = about_us,
                username = username,
                password=password

                )
            db.session.add(user)
            db.session.commit()

    except Exception as e:
        import traceback
        print('exceptions >>>>>>>>>>>>>>', e)
        print(traceback.format_exc())

    return render_template('register.html')


if __name__ == '__main__':
   # app.secret_key = os.urandom(12)
   db.create_all()
   app.run(host='0.0.0.0', debug=True)