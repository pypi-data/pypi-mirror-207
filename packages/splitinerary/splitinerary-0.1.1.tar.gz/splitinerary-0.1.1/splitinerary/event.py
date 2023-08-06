class Event:
    """Event object. Each event is sortable among other Events by datetime.

    Attributes:
        datetime (datetime.datetime): when the user wants to arrive at
            the event, NOT NECESSARILY when the event starts (e.g. user might
            arrive at the airport 2 hours before the flight departs).
    """

    def __init__(self, datetime, users=None):
        """Inits Event.

        Args:
            datetime (datetime.Datetime): datetime.Datetime object of when the
                user gets to the event.
            users (list of User, optional): Users participating in the Event.
                Defaults to None.
        """
        self.datetime = datetime
        if users is None:
            self.users = []
        else:
            self.users = users

    def add_user(self, user):
        """Add user to Event.

        Args:
            user (User): User to add to Event.
        """
        self.users.append(user)

    def get_users(self):
        """Get Users participating in Event.

        Returns:
            list of User: Users participating in Event if there are any,
                else None.
        """
        return self.users if self.users else None

    def get_date(self):
        """Get date of Event.

        Returns:
            datetime.Date: Date the event takes place on.
        """
        return self.datetime.date()

    def get_time(self):
        """Get time of Event (without the date).

        Returns:
            datetime.Time: Time the event takes place on.
        """
        return self.datetime.time()

    def __lt__(self, other):
        return self.datetime < other.datetime

    def __eq__(self, other):
        return self.datetime == other.datetime

    def __str__(self) -> str:
        date = str(self.get_date())
        time = str(self.get_time())
        users = str(self.get_users())
        return f'date: {date}, time: {time}, users: {users}'
