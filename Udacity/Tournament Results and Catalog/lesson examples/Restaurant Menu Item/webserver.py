from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import desc
import cgi

from database_setup import Base, Restaurant, MenuItem

# create engine
engine = create_engine('sqlite:///restaurantmenu.db')

# bind engine to base class
Base.metadata.bind = engine

# create sessionmaker object
DBSession = sessionmaker(bind=engine)

# create session
session = DBSession()

class webserverHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			if self.path.endswith("/edit"):
				# send headers
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				# get restaurant id
				restaurant_id = self.path.split('/')[2]
				
				# query for restaurant name
				restaurant = session.query(Restaurant).filter(Restaurant.id == int(restaurant_id)).one()
				
				# create output
				output = ""
				output += "<html><body><h1>%s</h1>" %(restaurant.name)
				output += '''<form method='POST' enctype='multipart/form-data' action='/restaurant/%s/edit'>''' %(restaurant.id)
				output += '''<input name="restaurant" placeholder = '%s'type="text" >''' %(restaurant.name)
				output += '''<input type="submit" value="Edit"> </form>'''

				self.wfile.write(output)

			if self.path.endswith("/delete"):
				# send headers
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				# get restaurant id
				restaurant_id = self.path.split('/')[2]
				
				# query for restaurant name
				restaurant = session.query(Restaurant).filter(Restaurant.id == int(restaurant_id)).one()
				
				# create output
				output = ""
				output += "<html><body><h1>Are you sure you want to delete %s?</h1>" %(restaurant.name)
				output += '''<form method='POST' enctype='multipart/form-data' action='/restaurant/%s/delete'>''' %(restaurant.id)
				output += '''<input type="submit" value="Delete"> </form>'''

				self.wfile.write(output)

			if self.path.endswith("/restaurant"):

				# get all restaurants
				all_res = session.query(Restaurant).all()

				# send headers
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				output = ""
				output += "<html><body><h1>Welcome to the Restaurant Page</h1>"
				output += "<h3><a href='/restaurant/new'>Create a New Restaurant!</a></h3>"

				for r in all_res:
					output += "<p>%s</p>" %r.name
					output += "<a href='/restaurant/%s/edit'>Edit</a><br>" %str(r.id)
					output += "<a href='/restaurant/%s/delete'>Delete</a>" %str(r.id)
				output += "</body></html>"
				
				self.wfile.write(output)

				return
			if self.path.endswith("/restaurant/new"):
				# send headers
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				output = ""
				output += "<html><body>"
				output += " <h2> Create a New Restaurant </h2>"
				output += '''<form method='POST' enctype='multipart/form-data' action='/restaurant/new'>'''
				output += '''<input name="restaurant" type="text" ><input type="submit" value="Create"> </form>'''
				output += "</body></html>"

				self.wfile.write(output)
				return

		except IOError:
			self.send_error(404, "File Not Found %s" % self.path)


	def do_POST(self):
		try:
			if self.path.endswith("/restaurant/new"):
				ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))

				if ctype == 'multipart/form-data':
					fields = cgi.parse_multipart(self.rfile, pdict)
					new_res = fields.get('restaurant')

					newRestaurant = Restaurant(name=new_res[0])
					
					# add new restaurant to database and commit changes
					session.add(newRestaurant)
					session.commit()

					# send headers
					self.send_response(301)
					self.send_header('Content-type', 'text/html')
					self.send_header('Location', '/restaurant')
					self.end_headers()

			if self.path.endswith("/edit"):
				ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))

				if ctype == 'multipart/form-data':
					fields = cgi.parse_multipart(self.rfile, pdict)
					update_res = fields.get('restaurant')

					# get restaurant id
					restaurant_id = self.path.split('/')[2]
					upd_restaurant = session.query(Restaurant).filter(Restaurant.id == int(restaurant_id)).one()
					
					# update restaurant name
					upd_restaurant.name = update_res[0]

					# add new restaurant to database and commit changes
					session.add(upd_restaurant)
					session.commit()

					# send headers
					self.send_response(301)
					self.send_header('Content-type', 'text/html')
					self.send_header('Location', '/restaurant')
					self.end_headers()

			if self.path.endswith("/delete"):
				ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))

				if ctype == 'multipart/form-data':
					fields = cgi.parse_multipart(self.rfile, pdict)

					# get restaurant id
					restaurant_id = self.path.split('/')[2]
					del_restaurant = session.query(Restaurant).filter(Restaurant.id == int(restaurant_id)).one()

					# add new restaurant to database and commit changes
					session.delete(del_restaurant)
					session.commit()

					# send headers
					self.send_response(301)
					self.send_header('Content-type', 'text/html')
					self.send_header('Location', '/restaurant')
					self.end_headers()

		except:
		    pass
        
def main():
	try:
		port= 8080
		server = HTTPServer(('', port), webserverHandler)
		print "Web server running on port %s" % port
		server.serve_forever()

	except KeyboardInterrupt:
		print "^C entered, stopping web server..."
		server.socket.close()

if __name__ == '__main__':
	main()