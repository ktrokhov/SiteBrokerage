import os
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey'

db = SQLAlchemy(app)

Migrate(app, db)


class Brocker(db.Model):
    __tablename__ = 'Broker'
    # делаем таблицу
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    SiteBankiRU = db.Column(db.REAL)
    SiteSmartLabRU = db.Column(db.REAL)
    SiteOtzovikRU = db.Column(db.REAL)

    def __init__(self, name, SiteBankiRU, SiteSmartLabRU, SiteOtzovikRU):
        self.name = name
        self.SiteBankiRU = SiteBankiRU
        self.SiteSmartLabRU = SiteSmartLabRU
        self.SiteOtzovikRU = SiteOtzovikRU

    def __repr__(self):
        return f"Test {self.name} "


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/list')
def listBr():
    brAll = Brocker.query.all()
    return render_template('list.html', brAll=brAll)


if __name__ == '__main__':
    app.run()
