import webapp2

from google.appengine.ext import db
from Main_Handler import Handler
from ..Functions.pw_functions import make_salt, make_pw_hash, valid_pw

# Handler to render the login page
class LoginPage(Handler):
	def get(self):
		self.render("login_template.html", username="",
										   error="", 
										   loginStatus=self.loginStatus())
	def post(self):
		username = self.request.get("username")
		password = self.request.get("password")

		# query the database for the given username and assign the result to current_user
		q = db.GqlQuery("SELECT * FROM User WHERE username = '%s'"%str(username))
		current_user = q.get()

		# check if username and password match the retrieved username and password
		# if not return error message
		if valid_pw(username, password, current_user.pw_hash):
			self.response.headers.add_header('Set-Cookie','key=%s; Path=/'%str(current_user.pw_hash))
			self.redirect("/welcome")
		else:
			self.render("login_template.html", username=username, error="Invalid Login", loginStatus=self.loginStatus())

# Handler to logout the current user
class Logout(Handler):
	def get(self):
		self.response.headers.add_header('Set-Cookie', 'key=; Path=/')
		self.redirect("/signup")