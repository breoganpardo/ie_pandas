import logging
import numpy as np
import matplotlib.pyplot as plt


class DataFrame:
    def __init__(self, data, cols=None, index=None):
        """Dataframe class takes an input of types: list of lists, numpy arrays, a dictionary of lists, and a dictionary of numpy arrays and returns a dataframe with the specified input. The class method also works with an optional argument of column names and row names as list."""
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
        """Used to map the specified index to the corresponding values within the dataframe"""
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
        """Used as a representation for the class object"""
        return self.formatted_frame()

    def __repr__(self):
        """Used as a representation of the class object"""
        return self.formatted_frame()

    def get_row(self, row):
        """Returns selected row from a dataframe by specifying row index"""
        if isinstance(row, str):
            row = self.index.index(row)
        return self.data[row].tolist()

    def __setitem__(self, index, value):
        """Used to alter/update the values in the specified index to new values"""
        self.data[index] = value

    def num_cols(self):
        """Returns the numeric columns in a dataframe as an array of lists"""
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
        """Returns a list of the minimum values for each of the numeric columns in a dataframe"""
        self_float = self.num_cols()

        mins = []
        for i in range(len(self_float[1])):
            mins.append(self_float[:, i].min())

        mins = [int(i) if i == int(i) else float(i) for i in mins]

        return mins

    def max(self):
        """Returns a list of the maximum values for each of the numeric columns in a dataframe"""
        self_float = self.num_cols()

        maxs = []
        for i in range(len(self_float[1])):
            maxs.append(self_float[:, i].max())

        maxs = [int(i) if i == int(i) else float(i) for i in maxs]

        return maxs

    def mean(self):
        """Returns a list of column means for all numeric columns in a dataframe"""

        self_float = self.num_cols()

        mean_lst = []
        for i in range(len(self_float[1])):
            mean_lst.append(self_float[:, i].mean())

        mean_lst = [int(i) if i == int(i) else float(i) for i in mean_lst]

        return mean_lst

    def median_from_list(self, lst):
        """Returns the median of a sorted list/column taking into consideration whether the column has an even or odd number of values"""
        sortedLst = sorted(lst)
        lstLen = len(lst)
        index = (lstLen - 1) // 2

        if lstLen % 2:
            return sortedLst[index]
        else:
            return (sortedLst[index] + sortedLst[index + 1]) / 2.0

    def median(self):
        """Returns a list of column medians for all numeric columns in a dataframe. The function appends median items computed from the median_from_list function and forms a list of medians"""

        self_float = self.num_cols()

        median_lst = []
        for i in range(len(self_float[1])):
            median_lst.append(self.median_from_list(self_float[:, i]))

        median_lst = [int(i) if i == int(i) else float(i) for i in median_lst]

        return median_lst

    def sum(self):
        """Returns a list of column summation for all numeric columns in a dataframe"""

        self_float = self.num_cols()

        summed = []
        for i in range(len(self_float[1])):
            summed.append(self_float[:, i].sum())

        summed = [int(i) if i == int(i) else float(i) for i in summed]

        return summed

    def visualize(self, col1, col2):
        """To return a plot, graphically showing relationship between 2 numerical columns."""
        lst = list(np.concatenate((col1, col2)))
        for i in lst:
            try:
                float(i)
            except:
                return print('Please enter numerical columns only.')
                
                
        plt.plot(col1, col2)
        plt.plot(col1, col2, 'o')
        plt.show()