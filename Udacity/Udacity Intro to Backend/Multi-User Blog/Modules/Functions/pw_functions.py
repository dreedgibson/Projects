import random
import string
import hashlib

# the following three functions are used to hash user passwords and
# verify that correct passwords have been entered for login purposes
def make_salt():
	return ''.join(random.choice(string.letters) for x in xrange(5))

def make_pw_hash(name, pw, salt=make_salt()):
	h = hashlib.sha256(name + pw + salt).hexdigest()
	return '%s|%s|%s' % (name, h, salt)

def valid_pw(name, pw, h):
	salt = h.split("|")[2]
	if h == make_pw_hash(name, pw, salt):
		return True