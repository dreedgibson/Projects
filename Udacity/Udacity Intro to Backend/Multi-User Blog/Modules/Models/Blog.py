from google.appengine.ext import db
class Blog(db.Model):
	title = db.StringProperty(required = True)
	blog = db.TextProperty(required = True)
	createdby = db.StringProperty()
	lastModified = db.DateTimeProperty(auto_now = True)
	created = db.DateTimeProperty(auto_now_add = True)