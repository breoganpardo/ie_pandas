from ie_pandas import DataFrame
import numpy as np
import pytest


# Test for dataframe taking the correct column names
@pytest.mark.parametrize(
    "dictionary,expected_names",
    [
        ({"c0": [1], "c1": [7], "c2": [2], "c3": [5]}, ["c0", "c1", "c2", "c3"]),
        (
            {"Col1": [2, 3, 5], "Col2": [5, 6, 8], "Col3": [10, 45, 7]},
            ["Col1", "Col2", "Col3"],
        ),
    ],
)
def test_correct_column_names_from_dictionary(dictionary, expected_names):
    df = DataFrame(dictionary)

    column_names = df.cols

    assert expected_names == column_names


@pytest.mark.parametrize(
    "data,given_names,expected_names",
    [
        (
            [[1, 3, 4, 7], [7, 2, 8, 65], [2, 3, 21, 54], [5, 7, 3, 1]],
            None,
            ["0", "1", "2", "3"],
        ),
        ([[2, 5, 9], [5, 13, 23], [5, 2, 9]], ["c0", "c1", "c2"], ["c0", "c1", "c2"]),
    ],
)
def test_correct_column_names_from_list(data, given_names, expected_names):
    df = DataFrame(data, cols=given_names)

    column_names = df.cols

    assert expected_names == column_names
