from flask import Flask, json
from flask_cors import CORS
from config import DevConfig
from resume.service import Service as Resume
from resume.schema import MeSchema, SkillSchema, ExperienceSchema

app = Flask(__name__)
app.config.from_object(DevConfig)
CORS(app)

@app.route('/')
def index():
  return 'Hello World!'

@app.route("/resume/me", methods=["GET"])
def me():
  return json_response(Resume().find_all_me())

@app.route("/resume/experiences", methods=["GET"])
def experiences():
  return json_response(Resume().find_all_experiences())

@app.route("/resume/skills", methods=["GET"])
def skills():
  return json_response(Resume().find_all_skills())

def json_response(payload, status=200):
  return (json.dumps(payload), status, {'content-type': 'application/json'})

if __name__ == '__main__':
  app.run()