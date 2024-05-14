from flask import Flask
import secrets
from flask_sqlalchemy import SQLAlchemy
from os import path

# db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY'] = secrets.token_hex(16)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # db.init_app(app)

    from .sudoku import sudoku
    app.register_blueprint(sudoku, url_prefix = '/')

    # create_database(app)
    with app.app_context():
        create_database(app)
    return app

def create_database(app):
    if not path.exists('instance/' + DB_NAME):
        # with app.app_context():
        # create_database(app=app)
        # db.create_all()
        print('Created Database!')