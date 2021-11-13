from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MyUser(db.Model):
    # __tablename__ = 'user'
    __tablename__ = 'test'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(20, 'utf8mb4_unicode_ci'))
    created = db.Column(db.DateTime, server_default=db.FetchedValue())
    updated = db.Column(db.DateTime, server_default=db.FetchedValue())

    def __init__(self, name, create, update):
        self.name = name
        self.created = create
        self.updated = update