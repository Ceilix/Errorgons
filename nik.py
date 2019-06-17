import webapp2
import os
import jinja2
import json
import HappyCloud
from google.appengine.api import urlfetch


jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

app = webapp2.WSGIApplication([
     ('', ),
], debug=True)
