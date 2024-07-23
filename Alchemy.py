from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["User"] = relationship(back_populates="addresses")
    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select

engine = create_engine("sqlite://", echo=True)
Base.metadata.create_all(engine)
session = Session(engine)

spongebob = User(
    name="spongebob",
    fullname="Spongebob Squarepants",
    addresses=[Address(email_address="spongebob@sqlalchemy.org")],
)
sandy = User(
    name="sandy",
    fullname="Sandy Cheeks",
    addresses=[
        Address(email_address="sandy@sqlalchemy.org"),
        Address(email_address="sandy@squirrelpower.org"),
    ],
)
patrick = User(name="patrick", fullname="Patrick Star")
session.add(spongebob)
session.add_all([sandy, patrick])
session.commit()

stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))

for user in session.scalars(stmt):
    print(user)

stmt = (
    select(Address)
    .join(Address.user)
    .where(User.name == "sandy")
    .where(Address.email_address == "sandy@sqlalchemy.org")
)
sandy_address = session.scalars(stmt).one()

stmt = select(User).where(User.name == "patrick")
patrick = session.scalars(stmt).one()
patrick.addresses.append(Address(email_address="patrickstar@sqlalchemy.org"))
sandy_address.email_address = "sandy_cheeks@sqlalchemy.org"

session.commit()

sandy = session.get(User, 2)
sandy.addresses.remove(sandy_address)

session.flush()

session.delete(patrick)

session.commit()

'''
class ModelName(db.Model):
    """
    docstring here
    """
    ...

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

user_query = session.query(User).filter_by(id=someid)
data_to_update = dict(name="marchel", fullname="richie marchel")
user_query.update(data_to_update)

sandy = User(id=2, name='sandy', fullname='Sandy Cheeks')
session.add(sandy)
#-----
sandy = session.execute(select(User).filter_by(name="sandy")).scalar_one()
sandy.fullname = "Sandy Squirrel"
#-----
sandy = session.get(User, 3)
#-----
sandy.__dict__ 
#-----
session.delete(patrick)
#-----
#session.flush()
session.commit()
session.close()
'''