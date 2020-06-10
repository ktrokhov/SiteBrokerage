from app import db, Brocker

# db.create_all()
# create
firstTest = Brocker('Test2')
db.session.add(firstTest)
db.session.commit()