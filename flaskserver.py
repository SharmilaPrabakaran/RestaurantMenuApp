from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
app = Flask(__name__)


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/restaurant/')
def showRestaurants():
  return "Show all restaurants"

@app.route('/restaurant/new/', methods = ['GET','POST'])
def newRestaurant():
  return "Created new restaurant"

@app.route('/restaurant/<int:restaurant_id>/edit/', methods = ['GET','POST'])
def editRestaurant(restaurant_id):
    return "Edited restaurant %s"%restaurant_id

@app.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    return 'This page will be for deleting restaurant %s' % restaurant_id

@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def showMenu(restaurant_id):
    return 'This page is for making a new menu item for restaurant %s'%restaurant_id

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit',methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    return 'This page is for editing menu item %s' % menu_id

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete',methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    return "This page is for deleting menu item %s" % menu_id

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
