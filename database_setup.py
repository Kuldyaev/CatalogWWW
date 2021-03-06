from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    picture = Column(String(250))
    


class Categories(Base):
    __tablename__ = 'category'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'id'           : self.id,
       }
 
class MenuItem(Base):
    __tablename__ = 'items'


    name =Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    price = Column(String(8))
    description = Column(String(250))
    category_id = Column(Integer,ForeignKey('category.id'))
    category = relationship(Categories)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)



    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'description'  : self.description,
           'id'           : self.id,
           'price'        : self.price,
        }



engine = create_engine('sqlite:///items.db?check_same_thread=False')
 

Base.metadata.create_all(engine)