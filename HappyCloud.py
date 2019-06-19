from google.appengine.ext import ndb

class Happy(ndb.Model):
    input1 = ndb.StringProperty(required = False)
    # HappyMessage = ndb.StringProperty(required = True)
    User = ndb.StringProperty(required = True)

class Usertemp(ndb.Model):
    Userkey = ndb.StringProperty(required=True)
    Counter = ndb.IntegerProperty(required = False)
