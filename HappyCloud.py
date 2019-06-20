from google.appengine.ext import ndb

class Happy(ndb.Model):
    input1 = ndb.StringProperty(required = False)
    # HappyMessage = ndb.StringProperty(required = True)
    User = ndb.StringProperty(required = True)
    UserAge = ndb.StringProperty(required = False)
    UserRegion = ndb.StringProperty(required = False)

class Usertemp(ndb.Model):
    Userkey = ndb.StringProperty(required=True)
    Score = ndb.IntegerProperty(required = False)
    Counter = ndb.IntegerProperty(required = False)
