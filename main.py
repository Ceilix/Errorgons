import webapp2
import os
import jinja2
import json
import HappyCloud
from HappyCloud import ModelUser
import random
import shelve
from google.appengine.api import urlfetch
from google.appengine.api import users


jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def get_message():
    message_list=['Tomorrow, you will meet a life-changing new friend.',
                  'Fame and Instagram followers are headed your way.',
                  'On the Tuesday after next, an odd meeting will lead to a new opportunity.',
                  'Despite dry skies, bring an umbrella tomorrow.',
                  'A thrilling time is in your immediate future.',
                  'Someone has Googled you recently.',
                  'Stay alert. You will be part of a rescue mission.',
                  'You will beat Watson in a game of Jeopardy. Start studying though']
    return(random.choice(message_list))

def get_goals():
    message_list=['Tomorrow, you will meet a life-changing new friend.',
                  'Fame and Instagram followers are headed your way.',
                  'On the Tuesday after next, an odd meeting will lead to a new opportunity.',
                  'Despite dry skies, bring an umbrella tomorrow.',
                  'A thrilling time is in your immediate future.',
                  'Someone has Googled you recently.',
                  'Stay alert. You will be part of a rescue mission.',
                  'You will beat Watson in a game of Jeopardy. Start studying though']
    return(random.choice(message_list))




def Happy_goals2():
    ModelUser.Happyupdate()
    return Happy_count
    #Create object for user
    #Append Happy count when submit is clicked
    #Return no. of items in Happy count to get a Daily_Happiness_Counter
    #Clear Happy_Count when HappyLibrary is accessed!


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
         # Userinfo = Dict(
         #          email = users.get_current_user().nickname())





         self.response.write(start_template.render())

class HappyInput(webapp2.RequestHandler):
      def post(self):
          Happy_goals2()
          start_template = jinja_current_dir.get_template("templates/input_page.html")
          Happythought1 = self.request.get('happy_input1')
          # Happythought2 = self.request.get('happy_input2')
          # Happythought3 = self.request.get('happy_input3')
          Happy = HappyCloud.Happyupdate(
              input1 =  Happythought1,
          )
          #How do I run a function from Happycloud on main.py()
          #How do I put this in the function
          Happy_counter = Happy_count
          Happymessage = get_message()
          Goals = get_goals()



          Happyvar = {
             'Daily_Happiness_Counter' : Happy_counter,
             'Wellness_Messages' : Happymessage,
             'Happy_goals' : Goals
          }

          self.response.write(start_template.render(Happyvar))

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
    def post(self):
        start_template = jinja_current_dir.get_template('templates/library.html')
        happy_query = HappyCloud.Happy.query()
        happy = happy_query.fetch()

        template_vars = {
               'happy' : happy,
               }

class NoUserHandler(webapp2.RequestHandler):
      def get(self):
          login_url = users.create_login_url("/")
          self.response.write("Please log in. <a href="+ login_url + ">Login There</a>")

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
