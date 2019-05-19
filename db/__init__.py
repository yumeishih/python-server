import os
from pymongo import MongoClient

class MongoDB(object):
  def __init__(self):
    mongo_url = "mongodb+srv://yumi:0000@cluster0-oycg2.mongodb.net/test?retryWrites=true"
    self.db = MongoClient(mongo_url).resume

  def find_all_me(self):
   return self.db.me.find({})

  def find_all_experiences(self):
   return self.db.experiences.find({})

  def find_all_skills(self):
   return self.db.skills.find({})