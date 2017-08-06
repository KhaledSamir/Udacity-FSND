from flask import Flask , render_template , url_for , request , redirect , flash , jsonify

app = Flask(__name__)

# import CRUD Operations from Lesson 1
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/Menu/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
    return render_template('menu.html' , restaurant = restaurant , items = items)

@app.route('/restaurants/<int:restaurant_id>/Menu/JSON')
def restaurantMenuJSON(restaurant_id):
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant_id)
    return jsonify(MenuItems=[i.serialize for i in items])


@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def menuItemJson(restaurant_id , menu_id):
    item = session.query(MenuItem).filter_by(restaurant_id = restaurant_id , id = menu_id).one()
    return jsonify(item = item.serialize)


@app.route('/restaurant/<int:restaurant_id>/new/', methods=["GET" , "POST"])
def newmenuitem(restaurant_id):
    if request.method == "POST":
        newitem = MenuItem(name = request.form["name"], restaurant_id=restaurant_id)
        session.add(newitem)
        session.commit()
        flash('new Menu added!')
    elif request.method == "GET":
        return render_template('newMenuItem.html' , restaurant_id = restaurant_id)
    return redirect(url_for('restaurantMenu' , restaurant_id = restaurant_id))
    #return "Page to create new MenuItem!"

@app.route('/restaurant/<int:restaurantId>/<int:menuItemId>/edit/' , methods= ["GET" , "POST"])
def editmenuitem(restaurantId,menuItemId):
    menuitem = session.query(MenuItem).filter_by(restaurant_id = restaurantId , id = menuItemId).one()
    if request.method == "POST":
        menuitem.name = request.form["name"]
        session.add(menuitem)
        session.commit()
        flash('menuitem has been modified!!')
        return redirect(url_for('restaurantMenu' , restaurant_id = restaurantId))
    return render_template('editMenuItem.html' , restaurantId = restaurantId , menuItemId = menuItemId , i = menuitem)


@app.route('/restaurant/<int:restaurantId>/<int:menuItemId>/delete/' , methods = ["GET" , "POST"])
def deletemenuitem(restaurantId,menuItemId):
    item = session.query(MenuItem).filter_by(restaurant_id = restaurantId , id = menuItemId).one()
    if request.method == "POST":
        session.delete(item)
        session.commit()
        flash('menuitem has been deleted!!')
        return redirect(url_for('restaurantMenu' , restaurant_id = restaurantId))
    return render_template('deleteMenuItem.html' , restaurantId = restaurantId , menuItemId = menuItemId , i = item)

if __name__ == "__main__":
 try:
        app.secret_key = 'super_secret_key'
        app.debug = True
        app.run(host='0.0.0.0' , port=5000)
 except KeyboardInterrupt:
        print 'Server Stopped'