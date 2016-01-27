from flask import Blueprint, jsonify
from flask.views import MethodView

from version import __version__


api = Blueprint('v1', __name__, static_folder='')


class Main(MethodView):
    """ Example view """
    methods = ['GET']

    def get(self):
        """
        Return some data
        ---
        responses:
            200:
                description: some data
        """
        data = {'message': 'Success'}
        return jsonify(data)


# URLs
api.add_url_rule('/', view_func=Main.as_view('main'))


@api.route('/swagger.yaml')
def spec():
    return api.send_static_file('swagger.yaml')


@api.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Authorization, Content-Type')
    response.headers.add('Access-Control-Expose-Headers', 'Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Max-Age', 60 * 60 * 24 * 20)
    return response
