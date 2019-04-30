# Test for dataframe taking the correct row indexes

from ie_pandas import DataFrame
import numpy as np
import pytest


@pytest.mark.parametrize(
    "data,given_index,expected_index",
    [
        ({"c0": [1], "c1": [7], "c2": [2], "c3": [5]}, ["row1"], ["row1"]),
        ({"c0": [1], "c1": [7], "c2": [2], "c3": [5]}, None, list(range(1))),
        (
            {"Col1": [2, 3, 5], "Col2": [5, 6, 8], "Col3": [10, 45, 7]},
            ["r1", "&", "r3"],
            ["r1", "&", "r3"],
        ),
        (
            {"Col1": [2, 3, 5], "Col2": [5, 6, 8], "Col3": [10, 45, 7]},
            None,
            list(range(3)),
        ),
    ],
)
def test_correct_row_index_names(data, given_index, expected_index):
    df = DataFrame(data, index=given_index)

    row_index = df.index
    assert expected_index == row_index
