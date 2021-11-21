from flask import Flask
# from flask_script import Manager

from flask_sqlalchemy import SQLAlchemy

from route.user_route import user_route

app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://[id]:[pw]@[ip]:[port]/[db]"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://kidulting:1234@localhost/compiler"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy()
db.init_app(app)

app.register_blueprint(user_route)

if __name__ == '__main__':
    app.run(debug=True)