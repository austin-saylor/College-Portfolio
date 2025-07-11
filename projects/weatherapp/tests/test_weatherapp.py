"""
Testing module. This module tests the
weather app.
"""

from unittest import mock
from hypothesis import given, strategies as st
import unittest
from app import Validate
from data import Location, Data
from format import GeneralFormat, WindFormat


class TestData(unittest.TestCase):
    """
    Testing class. This class tests
    the 'data' module.
    """

    def setUp(self) -> None:
        """
        Set up mock data to be tested.
        """
        self.data = {
            'name': "Mock City",
            'main': {
                'temp': 300,
                'temp_max': 305,
                'temp_min': 295,
                'feels_like': 303,
                'humidity': 70,
                'pressure': 1013
            },
            'weather': [{
                'description': 'clear sky'
            }],
            'visibility': 10000,
            'wind': {
                'speed': 5,
                'deg': 270
            },
            'sys': {
                'sunrise': 1684926645,
                'sunset': 1684977332,
            },
            'timezone': 0
        }

    @given(input_str=st.text())
    def test_location_exists(self, input_str: str) -> None:
        """
        Test if a given location exists.
        """
        # This test function was sourced from ChatGPT.
        with mock.patch('app.requests.get') as mock_get:
            # Mock the response object and configure the status_code
            mock_response = mock.Mock()
            mock_get.return_value = mock_response

            # Define a test where the location does exist
            mock_response.status_code = 200
            validator = Validate()
            self.assertTrue(validator.location_exists(input_str))

            # Define a test where the location does not exist
            mock_response.status_code = 404
            self.assertFalse(validator.location_exists(input_str))

    @given(input_str=st.text())
    def test_has_numbers(self, input_str: str) -> None:
        """
        Test if the given input string contains
        numbers.
        """
        location = Location(input_str)
        expected = any(char.isdigit() for char in input_str)
        self.assertEqual(location.has_numbers(), expected)

    @given(input_str=st.text())
    def test_getURL(self, input_str: str) -> None:
        """
        Test the acquisition of the url for a
        given input string.
        """
        data = Data(input_str)
        url = data.getURL()
        self.assertTrue(
            'https://api.openweathermap.org/data/2.5/weather?' in url
        )

    def test_searchinput_getter(self) -> None:
        """
        Test the getter method for
        the search input.
        """
        search_input: str = str(self.data['name'])
        location_instance = Location(search_input)
        search_input = location_instance._search_input

    @given(search_input=st.text())
    def test_searchinput_setter(self, search_input: str) -> None:
        """
        Test the setter method for
        the search input.
        """
        location_instance = Location(search_input)
        location_instance._search_input = search_input

    def test_location_getter(self) -> None:
        """
        Test the getter method for
        the location.
        """
        location: str = str(self.data['name'])
        data_instance = Data(location)
        location = data_instance._location

    @given(location=st.text())
    def test_location_setter(self, location: str) -> None:
        """
        Test the setter method for
        the location.
        """
        data_instance = Data(location)
        data_instance._location = location

    def test_city(self) -> None:
        """
        Test the city name.
        """
        location: str = str(self.data['name'])
        data_instance = Data(location)
        city = data_instance.city(self.data)

        self.assertEqual(city, "Mock City")

    def test_general_info(self) -> None:
        """
        Test the components of
        'general info'.
        """
        location: str = str(self.data['name'])
        data_instance = Data(location)
        mock_general_info = data_instance.general(self.data)
        self.assertIn("Temp:   [yellow]80[/]°F", mock_general_info)
        self.assertIn("Condition: [yellow]:sunny: [/]", mock_general_info)
        self.assertIn(
            "[red]Max: [/]  [yellow]89[/]°F " +
            "|[cyan] Min: [/]  [green]71[/]°F",
            mock_general_info
        )
        self.assertIn("Feels Like:   [yellow]86[/]°F", mock_general_info)
        self.assertIn("Visibility: 6.21+ mi", mock_general_info)
        self.assertIn("Humidity: 70%", mock_general_info)
        self.assertIn("Pressure: 29.91 inHg", mock_general_info)

    def test_wind_info(self) -> None:
        """
        Test the components of
        'wind info'.
        """
        location: str = str(self.data['name'])
        data_instance = Data(location)
        mock_wind_info = data_instance.wind(self.data)
        self.assertIn("Speed: [cyan]11[/]", mock_wind_info)
        self.assertIn("mph", mock_wind_info)
        self.assertIn("Direction: W (270°)", mock_wind_info)
        self.assertIn("Description: [cyan]Gentle Breeze[/]", mock_wind_info)

    def test_time_info(self) -> None:
        """
        Test the components of
        'time info'
        """
        location: str = str(self.data['name'])
        data_instance = Data(location)
        mock_time_info = data_instance.time(self.data)
        self.assertIn(
            "[yellow]:sunny: [/]" +
            "Sunrise: [yellow]11:10:45[/]",
            mock_time_info
        )
        self.assertIn(
            "[red]:sunny: [/]" +
            "Sunset: [red]01:15:32[/]",
            mock_time_info
        )


class TestFormat(unittest.TestCase):
    @given(condition=st.text())
    def test_condition_setter(self, condition: str) -> None:
        """
        Test the setter method of
        the condition.
        """
        general = GeneralFormat(10, "cloudy")
        general._condition = condition
        self.assertEqual(general._condition, condition)

    @given(temp=st.integers())
    def test_temp_setter(self, temp: int) -> None:
        """
        Test the setter method of
        the temperature.
        """
        general = GeneralFormat(10, "cloudy")
        general._temp = temp
        self.assertEqual(general._temp, temp)

    @given(speed=st.integers())
    def test_windspeed_setter(self, speed: int) -> None:
        """
        Test the setter method of
        the wind speed.
        """
        wind = WindFormat(20, 270)
        wind._speed = speed
        self.assertEqual(wind._speed, speed)

    @given(deg=st.integers())
    def test_winddeg_setter(self, deg: int) -> None:
        """
        Test the setter method of
        the wind degree.
        """
        wind = WindFormat(20, 270)
        wind._deg = deg
        self.assertEqual(wind._deg, deg)

    def test_temp_colorcode(self) -> None:
        """
        Test the color coding of the
        temperature.
        """
        # Test temperature color coding
        general = GeneralFormat(10, "clear sky")

        # Test extremely cold temperatures:
        general._temp = -999999999999
        self.assertEqual(
            general.colorcode_temp(),
            "[purple]-999999999999[/]°F"
        )

        # Test cold temperatures:
        general._temp = 0
        self.assertEqual(general.colorcode_temp(), "[blue]0[/]°F")

        # Test cool temperatures:
        general._temp = 32
        self.assertEqual(general.colorcode_temp(), "  [cyan]32[/]°F")

        # Test warm temperatures:
        general._temp = 70
        self.assertEqual(general.colorcode_temp(), "  [green]70[/]°F")

        # Test hot temperatures:
        general._temp = 90
        self.assertEqual(general.colorcode_temp(), "  [yellow]90[/]°F")

        # Test extremely hot temperatures:
        general._temp = 999999999999
        self.assertEqual(
            general.colorcode_temp(),
            " [red]999999999999[/]°F"
        )

    def test_icon(self) -> None:
        """
        Test the formatting of the icon.
        """
        # Test weather icon assignment
        general = GeneralFormat(50, "clear sky")

        # Test sunny weather:
        self.assertEqual(general.icon(), "[yellow]:sunny: [/]")

        # Test cloudy weather:
        general._condition = "few clouds"
        self.assertEqual(general.icon(), ":partly_sunny: ")
        general._condition = "clouds"
        self.assertEqual(general.icon(), ":cloud: ")
        general._condition = "haze"
        self.assertEqual(general.icon(), ":cloud: ")
        general._condition = "fog"
        self.assertEqual(general.icon(), ":cloud: ")
        general._condition = "mist"
        self.assertEqual(general.icon(), ":cloud: ")

        # Test rainy weather:
        general._condition = "light rain"
        self.assertEqual(general.icon(), ":droplet: ")
        general._condition = "rain"
        self.assertEqual(general.icon(), ":sweat_drops: ")
        general._condition = "moderate rain"
        self.assertEqual(general.icon(), ":sweat_drops: ")

        # Test stormy weather:
        general._condition = "thunderstorms"
        self.assertEqual(general.icon(), ":zap: ")

        # Test snowy weather:
        general._condition = "snow"
        self.assertEqual(general.icon(), "[cyan]:snowflake: [/]")

    def test_wind_direction_formatting(self) -> None:
        """
        Test the wind direction.
        """
        # Test wind direction determination
        wind = WindFormat(15, 350)

        # Test northern directions: ------------------------------------------
        wind._deg = 315
        self.assertEqual(wind.format_direction(), "NW")

        wind._deg = 335
        self.assertEqual(wind.format_direction(), "N/NW")

        wind._deg = 350
        self.assertEqual(wind.format_direction(), "N")

        wind._deg = 25
        self.assertEqual(wind.format_direction(), "N/NE")

        wind._deg = 45
        self.assertEqual(wind.format_direction(), "NE")

        # Test eastern directions: ------------------------------------------
        wind._deg = 65
        self.assertEqual(wind.format_direction(), "E/NE")

        wind._deg = 90
        self.assertEqual(wind.format_direction(), "E")

        wind._deg = 115
        self.assertEqual(wind.format_direction(), "E/SE")

        # Test southern directions: -----------------------------------------
        wind._deg = 135
        self.assertEqual(wind.format_direction(), "SE")

        wind._deg = 155
        self.assertEqual(wind.format_direction(), "S/SE")

        wind._deg = 180
        self.assertEqual(wind.format_direction(), "S")

        wind._deg = 205
        self.assertEqual(wind.format_direction(), "S/SW")

        wind._deg = 225
        self.assertEqual(wind.format_direction(), "SW")

        # Test western directions: ------------------------------------------
        wind._deg = 245
        self.assertEqual(wind.format_direction(), "W/SW")

        wind._deg = 270
        self.assertEqual(wind.format_direction(), "W")

        wind._deg = 295
        self.assertEqual(wind.format_direction(), "W/NW")

    def test_wind_speed_description(self) -> None:
        """
        Test the formatting of the
        wind speed description.
        """
        # Test wind speed descriptions
        wind = WindFormat(45, 100)

        # Test calm/no wind: ------------------------------------------------
        wind._speed = 0
        self.assertEqual(
            wind.format_wind_description(),
            "[blue]Calm[/]"
        )

        # Test light wind: --------------------------------------------------
        wind._speed = 2
        self.assertEqual(
            wind.format_wind_description(),
            "[cyan]Light Air[/]"
        )

        wind._speed = 5
        self.assertEqual(
            wind.format_wind_description(),
            "[cyan]Light Breeze[/]"
        )

        wind._speed = 10
        self.assertEqual(
            wind.format_wind_description(),
            "[cyan]Gentle Breeze[/]"
        )

        # Test moderate wind: -----------------------------------------------
        wind._speed = 15
        self.assertEqual(
            wind.format_wind_description(),
            "[green]Moderate Breeze[/]"
        )

        wind._speed = 20
        self.assertEqual(
            wind.format_wind_description(),
            "[green]Fresh Breeze[/]"
        )

        wind._speed = 30
        self.assertEqual(
            wind.format_wind_description(),
            "[green]Strong Breeze[/]"
        )

        # Test high wind: ---------------------------------------------------
        wind._speed = 35
        self.assertEqual(
            wind.format_wind_description(),
            "[yellow]High Wind[/]"
        )

        wind._speed = 40
        self.assertEqual(
            wind.format_wind_description(),
            "[yellow]Gale[/]"
        )

        wind._speed = 50
        self.assertEqual(
            wind.format_wind_description(),
            "[yellow]Strong Gale[/]"
        )

        # Test extremely high wind: -----------------------------------------
        wind._speed = 60
        self.assertEqual(
            wind.format_wind_description(),
            "[red]Storm[/]"
        )

        wind._speed = 70
        self.assertEqual(
            wind.format_wind_description(),
            "[red]Violent Storm[/]"
        )

        wind._speed = 75
        self.assertEqual(
            wind.format_wind_description(),
            "[red]Hurricane-Force[/]"
        )


if __name__ == '__main__':
    unittest.main()
