from models import *
import requests
import traceback
from settings import token


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


def sendMessage(target_user, msg):
    try:
        payload = {'recipient': {'id': target_user}, 'message': {'text': msg}}
        r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload)
    except Exception as e:
        print(traceback.format_exc())  # something went wrong
    return "Foo!"  # Not Really Necessary


def getLendList(sender):
    b_list = filter(lambda b: b.amount > 0, session.query(BorrowTrans).filter_by(creditor_id=sender))
    s = "## Lend List\n"
    for b in b_list:
        s += "{}: {}\n".format(b.me.name, b.amount)
    # print(s)
    return s


def getBorrowList(sender):
    b_list = filter(lambda b: b.amount > 0, session.query(BorrowTrans).filter_by(me_id=sender))
    s = "## Borrow List\n"
    for b in b_list:
        s += "{}: {}\n".format(b.creditor.name, b.amount)
    # print(s)
    return s