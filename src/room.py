# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):

        p = f"Room Name:   {self.name}\n"
        return p

    def __repr__(self):
        return f"Name({repr(self.name)})"