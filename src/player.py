# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_location):
        self.name = name
        self.current_location = current_location
        self.items = []

    def __str__(self):
        return f"My Name is '{self.name}', I am currently located  {self.current_location}"

    def collect_item(self, item):
        self.items.append(item)
        print(self.current_location.item)
        # print(f"you place the {chosen_item} in your bag")

    def drop_item(self, item):
        self.items.remove(item)
