from flask import Flask
from flask_restful import Api
from api.login import Login 
from api.post.post import Post 
from api.post.posts import Posts 

app = Flask(__name__)
api = Api(app)
api.add_resource(Login, '/login')
api.add_resource(Posts, '/posts')
api.add_resource(Post, '/posts/<int:id>')
api.init_app(app)
if __name__ == '__main__':
    app.run(debug=True)