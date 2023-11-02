from configs import BaseService


class WebhookManager(BaseService):
    def __init__(self, url: str):
        self._url = url

    def execute(self):
        pass
