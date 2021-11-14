import datetime
# from pytz import timezone

from flask import Blueprint, request, jsonify
from model import user_model as test_user

user_route = Blueprint('user_route', __name__)

@user_route.route('/', methods=['GET'])
def main():
    aa = test_user.MyUser.query.all()

    if len(aa) == 0:
        return "hi"
    else:
        user_list = []
        for user in aa:
            data = dict(id = user.id, name = user.name)
            user_list.append(data)

    return jsonify(user_list)

