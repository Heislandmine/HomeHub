from flask import Blueprint, jsonify, request, Response, current_app
from model.model import get_all, get_resource_by_id, delete_resource_by_id
import os
import os.path
from model.model import Videos, Tags, Categorys
from database import db

video_api = Blueprint("video_api", __name__)

@video_api.route("/", methods=["GET"])
def get_all_videos():
    
    return Response(status=200)

@video_api.route("/<int:id>", methods=["GET"])
def get_video(id):
    data = get_resource_by_id(id)
    return jsonify(data)

@video_api.route("/", methods=["POST"])
def post_video():
    save_dir = current_app.config["BASE_PATH"] + "/" + current_app.config["MEDIA_PATH"]
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    
    file_name = "test"
    save_path = save_dir + "/" + file_name
    video = Videos(path=save_path)
    db.session.add(video)
    db.session.commit()
    return Response(status=204)

@video_api.route("/", methods=["DELETE"])
def delete_video():
    data = request.get_json()
    delete_resource_by_id(data["id"])
    
    return Response(status=204)