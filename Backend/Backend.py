from flask import Flask, request, jsonify, send_file, make_response
from flask_cors import CORS
import os
import sys



app = Flask(__name__)


CORS(app) # Enable CORS on server side

# Index route and most basic example
@app.route('/', methods=['GET'])
def index():
    return jsonify({"Status": "Online!"})

@app.route('/submit-form', methods=['POST'])
def submit_form():
    email = request.form['email']
    date = request.form['date']
    print(f"Received email {email} at {date}")
    return 'Success!'


if __name__ == '__main__':
    from waitress import serve
    # This line is to debug requests made to the server on development
    app.run(use_reloader=True, port=3000, threaded=True)
    # This is to run the server on deployment and get full performance
    #serve(app, host="0.0.0.0", port=3000, url_scheme='https')