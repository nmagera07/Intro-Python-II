# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):

        p = f"Player Name:   {self.name}\n"
        return p

    def __repr__(self):
        return f"Name({repr(self.name)})"



p = Player("Argon", "outside")

x = input("Enter player name: ")
if x == 'nate':
    print('cool')
elif x == 'cassie':
    print('you suck')
else:
    print(f"\nYour name is: {x}")
