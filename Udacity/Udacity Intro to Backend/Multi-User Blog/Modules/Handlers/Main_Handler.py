import webapp2
import os
import jinja2
# Parent handler class that contains the three functions given during the 
# course as well as two others used to verify if someone is logged in and
# to return the username of the person logged in

basepath = os.path.dirname(__file__)
template_dir = os.path.join(basepath, '..', 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

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

	def validPost(self, blog):
		return blog == None

	def getUsername(self):
		if self.loginStatus() == 0:
			username = self.request.cookies.get("key")
			if username != None:
				return username.split("|")[0]
			else:
				return ""
		else: 
			return ""

	def userOwnsPost(self, blog):
		return self.getUsername() == blog.createdby

	def validComment(self, comment):
		return comment == None

	def userOwnsComment(self, comment):
		return self.getUsername() == comment.username