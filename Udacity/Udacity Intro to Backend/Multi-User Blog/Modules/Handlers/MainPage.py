import webapp2
from google.appengine.ext import db
from Main_Handler import Handler

# Front page ("/") handler that renders the front page of the blog
# all remaining classes will inherit from the 'Handler' class defined
# above, LoginStatus will be passed from now into every render page
# LoginStatus is needed to determine what buttons are rendered into 
# the header either logout or login and register

class MainPage(Handler):
	def render_front(self):
		blogs = db.GqlQuery("SELECT * FROM Blog ORDER BY created DESC limit 10")
		self.render("front.html", blogs = blogs, loginStatus=self.loginStatus(), current_user = self.getUsername())

	def get(self):
		self.render_front()

	def post(self):
		blog_id = self.request.get("blog_id")
		self.redirect("/editpost/" + str(blog_id))