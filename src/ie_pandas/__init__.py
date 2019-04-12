class DataFrame:
    def __init__(self, dictionary): #intializing the class
            self._col_names = dictionary.keys() 
            self._col_values = dictionary.values()
            self._items = dictionary
    def __setitem__(self, key, new_value):
        self._items[key] = new_value

    def __getitem__(self, key):
        return np.array(self._items[key])


