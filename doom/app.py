import sys
import logging
from flask import Flask
from doom import commands
from doom.api import sms_api
from doom.settings import get_config
from doom.extensions import (
    db,
    bcrypt,
    migrate,
)


def create_app(config_object=get_config()):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_shellcontext(app)
    register_commands(app)
    configure_logger(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    db.init_app(app)
    bcrypt.init_app(app)
    sms_api.init_app(app)
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
