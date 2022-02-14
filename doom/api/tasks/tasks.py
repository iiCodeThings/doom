from flask import request
from worker.worker import async_add_task
from . import async_blueprint


@async_blueprint.route('/task/add', methods=['GET'])
def async_do_add_task():
    args = request.args or {}
    async_add_task.delay(args.get('a', 0), args.get('b', 0))
    return "do add task, see logs for details"

