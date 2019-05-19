from db import MongoDB
from .schema import MeSchema, SkillSchema, ExperienceSchema

class Service(object):
  def __init__(self, repo_client=MongoDB):
    self.repo_client = repo_client()

  def find_all_me(self):
    mes = self.repo_client.find_all_me()
    return [self.dump_me(me) for me in mes]

  def find_all_experiences(self):
    experiences  = self.repo_client.find_all_experiences()
    return [self.dump_experiences(experience) for experience in experiences]

  def find_all_skills(self):
    skills  = self.repo_client.find_all_skills()
    return [self.dump_skills(skill) for skill in skills]

  def dump_me(self, data):
    return MeSchema(exclude=['_id']).dump(data).data

  def dump_experiences(self, data):
    return ExperienceSchema(exclude=['_id']).dump(data).data

  def dump_skills(self, data):
    return SkillSchema(exclude=['_id']).dump(data).data
