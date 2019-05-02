# Test index
import numpy as np
import ie_pandas as ie
import pytest


@pytest.mark.parametrize(
    "input, expected_out",
    [
        (ie.DataFrame(np.array([[1, 2, 3], [7, 3, 6], [7, 7, 9]])), [0, 1, 2]),
        (
            ie.DataFrame(
                {
                    "c1": np.array(["a", "b", "c"]),
                    "c2": np.array([1, 3, 5]),
                    "c3": np.array([2, 7, 9]),
                }
            ),
            [0, 1, 2],
        ),
    ],
)
def test_index_created_when_not_specified(input, expected_out):

    output = input.index
    assert output == expected_out


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
    df = ie.DataFrame(data, index=given_index)

    row_index = df.index
    assert expected_index == row_index


@pytest.mark.parametrize(
    "input, expected_out",
    [
        (ie.DataFrame(np.array([[1, 2, 3], [7, 3, 6], [7, 7, 9]])), [7, 3, 6]),
        (
            ie.DataFrame(
                {
                    "c1": np.array(["a", "b", "c"]),
                    "c2": np.array([1, 3, 5]),
                    "c3": np.array([2, 7, 9]),
                }
            ),
            ["b", 3, 7],
        ),
    ],
)
def test_get_row_works_by_position(input, expected_out):

    output = input.get_row(1)
    assert output == expected_out


@pytest.mark.parametrize(
    "input, expected_out",
    [
        (
            ie.DataFrame(
                np.array([[1, 2, 3], [7, 3, 6], [7, 7, 9]]), index=["r1", "r2", "r3"]
            ),
            [7, 3, 6],
        ),
        (
            ie.DataFrame(
                {
                    "c1": np.array(["a", "b", "c"]),
                    "c2": np.array([1, 3, 5]),
                    "c3": np.array([2, 7, 9]),
                },
                index=["r1", "r2", "r3"],
            ),
            ["b", 3, 7],
        ),
    ],
)
def test_get_row_works_by_row_name(input, expected_out):

    output = input.get_row("r2")
    assert output == expected_out
