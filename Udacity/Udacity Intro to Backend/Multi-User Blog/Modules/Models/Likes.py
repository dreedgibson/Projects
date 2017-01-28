from google.appengine.ext import db
class Likes(db.Model):
	"""
	Likes are used to determine who has liked the post and store the id of the blog post they liked
	"""
	blog_id = db.StringProperty(required = True)
	username = db.StringProperty(required = True)