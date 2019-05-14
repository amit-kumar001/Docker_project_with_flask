from flask import Flask, url_for, redirect, render_template,request,flash
# import mysql.connector as msc
# msc.__version__
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy # use to create a connection with database

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@db:3306/list_db' #provide password and name of database

db = SQLAlchemy(app)

class User(db.Model):# name of table in data base
    id = db.Column(db.BigInteger, primary_key=True)
    first = db.Column(db.String(60), unique=True) # define column name and attributes
    second = db.Column(db.String(60), unique=True)
    third = db.Column(db.String(60), unique=True)


    def __init__(self, id,first, second, third):
        self.id = id
        self.first = first
        self.second = second
        self.third = third

    @property
    def serialize(self):
        context = {
            'id': self.id,
            'first': self.first,
            'second': self.second,
            'third': self.third
        }
        return context




@app.route('/', methods = ['GET','POST'])
def index():
    try:
        if request.method == 'POST':  # request method to use 'POST'
            id = request.form['id']
            first = request.form['first']
            second = request.form['second']# syntax to use get() method &&&&DNS_PROBE_FINISHED_NO_INTERNET
            third = request.form['third']

            user = User(
                id=id,
                first=first,
                second=second,
                third=third
                )
            db.session.add(user)
            db.session.commit()

    except Exception as e:
        import traceback
        print('exceptions >>>>>>>>>>>>>>', e)
        print(traceback.format_exc())

    return render_template('list.html')


if __name__ == '__main__':
   # app.secret_key = os.urandom(12)
   db.create_all()
   app.run(host='0.0.0.0', debug=True)