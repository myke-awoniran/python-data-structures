class HashTable:
    def __init__(self, size=7):
        # self.size = size
        self.data_map = size * [None]

    def __hash(self, key):
        my_hash = 0

        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    # def set(self, key, value):


new_hash_table = HashTable()
