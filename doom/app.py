import sys
import logging
from flask import Flask
from doom import commands
from doom.extensions import db
from doom.extensions import bcrypt
from doom.extensions import migrate
from doom.api.restf import restf_api
from doom.settings import get_config
from doom.api.tasks import async_blueprint


def create_app(config_object=get_config()):
    app = Flask(__name__)
    app.config.from_object(config_object)
    configure_logger(app)
    register_commands(app)
    register_extensions(app)
    register_shellcontext(app)
    app_register_blueprints(app)
    return app


def app_register_blueprints(app):
    app.register_blueprint(async_blueprint)


def register_extensions(app):
    """Register Flask extensions."""
    db.init_app(app)
    bcrypt.init_app(app)
    restf_api.init_app(app)
    migrate.init_app(app, db)


def register_shellcontext(app):
    """Register shell context objects."""

    def shell_context():
        """Shell context objects."""
        return {"db": db, "app": app}

    app.shell_context_processor(shell_context)


def register_commands(app):
    """Register Click commands."""
    app.cli.add_command(commands.create_admin_user)


def configure_logger(app):
    """Configure loggers."""
    handler = logging.StreamHandler(sys.stdout)
    if not app.logger.handlers:
        app.logger.addHandler(handler)
