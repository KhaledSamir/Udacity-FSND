from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

# import CRUD Operations from Lesson 1
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class webServerHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            try:
                if self.path.endswith("/hello"):
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output = ""
                    output += "<html><body>"
                    output += "<h1>Hello!</h1>"
                    output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                    output += "</body></html>"
                    self.wfile.write(output)
                    print(output)
                    

                if self.path.endswith("/hola"):
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output = ""
                    output += "<html><body>"
                    output += "<h1>&#161 Hola !</h1>"
                    output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                    output += "</body></html>"
                    self.wfile.write(output)
                    print(output)
                
                if self.path.endswith('/restaurants'):
                    self.send_response(200)
                    self.send_header('Content-type' , 'text/html')
                    self.end_headers()
                    restaurants = session.query(Restaurant).all()
                    output = ""
                    output += "<html><body>"
                    output += ''' <a href="/restaurant/new">Make a new Restaurant Here</a> <br>'''
                    for res in restaurants:
                        output +=  "<strong>" + str(res.id) + " " + res.name + "</strong>"
                        output +=  "<br><a href='/restaurant/%s/edit'>Edit</a> <br>"  % str(res.id)
                        output +=  "<a href='/restaurant/%s/delete'>Delete</a> <br><br>" % str(res.id)
                    output += "</body></html>"
                    self.wfile.write(output)
                    return

                if self.path.endswith('/restaurant/new'):
                    self.send_response(200)
                    self.send_header('Content-type' , 'text/html')
                    self.end_headers()
                    output = ""
                    output += '''<form method='POST' enctype='multipart/form-data' action='/restaurant/new'>
                                 <h2>Make a New Restaurant</h2><input name="resname" type="text" >
                                 <input type="submit" value="Create"> </form>'''
                    
                    self.wfile.write(output)
                    return

                if self.path.endswith("/edit"):
                    restaurantIDPath = self.path.split("/")[2]
                    myRestaurantQuery = session.query(Restaurant).filter_by(
                        id=restaurantIDPath).one()
                    if myRestaurantQuery:
                        self.send_response(200)
                        self.send_header('Content-type', 'text/html')
                        self.end_headers()
                        output = "<html><body>"
                        output += "<h1>"
                        output += myRestaurantQuery.name
                        output += "</h1>"
                        output += "<form method='POST' enctype='multipart/form-data' action = '/restaurant/%s/edit' >" % restaurantIDPath
                        output += "<input name = 'resname' type='text' placeholder = '%s' >" % myRestaurantQuery.name
                        output += "<input type = 'submit' value = 'Rename'>"
                        output += "</form>"
                        output += "</body></html>"

                        self.wfile.write(output)
                
                if self.path.endswith("/delete"):
                    restaurantIDPath = self.path.split("/")[2]
                    myRestaurantQuery = session.query(Restaurant).filter_by(
                        id=restaurantIDPath).one()
                    if myRestaurantQuery:
                        self.send_response(200)
                        self.send_header('Content-type', 'text/html')
                        self.end_headers()
                        output = "<html><body>"
                        output += "<h1>"
                        output += "Are you sure you wanna delete " + myRestaurantQuery.name
                        output += "</h1>"
                        output += "<form method='POST' enctype='multipart/form-data' action = '/restaurant/%s/delete' >" % restaurantIDPath
                        output += "<input type = 'submit' value = 'Delete'>"
                        output += "</form>"
                        output += "</body></html>"

                        self.wfile.write(output)

            except IOError:
                self.send_error(404, 'File Not Found: %s' % self.path)

        def do_POST(self):
            try:
                
                if self.path.endswith("/restaurant/new"):
                    ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                    if ctype == 'multipart/form-data':
                        fields = cgi.parse_multipart(self.rfile, pdict)
                        messagecontent = fields.get('resname')

                        # Create new Restaurant Object
                        newRestaurant = Restaurant(name=messagecontent[0])
                        session.add(newRestaurant)
                        session.commit()

                        self.send_response(301)
                        self.send_header('Content-type', 'text/html')
                        self.send_header('Location', '/restaurants')
                        self.end_headers()
                        return

                if self.path.endswith("/edit"):
                    ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                    if ctype == 'multipart/form-data':
                        fields = cgi.parse_multipart(self.rfile, pdict)
                        messagecontent = fields.get('resname')
                        restaurantIDPath = self.path.split("/")[2]

                        myRestaurantQuery = session.query(Restaurant).filter_by(
                            id=restaurantIDPath).one()
                        if myRestaurantQuery != []:
                            myRestaurantQuery.name = messagecontent[0]
                            session.add(myRestaurantQuery)
                            session.commit()
                            self.send_response(301)
                            self.send_header('Content-type', 'text/html')
                            self.send_header('Location', '/restaurants')
                            self.end_headers()
                        return
                if self.path.endswith("/delete"):
                    ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                    if ctype == 'multipart/form-data':
                        fields = cgi.parse_multipart(self.rfile, pdict)
                        messagecontent = fields.get('resname')
                        restaurantIDPath = self.path.split("/")[2]

                        myRestaurantQuery = session.query(Restaurant).filter_by(
                            id=restaurantIDPath).one()
                        if myRestaurantQuery != []:
                            session.delete(myRestaurantQuery)
                            session.commit()
                            self.send_response(301)
                            self.send_header('Content-type', 'text/html')
                            self.send_header('Location', '/restaurants')
                            self.end_headers()
                        return
                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()
                    return

                self.send_header('Content-type', 'text/html')
                self.end_headers()
                ctype, pdict = cgi.parse_header(
                self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('message')
                output = ""
                output += "<html><body>"
                output += " <h2> Okay, how about this: </h2>"
                output += "<h1> %s </h1>" % messagecontent[0]
                output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                output += "</body></html>"
                self.wfile.write(output)
                print(output)
            except:
                pass

def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webServerHandler)
        print "Web Server running on port %s" % port
        server.serve_forever()
    except KeyboardInterrupt:
        print(" ^C entered, stopping web server....")
        server.socket.close()

if __name__ == '__main__':
    main()