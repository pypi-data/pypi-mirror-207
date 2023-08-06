import requests


class LOTR_SDK_Base:
    def __init__(self, bearer_token):
        self.base_url = "https://the-one-api.dev/v2"
        self.headers = {"Authorization": f"Bearer {bearer_token}"}

    def _make_request(self, endpoint):
        response = requests.get(f"{self.base_url}{endpoint}", headers=self.headers)
        response.raise_for_status()
        return response.json()
