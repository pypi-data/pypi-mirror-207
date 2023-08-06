from . import event


class Transportation(event.Event):
    """Transporation object that the vehicle objects inherit from."""

    def __init__(self, departure_time, arrival_time, cost=0, confirmation_code=None, *args, **kw):  # noqa
        """Inits Transportation.

        Args:
            departure_time (datetime.time): Time the transportation departs.
            arrival_time (datetime.time): Time the transportation arrives.
            cost (int, optional): Cost of the transporation. Defaults to 0.
            confirmation_code (str, optional): Confirmation code of the
                transportation. Defaults to None.
        """
        self.cost = cost
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.confirmation_code = confirmation_code
        super().__init__(*args, **kw)

    def __str__(self) -> str:
        return super().__str__() + f', departure time: {self.departure_time}, arrival time: {self.arrival_time}'  # noqa


class Plane(Transportation):
    """Plane transportation method."""

    def __init__(self, flight_number, departure_terminal=None, arrival_terminal=None, *args, **kw):  # noqa
        """Inits Plane

        Args:
            flight_number (str): Flight number.
            departure_terminal (str, optional): Departure airport. Defaults to
                None.
            arrival_terminal (str, optional): Arrival airport. Defaults to
                None.
        """
        self.flight_number = flight_number
        self.departure_terminal = departure_terminal
        self.arrival_terminal = arrival_terminal
        super().__init__(*args, **kw)

    def __str__(self) -> str:
        return super().__str__() + f', FLIGHT, flight_number: {self.flight_number}'  # noqa


class Train(Transportation):
    """Train transporation method."""

    def __init__(self, departure_station, arrival_station, train_line=None, *args, **kw):  # noqa
        """Inits Train

        Args:
            departure_station (str): Station the train departs from.
            arrival_station (str): Station the train arrives to.
            train_line (str, optional): Train line or route the train runs on.
                Defaults to None.
        """
        self.departure_station = departure_station
        self.arrival_station = arrival_station
        self.train_line = train_line
        super().__init__(*args, **kw)

    def __str__(self) -> str:
        return (
            super().__str__()
            + f', TRAIN, departure_station: {self.departure_station}, arrival_station: {self.arrival_station}'  # noqa
        )


class Boat(Transportation):
    """Boat transportation method."""

    def __init__(self, departure_terminal, arrival_terminal, route=None, *args, **kw):  # noqa
        """_summary_

        Args:
            departure_terminal (str): Terminal the boat departs from.
            arrival_terminal (str): Terminal the boat arrives to.
            route (str, optional): Line or route the boat takes.
                Defaults to None.
        """
        self.departure_terminal = departure_terminal
        self.arrival_terminal = arrival_terminal
        self.route = route
        super().__init__(*args, **kw)

    def __str__(self) -> str:
        return (
            super().__str__()
            + f', BOAT, departure_terminal: {self.departure_terminal}, arrival_terminal: {self.arrival_terminal}'  # noqa
        )


class Car(Transportation):
    """Car transportation method."""

    def __init__(self, departure_location, arrival_location, company=None, *args, **kw):  # noqa
        """_summary_

        Args:
            departure_location (str): Location the car departs from.
            arrival_location (str): Location the car arrives to.
            company (str, optional): Company the car belongs to, like Uber or
                Lyft. Defaults to None.
        """
        self.departure_location = departure_location
        self.arrival_location = arrival_location
        self.company = company
        super().__init__(*args, **kw)

    def __str__(self) -> str:
        return (
            super().__str__()
            + f', CAR, departure_location: {self.departure_location}, arrival_location: {self.arrival_location}'  # noqa
        )
