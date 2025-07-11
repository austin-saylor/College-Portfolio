import typing
import time
from format import GeneralFormat, WindFormat

key = 'API_KEY'


class Location:
    """
    Identify the location based on the input.
    """

    def __init__(self, search_input: str) -> None:
        """
        Initialize the search_input variable.
        """
        self.__search_input = search_input

    @property
    def _search_input(self) -> str:
        """
        Get the search_input property.
        """
        return self.__search_input

    @_search_input.setter
    def _search_input(self, newSearchInput: str) -> None:
        """
        Set the value of the search_input.
        """
        self.__search_input = newSearchInput

    def has_numbers(self) -> bool:
        """
        Check if the input has numbers.
        """
        return any(char.isdigit() for char in self.__search_input)


class Data():
    """
    Retrieve various types of weather data from the URL.
    """

    def __init__(self, location: str) -> None:
        """
        Initialize the variables to be formatted.
        """
        self.__location = location

    @property
    def _location(self) -> str:
        """
        Get the city property.
        """
        return self.__location

    @_location.setter
    def _location(self, newLocation: str) -> None:
        """
        Set the value of the city.
        """
        self.__location = newLocation

    def getURL(self) -> str:
        """
        Given the location, get a url based on the
        format that the location is given in.
        """
        base_url = 'https://api.openweathermap.org/data/2.5/weather?'
        appid_str = f'appid={key}'

        location = Location(self._location)
        loc = self._location
        has_numbers = location.has_numbers()

        if has_numbers:
            url = f'{base_url}zip={loc}&{appid_str}'
        else:
            loc_parts = loc.split(",")
            city = loc_parts[0]

            if len(loc_parts) == 1:
                url = f'{base_url}q={city}&{appid_str}'

            elif len(loc_parts) == 2:
                country = loc_parts[1].strip()
                loc_str = f'{city},{country}'
                url = f'{base_url}q={loc_str}&{appid_str}'

            elif len(loc_parts) == 3:
                state = loc_parts[1].strip()
                country = loc_parts[2].strip()
                loc_str = f'{city},{state},{country}'
                url = f'{base_url}q={loc_str}&{appid_str}'

            else:
                url = f'{base_url}q={city}&{appid_str}'

        return url

    def city(self, data: typing.Any) -> str:
        """
        Retireve the city name of the given
        location.
        """
        city = str(data['name'])

        return city

    def general(self, data: typing.Any) -> str:
        """
        Retrieve general data, and put it into a string that
        includes the temperature, condition, max/min temperatures,
        what it 'feels like', visibility, humidity, and air pressure.
        """
        p_conv = 0.02952998057228486

        temp = round(1.8 * (data['main']['temp'] - 273.15) + 32)
        condition = data['weather'][0]['description']
        max = round(1.8 * (data['main']['temp_max'] - 273.15) + 32)
        min = round(1.8 * (data['main']['temp_min'] - 273.15) + 32)
        feels_like = round(1.8 * (data['main']['feels_like'] - 273.15) + 32)
        visibility = str(round(data['visibility'] / 1609.34, 2)) + " mi"
        humidity = str(data['main']['humidity']) + "%"
        pressure = str(round(data['main']['pressure'] * p_conv, 2)) + " inHg"

        format = GeneralFormat(temp, condition)
        temp = format.colorcode_temp()

        format = GeneralFormat(max, condition)
        max = format.colorcode_temp()

        format = GeneralFormat(min, condition)
        min = format.colorcode_temp()

        format = GeneralFormat(feels_like, condition)
        feels_like = format.colorcode_temp()

        if visibility == "6.21 mi":
            visibility = "6.21+ mi"
        icon = format.icon()

        t_str = "Temp: " + temp
        c_str = "\nCondition: " + icon + condition
        e_str = "\n[red]" + "Max: " + "[/]" + max + \
            " |" + "[cyan]" + " Min: " + "[/]" + min
        f_str = "\nFeels Like: " + feels_like
        v_str = "\n\nVisibility: " + visibility
        h_str = "\nHumidity: " + humidity
        p_str = "\nPressure: " + pressure

        general_info = str(
            t_str +
            c_str +
            e_str +
            f_str +
            v_str +
            h_str +
            p_str)

        return general_info

    def wind(self, data: typing.Any) -> str:
        """
        Retrieve wind data, and put it into a string that includes
        speed, direction, degree, and a description. The description
        is based on the Beaufort Scale.
        """
        speed = round(((data['wind']['speed'] / 1609.34) * 60) * 60)
        deg = data['wind']['deg']

        format = WindFormat(speed, deg)

        dir = format.format_direction()
        desc = format.format_wind_description()
        speed = format.colorcode_speed()

        speed_str = "\nSpeed: " + speed + " mph"
        dir_str = "\nDirection: " + dir + " (" + str(deg) + "°)"
        desc_str = "\nDescription: " + desc
        wind_info = str(":leaves: Wind Info:" + speed_str + dir_str + desc_str)

        return wind_info

    def time(self, data: typing.Any) -> str:
        """
        Retrieve sunrise/sunset data, and put it into a string.
        """
        t_zone = data['timezone']

        rise_time = time.gmtime(data['sys']['sunrise'] + t_zone)
        set_time = time.gmtime(data['sys']['sunset'] + t_zone)

        rise = time.strftime("%I:%M:%S", rise_time)
        set = time.strftime("%I:%M:%S", set_time)

        rise_str = "[yellow]:sunny: [/]" + \
            "Sunrise: " + "[yellow]" + rise + "[/]"
        set_str = "[red]:sunny: [/]" + "Sunset: " + "[red]" + set + "[/]"
        time_info = str(
            "  :clock1: Time Info:" +
            "\n" +
            rise_str +
            "\n" +
            set_str)

        return time_info
