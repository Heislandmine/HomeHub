import json
from database import db
from datetime import datetime
class Videos(db.Model):
    __tablename__ = 'videos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    path = db.Column(db.String(255), nullable=False)
    tags_id = db.Column(db.Integer, autoincrement=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

class Tags(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, nullable=False)

class Categorys(db.Model):
    __tablename__ = 'categorys'
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(255), nullable=False)

# db.json用 後で消す
db_dist = "./backend/" + "db.json"

def _load_data():
    # todo:DBの接続先を変数で変える
    with open(db_dist, "r") as f:
        data = json.load(f)
    return data

def _save_data(data):
    with open(db_dist, "w") as f:
        json.dump(data, f)

def get_all():
    return _load_data()

def get_resource_by_id(id):
    datas = _load_data()
    for data in datas:
        if data["id"] == id:
            return data
        else:
            pass # エラーハンドリングする

def delete_resource_by_id(id):
    datas = _load_data()
    datas = [data for data in datas if data["id"] != id]
    _save_data(datas)
