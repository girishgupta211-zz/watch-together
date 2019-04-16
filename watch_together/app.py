"""
Flask App declaration
"""

from flask import Flask, jsonify
from flask_cors import CORS

from werkzeug.contrib.fixers import ProxyFix

from watch_together import settings
from watch_together.apis import blueprint as api_blueprint
from watch_together.config import Config
from watch_together.models import db


def register_blueprints(app):
    """
    Register blueprint
    """
    app.register_blueprint(api_blueprint, url_prefix='/watch-together/api')


def create_app():
    """
    flask app creation method
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        settings.POSTGRES_URI
    )
    app.config.SWAGGER_UI_DOC_EXPANSION = 'list'
    app.config.SWAGGER_UI_OPERATION_ID = True
    app.config.SWAGGER_UI_REQUEST_DURATION = True

    app.wsgi_app = ProxyFix(app.wsgi_app)

    # register blueprints
    register_blueprints(app)

    # enable cors
    CORS(app)
    # init database
    db.init_app(app)
    return app


app = create_app()


@app.route('/health', methods=['GET'])
def health_check():
    """
    health check
    """
    return 'OK', 200


@app.errorhandler(AssertionError)
def handle_assertion(error):
    """
    Error handler
    """
    ret = {'code': 400, 'error': error.args[0]}
    app.logger.warn('400 %s', ret['error'])
    return jsonify(**ret), ret['code']
