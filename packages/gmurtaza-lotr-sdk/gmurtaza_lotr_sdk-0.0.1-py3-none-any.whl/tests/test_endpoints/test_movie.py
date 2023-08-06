import unittest
from unittest.mock import Mock, patch

from lotr_sdk.movies import LOTR_SDK_Movies


class TestMoviesAPI(unittest.TestCase):
    def setUp(self):
        self.bearer_token = "my_token"
        self.client = LOTR_SDK_Movies(self.bearer_token)

    @patch("lotr_sdk.movies.requests.get")
    def test_get_movies(self, mock_get):
        # Set up mock response from server
        expected_data = [{"_id": "1", "name": "The Fellowship of the Ring"}, {"_id": "2", "name": "The Two Towers"}]
        mock_response = Mock()
        mock_response.json.return_value = expected_data
        mock_get.return_value = mock_response

        # Call the method and check the result
        result = self.client.get_movies()
        self.assertEqual(result, expected_data)

        # Check that the correct endpoint and headers were used
        mock_get.assert_called_once_with("https://the-one-api.dev/v2/movie",
                                         headers={"Authorization": "Bearer my_token"})
