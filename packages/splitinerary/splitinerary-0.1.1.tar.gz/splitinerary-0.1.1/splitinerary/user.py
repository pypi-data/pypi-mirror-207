class User:
    """User object to represent people participating in a Trip.

    Attributes:
        first_name (str): First name of person.
        last_name (str): Last name of person.
        email (str, optional): Email of person. Defaults to None.
    """

    def __init__(self, first_name, last_name, email=None):
        """Inits User.

        Args:
            first_name (str): First name of person.
            last_name (str): Last name of person.
            email (str, optional): Email of person. Defaults to None.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email  # assume that emails are unique to the user

    def get_email(self):
        """Get the email of a User.

        Returns:
            str: The email of the User.
        """
        return self.email

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}({self.email})'

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return self.email == other.email
