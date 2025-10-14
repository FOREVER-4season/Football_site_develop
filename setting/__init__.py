from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db=SQLAlchemy()
migrate=Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.secret_key = 'your_secret_key_here'

    #ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    #블루프린트 등록
    from .views import main_views,stadium,mypage, matches, auth, order, money,manager
    app.register_blueprint(main_views.bp)
    app.register_blueprint(stadium.bp)
    app.register_blueprint(mypage.bp)
    app.register_blueprint(matches.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(order.bp)
    app.register_blueprint(money.bp)
    app.register_blueprint(manager.bp)

    return app