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
         start_template = jinja_current_dir.get_template("Interface.html")
         Icons = {
          }
         self.response.write(start_template.render(Icons))

class HappyInput(webapp2.RequestHandler):
      def post(self):
          start_template = jinja_current_dir.get_template("Happys.html")

          Happythought1 = self.request.get('sobjectA')
          Happythought2 = self.request.get('Adjectif')
          Happythought3 = self.request.get('sobjectB"')
          usernamer = self.request.get("Vert")
          # date = str(datetime.strptime(self.request.get('date'), "%Y-%m-%d"))

          # if  meme_choice == 'college-grad':
          #     url = "https://i.imgflip.com/9g776.jpg"
          #
          # elif meme_choice == 'coding':
          #     url = "https://www.theperfectloaf.com/wp-content/uploads/2019/04/theperfectloaf-sourdough-fougasse-hummus-1-1600x1068.jpg"
          #
          # elif meme_choice == 'thinking-ape':
          #     url = "https://g89tz9aafd62c4p7-zippykid.netdna-ssl.com/wp-content/uploads/2019/03/theperfectloaf-pain-de-mie-feature-1160x774.jpg"
          #
          # elif meme_choice == "old-class":
          #     url = "https://www.theperfectloaf.com/wp-content/uploads/2019/03/theperfectloaf-pain-de-mie-14-1600x1068.jpg"




          Happy = HappyCloud.Happy(
               Happythought1 =  Happythought1,
               Happythought2 =  Happythought2,
               Happythought3 =  Happythought3,
               User = usernamer,
          )

          Happy.put()

          self.response.write(start_template.render())

class HappyRetreive(webapp2.RequestHandler):
      def post(self):
          start_template = jinja_current_dir.get_template("Readthoughts.html")
          happy_query = HappyCloud.Happy.query()
          happy = happy_query.fetch()

          template_vars = {
                'memes' : memes,
          }

          self.response.write(start_template.render(template_vars))

app = webapp2.WSGIApplication([
     ('/',MainHandler),
     ('/Happy', HappyInput),
     ('/Happier',HappyRetreive)
], debug=True)
