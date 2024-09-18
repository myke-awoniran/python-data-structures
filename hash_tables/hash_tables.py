class HashTable:
    def __init__(self, size=7):
        # self.size = size
        self.data_map = size * [None]

    def __hash(self, key):
        my_hash = 0

        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

    # common interview questions
    ## if two items contain same thing

    def items_in_common(self, list1, list2):
        dict={}
        for i in list1:
            dict[i]=True
        for i in list2:
            if i in dict:
                return True
        return False



new_hash_table = HashTable()
new_hash_table.set_item('bolts', 50)
new_hash_table.set_item('washers', 1500)

print(new_hash_table.get_item('bolts'))
print(new_hash_table.get_item('washers'))
print(new_hash_table.get_item('michael'))
print(new_hash_table.keys())
print(new_hash_table.items_in_common([1,2,3,4,5], [6,7,8]))
