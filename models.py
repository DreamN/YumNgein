import datetime
from sqlalchemy import Column, ForeignKey, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from settings import getDatabaseString

Base = declarative_base()
engine = create_engine(getDatabaseString())
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class Person(Base):
    __tablename__ = "person"
    id = Column(String(30), primary_key=True)
    name = Column(String(10))

    def __init__(self, facebook_id):
        self.id = facebook_id

    @property
    def serialize(self):
        return {
            'id': self.facebook_id,
            'name': self.name
        }
    # def getBorrowList(self):
    # def getLendList(self):


class BorrowTrans(Base):
    __tablename__ = "borrow_trans"
    id = Column(Integer, primary_key=True)
    me_id = Column(String(30), ForeignKey('person.id'))
    me = relationship(Person, foreign_keys=[me_id])
    creditor_id = Column(String(30), ForeignKey('person.id'))
    creditor = relationship(Person, foreign_keys=[creditor_id])
    amount = Column(Integer, nullable=False)

    def __init__(self, me, creditor):
        self.me = me
        self.creditor = creditor
        self.amount = 0

    def borrow(self, amount):
        self.amount += amount

    def returnMoney(self, amount):
        self.amount = 0 if self.amount < amount else self.amount - amount

    @property
    def serialize(self):
        return {
            'person': self.person,
            'creditor': self.creditor,
            'amount': self.amount
        }


class Transactions(Base):
    __tablename__ = "transaction"
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    form_user_id = Column(String(30), ForeignKey('person.id'))
    form_user = relationship(Person, foreign_keys=[form_user_id])
    to_user_id = Column(String(30), ForeignKey('person.id'))
    to_user = relationship(Person, foreign_keys=[to_user_id])
    amount = Column(Integer, nullable=False)
    transaction_type = Column(String(10), nullable=False)

    def __int__(self, form_user, to_user, amount, transaction_type):
        self.form_user = form_user
        self.to_user = to_user
        self.amount = amount
        self.type = transaction_type

Base.metadata.create_all(engine)