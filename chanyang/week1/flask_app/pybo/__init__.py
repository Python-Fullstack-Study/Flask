from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()
from . import models

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

    # Blueprint
    from .views import main_view, question_views, answer_views
    app.register_blueprint(main_view.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)

    # Filter
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    return app
