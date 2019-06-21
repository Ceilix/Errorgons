import webapp2
import os
import jinja2
import json
import random
import HappyCloud
from HappyCloud import Happy
from HappyCloud import Usertemp
from google.appengine.api import urlfetch
from google.appengine.api import users

jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def get_message():
    message_list=['Line encoding error']
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
          userchecker = Usertemp.query(Usertemp.Userkey == str(users.get_current_user())).fetch()


          if len(userchecker)== 0:


           Userinit = Usertemp(
                 Userkey = str(users.get_current_user()),
                 Counter = 0,


                 # Surveycomplete = 0
 #How to prevent this from resetting all the time?


            )
           Userinit.put()


           self.redirect("/DataInput")

          else:
              if user:
            # self.response.write("To be or not to be")

                self.redirect("/HappyInterface")

              else:
        #     self.response.write("You are not logged in")
                self.redirect("/nouser")

class MainPage(webapp2.RequestHandler):
      def get(self):
         print("1")
         print(get_message())
         print("2")
         print('Mainhandlerhello')

         start_template = jinja_current_dir.get_template("templates/Interface.html")
         Icons = {
          }
         self.response.write(start_template.render(Icons))

class HappySurvey(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_current_dir.get_template("templates/Survey.html")
        self.response.write(start_template.render())
    def post(self):
        start_template = jinja_current_dir.get_template("templates/Survey.html")
        self.response.write(start_template.render())


class HappyInput(webapp2.RequestHandler):
      def post(self):
          #Placeholder location for survey classifcation input
          username = str(users.get_current_user())
          Agegrp = self.request.get('Age-Group')
          Regiongrp = self.request.get('Region')
          print("Regiongrp", Regiongrp)
          Surveyresult = HappyCloud.Happy(
                      User = username,
                      UserAge = Agegrp,
                      UserRegion = Regiongrp
                )
          Surveyresult.put()
          print(self.request)
        #  print(Surveyresult)
          print("Hi we are here")




          #1. Retrieve surveyresults
          #2. Put surveyresults w user
          #2. Fetch Surveyresults when inputting new data
          #3. Input Surveyresults w Happyinput


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


          #print(Happy.query(Happy.User == str(users.get_current_user())).fetch())
          print('OK')
          #Happy.query returns nothing
          #Possibility 1 : Usersurvey not put() properly
          #Possibility 2 : THe query is looking for the wrong thing
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
         # UserSurveyall = Happy.query()
         Usersurvey = Happy.query(Happy.User == str(users.get_current_user())).fetch()
         Userinfo = Usersurvey[0]
         usercurrent = user[0]
         Happythought1 = self.request.get('Happy_thought1')
         username = str(users.get_current_user())
         Userager = Userinfo.UserAge
         Userregioner = Userinfo.UserRegion
         if Happythought1 != "":
             Renamed = HappyCloud.Happy(
                    User = username,
                   # Identity = surveyresults
                    input1 = Happythought1,
                    UserAge = Userager,
                    UserRegion = Userregioner
              )
             usercurrent.Counter += 1

             usercurrent.put()
             Renamed.put()

         unlockbutton = ""

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
          user = Usertemp.query(Usertemp.Userkey == str(users.get_current_user())).fetch()
          username = str(users.get_current_user())
          Happythought1 = self.request.get('Happy_thought1')
          username = str(users.get_current_user())
          if Happythought1 != "":
              Happythought1 = self.request.get('Happy_thought1')
              Happy = HappyCloud.Happy(
                     User = username,
                    # Identity = surveyresults
                     input1 =  Happythought1
               )



          usercurrent = user[0]
          usercurrent.Counter = 0
          usercurrent.put()
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

        Userperm = Happy.query(Happy.User == str(users.get_current_user())).fetch()
        print("Hello")
        def Number():
            noomber = random.randint(0,len(Userperm)-1)
            return noomber


        Happythought1 = self.request.get('Happy_thought1')
        unlockbutton = ""
        done = True
        Usernewer1 = Userperm[Number()]
        Usernewer2 = Userperm[Number()]
        Usernewer3 = Userperm[Number()]

        while str(Usernewer1.input1) == "None":
              Usernewer1 = Userperm[Number()]

        while str(Usernewer2.input1) == "None":
              Usernewer2 = Userperm[Number()]

        while str(Usernewer3.input1) == "None":
              Usernewer3 = Userperm[Number()]


        new22 = str(Usernewer1.input1)
        new33 = str(Usernewer2.input1)
        new44 = str(Usernewer3.input1)

        #Ensure input is not = ""
        #OR if input is "" refresh new22  until input retrieved not ""




        template_vars = {
               'happy1' : new22,
               'happy2' : new33,
               'happy3' : new44

               }

        self.response.write(results_template.render(template_vars))

class HappyLibraryRand(webapp2.RequestHandler):
    def get(self):
        results_template = jinja_current_dir.get_template('templates/library.html')

        Userperm = Happy.query(Happy.User == str(users.get_current_user())).fetch()
        print('Hello')
        def Number(mylist):
            noomber = random.randint(0,len(mylist)-1)
            return noomber


        Happythought1 = self.request.get('Happy_thought1')
        unlockbutton = ""
        Usernewer = Userperm[Number(Userperm)]
                 #Placeholder location for survey classifcation input
        username = str(users.get_current_user())
        Agegrp = self.request.get('Age-Group')
        Regiongrp = self.request.get('Region')
        Surveyresult = HappyCloud.Happy(
                User = username,
                UserAge = Agegrp,
                UserRegion = Regiongrp
                       )
        print(Agegrp)
        print(Regiongrp)
        Userany = Happy.query().filter(Happy.User!=username).fetch()
        print(Userperm)
        current_user = Happy.query().filter(Happy.User==username).fetch()[0]
        print(current_user.UserAge)
        print(current_user.UserRegion)
        result = []

        for user in Userany:
            if user.UserAge == current_user.UserAge and user.UserRegion == current_user.UserRegion:
                result.append(user)


        print(result)
        Result1 = result[Number(result)]
        Result2 = result[Number(result)]
        Result3 = result[Number(result)]



        # while Usernewer1.Agegrp != Randomuserlist.Agegrp:
        #     done = False

        # for x in Userperm:
        #     if Agegrp == x.UserAge and Regiongrp == x.UserRegion:
        #       print(x.input1)



        template_vars = {
               'happy1' : Result1.input1,
               'happy2' : Result2.input1,
               'happy3' : Result3.input1

               }

        self.response.write(results_template.render(template_vars))



class NoUserHandler(webapp2.RequestHandler):
      def get(self):
          login_url = users.create_login_url("/")
          self.response.write("Please log in. <a href="+ login_url + ">Login There</a>")

app = webapp2.WSGIApplication([
     ('/',MainHandler),
     ('/DataInput',HappySurvey),
     ('/HappyInterface',MainPage),
     ('/Happy', HappyInput),
     ('/Happy2', HappyInputClone),
     ('/Happier',HappyRetreive),
     ('/library', HappyLibraryRand),
     ('/nouser', NoUserHandler)
], debug=True)
