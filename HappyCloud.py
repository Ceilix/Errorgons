from google.appengine.ext import ndb

class Happy(ndb.Model):
    input1 = ndb.StringProperty(required = True)
    input2 = ndb.StringProperty(required = True)
    input3 = ndb.StringProperty(required = True)
    # HappyMessage = ndb.StringProperty(required = True)
    User = ndb.StringProperty(required = False)
