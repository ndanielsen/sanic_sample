from sanic_openapi import swagger_blueprint
from sanic_openapi import openapi_blueprint

def add_swagger(app):
    app.blueprint(openapi_blueprint)
    app.blueprint(swagger_blueprint)
    app.config.API_VERSION = '1.0.0'
    app.config.API_TITLE = 'Car API'
    app.config.API_DESCRIPTION = 'Car API'
    app.config.API_TERMS_OF_SERVICE = 'Use with caution!'
    app.config.API_PRODUCES_CONTENT_TYPES = ['application/json']
    app.config.API_CONTACT_EMAIL = 'channelcat@gmail.com'
    return app
