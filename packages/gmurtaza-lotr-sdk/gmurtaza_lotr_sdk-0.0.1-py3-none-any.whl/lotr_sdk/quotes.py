import requests
from .base import LOTR_SDK_Base


class LOTR_SDK_Quotes(LOTR_SDK_Base):
    def __init__(self, bearer_token):
        super().__init__(bearer_token)

    def get_quotes(self):
        return self._make_request("/quote")

    def get_quote(self, quote_id):
        return self._make_request(f"/quote/{quote_id}")
