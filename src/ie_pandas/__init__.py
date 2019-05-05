import numpy as np
import statistics
import matplotlib.pyplot as plt


class DataFrame:
    def __init__(self, dictionary):
        len_check = []
        for k in dictionary:
            len_check.append(len(dictionary[k]))
        if len(set(len_check)) == 1:
            self._col_names = dictionary.keys()
            self._col_values = dictionary.values()
            self._items = dictionary
        else:
            raise Exception(
                "sorry, the number of dimensions in each column does not match"
            )

    def __setitem__(self, key, new_value):
        temp_dictionary = self._items
        temp_dictionary[key] = new_value
        len_check = []
        for k in temp_dictionary:
            len_check.append(len(temp_dictionary[k]))
        if len(set(len_check)) == 1:
            self._items[key] = new_value
        else:
            raise Exception(
                "sorry, the number of dimensions in each column does not match"
            )

    def __getitem__(self, key):
        getitem = [self._items[k] for k in key if k in self._items]
        rows = len(getitem[0])
        cols = len(getitem)
        text = []
        for j in range(rows):
            for i in range(cols):
                text.append(getitem[i][j])
        final_text = []
        for i in range(0, cols * rows, cols):
            final_text.append(text[slice(i, i + cols)])
        table = plt.table(
            cellText=final_text, colLabels=key, colColours=["c"] * cols, loc="center"
        )
        table.set_fontsize(14)
        table.scale(1.5, 1.5)
        plt.axis("off")
        return getitem

    def get_row(self, index):
        get_row = []
        columns = []
        for i in index:
            for key in self._items:
                columns.append(key)
                get_row.append(self._items[key][i])
        size = len(self._items)
        if len(get_row) == size:
            table = plt.table(
                cellText=[get_row],
                colLabels=columns,
                colColours=["c"] * len(columns),
                loc="center",
            )
            table.set_fontsize(14)
            table.scale(1.5, 1.5)
            plt.axis("off")
            return get_row
        else:
            sub_row = []
            while len(get_row) > size:
                row = get_row[:size]
                sub_row.append(row)
                get_row = get_row[size:]
            sub_row.append(get_row)
            table = plt.table(
                cellText=sub_row,
                colLabels=columns,
                colColours=["c"] * len(columns),
                loc="center",
            )
            table.set_fontsize(14)
            table.scale(1.5, 1.5)
            plt.axis("off")
            return sub_row

    def col_names(self):
        return list(self._col_names)

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
        table = plt.table(
            cellText=[sum_collector],
            colLabels=columns,
            colColours=["c"] * len(columns),
            loc="center",
        )
        table.set_fontsize(14)
        table.scale(1.5, 1.5)
        plt.axis("off")
        return sum_collector

    def median(self):
        med_collector = []
        columns = []
        for key in self._items:
            if self._items[key].dtype == "float64" or self._items[key].dtype == "int32":
                columns.append(key)
                med_collector.append(statistics.median(self._items[key]))
        table = plt.table(
            cellText=[med_collector],
            colLabels=columns,
            colColours=["c"] * len(columns),
            loc="center",
        )
        table.set_fontsize(14)
        table.scale(1.5, 1.5)
        plt.axis("off")
        return med_collector

    def min(self):
        min_collector = []
        columns = []
        for key in self._items:
            if self._items[key].dtype == "float64" or self._items[key].dtype == "int32":
                columns.append(key)
                min_collector.append(min(self._items[key]))
        table = plt.table(
            cellText=[min_collector],
            colLabels=columns,
            colColours=["c"] * len(columns),
            loc="center",
        )
        table.set_fontsize(14)
        table.scale(1.5, 1.5)
        plt.axis("off")
        return min_collector

    def max(self):
        max_collector = []
        columns = []
        for key in self._items:
            if self._items[key].dtype == "float64" or self._items[key].dtype == "int32":
                columns.append(key)
                max_collector.append(max(self._items[key]))
        table = plt.table(
            cellText=[max_collector],
            colLabels=columns,
            colColours=["c"] * len(columns),
            loc="center",
        )
        table.set_fontsize(14)
        table.scale(1.5, 1.5)
        plt.axis("off")
        return max_collector

    def __repr__(self):
        table = plt.table(
            cellText=np.array(list(self._col_values)).transpose(),
            colLabels=list(self._col_names),
            colColours=["c"] * len(self._items),
            loc="center",
        )
        table.set_fontsize(14)
        table.scale(1.5, 1.5)
        plt.axis("off")
        return f"{self._items}"
