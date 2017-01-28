import webapp2
from google.appengine.ext import db
from Main_Handler import Handler
from ..Models.Blog import Blog

# Handler to render the page to create a new post
class NewBlogPage(Handler):
	def get(self):
		if self.loginStatus() == 1:
			self.redirect("/login")  # must be logged in to post, if not redirected
			return
		self.render("NewPost.html", title="", blog="", error="", loginStatus=self.loginStatus())

	def post(self):
		if self.loginStatus() == 1:
			self.redirect("/login")  # must be logged in to post, if not redirected
			return
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