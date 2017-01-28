import webapp2

from google.appengine.ext import db
from Main_Handler import Handler

class EditComment(Handler):
	def get(self, comment_id):
		# make sure user is signed in
		if self.loginStatus() == 1:
			self.redirect("/login")
			return
		
		key = db.Key.from_path('Comments', int(comment_id))
		comment = db.get(key)

		# make sure the comment exists
		if self.validComment(comment):
			self.redirect("/")
			return

		# ensure that user owns the comment
		if not self.userOwnsComment(comment):
			self.redirect("/")
			return

		# if reached by get populate the form with the post properties
		self.render('editcomment.html', comment = comment, loginStatus = self.loginStatus(), username=self.getUsername(), error="")

	def post(self, comment_id):
		# make sure user is signed in
		if self.loginStatus() == 1:
			self.redirect("/login")
			return

		comment_field = self.request.get("Comment")

		key = db.Key.from_path('Comments', int(comment_id))
		comment_to_update = db.get(key)

		# make sure the comment exists
		if self.validComment(comment_to_update):
			self.redirect("/")
			return

		# ensure that user owns comment
		if not self.userOwnsComment(comment_to_update):
			self.redirect("/")
			return

		# update the blog post and redirect back to the permalink page
		if comment_field:
			comment_to_update.comment_field = comment_field
			comment_to_update.put()

			self.redirect("/" + str(comment_to_update.blog_id))
			return
		else:
			error = "You need to include a comment field"
			self.render('editcomment.html', comment = comment, loginStatus = self.loginStatus(), username=self.getUsername(), error=error)

# Handler to delete comments
class DeleteComment(Handler):
	def post(self, comment_id):
		# make sure user is signed in
		if self.loginStatus() == 1:
			self.redirect("/login")

		key = db.Key.from_path('Comments', int(comment_id))
		comment_to_delete = db.get(key)

		# make sure the comment exists
		if self.validComment(comment_to_delete):
			self.redirect("/")

		# only allowed to delete if the usernames match
		if self.userOwnsComment(comment_to_delete):
			db.delete(comment_to_delete)
			self.redirect('/')
		else:
			self.redirect(404)