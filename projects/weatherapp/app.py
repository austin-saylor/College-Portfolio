from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Input, Static
from textual.validation import ValidationResult, Validator
from textual.containers import Horizontal, VerticalScroll
from textual.events import Key
from data import Location, Data
import requests


class Bar(Static):
    """
    Format the bars that are used in the user interface.
    """
    pass


class Validate(Validator):
    """
    Determine if the input is valid.
    """

    def validate(self, input_string: str) -> ValidationResult:
        """
        If the location exists, report success. If not,
        report failure.
        """
        if self.location_exists(input_string):
            return self.success()
        else:
            return self.failure()

    @staticmethod
    def location_exists(input_string: str) -> bool:
        """
        Verify that the given location exists.
        """
        data = Data(input_string)

        url = data.getURL()
        response = requests.get(url)

        return bool(response.status_code == 200)


class WeatherApp(App):  # type: ignore
    """
    Compose and run the application.
    """

    CSS_PATH = "app.tcss"

    def compose(self) -> ComposeResult:
        """
        Compose the application, starting with the input box.
        """
        input = Input(value="", placeholder="Enter a location...",
                      validators=[Validate()], validate_on=["submitted"],
                      classes="input")
        yield input

    def action_report_forecast(self, input: str, feedback: str) -> None:
        """
        If the feedback gives a failure, report an 'Invalid Input' error.
        If the feedback gives a success, report the current forecast
        for the given location.
        """
        if feedback == "success":
            location = Location(input)
            loc = input
            data = Data(loc)

            url = data.getURL()
            response = requests.get(url)

            weatherdata = response.json()

            c = data.city(weatherdata)
            general_info = data.general(weatherdata)
            time_info = data.time(weatherdata)
            wind_info = data.wind(weatherdata)

            has_numbers = location.has_numbers()

            if has_numbers:
                location_code = loc.split(",")
                z = location_code[0]
                b0 = Bar(
                    "Current Forecast for: " +
                    c +
                    " | ZIP Code: [" +
                    z + "]",
                    classes="top")
                b2 = Bar(general_info, classes="general")
            else:
                b0 = Bar("Current Forecast for: " + input, classes="top")
                b2 = Bar(general_info, classes="general")
            b1 = Bar(time_info, classes="time")
            b3 = Bar(wind_info, classes="air")
            report = VerticalScroll(b0, Horizontal(b1, b2, b3))
        else:
            loc = input
            invalid = "Invalid Input: Location '" + input + "' not found!"
            report = VerticalScroll(Bar(invalid, classes="error"))

        self.mount(report)
        self.call_after_refresh(self.screen.scroll_end, animate=False)

    @on(Input.Submitted)
    def feedback(self, event: Input.Submitted) -> None:
        """
        Based on whether the given input was validated,
        confirm either a success or a failure.
        """
        assert (event.validation_result is not None), (
            "validation_result is unexpectedly None"
        )
        loc = event.input.value

        if event.validation_result.is_valid:
            self.action_report_forecast(loc, "success")
        else:
            self.action_report_forecast(loc, "failure")

    @on(Key)
    def quit(self, event: Key) -> None:
        """
        If the user presses the escape key,
        close the app.
        """
        if event.key == 'escape':
            exit()


if __name__ == "__main__":
    app = WeatherApp()
    app.run()
