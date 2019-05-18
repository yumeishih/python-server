import pymongo
from bson import ObjectId

class db:
  client = pymongo.MongoClient("mongodb+srv://yumi:0000@cluster0-oycg2.mongodb.net/test?retryWrites=true")
  database = client['resume']
  me = database.me
  experienced = database.experiences
  skills = database.skills

  def get_all_me(self):
    return self.me.find({})

  def get_all_experiences(self):
    return self.experienced.find({})

  def get_all_skills(self):
    return self.skills.find({})

testDb = db()

print(testDb.get_all_me()[0])

for e in testDb.get_all_experiences():
  print(e)

for e in testDb.get_all_skills():
  print(e)
