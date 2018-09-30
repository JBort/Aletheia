import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    #
    # app = Flask(__name__, instance_relative_config=True):
    #   creates the flask instance
    # __name__
    #   name of the current Python module, tells app location to set up paths
    # instance_relative_config=True
    #   config files are relative to the instance folder (outside the Aletheia package)
    # app.config.from_mapping():
    #   sets some default configuration for the app
    # SECRET_KEY
    #   used by Flask and extensions to secure data.
    #   'dev' provides a development value, replace for deployment
    # DATABASE
    #   path to DATABASE, app.instance_path uses Flask instance folder
    # app.config.from_pyfile():
    #   overrides default configuration with config.py if exists. Use for deployment
    # test_config
    #   loads test configuration independently of any development values
    # os.makesdirs()
    #   ensures that app.instance_path exists

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev', DATABASE=os.path.join(app.instance_path, 'Aletheia.sqlite'),)

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
#    app.add_url_rule('/', endpoint='blog')

    from . import home
    app.register_blueprint(home.bp)
    app.add_url_rule('/', endpoint='home')

    return app
