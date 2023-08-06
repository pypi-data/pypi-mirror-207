import unittest
from unittest.mock import patch, Mock
from lotr_sdk.quotes import LOTR_SDK_Quotes


class TestQuotesAPI(unittest.TestCase):
    def setUp(self):
        self.bearer_token = "my_token"
        self.client = LOTR_SDK_Quotes(self.bearer_token)

    @patch("lotr_sdk.quotes.requests.get")
    def test_get_quotes(self, mock_get):
        # Set up mock response from server
        expected_data = [{"_id": "1", "dialog": "You shall not pass!"}, {"_id": "2", "dialog": "My precious"}]
        mock_response = Mock()
        mock_response.json.return_value = expected_data
        mock_get.return_value = mock_response

        # Call the method and check the result
        result = self.client.get_quotes()
        self.assertEqual(result, expected_data)

        # Check that the correct endpoint and headers were used
        mock_get.assert_called_once_with("https://the-one-api.dev/v2/quote",
                                         headers={"Authorization": "Bearer my_token"})

    @patch("lotr_sdk.quotes.requests.get")
    def test_get_quote(self, mock_get):
        # Set up mock response from server
        expected_data = {"_id": "1", "dialog": "You shall not pass!"}
        mock_response = Mock()
        mock_response.json.return_value = expected_data
        mock_get.return_value = mock_response

        # Call the method and check the result
        result = self.client.get_quote("1")
        self.assertEqual(result, expected_data)

        # Check that the correct endpoint and headers were used
        mock_get.assert_called_once_with("https://the-one-api.dev/v2/quote/1",
                                         headers={"Authorization": "Bearer my_token"})
