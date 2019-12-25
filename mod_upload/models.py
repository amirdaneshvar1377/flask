from app import db
import datetime

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(256), nullable=False, unique=True)
    upload_date = db.Column(db.DateTime, nullable=False, unique=False, default=datetime.datetime.utcnow)