from flask import Flask, request, jsonify, make_response
from CONTROLLERS.usersController import registerController, usersController
import json
from flask_cors import CORS, cross_origin
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)


@app.route('/register', methods=['POST'])
@cross_origin()
def registerUsers():
    data = request.form.to_dict()
    response, status = registerController(data)
    return response, status


@app.route("/users", methods=['GET'])
def getUsers():
    data, status = usersController()
    response = jsonify(data)
    return response, status


if __name__ == "__main__":
    app.run(debug=True)
