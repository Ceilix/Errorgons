import webapp2
import os
import jinja2
import json
import HappyCloud
from google.appengine.api import urlfetch
from google.appengine.api import users

jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainHandler(webapp2.RequestHandler):
      def get(self):
          user = users.get_current_user()
          if user:

            # self.response.write("To be or not to be")
            self.redirect("/HappyInterface")
          else:
        #     self.response.write("You are not logged in")
            self.redirect("/nouser")

class MainPage(webapp2.RequestHandler):
      def get(self):
         print('Mainhandlerhello')
         start_template = jinja_current_dir.get_template("templates/Interface.html")
         Icons = {
          }
         self.response.write(start_template.render(Icons))

class HappyInput(webapp2.RequestHandler):
      def post(self):
          start_template = jinja_current_dir.get_template("templates/input_page.html")
          self.response.write(start_template.render())



class HappyRetreive(webapp2.RequestHandler):
      def post(self):
          Happythought1 = self.request.get('Happy_thought1')
          Happythought2 = self.request.get('Happy_thought2')
          Happythought3 = self.request.get('Happy_thought3')
          Happy = HappyCloud.Happy (
               input1 =  Happythought1,
               input2 =  Happythought2,
               input3 =  Happythought3
          )

          Happy.put()
          start_template = jinja_current_dir.get_template("templates/Readthoughts.html")
          happy_query = HappyCloud.Happy.query()
          happy = happy_query.fetch()

          template_vars = {
                'happy' : happy,
          }
          self.response.write(start_template.render(template_vars))

class HappyLibrary(webapp2.RequestHandler):
    def get(self):
        results_template = jinja_current_dir.get_template('templates/library.html')

        happy_query = HappyCloud.Happy.query()
        happy = happy_query.fetch()

        template_vars = {
               'happy' : happy
               }
        self.response.write(results_template.render(template_vars))

class NoUserHandler(webapp2.RequestHandler):
      def get(self):
          login_url = users.create_login_url("/")
          self.response.write("Please log in. <a href="+ login_url + ">Login There</a>")

app = webapp2.WSGIApplication([
     ('/',MainHandler),
     ('/HappyInterface',MainPage),
     ('/Happy', HappyInput),
     ('/Happier',HappyRetreive),
     ('/library', HappyLibrary),
     ('/nouser', NoUserHandler)
], debug=True)
# random.choice() use this to do the randomizer tomorrow
