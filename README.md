# RestaurantMenu
  An interactive Web Application thats presents different Restaurants and their variety of Menu Items that they can view, create, modify and delete.

Software and Libraries this project uses the following libraries:

* Python
* Flask https://flask.pocoo.org/
* SQLAlchemy https://www.sqlalchemy.org/

# Installation

pip install -r requirements.txt

# To run this project

1. Run database_setup.py to create the database using SQLAlchemy, a Python SQL toolkit and Object Relational Mapper.

2. Run menus.py to populate the database.

3. Run server.py in command prompt to start webserver. Client (browser) communicates with server using REST API. REST API is written using flask framework.

4. Navigate to localhost:5000/restaurant/ in the browser to run the app.

# Restaurant End-points:
* /restaurant/                        --  Show all restaurants.
* /restaurant/new/                    --  Add a new restaurant.
* /restaurant/<restaurant_id>/edit/   --  Edit a restaurant.
* /restaurant/<restaurant_id>/delete/ --  Delete a restaurant

# Menu End-points:
* /restaurant/<restaurant_id>(/menu/)           -- Show the full menu
* /restaurant/<restaurant_id>/new/              -- Add a menu item
* /restaurant/<restaurant-id>/<menuid>/edit     -- Edit a menu item
* /restaurant/<restaurant_id>/<menuid>/delete   -- Delete a menu item
  
# CRUD functions:
* showRestaurants()
* newRestaurant()
* editRestaurant()
* deleteRestaurant()
* showMenu()
* newMenuItem()
* editMenuItem()
* deleteMenuItem()
