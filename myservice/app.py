from flask import Flask, jsonify
from flask.views import MethodView

from flask_swagger import swagger


app = Flask(__name__)


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

app.add_url_rule('/', view_func=Main.as_view('main'))


@app.route('/alpha/swagger.json')
def specs():
    swag = swagger(app)
    swag['info']['version'] = "0.0.1"
    swag['info']['title'] = "myservice"
    return jsonify(swag)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Authorization, Content-Type')
    response.headers.add('Access-Control-Expose-Headers', 'Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Max-Age', 60 * 60 * 24 * 20)
    return response


if __name__ == '__main__':
    app.run('0.0.0.0', threaded=True, debug=True)

