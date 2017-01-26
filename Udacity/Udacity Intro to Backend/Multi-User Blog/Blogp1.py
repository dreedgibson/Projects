# import statements to ensure that all various classes are working in cohesion
import os
import webapp2
import jinja2
import re
import random
import string
import hashlib
from google.appengine.ext import db

#create the jinja environment that allows for templating html files
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

#regex for validation purposes
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")

# the following three functions are used to hash user passwords and
# verify that correct passwords have been entered for login purposes
def make_salt():
	return ''.join(random.choice(string.letters) for x in xrange(5))

def make_pw_hash(name, pw, salt=make_salt()):
	h = hashlib.sha256(name + pw + salt).hexdigest()
	return '%s|%s|%s' % (name, h, salt)

def valid_pw(name, pw, h):
	salt = h.split("|")[2]
	if h == make_pw_hash(name, pw, salt):
		return True

# Parent handler class that contains the three functions given during the 
# course as well as two others used to verify if someone is logged in and
# to return the username of the person logged in
class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

	def loginStatus(self):
		if self.request.cookies.get("key") == "":
			return 1
		else:
			return 0
	def getUsername(self):
		if self.loginStatus() == 0:
			username = self.request.cookies.get("key")
			if username != None:
				return username.split("|")[0]
			else:
				return ""
		else: 
			return ""

# Two google datastore databases: 
# Blog is used to store all of the properties associated with the blog posts
# User is used to store data about all users registered to site
class Blog(db.Model):
	title = db.StringProperty(required = True)
	blog = db.TextProperty(required = True)
	createdby = db.StringProperty()
	lastModified = db.DateTimeProperty(auto_now = True)
	created = db.DateTimeProperty(auto_now_add = True)

class User(db.Model):
	username = db.StringProperty(required = True)
	pw_hash = db.StringProperty(required = True)
	email = db.StringProperty()

class Comments(db.Model):
	blog_id = db.StringProperty(required = True)
	username = db.StringProperty(required = True)
	comment_field = db.TextProperty(required = True)
	date_of_comment = db.DateTimeProperty(auto_now_add = True)

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

# Handler to render the page to create a new post
class NewBlogPage(Handler):
	def get(self):
		if self.loginStatus() == 1:
			self.redirect("/login")  # must be logged in to post, if not redirected
		self.render("NewPost.html", title="", blog="", error="", loginStatus=self.loginStatus())

	def post(self):
		title = self.request.get("title")
		blog = self.request.get("blog")

		# subject and content are required field, ensure they are filled in
		if title and blog:
			b = Blog(title = title, blog = blog, createdby = self.getUsername())
			b.put()
			self.redirect("/" + str(b.key().id())) # after successful creation redirect to permalink page
		else:
			error = "we need both a subject and content!"
			self.render_front("NewPost.html", title, blog, error)
		
# Handler to render the permalink page	
class PostedBlog(Handler):
	def get(self, blog_id):
		key = db.Key.from_path('Blog', int(blog_id))
		blog = db.get(key)

		comments = db.GqlQuery("SELECT * FROM Comments WHERE blog_id = '%s'" %str(blog.key().id()))
		self.render("permalink.html", blog=blog, username = self.getUsername(), loginStatus=self.loginStatus(), comments = comments, error = "")

	def post(self, blog_id):
		key = db.Key.from_path('Blog', int(blog_id))
		blog = db.get(key)

		# retrieve the comment from the form
		comment = self.request.get("Comment")

		if comment:
			c = Comments(blog_id = str(blog.key().id()), username = self.getUsername(), comment_field = comment)
			c.put()
			self.redirect("/" + str(blog.key().id()))
		else:
			error = "You must enter a comment"
			comments = db.GqlQuery("SELECT * FROM Comments WHERE blog_id = '%s'" %str(blog.key().id()))
			self.render("permalink.html", blog=blog, username = self.getUsername(), loginStatus=self.loginStatus(), comments = comments, error = error)

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

# Handler which generates the editpost page
class EditPost(Handler):
	def get(self, blog_id):
		if self.loginStatus() == 1:
			self.redirect("/login")
		
		key = db.Key.from_path('Blog', int(blog_id))
		blog = db.get(key)

		# if reached by get populate the form with the post properties
		self.render('editpost.html', blog = blog, loginStatus = self.loginStatus())

	def post(self, blog_id):
		title = self.request.get("title")
		blog = self.request.get("blog")
		blog_id =self.request.get("blog_id")

		key = db.Key.from_path('Blog', int(blog_id))
		blog_to_update = db.get(key)

		# update the blog post and redirect back to the permalink page
		if title and blog:
			blog_to_update.blog = blog
			blog_to_update.title = title
			blog_to_update.put()

			self.redirect("/" + str(blog_to_update.key().id()))
		else:
			error = "we need both a subject and content!"
			self.render("editpost.html", title, blog, error)

# Handler to delete a blog post
class DeleteBlogPost(Handler):
	def get(self, blog_id):
		
		key = db.Key.from_path('Blog', int(blog_id))
		blog_to_delete = db.get(key)

		# only allowed to delete if the usernames match
		if blog_to_delete.createdby == self.getUsername():
			db.delete(blog_to_delete)
			self.redirect('/')
		else:
			self.redirect(404)

# Handler to delete comments
class DeleteComment(Handler):
	def post(self, comment_id):
		
		key = db.Key.from_path('Comments', int(comment_id))
		comment_to_delete = db.get(key)

		# only allowed to delete if the usernames match
		if comment_to_delete.username == self.getUsername():
			db.delete(comment_to_delete)
			self.redirect('/')
		else:
			self.redirect(404)

# mapping of url to handlers
app = webapp2.WSGIApplication([('/', MainPage),
							   ('/newpost', NewBlogPage),
							   ('/([0-9]+)', PostedBlog),
							   ('/signup', SignUpPage), 
							   ('/welcome', WelcomePage),
							   ('/login', LoginPage),
							   ('/logout', Logout),
							   ('/editpost/([0-9]+)', EditPost),
							   ('/deleteblogpost/([0-9]+)', DeleteBlogPost),
							   ('/deletecomment/([0-9]+)', DeleteComment)], debug=True)
