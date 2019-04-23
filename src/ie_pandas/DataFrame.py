import numpy as np


class DataFrame:
    def __init__(self, data, cols=None, index=None):

        if isinstance(data, list):
            data = np.array(data)

        if isinstance(data, dict):
            cols = list(data.keys())
            matrix = []

            for ind in range(len(data[cols[0]])):
                row = [data[col][ind] for col in cols]
                matrix.append(row)

            data = np.array(matrix)

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

    def min(self):
        mins = []
        for i in self.cols:
            try:
                mins.append(self.__getitem__(i).astype(np.number).min())
            except:
                pass

        return mins
