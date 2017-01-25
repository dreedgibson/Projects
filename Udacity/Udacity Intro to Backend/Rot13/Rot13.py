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

class MainPage(Handler):
	def get(self):
		self.render("ROT13_template.html", text="")

	def post(self):
		text = self.request.get("text")
		text = self.cipher(text)
		self.render("ROT13_template.html", text=text)

	def cipher(self, text):
		text = list(text)
		for i in range(len(text)):
			if text[i].islower():
				text[i] = chr((((ord(text[i]) - 97) + 13) % 26) + 97)
			elif text[i].isupper():
				text[i] = chr((((ord(text[i]) - 65) + 13) % 26) + 65)
		return ''.join(text)

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
