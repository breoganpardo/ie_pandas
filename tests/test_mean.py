# Test mean
import numpy as np
import ie_pandas as ie
import pytest


@pytest.mark.parametrize(
    "input, expected_out",
    [
        (
            ie.DataFrame(
                np.array([[1, 2, 3], [7, 3, 6], [7, 7, 9]]),
                ["c1", "c2", "c3"],
                ["r1", "r2", "r3"],
            ),
            [5, 4, 6],
        ),
        (
            ie.DataFrame(
                {
                    "c1": np.array(["a", "b", "c"]),
                    "c2": np.array([1, 3, 5]),
                    "c3": np.array([2, 7, 9]),
                }
            ),
            [3, 6],
        ),
        (ie.DataFrame({"c1": [1, 2, 3], "c2": [6, 3, 6], "c3": [7, 7, 1]}), [2, 5, 5]),
        (
            ie.DataFrame(
                {
                    "c1": np.array(["a", 1, 2]),
                    "c2": np.array([1, 3, 5]),
                    "c3": np.array([2, 7, 9]),
                }
            ),
            [3, 6],
        ),
        (ie.DataFrame([[1, 2, 3], [7, 3, 6], [7, 7, 9]]), [5, 4, 6]),
        (
            ie.DataFrame({"c1": [1.0, 2, 3], "c2": [6, 3.0, 6], "c3": [7, 7.0, 1]}),
            [2, 5, 5],
        ),
    ],
)
def test_mean(input, expected_out):

    output = input.mean()
    assert output == expected_out
