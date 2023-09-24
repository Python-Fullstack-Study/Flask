from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import chanyang.week1.ch2.config as config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

    # Blueprint
    from .views import main_view
    app.register_blueprint(main_view.bp)

    return app
