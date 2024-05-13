#!/usr/bin/python3
"""
This script defines a User class with an email attribute.
"""


class User():
    """
    This class represents a user with an email attribute.
    """

    def __init__(self):
        """
        Initialize a User instance with an email attribute set to None.
        """
        self.__email = None

    @property
    def email(self):
        """
        Getter method for the email attribute.
        Returns:
            str: The email of the user.
        """
        return self.__email

    @email.setter
    def email(self, value):
        """
        Setter method for the email attribute.
        Args:
            value (str): The email to set for the user.
        Raises:
            TypeError: If the provided value is not a string.
        """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":
    # Creating a User instance
    u = User()
    # Setting the email attribute
    u.email = "john@snow.com"
    # Printing the email attribute
    print(u.email)
