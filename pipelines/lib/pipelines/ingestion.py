class Calculator:
    """
    A simple calculator class.
    """

    def __init__(self, initial_value=0):
        """
        Initialize the calculator with an initial value.

        :param initial_value: A value to start calculations with. Default is 0.
        """
        self.value = initial_value

    def add(self, number):
        """
        Add a number to the current value.

        :param number: The number to add.
        :return: Updated value.
        """
        self.value += number
        return self.value

    def subtract(self, number):
        """
        Subtract a number from the current value.

        :param number: The number to subtract.
        :return: Updated value.
        """
        self.value -= number
        return self.value

    def multiply(self, number):
        """
        Multiply the current value by a number.

        :param number: The number to multiply by.
        :return: Updated value.
        """
        self.value *= number
        return self.value

    def divide(self, number):
        """
        Divide the current value by a number.

        :param number: The number to divide by.
        :return: Updated value.
        """
        if number == 0:
            raise ValueError("Cannot divide by zero.")
        self.value /= number
        return self.value

    def reset(self):
        """
        Reset the calculator's value to zero.
        """
        self.value = 0

    def __str__(self):
        """
        String representation of the calculator's value.
        """
        return str(self.value)
