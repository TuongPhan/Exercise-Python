
"""
This program show their name and their age input.
Print out a message addressed to them that tells them the year that they will turn X years old (default X = 100).
"""
import time


class Info:

    def __init__(self):
        self.name = input("Input your name: ")
        while self.validate_name():
            self.name = input("Input your name again: ")

        self.age = input("Input your age: ")
        while not self.validate_age():
            self.age = input("Input your age again: ")

        self.turn = input("Year turn X years old (default X = 100): ")
        if not self.turn:
            self.turn = "100"
        while not self.validate_turn():
            self.turn = input("Year turn X years old again:")

    def validate_name(self):
        """
        If str
        :return: True
        """
        return self.name.isdigit()

    def validate_age(self):
        if self.age.isdigit() is True and int(self.age) < 99:
            return True
        else:
            return False

    def validate_turn(self):
        if self.turn.isdigit() is True and int(self.age) < int(self.turn):
            return True
        else:
            return False

    def turn_yrs(self):
        year = int(self.turn)-int(self.age) + time.localtime(time.time()).tm_year
        print("The year you will turn %s years old: %s " % (self.turn, year))


info = Info()
info.turn_yrs()

