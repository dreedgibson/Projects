import webapp2
import re

from google.appengine.ext import db
from Main_Handler import Handler
from ..Models.User import User
from ..Functions.pw_functions import make_salt, make_pw_hash, valid_pw

#regex for validation purposes
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")

# Handler to render the registration page
class SignUpPage(Handler):
	def get(self):
		self.render("user_template.html", username="",
										  username_error="",
										  password_error="",
										  verify_error="",
										  email="",
										  email_error="",
										  unique_error="", 
										  loginStatus=self.loginStatus())

	def post(self):
		# retrieve form field and validate input
		username = self.request.get("username")
		password = self.request.get("password")
		verify = self.request.get("verify")
		email = self.request.get("email")
		
		error_message = self.validate(username, password, verify, email)

		if not error_message:
			pw_hash=make_pw_hash(username, password)
			
			u = User(username = username, pw_hash=pw_hash, email=email)
			u.put()
			self.response.headers.add_header('Set-Cookie','key=%s; Path=/'%str(pw_hash))
			self.redirect("/welcome")
		else:
			self.render("user_template.html", username = username,
											  username_error = error_message.get('username_error', ""),
											  password_error = error_message.get('password_error', ""),
											  verify_error = error_message.get('verify_error', ""),
											  email = email,
											  email_error = error_message.get('email_error', ""),
											  unique_error= error_message.get('unique_error',""), 
											  loginStatus=self.loginStatus())

	# validate function to ensure that every condition has been met in order to sign up
	# ie valid emails passwords and usernames have been chosen
	# the database is queried in verifyUniqueUser in order to determine if the 
	# selected username has already been taken.
	def validate(self, username, password, verify, email):
		error_message = {}
		if not self.valid_username(username):
			error_message['username_error'] = "That is not a valid username"
		if not self.valid_password(password):
			error_message['password_error'] = "That is not a valid password"
		if not self.verify_pass(password, verify):
			error_message['verify_error'] = "The two passwords must match"
		if not self.verify_email(email):
			error_message['email_error'] = "That is not a valid email"
		if not self.verifyUniqueUser(username):
			error_message['unique_error'] = "That username already exists"

		return error_message

	def valid_username(self, username):
		return USER_RE.match(username)
	def valid_password(self, password):
		return PASS_RE.match(password)
	def verify_pass(self, password, verify):
		return password == verify
	def verify_email(self, email):
		return EMAIL_RE.match(email) or email == ""
	def verifyUniqueUser(self, username):
		q = db.GqlQuery("SELECT * FROM User WHERE username = '%s'"%str(username))
		return q.count() == 0

# Handler to render the welcome page
class WelcomePage(Handler):
	def get(self):
		if self.loginStatus == 1:
			self.redirect("/login")
		self.render("welcome.html", username = self.getUsername(), loginStatus=self.loginStatus())