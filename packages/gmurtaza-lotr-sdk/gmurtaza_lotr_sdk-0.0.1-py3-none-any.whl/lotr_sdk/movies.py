import requests
from .base import LOTR_SDK_Base


class LOTR_SDK_Movies(LOTR_SDK_Base):
    def __init__(self, bearer_token):
        super().__init__(bearer_token)

    def get_movies(self):
        return self._make_request("/movie")

    def get_movie(self, movie_id):
        return self._make_request(f"/movie/{movie_id}")

    def get_movie_quotes(self, movie_id):
        return self._make_request(f"/movie/{movie_id}/quote")
