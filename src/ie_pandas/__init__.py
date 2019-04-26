import numpy as np
import statistics

class DataFrame:
	def __init__(self, dictionary): #intializing the class
		self._col_names = dictionary.keys()
		self._col_values = dictionary.values()
		self._items = dictionary

	def __setitem__(self, key, new_value):
		self._items[key] = new_value

	def __getitem__(self, key):
		return np.array(self._items[key])

	def get_row(self, index):
		get_row = []
		columns = []
		for key in self._items:
			columns.append(key)
			get_row.append(self._items[key][index])
			print(columns)
		return get_row

	def ncols(self):
		return len(self._items)

	def nrows(self):
		len_check = []
		for key in self._items:
			len_check.append(len(self._items[key]))
		return len_check[0]

	def sum(self):
		sum_collector = []
		columns = []
		for key in self._items:
			if self._items[key].dtype == "float64" or self._items[key].dtype == "int32":
				columns.append(key)
				sum_collector.append(sum(self._items[key]))
		print(columns)
		return sum_collector

	def median(self):
		med_collector = []
		columns = []
		for key in self._items:
			if self._items[key].dtype == "float64" or self._items[key].dtype == "int32":
				columns.append(key)
				med_collector.append(statistics.median(self._items[key]))
		print(columns)
		return med_collector

	def min(self):
		min_collector = []
		columns = []
		for key in self._items:
			if self._items[key].dtype == "float64" or self._items[key].dtype == "int32":
				columns.append(key)
				min_collector.append(min(self._items[key]))
		print(columns)
		return min_collector

	def max(self):
		max_collector = []
		columns = []
		for key in self._items:
			if self._items[key].dtype == "float64" or self._items[key].dtype == "int32":
				columns.append(key)
				max_collector.append(max(self._items[key]))
		print(columns)
		return max_collector
