from flask import Flask, render_template, redirect, url_for, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
app = Flask(__name__)


engine = create_engine('sqlite:///restaurantmenu.db',connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/restaurant/')
def showRestaurants():
  restaurant = session.query(Restaurant).all()
  return render_template('restaurants.html', restaurant=restaurant)
  return "Show all restaurants"

@app.route('/restaurant/new/', methods = ['GET','POST'])
def newRestaurant():
  if request.method == 'POST':
    newRestaurant = Restaurant(name=request.form['name'])
    session.add(newRestaurant)
    session.commit()
    return redirect(url_for('showRestaurants'))
  else:
    return render_template('newRestaurant.html')
  return "Created new restaurant"

@app.route('/restaurant/<int:restaurant_id>/edit/', methods = ['GET','POST'])
def editRestaurant(restaurant_id):
  editedRestaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
  if request.method == 'POST':
    if request.form['name']:
      editedRestaurant.name = request.form['name']
      return redirect(url_for('showRestaurants'))
    else:
        return render_template(
            'editRestaurant.html', restaurant=editedRestaurant)
  return "Edited restaurant %s"%restaurant_id

@app.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
  restaurantToDelete = session.query(Restaurant).filter_by(id=restaurant_id).one()
  if request.method == 'POST':
    session.delete(restaurantToDelete)
    session.commit()
    return redirect(url_for('showRestaurants', restaurant_id=restaurant_id))
  else:
    return render_template('deleteRestaurant.html', restaurant=restaurantToDelete)
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
