from marshmallow import Schema, fields

class MeSchema(Schema):
  __id = fields.Str()
  name = fields.Str()
  jobTitle = fields.Str()
  local = fields.Str()
  email = fields.Str()
  gitHub = fields.URL()
  linkedin = fields.URL()

class SkillSchema(Schema):
  _id = fields.Str()
  me_id = fields.Str()
  skillType = fields.Str()
  text = fields.Str()
  rate = fields.Str()
  description = fields.Str()


class ExperienceSchema(Schema):
  _id = fields.Str()
  me_id = fields.Str()
  experienceType = fields.Str()
  subtitle = fields.Str()
  organization = fields.Str()
  local = fields.Str()
  start = fields.Date()
  end = fields.Date()
  detail = fields.Str()
