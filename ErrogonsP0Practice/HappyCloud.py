from google.appengine.ext import ndb

class Happy(ndb.Model):
    Happythought1 = ndb.StringProperty(required=False)
    Happythought2 = ndb.StringProperty(required = False)
    Happythought3 = ndb.StringProperty(required = True)
    # HappyMessage = ndb.StringProperty(required = True)
    User = ndb.StringProperty(required = True)
