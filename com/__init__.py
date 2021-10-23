from flask_restplus import Api
from flask import Blueprint

from com.kidulting.hw-compiler.controller.v1.call import api as call_v1

blueprint_v1 = Blueprint('API1.0', __name__)
api_v1 = Api(blueprint_v1, 
            title='kidulting APIs version 1.0', 
            version='1.0', 
            description='Flask RESTPlus web service APIs documents.')
api_v1.add_namespace(call_v1, path='')