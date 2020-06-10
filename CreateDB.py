from app import db, Brocker

# db.create_all()
# create
firstTest = Brocker('Test3')
db.session.add(firstTest)
db.session.commit()