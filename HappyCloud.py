from google.appengine.ext import ndb

class ModelUser(ndb.Model):
    email = ndb.StringProperty(required = True)
    input = ndb.StringProperty(required = True)
    def __init__(self,counter = 0):

     user_id = create_account()
     return user_id

    def Happyupdate(self):
     counter.self = ndb.StringProperty(required = True)
     Happy_count = counter.self

    def __init__(self,counter = 0):

     user_id = create_account()
     return user_id

    def create_account(self, new_account):

        #Maybe create function
        if new_account.username not in self.users:
           self.users[new_account.username] = new_account

           #create
        else:
            return False


    # def get_by_user(cls, user):
    #     return cls.query().filter(cls.user_id) == user.user_id().get()






# class Happy(ndb.Model):
#     input1 = ndb.StringProperty(required = True)
#     input2 = ndb.StringProperty(required = False)
#     input3 = ndb.StringProperty(required = False)
#     # HappyMessage = ndb.StringProperty(required = True)
#     User = ndb.StringProperty(required = False)
