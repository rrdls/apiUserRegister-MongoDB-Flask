from flask import Flask, request, jsonify, make_response
from CONTROLLERS.usersController import registerController, usersController
import json
from flask_cors import CORS, cross_origin
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)


@app.route('/register', methods=['POST'])
def registerUsers():
    """Route for users to register.

    Returns:
        dict/int -- The response variable returns a dictionary 
        with the data that was entered by the user. The status 
        variable informs if the request was sucessfully. The status 
        variable tells you whether the request was successful or not.
    """
    data = request.get_json(force=True)
    response, status = registerController(data)
    return response, status


@app.route("/users", methods=['GET'])
def getUsers():
    """Route to search for registered users.

    Returns:
        list/int -- The response variable returns a list of dictionaries 
        with the data that was entered by the user. 
        The status variable informs if the request was sucessfully.
        The status variable tells you whether the request was successful or not.
    """
    data, status = usersController()
    response = jsonify(data)
    return response, status


if __name__ == "__main__":
    app.run(debug=True)
