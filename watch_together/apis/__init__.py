"""
APIs init file
"""

from flask import Blueprint

from flask_restplus import Api, Namespace

blueprint = Blueprint('Watch-Together', __name__)

api = Api(
    blueprint,
    title='Watch Together API',
    description='Create and Modify Watch Together',
    version='v1',
    contact='piyush.chourasiya@hotstar.com',
    doc='/swagger_doc'
)

ns = Namespace('v1', description='Watch Together',
               path='/v1/')

api.add_namespace(ns)

from watch_together.apis import routes
