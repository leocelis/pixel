from flask import Flask
from flask.ext.restful import Api
from flask_cors import CORS

from pixel import Pixel

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(Pixel, '/pixel/p', '/')

if __name__ == '__main__':
    app.run(debug=True)
