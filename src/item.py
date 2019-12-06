class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    # def on_take(self):
    #     print(f"you have picked up the {self.name}")

    # def on_drop(self):
    #     print(f"you have dropped the {self.name}")

    # def on_look(self):
    #     return f'Item: {self.name}, Description: {self.description}'

    def __str__(self):
        return f"'{self.name}', {self.description}"
