import webapp2

from google.appengine.ext import db
from Main_Handler import Handler

# Handler which generates the editpost page
class EditPost(Handler):
	def get(self, blog_id):
		# make sure user is signed in
		if self.loginStatus() == 1:
			self.redirect("/login")
			return
		
		key = db.Key.from_path('Blog', int(blog_id))
		blog = db.get(key)

		# make sure the post exists
		if self.validPost(blog):
			self.redirect("/")
			return

		# ensure that user owns post
		if not self.userOwnsPost(blog):
			self.redirect("/")
			return

		# if reached by get populate the form with the post properties
		self.render('editpost.html', blog = blog, loginStatus = self.loginStatus())

	def post(self, blog_id):
		# make sure user is signed in
		if self.loginStatus() == 1:
			self.redirect("/login")
			return

		title = self.request.get("title")
		blog = self.request.get("blog")
		blog_id =self.request.get("blog_id")

		key = db.Key.from_path('Blog', int(blog_id))
		blog_to_update = db.get(key)

		# make sure the post exists
		if self.validPost(blog_to_update):
			self.redirect("/")
			return

		# ensure that user owns post
		if not self.userOwnsPost(blog_to_update):
			self.redirect("/")
			return

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
		# make sure user is signed in
		if self.loginStatus() == 1:
			self.redirect("/login")
			return

		key = db.Key.from_path('Blog', int(blog_id))
		blog_to_delete = db.get(key)

		# make sure the post exists
		if self.validPost(blog_to_delete):
			self.redirect("/")
			return

		# only allowed to delete if the usernames match
		if self.userOwnsPost(blog_to_delete):
			db.delete(blog_to_delete)
			self.redirect('/')
		else:
			self.redirect('/')