import os
import webapp2
import jinja2

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class Blog(db.Model):
	title = db.StringProperty(required = True)
	blog = db.TextProperty(required = True)
	lastModified = db.DateTimeProperty(auto_now = True)
	created = db.DateTimeProperty(auto_now_add = True)


class MainPage(Handler):
	def render_front(self):
		blogs = db.GqlQuery("SELECT * FROM Blog ORDER BY created DESC limit 10")
		self.render("front.html", blogs = blogs)

	def get(self):
		self.render_front()

class NewBlogPage(Handler):
	def get(self):
		self.render("NewPost.html", title="", blog="", error="")

	def post(self):
		title = self.request.get("title")
		blog = self.request.get("blog")

		if title and blog:
			b = Blog(title = title, blog = blog)
			b.put()

			self.redirect("/" + str(b.key().id()))
		else:
			error = "we need both a subject and content!"
			self.render_front("NewPost.html", title, blog, error)
		
		
class PostedBlog(Handler):
	def get(self, blog_id):
		key = db.Key.from_path('Blog', int(blog_id))
		blog = db.get(key)

		self.render("permalink.html", blog=blog)


app = webapp2.WSGIApplication([('/', MainPage),
							   ('/newpost', NewBlogPage),
							   ('/([0-9]+)', PostedBlog)], debug=True)
