from models import *


def getPersonById(sender):
    try:
        person = session.query(Person).filter_by(id=sender).one()
    except:
        print("New user")
        person = Person(sender)
    return person


def getPersonByName(name):
    try:
        person = session.query(Person).filter_by(name=name).one()
        return person
    except:
        return "name not found"


def getBorrowTrans(me, creditor):
    try:
        trans = session.query(BorrowTrans).filter_by(me_id=me.id).filter_by(creditor_id=creditor.id).one()
    except:
        print("New borrow trans")
        trans = BorrowTrans(me, creditor)
    return trans


def save(obj):
    session.add(obj)
    session.commit()
    return True


def CreateTransaction(from_user, to_user, amount, transaction_type):
    t = Transactions(form_user=from_user, to_user=to_user, amount=amount, transaction_type=transaction_type)
    save(t)


def changePersonName(person, name):
    if(person.name == name):
        return "You haven't change your name"
    else:
        try:
            person = session.query(Person).filter_by(name=name).one()
            return "This name is already exist!, Try another name"
        except:
            old_name = person.name
            person.name = name
            session.add(person)
            session.commit()
            return "Changed name from {} to {}".format(old_name, name)