from flask import Flask, flash, redirect, url_for, render_template
from app.config import Config
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

application = Flask(__name__)
application.config.from_object(Config)
db = SQLAlchemy(application)
migrate = Migrate(application, db)
bootstrap = Bootstrap(application)

from app import routes
from app.db_models import *

from app.api import bp as api_bp
application.register_blueprint(api_bp, url_prefix="/api")