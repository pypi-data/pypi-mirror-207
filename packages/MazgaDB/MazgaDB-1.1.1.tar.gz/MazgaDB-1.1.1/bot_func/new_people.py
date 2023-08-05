from sql_func import *


def new_people(db, message):
    if not db.is_there(message.from_user.id):
        db.append([message.from_user.id, message.from_user.first_name, 100])
