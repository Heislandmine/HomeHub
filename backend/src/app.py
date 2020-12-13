from flask import Flask
from controller.video_api import video_api 
from database import init_db
from dotenv import load_dotenv
import os.path
from model.model import Videos, Tags, Categorys

app = Flask(__name__)
app.config["BASE_PATH"] = os.path.dirname(os.path.dirname(__file__))
app.register_blueprint(video_api, url_prefix="/api/videos")
app.config.from_pyfile(app.config["BASE_PATH"] + "/app.conf")
init_db(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

