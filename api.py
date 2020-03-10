from flask import Flask, request, jsonify, make_response
from CONTROLLERS.usersController import registerController, usersController
import json
app = Flask(__name__)


@app.route('/register', methods=['POST'])
def registerUsers():
    data = request.json
    return registerController(data)


@app.route("/users", methods=['GET'])
def getUsers():
    data, status = usersController()
    return jsonify(data), status


if __name__ == "__main__":
    app.run(debug=True)
