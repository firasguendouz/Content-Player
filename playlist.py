'''
Handles the management of the playlist.
'''
class Playlist:
    def __init__(self):
        self.items = []
    def add_item(self, item, duration):
        self.items.append((item, duration))
    def remove_item(self, index):
        del self.items[index]
    def rearrange_items(self, old_index, new_index):
        item = self.items.pop(old_index)
        self.items.insert(new_index, item)
    def get_items(self):
        return self.items