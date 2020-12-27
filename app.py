import os, json
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from secure_check import authenticate, identity
from flask_jwt import JWT
from flask_restful import Api, Resource
from flask_cors import CORS

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey'

db = SQLAlchemy(app)
Migrate(app, db)
CORS(app)

api = Api(app)
jwt = JWT(app, authenticate, identity)


class Brocker(db.Model):
    __tablename__ = 'Broker'
    # делаем таблицу
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    SiteBankiRU = db.Column(db.REAL)
    SiteSmartLabRU = db.Column(db.REAL)
    SiteOtzovikRU = db.Column(db.REAL)
    Average = db.Column(db.REAL)
    Reviews = db.Column(db.TEXT)

    # def __init__(self, name, SiteBankiRU, SiteSmartLabRU, SiteOtzovikRU, Average, Reviews):
    #     print("KEK")
    #     self.name = name
    #     self.SiteBankiRU = SiteBankiRU
    #     self.SiteSmartLabRU = SiteSmartLabRU
    #     self.SiteOtzovikRU = SiteOtzovikRU
    #     self.Average = Average
    #     if Reviews is None or Reviews == '':
    #         Reviews = '[]'
    #     self.Reviews = json.loads(Reviews)
    #     print(self.Reviews)
    #     print("LEL")

    def json(self):
        if self.Reviews is None or self.Reviews == '':
            self.Reviews = '[]'
        self.Reviews = json.loads(self.Reviews)
        # print(self.Reviews)
        return {'name': self.name, 'SiteBankiRU': self.SiteBankiRU, 'SiteSmartLabRU': self.SiteSmartLabRU,
                'SiteOtzovikRU': self.SiteOtzovikRU, 'Average': self.Average, 'reviews': self.Reviews}

    def __repr__(self):
        return f" {self.name, self.SiteBankiRU, self.SiteSmartLabRU, self.SiteOtzovikRU} "


class AllData(Resource):

    def get(self):
        allBrockers = Brocker.query.all()
        return [pup.json() for pup in allBrockers]


api.add_resource(AllData, '/brk')


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/list')
def listBr():
    brAll = Brocker.query.all()
    return render_template('list.html', brAll=brAll)


if __name__ == '__main__':
    app.run()
