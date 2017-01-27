from google.appengine.ext import db
class Comments(db.Model):
	blog_id = db.StringProperty(required = True)
	username = db.StringProperty(required = True)
	comment_field = db.TextProperty(required = True)
	date_of_comment = db.DateTimeProperty(auto_now_add = True)