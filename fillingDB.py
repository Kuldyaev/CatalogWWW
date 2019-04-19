from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import *

engine = create_engine('sqlite:///items.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Menu for UrbanBurger
category1 = Categories(name="Books", user_id=1)

session.add(category1)
session.commit()

category2 = Categories(name="Fotos", user_id=1)

session.add(category2)
session.commit()

category3= Categories(name="Mags", user_id=1)

session.add(category3)
session.commit()

category4 = Categories(name="Posters", user_id=1)

session.add(category4)
session.commit()

menuItem2 = MenuItem(name="Harry Potter", description="fantasy about student in Magic School",
                     price="$7.50", category=category1, user_id=1)

session.add(menuItem2)
session.commit()


menuItem1 = MenuItem(name="Lord of Rings", description="very interesting book",
                     price="$2.99", category=category1, user_id=1)

session.add(menuItem1)
session.commit()

menuItem22 = MenuItem(name="Flowers", description="Instructions for gardening",
                     price="$5.50", category=category1, user_id=1)

session.add(menuItem22)
session.commit()

menuItem3 = MenuItem(name="Troy", description="Are you heard about it?",
                     price="$3.99", category=category1, user_id=1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Solt", description="fantastic story",
                     price="$7.99", category=category1, user_id=1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="Disney World Stories", description="fanny stories with old friends",
                     price="$1.99", category=category1, user_id=1)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(name="World History", description="very short about great things",
                     price="$125.99", category=category1, user_id=1)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(name="Best recipes", description="You need it on your kitchen",
                     price="$3.49", category=category1, user_id=1)

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(name="Math for children", description="Useful book for all ages",
                     price="$5.99", category=category1, user_id=1)

session.add(menuItem8)
session.commit()

menuItem9 = MenuItem(name="Cars", description="McQuinn Lightning",
                     price="$9.99", category=category4, user_id=1)

session.add(menuItem9)
session.commit()
                     
menuItem10 = MenuItem(name="Hot and black", description="Mug for coffee",
                     price="$4.99", category=category3, user_id=1)

session.add(menuItem10)
session.commit()


menuItem11 = MenuItem(name="3*5", description="most common size",
                     price="$0.99", category=category2, user_id=1)

session.add(menuItem11)
session.commit()


menuItem12 = MenuItem(name="5*7", description="Bigger then standart",
                     price="$1.49", category=category2, user_id=1)

session.add(menuItem12)
session.commit()



print("added menu items!")