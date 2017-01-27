import webapp2
from google.appengine.ext import db
from Main_Handler import Handler
from ..Models.Comments import Comments

# Handler to render the permalink page
class PostedBlog(Handler):
	def get(self, blog_id):
		key = db.Key.from_path('Blog', int(blog_id))
		blog = db.get(key)

		if self.validPost(blog):
			self.redirect("/")

		comments = db.GqlQuery("SELECT * FROM Comments WHERE blog_id = '%s'" %str(blog.key().id()))
		self.render("permalink.html", blog=blog, username = self.getUsername(), loginStatus=self.loginStatus(), comments = comments, error = "")

	def post(self, blog_id):
		key = db.Key.from_path('Blog', int(blog_id))
		blog = db.get(key)

		if self.validPost(blog):
			self.redirect("/")
			
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