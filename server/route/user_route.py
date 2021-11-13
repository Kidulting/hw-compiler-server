import datetime
# from pytz import timezone

from flask import Blueprint, request, jsonify
from model import user_model as user

user_route = Blueprint('user_route', __name__)

@user_route.route('/', methods=['GET'])
def main():
    aa = user.MyUser.query.filter_by(id='1').all()
    return dict(id = aa.id, name = aa.name)

