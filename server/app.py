from flask import Flask
from flask_restful import Api
from api.login import Login 

app = Flask(__name__)
api = Api(app)
api.add_resource(Login, '/login')
api.init_app(app)
if __name__ == '__main__':
    app.run(debug=True)