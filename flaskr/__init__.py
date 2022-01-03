import os
import json
from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/tabla1')
    def tabla1():
        with open('try_json_1D.json', 'r') as f:
            x = json.load(f)
            return x
    @app.route('/tabla2')
    def tabla2():
        with open('try_json_2D.json', 'r') as f:
            x = json.load(f)
            return x
    @app.route('/tabla3')
    def tabla3():
        with open('try_json_3D.json', 'r') as f:
            x = json.load(f)
            return x
    @app.route('/tabla4')
    def tabla4():
        with open('try_json_4D.json', 'r') as f:
            x = json.load(f)
            return x
    @app.route('/tabla5')
    def tabla5():
        with open('try_json_5D.json', 'r') as f:
            x = json.load(f)
            return x
    @app.route('/tabla6')
    def tabla6():
        with open('try_json_6D.json', 'r') as f:
            x = json.load(f)
            return x
    @app.route('/tabla7')
    def tabla7():
        with open('try_json_7D.json', 'r') as f:
            x = json.load(f)
            return x
    return app