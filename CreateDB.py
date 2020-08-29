# import sqlite3
# from app import db, Brocker
#
# db1 = sqlite3.connect('data.sqlite')
# sql = "SELECT * from Broker;"
# cur = db1.cursor()
# cur.execute(sql)
# while True:
#     record = cur.fetchall()
#     if record is None:
#         break
#     for i in record:
#         if i[2] != 0.0 and i[3] != 0.0 and i[4] != 0.0:
#             avg = (i[2] + i[3] + i[4]) / 3
#             ans = int(avg * 100)/100
#             puppyFr = Brocker.query.filter_by(name=i[1]).update({'Average': ans})
#             db.session.commit()
#         if i[2] == 0.0 and i[3] != 0.0 and i[4] != 0.0:
#             avg = (i[3] + i[4]) / 2
#             ans = int(avg * 100) / 100
#             float("{0:.1f}".format(avg))
#             puppyFr = Brocker.query.filter_by(name=i[1]).update({'Average': ans})
#             db.session.commit()
#
#         if i[2] != 0.0 and i[3] == 0.0 and i[4] != 0.0:
#             avg = (i[2] + i[4]) / 2
#             ans = int(avg * 100) / 100
#             float("{0:.1f}".format(avg))
#             puppyFr = Brocker.query.filter_by(name=i[1]).update({'Average': ans})
#             db.commit()
#         if i[2] != 0.0 and i[3] != 0.0 and i[4] == 0.0:
#             avg = (i[2] + i[3]) / 2
#             ans = int(avg * 100) / 100
#             float("{0:.1f}".format(avg))
#             puppyFr = Brocker.query.filter_by(name=i[1]).update({'Average': ans})
#             db.session.commit()
#
#         if i[2] == 0.0 and i[3] == 0.0 and i[4] != 0.0:
#             avg = i[4]
#             ans = int(avg * 100)/100
#             puppyFr = Brocker.query.filter_by(name=i[1]).update({'Average': ans})
#             db.session.commit()
#
#         if i[2] != 0.0 and i[3] == 0.0 and i[4] == 0.0:
#             avg = i[2]
#             ans = int(avg * 100)/100
#             puppyFr = Brocker.query.filter_by(name=i[1]).update({'Average': ans})
#             db.session.commit()
#
#         if i[2] == 0.0 and i[3] != 0.0 and i[4] == 0.0:
#             avg = i[3]
#             ans = int(avg * 100)/100
#             puppyFr = Brocker.query.filter_by(name=i[1]).update({'Average': ans})
#             db.session.commit()
#
#         if i[2] == 0.0 and i[3] == 0.0 and i[4] == 0.0:
#             avg = i[3]
#
#             puppyFr = Brocker.query.filter_by(name=i[1]).update({'Average': 0.0})
#             db.session.commit()
# db.close()

