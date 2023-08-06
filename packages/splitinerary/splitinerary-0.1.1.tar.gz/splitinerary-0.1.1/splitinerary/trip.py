import datetime
from collections import defaultdict


class Trip:
    """Trip object that everything else in Splitinerary gets added to.

    Attributes:
        dates_list (list of datetime.date): sortable list of datetime.date,
            used to keep track of which dates have events on them.
        dates_dict (dict of datetime.date : event.Event):
            keys can be used to see if date exists in trip, values are lists
            (that can be sorted) of each day's events.
        user_activities (dict of user: {date: [event1, event2]}):
            Maps users to their activities on dates
    """

    def __init__(self):
        """Inits Trip."""
        self.dates_list = []
        self.dates_dict = {}
        self.user_activities = defaultdict(lambda: defaultdict(list))

    def add_event(self, event):
        """Add an Event object to the Trip.
        This involves adding the date of the event to self.dates_list and
        adding the event to self.dates_dict[date].

        Args:
            event (Event):  The event to be added to the Trip.
        """
        date = event.get_date()
        if date not in self.dates_dict:
            self.dates_list.append(date)
            self.dates_dict[date] = []
        self.dates_dict[date].append(event)

        users = event.get_users()
        if users is not None:
            for user in users:
                self.user_activities[user][date].append(event)

    def get_events_on_date(self, date):
        """Returns of the events on a certain day in order of start time.

        Args:
            date (datetime.date):  the date whose events are to be returned.

        Returns:
            list of (datetime.time, Event): sorted list of tuples of
            events on the input date if it exists, else None.
        """
        if date not in self.dates_dict:
            return None
        else:
            self.dates_dict[date].sort()
            return self.dates_dict[date]

    def get_eventful_dates(self):
        """Print all of the dates that have an event on them in order of start
            time.

        Returns:
            list of datetime.date: sorted list of dates that have
            events on them if it exists, else None.
        """
        if not self.dates_list:
            return None
        self.dates_list.sort()
        return self.dates_list

    def get_all_events(self):
        """Returns all events in the Trip in order of start time.

        Returns:
            list of Event: sorted list of all events in the
            trip.
        """
        if not self.dates_dict:
            return None
        all_events = []
        for events in self.dates_dict.values():
            all_events.extend(events)
        all_events.sort()
        return all_events

    def get_next_event(self):
        """Returns the next event that will take place for any user.

        Returns:
            Event: the next event that will take place for any
            User if it exists, else None.
        """
        now = datetime.datetime.now()
        all_events = self.get_all_events()
        for event in all_events:
            if event.datetime < now:
                continue
            return event
        return None

    def get_users_list(self):
        """Gets list of users participating in Trip.

        Returns:
            list of Users: A list of users participating in Trip.
        """
        return list(self.user_activities.keys())

    def get_events_of_user(self, user):
        """Gets the events of a given User.

        Args:
            user (User): A User in the Trip.

        Returns:
            dict of user: {date: [event1, event2]} : dictionary of user's
            events for each day.
        """
        if user not in self.user_activities:
            return None
        return self.user_activities[user]

    def remove_event_by_index(self, date, index):
        """Remove an Event from a Trip given a date and index of Event on date.

        Args:
            date (datetime.Date): Date of event.
            index (int): Index of Event on date, in order of time.
        """
        if date not in self.dates_dict:
            return
        days_events_list = self.dates_dict[date]
        if index < 0 or index >= len(days_events_list):
            return
        removed_event = days_events_list.pop(index)
        event_date = removed_event.get_date()

        # remove from dates_list if necessary
        if len(days_events_list) == 0:
            self.dates_list.remove(event_date)

        # remove event from each affected user's user_activities dict entry
        affected_users = removed_event.get_users()
        for user in affected_users:
            users_events = self.user_activities[user]
            users_events[event_date].remove(removed_event)

    def remove_user_from_event(self, user, event):
        """Remove a User from an Event in the Trip.

        Args:
            user (User): User to remove from Event.
            event (Event): Event from which User is being removed.
        """
        event_date = event.get_date()

        users_events = self.user_activities[user]
        users_events[event_date].remove(event)

        users_list = event.get_users()
        users_list.remove(user)

    def add_user_to_event(self, user, event):
        """Add a user to an Event in the Trip.

        Args:
            user (User): User to add to the Event.
            event (Event): Event from which User is being added.
        """
        event_date = event.get_date()

        users_events = self.user_activities[user]
        users_events[event_date].append(event)

        event.add_user(user)
