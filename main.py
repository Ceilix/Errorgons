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


class MainHandler(webapp2.RequestHandler):
      def get(self):
         print('Mainhandlerhello')
         start_template = jinja_current_dir.get_template("templates/Interface.html")
         Icons = {
          }
         self.response.write(start_template.render(Icons))

class HappyInput(webapp2.RequestHandler):
      def post(self):
          start_template = jinja_current_dir.get_template("templates/input_page.html")

          Happythought1 = self.request.get('happy_input1')
          Happythought2 = self.request.get('happy_input2')
          Happythought3 = self.request.get('happy_input3')
          Happy = HappyCloud.Happy (
              input1 = Happythought1,
              input2 =  Happythought2,
              input3 =  Happythought3
          )

          Happy.put()

          self.response.write(start_template.render(Happy))

class HappyRetreive(webapp2.RequestHandler):
      def post(self):
          start_template = jinja_current_dir.get_template("templates/Readthoughts.html")
          happy_query = HappyCloud.Happy.query()
          happy = happy_query.fetch()

          template_vars = {
                'happy' : happy,
          }

          self.response.write(start_template.render(template_vars))

class HappyLibrary(webapp2.RequestHandler):
    def get(self):
        results_template = the_jinja_env.get_template('templates/library.html')

app = webapp2.WSGIApplication([
     ('/',MainHandler),
     ('/Happy', HappyInput),
     ('/Happier',HappyRetreive),
     ('/library', HappyLibrary)
], debug=True)
