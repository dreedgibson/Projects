# import webapp2
import webapp2

# import all of the different page handlers that allow for rendering of website
from Modules.Handlers.MainPage import MainPage
from Modules.Handlers.NewPost import NewBlogPage
from Modules.Handlers.Permalink import PostedBlog
from Modules.Handlers.Registration import SignUpPage, WelcomePage
from Modules.Handlers.Login_outHandlers import LoginPage, Logout
from Modules.Handlers.PostHandlers import EditPost, DeleteBlogPost
from Modules.Handlers.CommentHandlers import DeleteComment, EditComment
from Modules.Handlers.LikePost import LikePost

# mapping of url to handlers
app = webapp2.WSGIApplication([('/', MainPage),
							   ('/newpost', NewBlogPage),
							   ('/([0-9]+)', PostedBlog),
							   ('/signup', SignUpPage), 
							   ('/welcome', WelcomePage),
							   ('/login', LoginPage),
							   ('/logout', Logout),
							   ('/editpost/([0-9]+)', EditPost),
							   ('/deleteblogpost/([0-9]+)', DeleteBlogPost),
							   ('/deletecomment/([0-9]+)', DeleteComment),
							   ('/editcomment/([0-9]+)', EditComment),
							   ('/likepost/([0-9]+)', LikePost)], debug=True)
