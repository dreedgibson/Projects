# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import webapp2
import jinja2
import re

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class MainPage(Handler):
	def get(self):
		self.render("user_template.html", username="",
										  username_error="",
										  password_error="",
										  verify_error="",
										  email="",
										  email_error="")

	def post(self):
		username = self.request.get("username")
		password = self.request.get("password")
		verify = self.request.get("verify")
		email = self.request.get("email")
		
		error_message = self.validate(username, password, verify, email)

		if not error_message:
			self.redirect("/welcome?username=" + username)
		else:
			self.render("user_template.html", username = username,
											  username_error = error_message.get('username_error', ""),
											  password_error = error_message.get('password_error', ""),
											  verify_error = error_message.get('verify_error', ""),
											  email = email,
											  email_error = error_message.get('email_error', ""))

	def validate(self, username, password, verify, email):
		error_message = {}
		if not self.valid_username(username):
			error_message['username_error'] = "That is not a valid username"
		if not self.valid_password(password):
			error_message['password_error'] = "That is not a valid password"
		if not self.verify_pass(password, verify):
			error_message['verify_error'] = "The two passwords must match"
		if not self.verify_email(email):
			error_message['email_error'] = "That is not a valid email"

		return error_message

	def valid_username(self, username):
		return USER_RE.match(username)
	def valid_password(self, password):
		return PASS_RE.match(password)
	def verify_pass(self, password, verify):
		return password == verify
	def verify_email(self, email):
		return EMAIL_RE.match(email) or email == ""

class WelcomePage(Handler):
	def get(self):
		username = self.request.get("username")
		self.render("welcome.html", username = username)

app = webapp2.WSGIApplication([('/', MainPage), 
							   ('/welcome', WelcomePage)], debug=True)
