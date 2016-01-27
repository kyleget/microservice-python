from flask import Flask

from v1 import api as v1


app = Flask(__name__)


# API Versions
app.register_blueprint(v1, url_prefix='/v1')


if __name__ == '__main__':
    app.run('0.0.0.0', threaded=True, debug=True)

