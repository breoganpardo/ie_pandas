import logging
import numpy as np


class DataFrame:
    def __init__(self, data, cols=None, index=None):

        if isinstance(data, np.ndarray) and data.dtype.type is np.str_:
            logging.warning(
                'All values in the dataframe are strings, if you wish to avoid this add dtype="object" inside the numpy array'
            )
        elif isinstance(data, list):
            data = np.array(data, dtype=object)
        elif isinstance(data, dict):
            cols = list(data.keys())
            matrix = []

            for ind in range(len(data[cols[0]])):
                row = [data[col][ind] for col in cols]
                matrix.append(row)

            data = np.array(matrix, dtype=object)

        if cols is None:
            cols = [str(col) for col in list(range(len(data[0])))]

        if index is None:
            index = list(range(len(data)))

        self.cols = cols
        self.index = index
        self.data = data

    def __getitem__(self, items):
        if isinstance(items, list):
            cols = [self.cols.index(item) for item in items]
            return self.data[:, cols]
        elif isinstance(items, str):
            cols = self.cols.index(items)
            return self.data[:, cols]

        return self.data[items]

    def formatted_frame(self):
        string = "\t" + "\t".join(map(str, self.cols)) + "\n"

        for ind, row in enumerate(self.data):
            string += str(self.index[ind]) + " |\t" + "\t".join(map(str, row)) + "\n"

        return string

    def __str__(self):
        return self.formatted_frame()

    def __repr__(self):
        return self.formatted_frame()

    def get_row(self, row):
        if isinstance(row, str):
            row = self.index.index(row)
        return self.data[row].tolist()

    def __setitem__(self, index, value):
        self.data[index] = value

    def num_cols(self):
        lst = []
        for i in range(len(self[1])):
            for j in self[:, i]:
                try:
                    float(j)
                    lst.append(i)
                except:
                    pass

        lst_indices = []
        for i in lst:
            if lst.count(i) == len(self[:, 1]):
                lst_indices.append(i)
        lst_indices = list(set(lst_indices))

        self_float = self[:, lst_indices].astype("float64")

        return self_float

    def min(self):

        self_float = self.num_cols()

        mins = []
        for i in range(len(self_float[1])):
            mins.append(self_float[:, i].min())

        mins = [int(i) if i == int(i) else float(i) for i in mins]

        return mins

    def max(self):

        self_float = self.num_cols()

        maxs = []
        for i in range(len(self_float[1])):
            maxs.append(self_float[:, i].max())

        maxs = [int(i) if i == int(i) else float(i) for i in maxs]

        return maxs

    def mean(self):

        self_float = self.num_cols()

        mean_lst = []
        for i in range(len(self_float[1])):
            mean_lst.append(self_float[:, i].mean())

        mean_lst = [int(i) if i == int(i) else float(i) for i in mean_lst]

        return mean_lst

    def median_from_list(self, lst):
        sortedLst = sorted(lst)
        lstLen = len(lst)
        index = (lstLen - 1) // 2

        if lstLen % 2:
            return sortedLst[index]
        else:
            return (sortedLst[index] + sortedLst[index + 1]) / 2.0

    def median(self):

        self_float = self.num_cols()

        median_lst = []
        for i in range(len(self_float[1])):
            median_lst.append(self.median_from_list(self_float[:, i]))

        median_lst = [int(i) if i == int(i) else float(i) for i in median_lst]

        return median_lst

    def sum(self):

        self_float = self.num_cols()

        summed = []
        for i in range(len(self_float[1])):
            summed.append(self_float[:, i].sum())

        summed = [int(i) if i == int(i) else float(i) for i in summed]

        return summed
