# Welcome to Splitinerary's documentation!

## Installation

Shell command to install the library from PyPI:
```
pip install splitinerary
```

## Usage

After installing the library, import the splitinerary module:
```
import splitinerary
```
Or import specific objects to use:
```
from splitinerary import Trip, Plane
```

Example program for a simple trip:
```
from splitinerary import Trip, Plane
import datetime

now = datetime.datetime.now()
date = now.date()
trip = Trip()
event = Event(now)

trip.add_event(event)

events = trip.get_all_events()
```

For a full list of objects and functions, please see documentation.

```eval_rst
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules
```
## Indices and tables
```eval_rst
* :ref:`genindex`
* :ref:`modindex`
```

## Examples

```python
from splitinerary import Trip, User, CustomEvent, Plane
import datetime

# Create Users
alice = User("Alice", "Smith", "Alice@Columbia.edu")
bob = User("Bob", "Jones", "Bob@Columbia.edu")
charlie = User("Charlie", "Berens", "Charlie@Columbia.edu")

# Create times
now = datetime.datetime.now()
tomorrow = now + datetime.timedelta(days=1)


# Create Trip
summer_vacation = Trip()

# Create Events
alice_flight = Plane("DL188",
                     "DTW",
                     "LGA",
                     now+datetime.timedelta(hours=3),
                     now+datetime.timedelta(hours=5),
                     155.85,
                     "GY60P1Q",
                     now,
                     [alice]
                     )

bob_flight = Plane("NKS183",
                   "PHL",
                   "LGA",
                   now+datetime.timedelta(hours=4),
                   now+datetime.timedelta(hours=6),
                   129.44,
                   "HS15ON7",
                   now+datetime.timedelta(hours=3),
                   [bob])

concert = CustomEvent("Dua Lipa Concert",
                      "Part of a music festival",
                      tomorrow,
                      tomorrow+datetime.timedelta(hours=5),
                      450.00,
                      tomorrow,
                      [alice, bob])

# Add Events to Trip
summer_vacation.add_event(alice_flight)
summer_vacation.add_event(bob_flight)
summer_vacation.add_event(concert)

# get_events_on_date usage example 1
print('----------Example 1----------')
todays_events = summer_vacation.get_events_on_date(tomorrow.date())
for i, event in enumerate(todays_events, 1):
    print(f'{i}: {event}')

# get_eventful_dates usage example 2
print('----------Example 2----------')
eventful_dates = summer_vacation.get_eventful_dates()
print(eventful_dates)

# get_all_events usage example 3
print('----------Example 3----------')
all_events = summer_vacation.get_all_events()
for i, event in enumerate(all_events, 1):
    print(f'{i}: {event}')

# get_next_event usage example 4
print('----------Example 4----------')
next_event = summer_vacation.get_next_event()
print(next_event)

# get_users_list usage example 5
print('----------Example 5----------')
users_list = summer_vacation.get_users_list()
for i, user in enumerate(users_list, 1):
    print(f'{i}: {user}')

# get_events_of_user usage example 6
print('----------Example 6----------')
alices_events = summer_vacation.get_events_of_user(alice)
for i, event in enumerate(alices_events, 1):
    print(f'{i}: {event}')

# remove_user_from_event usage example 7
print('----------Example 7----------')
summer_vacation.remove_user_from_event(bob, concert)
bobs_events = summer_vacation.get_events_of_user(bob)
for i, event in enumerate(bobs_events, 1):
    print(f'{i}: {event}')

# remove_event_by_index usage example 8
print('----------Example 8----------')
summer_vacation.remove_event_by_index(tomorrow, 0)
trips_events = summer_vacation.get_all_events()
for i, event in enumerate(trips_events, 1):
    print(f'{i}: {event}')

# add_user_to_event usage example 9
print('----------Example 9----------')
summer_vacation.add_user_to_event(charlie, concert)
charlies_events = summer_vacation.get_events_of_user(charlie)
for i, event in enumerate(charlies_events, 1):
    print(f'{i}: {event}')
```