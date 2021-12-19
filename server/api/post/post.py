# import config
import config
from flask import Flask
from flask_restful import Resource, reqparse
from flaskext.mysql import MySQL

class Post(Resource):
    def __init__(self):
        # self.mysql = init()

        app = Flask(__name__)
        self.mysql = MySQL()
        
        app.config['MYSQL_DATABASE_USER'] = config.db['MYSQL_DATABASE_USER']
        app.config['MYSQL_DATABASE_PASSWORD'] = config.db['MYSQL_DATABASE_PASSWORD']
        app.config['MYSQL_DATABASE_HOST'] = config.db['MYSQL_DATABASE_HOST']
        app.config['MYSQL_DATABASE_DB'] = config.db['MYSQL_DATABASE_DB']
        
        self.mysql.init_app(app)
    
    def get(self, id:int):
        try:
            conn = self.mysql.connect()
            cursor = conn.cursor()
            sql = f"SELECT * FROM post WHERE id={id}"
            cursor.execute(sql)
            data = cursor.fetchall()

            if len(data) == 0:
                conn.commit()
                return {'StatusCode': '200', 'Message': data}
            else:
                return {'StatusCode': '500', 'Message': str(data[0])}
        except Exception as e:
            return {'error': str(e)}
    
    # update
    def post(self, id:int):
        print(id)
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('user_id', type=str)
            parser.add_argument('year', type=str)
            parser.add_argument('subject', type=str)
            parser.add_argument('professor', type=str)
            parser.add_argument('problem', type=str)
            parser.add_argument('input_file_url', type=str)
            parser.add_argument('output_file_url', type=str)
            parser.add_argument('content', type=str)
            args = parser.parse_args()

            user_id = args['user_id']
            year = args['year']
            subject = args['subject']
            professor = args['professor']
            problem = args['problem']
            input_file_url = args['input_file_url']
            output_file_url = args['output_file_url']
            content = args['content']

            conn = self.mysql.connect()
            cursor = conn.cursor()
            sql = f"UPDATE post SET user_id=%s, year=%s, subject=%s, professor=%s, problem=%s, input_file_url=%s, output_file_url=%s, content=%s WHERE id={id}"
            cursor.execute(sql,(user_id, year, subject, professor, problem, input_file_url, output_file_url, content))
            data = cursor.fetchall()

            if len(data) == 0:
                conn.commit()
                return {'StatusCode': '200', 'Message': '게시물이 수정 되었습니다.'}
            else:
                return {'StatusCode': '500', 'Message': str(data[0])}
        except Exception as e:
            return {'error': str(e)}
      
    # delete  
    def delete(self, id:int):
        try:
            conn = self.mysql.connect()
            cursor = conn.cursor()
            sql = f"DELETE FROM post WHERE id={id}"
            cursor.execute(sql)
            data = cursor.fetchall()

            if len(data) == 0:
                conn.commit()
                return {'StatusCode': '200', 'Message': '게시물이 삭제 되었습니다.'}
            else:
                return {'StatusCode': '500', 'Message': str(data[0])}
        except Exception as e:
            return {'error': str(e)}