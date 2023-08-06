from splitinerary import CustomEvent, User

import unittest
import datetime


class TestCustomEvent(unittest.TestCase):
    def test_create_custom_event_with_user_success(self):
        # arrange
        now = datetime.datetime.now()
        later = now+datetime.timedelta(hours=1)

        user = User('first', 'last', 'email@email.com')
        
        # act
        custom_event = CustomEvent('test_event', 'test_description', now, later, 100.50, now, [user])
        # assert
        self.assertListEqual(custom_event.users, [user])

    def test_create_custom_event_without_user_success(self):
        # arrange
        now = datetime.datetime.now()
        later = now+datetime.timedelta(hours=1)
        # act
        custom_event = CustomEvent('test_event', 'test_description', now, later, 100.50, now)
        # assert
        self.assertListEqual(custom_event.users, [])

    def test_custom_event_str(self):
        # arrange
        now = datetime.datetime.now()
        later = now+datetime.timedelta(hours=1) 
        expected_str = f'date: {now.date()}, time: {now.time()}, users: None, Event name: test_event, Description: test_description, Start time: {now}, End time: {later}, Cost: 100.5'
        # act
        custom_event = CustomEvent('test_event', 'test_description', now, later, 100.5, now)
        # assert
        self.assertEqual(str(custom_event), expected_str)

    def test_custom_event_eq(self):
        # arrange
        now = datetime.datetime.now()
        later = now+datetime.timedelta(hours=1) 
        # act
        custom_event = CustomEvent('test_event', 'test_description', now, later, 100.5, now)
        second_event = CustomEvent('test_event', 'test_description', now, later, 100.5, now)
        # assert
        self.assertEqual(custom_event, second_event)