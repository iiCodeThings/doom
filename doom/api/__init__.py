from flask_restful import Api


sms_api = Api(prefix='/api/2.0')

from .sms import SendSms
from .sms import DiffSendSms
from .sms import BatchSendSms


sms_api.add_resource(SendSms, '/sms/send')
sms_api.add_resource(DiffSendSms, '/sms/diff/send')
sms_api.add_resource(BatchSendSms, '/sms/batch/send')

