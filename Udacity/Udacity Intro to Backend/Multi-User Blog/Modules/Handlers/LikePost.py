import webapp2
from google.appengine.ext import db
from Main_Handler import Handler
from ..Models.Likes import Likes

# Handler to render the permalink page
class LikePost(Handler):
	def post(self, blog_id):
		# make sure user is signed in
		if self.loginStatus() == 1:
			self.redirect("/login")
			return

		key = db.Key.from_path('Blog', int(blog_id))
		blog = db.get(key)

		# ensure validity of post
		if self.validPost(blog):
			self.redirect("/")
			return

		comments = db.GqlQuery("SELECT * FROM Comments WHERE blog_id = '%s'" %str(blog.key().id()))
		like = db.GqlQuery("SELECT * FROM Likes WHERE blog_id = '%s'" %str(blog.key().id()))
		numlikes = like.count()

		# error if try to like own post
		if blog.createdby == self.getUsername():
			error = "you can't like your own posts!"
			self.render("permalink.html", blog=blog, username = self.getUsername(), loginStatus=self.loginStatus(), 
										  comments = comments, error = "", like_error = error, numlikes = numlikes)
			return

		# error if trying to like post more than once
		if numlikes >= 1:
			error = "you can only like a post once"
			self.render("permalink.html", blog=blog, username = self.getUsername(), loginStatus=self.loginStatus(), 
										  comments = comments, error = "", like_error = error, numlikes = numlikes)
			return

		l = Likes(blog_id = str(blog.key().id()), username = self.getUsername())
		l.put()

		self.redirect("/" + str(blog.key().id()))