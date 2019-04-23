#configuration
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base #sqlalchemytables
from sqlalchemy.orm import relationship #mapper
from sqlalchemy import create_engine

#Base object:inherit all features of sqlalchemy to build tables
Base = declarative_base()
 
class Restaurant(Base):#class
    __tablename__ = 'restaurant'#corresponding table
   
    id = Column(Integer, primary_key=True)#mapper code Column
    name = Column(String(250), nullable=False)
 
class MenuItem(Base):
    __tablename__ = 'menu_item'

    name =Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer,ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant) #mapper code

#instance of create_engine
engine = create_engine('sqlite:///restaurantmenu.db')
# add and modify tables
Base.metadata.create_all(engine)
