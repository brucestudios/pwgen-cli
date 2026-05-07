import unittest
from unittest.mock import patch, Mock
from weather_cli import get_weather

class TestWeatherCLI(unittest.TestCase):

    @patch('weather_cli.requests.get')
    def test_get_weather_with_location(self, mock_get):
        # Setup mock response
        mock_response = Mock()
        mock_response.text = "London: +Cloudy +15°C"
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # Call function
        result = get_weather("London")

        # Assertions
        mock_get.assert_called_once_with("http://wttr.in/London?format=2", timeout=10)
        self.assertEqual(result, "London: +Cloudy +15°C")

    @patch('weather_cli.requests.get')
    def test_get_weather_without_location(self, mock_get):
        # Setup mock response
        mock_response = Mock()
        mock_response.text = "Unknown location: +Sunny +20°C"
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # Call function
        result = get_weather("")

        # Assertions
        mock_get.assert_called_once_with("http://wttr.in?format=2", timeout=10)
        self.assertEqual(result, "Unknown location: +Sunny +20°C")

    @patch('weather_cli.requests.get')
    def test_get_weather_error(self, mock_get):
        # Setup mock to raise an exception
        mock_get.side_effect = Exception("Network error")

        # Call function
        result = get_weather("London")

        # Assertions
        self.assertTrue(result.startswith("Error fetching weather:"))

if __name__ == '__main__':
    unittest.main()