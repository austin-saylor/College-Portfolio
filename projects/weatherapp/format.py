import sys


class GeneralFormat():
    """
    Format various numbers to include colors that
    indicate their intensity, and format conditions
    by assigning an icon to them.
    """

    def __init__(self, temp: int, condition: str) -> None:
        """
        Initialize the variables to be formatted.
        """
        self.__temp = temp
        self.__condition = condition

    @property
    def _temp(self) -> int:
        """
        Get the temperature property.
        """
        return self.__temp

    @_temp.setter
    def _temp(self, newTemp: int) -> None:
        """
        Set the value of the temperature.
        """
        self.__temp = newTemp

    @property
    def _condition(self) -> str:
        """
        Get the condtion property.
        """
        return self.__condition

    @_condition.setter
    def _condition(self, newCondition: str) -> None:
        """
        Set the value of the temperature.
        """
        self.__condition = newCondition

    def colorcode_temp(self) -> str:
        """
        Colors the temperatures based on the range of
        values that they lie within. This function also
        adds the degree symbol.
        """
        temp = self._temp

        temp_str = str(temp)

        if temp < -20:
            t_str = "[purple]" + temp_str + "[/]" + "°F"
        elif temp >= -20 and temp < 20:
            t_str = "[blue]" + temp_str + "[/]" + "°F"
        elif temp >= 20 and temp < 50:
            t_str = "  " + "[cyan]" + temp_str + "[/]" + "°F"
        elif temp >= 50 and temp < 80:
            t_str = "  " + "[green]" + temp_str + "[/]" + "°F"
        elif temp >= 80 and temp < 100:
            t_str = "  " + "[yellow]" + temp_str + "[/]" + "°F"
        elif temp >= 100:
            t_str = " " + "[red]" + temp_str + "[/]" + "°F"
        return t_str

    def icon(self) -> str:
        """
        Assigns an icon to the weather, based on
        the current weather condition.
        """
        condition = self.__condition

        icon = ""
        if "clouds" or "haze" or "fog" or "mist" in condition:
            icon = ":cloud: "
        if "clear sky" in condition:
            icon = "[yellow]:sunny: [/]"
        if "few clouds" in condition:
            icon = ":partly_sunny: "
        if "rain" in condition:
            if condition == "light rain":
                icon = ":droplet: "
            else:
                icon = ":sweat_drops: "
        if "thunder" in condition:
            icon = ":zap: "
        if "snow" in condition:
            icon = "[cyan]:snowflake: [/]"
        return icon


class WindFormat():
    """
    Format various numbers to include colors that
    indicate their intensity.
    """

    def __init__(self, speed: int, deg: int) -> None:
        """
        Initialize the variables to be formatted.
        """
        self.__speed = speed
        self.__deg = deg

    @property
    def _speed(self) -> int:
        """
        Get the speed property.
        """
        return self.__speed

    @_speed.setter
    def _speed(self, newSpeed: int) -> None:
        """
        Set the value of the temperature.
        """
        self.__speed = newSpeed

    @property
    def _deg(self) -> int:
        """
        Get the degree property.
        """
        return self.__deg

    @_deg.setter
    def _deg(self, newDeg: int) -> None:
        """
        Set the value of the degree.
        """
        self.__deg = newDeg

    def colorcode_speed(self) -> str:
        """
        Colors the wind speeds based on the range of
        values that they lie within.
        """
        speed = self._speed

        speed_str = str(speed)

        if speed < 1:
            s_str = str("[blue]" + speed_str + "[/]")
        elif speed >= 1 and speed < 12:
            s_str = str("[cyan]" + speed_str + "[/]")
        elif speed >= 12 and speed < 31:
            s_str = str("[green]" + speed_str + "[/]")
        elif speed >= 31 and speed < 55:
            s_str = str("[yellow]" + speed_str + "[/]")
        else:
            s_str = str("[red]" + speed_str + "[/]")

        return s_str

    def format_direction(self) -> str:
        """
        Given the degree that the wind is blowing at,
        determine its direction. This function was sourced
        from ChatGPT.
        """
        deg = self._deg

        directions = [
            "N", "N/NE", "NE", "E/NE", "E", "E/SE", "SE", "S/SE",
            "S", "S/SW", "SW", "W/SW", "W", "W/NW", "NW", "N/NW", "N"
        ]
        idx = round(deg / 22.5) % 16

        return directions[idx]

    def format_wind_description(self) -> str:
        """
        Given the wind speed, identify a description for
        the wind, and colorcode it based on the range
        that the speed lies within. To determine the
        description, the Beaufort Scale is utilized.
        This function was sourced from ChatGPT.
        """
        speed = self._speed

        descriptions = [
            (1, "[blue]Calm[/]"),
            (3, "[cyan]Light Air[/]"),
            (7, "[cyan]Light Breeze[/]"),
            (12, "[cyan]Gentle Breeze[/]"),
            (18, "[green]Moderate Breeze[/]"),
            (24, "[green]Fresh Breeze[/]"),
            (31, "[green]Strong Breeze[/]"),
            (39, "[yellow]High Wind[/]"),
            (46, "[yellow]Gale[/]"),
            (55, "[yellow]Strong Gale[/]"),
            (64, "[red]Storm[/]"),
            (73, "[red]Violent Storm[/]"),
            (sys.maxsize, "[red]Hurricane-Force[/]"),
        ]

        for threshold, description in descriptions:
            if speed < threshold:
                return description

        return descriptions[-1][1]
