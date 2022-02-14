from doom.api.base import BaseResource


class SendSms(BaseResource):

    def post(self):
        return "send sms"


class BatchSendSms(BaseResource):

    def post(self):
        pass


class DiffSendSms(BaseResource):

    def post(self):
        pass

