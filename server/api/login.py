import config
from flask import Flask
from flask_restful import Resource, reqparse
from flaskext.mysql import MySQL
from datetime import datetime

class Login(Resource):
    def post(self):
        app = Flask(__name__)
        mysql = MySQL()
                
        app.config['MYSQL_DATABASE_USER'] = config.db['MYSQL_DATABASE_USER']
        app.config['MYSQL_DATABASE_PASSWORD'] = config.db['MYSQL_DATABASE_PASSWORD']
        app.config['MYSQL_DATABASE_HOST'] = config.db['MYSQL_DATABASE_HOST']
        app.config['MYSQL_DATABASE_DB'] = config.db['MYSQL_DATABASE_DB']
        
        mysql.init_app(app)
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('student_id', type=str)
            args = parser.parse_args()

            _student_id = args['student_id']
            current_date = datetime.now()
            conn = mysql.connect()
            cursor = conn.cursor()
            sql = "insert into login(student_id, last_log_in) values(%s, %s) on duplicate key update last_log_in=%s"
            cursor.execute(sql,(_student_id, current_date, current_date))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return {'StatusCode': '200', 'Message': 'log in success'}
            else:
                return {'StatusCode': '1000', 'Message': str(data[0])}
        except Exception as e:
            return {'error': str(e)}