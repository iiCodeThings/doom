from flask import Blueprint


async_blueprint = Blueprint('async', __name__, url_prefix='/async')


from .tasks import async_do_add_task

