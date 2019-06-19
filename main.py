import webapp2
import os
import jinja2
import json
import random
import HappyCloud
from HappyCloud import Usertemp
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

#global Happymessage = str(get_message())

#global Goals = str(get_goals())

class MainHandler(webapp2.RequestHandler):
      def get(self):
          user = users.get_current_user()
          if user:


            Userinit = Usertemp(
                 Userkey = str(users.get_current_user()),
                 Counter = 0


            )

            Userinit.put()
            self.redirect("/HappyInterface")

          else:
            self.redirect("/nouser")

class MainPage(webapp2.RequestHandler):
      def get(self):
         print(get_message())
         print('Mainhandlerhello')

         start_template = jinja_current_dir.get_template("templates/Interface.html")
         Icons = {
          }
         self.response.write(start_template.render(Icons))

class HappySurvey(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_current_dir.get_template("templates/survey.html")
        self.response.write(start_template.render())
    def post(self):
        start_template = jinja_current_dir.get_template("templates/survey.html")
        self.response.write(start_template.render())    


class HappyInput(webapp2.RequestHandler):
      def post(self):
          user = Usertemp.query(Usertemp.Userkey == str(users.get_current_user())).fetch()
          usercurrent = user[0]


          #Get userlogin infoi
          #Use user login info id to get students
          #Take the first element of students to remove the array
          #Increase the counter of the first student +=1 and save it to database in put()
          unlockbutton = ""
          if usercurrent.Counter >= 3:
             unlockbutton = "submit"
          else:
             unlockbutton = "hidden"



          print('OK')
          template_vars = {
                  'status': unlockbutton,
                  'Wellness_Messages' : get_message(),
                  'happy' : usercurrent.Counter,
                  'Happy_goals' : get_goals()
            }

          start_template = jinja_current_dir.get_template("templates/input_page.html")
          self.response.write(start_template.render(template_vars))

class HappyInputClone(webapp2.RequestHandler):
     def post(self):
         user = Usertemp.query(Usertemp.Userkey == str(users.get_current_user())).fetch()
         usercurrent = user[0]
         Happythought1 = self.request.get('Happy_thought1')
         unlockbutton = ""
         if Happythought1 != "":
            usercurrent.Counter += 1
            usercurrent.put()

         if usercurrent.Counter >= 3:
            unlockbutton = "submit"
         else:
            unlockbutton = "hidden"


         #Get userlogin infoi
         #Use user login info id to get students
         #Take the first element of students to remove the array
         #Increase the counter of the first student +=1 and save it to database in put()

         print('OK')
         template_vars = {
                 'status': unlockbutton,
                 'happy' : usercurrent.Counter,
                 'Happy_goals' : get_goals(),
                 'Wellness_Messages' : get_message(),
           }

         start_template = jinja_current_dir.get_template("templates/input_page.html")
         self.response.write(start_template.render(template_vars))

class HappyRetreive(webapp2.RequestHandler):
      def post(self):
          Happythought1 = self.request.get('Happy_thought1')
          user = Usertemp.query(Usertemp.Userkey == str(users.get_current_user())).fetch()
          usercurrent = user[0]
          usercurrent.Counter = 0
          usercurrent.put()
          username = str(users.get_current_user())
          Happy = HappyCloud.Happy (
               User = username,
              # Identity = surveyresults
               input1 =  Happythought1
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
          self.response.write("Please log in. <a href="+ login_url + ">Login Here</a>")

app = webapp2.WSGIApplication([
     ('/',MainHandler),
     ('/DataInput',HappySurvey),
     ('/HappyInterface',MainPage),
     ('/Happy', HappyInput),
     ('/Happy2', HappyInputClone),
     ('/Happier',HappyRetreive),
     ('/library', HappyLibrary),
     ('/nouser', NoUserHandler)
], debug=True)
# random.choice() use this to do the randomizer tomorrow
