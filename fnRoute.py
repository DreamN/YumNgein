from regRouteLib import *
from utils import *
from models import Base, engine, session, BorrowTrans, Person

regFunc = regFnDetector()


@regFunc.route("hi")
def hello(sender):
    return "Hello there!"


@regFunc.route(r"^i am (?P<name>.+)")
def regName(sender, name):
    person = getPersonById(sender)
    return changePersonName(person, name)


@regFunc.route(r"^borrow (?P<creditor>.+) (?P<amount>.+)")
def borrow_money(sender, creditor, amount):
    creditor_user = getPersonByName(creditor)
    me = getPersonById(sender)
    if(creditor_user == "name not found"):
        return "name not found"
    else:
        trans = getBorrowTrans(me, creditor_user)
        old_amount = trans.amount
        trans.borrow(amount=int(amount))
        save(trans)
        CreateTransaction(me, creditor_user, int(amount), "Borrow")
        sendMessage(creditor_user.id, "{} is borrowed {} from you".format(me.name, amount))
        return "You borrowed {} Amount: {} ({}+{})".format(creditor, trans.amount, old_amount, amount)


@regFunc.route(r"^(?P<debtor>.+) return (?P<amount>.+)")
def return_money(sender, debtor, amount):
    debtor_user = getPersonByName(debtor)
    me = getPersonById(sender)
    if(debtor_user == "name not found"):
        return "name not found"
    else:
        trans = getBorrowTrans(debtor_user, me)
        changes = 0 if int(amount) < trans.amount else int(amount) - trans.amount
        trans.returnMoney(amount=int(amount))
        save(trans)
        CreateTransaction(me, debtor_user, int(amount)-changes, "Return")
        sendMessage(debtor_user.id, "you're returned {} to {}".format(amount, me.name))
        if(changes == 0):
            return "{0} return {1} Successfully!!".format(debtor, amount)
        else:
            return "{0} return {1} Successfully!! and {0} recieve changes: {2}".format(debtor, amount, changes)


@regFunc.route(r"borrowlist")
def borrow_list(sender):
    return getBorrowList(sender)


@regFunc.route(r"lendlist")
def lend_list(sender):
    return getLendList(sender)