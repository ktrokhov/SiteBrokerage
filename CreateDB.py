from app import db, Brocker

db.create_all()
# create
firstTest = Brocker('Test1')
db.session.add(firstTest)
db.session.commit()