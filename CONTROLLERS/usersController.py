from database import CLIENT
from MODELS.usersModel import userSchema
from cerberus import Validator
import datetime
from copy import deepcopy
import json
from flask import jsonify

VALIDATE = Validator(require_all=True).validate
USER = CLIENT['user']


def registerController(data):
    dataWithoutDate = deepcopy(data)
    data['date'] = datetime.datetime.utcnow()
    if VALIDATE(data, userSchema) == True:
        USER.insert_one(data)
        return dataWithoutDate, 201
    else:
        return {"error": "Invalid data"}, 400


def usersController():
    users = []
    for user in USER.find():
        user['_id'] = str(user['_id'])
        users.append(user)

    return users, 200
