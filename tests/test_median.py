# Test median
import numpy as np
import ie_pandas as ie
import pytest


@pytest.mark.parametrize(
    "input, expected_out",
    [
        (
            ie.DataFrame(
                np.array([[1, 2, 3], [2, 3, 6], [3, 7, 9]]),
                ["c1", "c2", "c3"],
                ["r1", "r2", "r3"],
            ),
            [2, 3, 6],
        ),
        (
            ie.DataFrame(
                {
                    "c1": np.array(["a", "b", "c"]),
                    "c2": np.array([1, 3, 5]),
                    "c3": np.array([2, 7, 9]),
                }
            ),
            [3, 7],
        ),
        (
            ie.DataFrame(
                {
                    "c1": np.array(["a", 1, 2]),
                    "c2": np.array([1, 3, 5]),
                    "c3": np.array([2, 7, 9]),
                }
            ),
            [3, 7],
        ),
    ],
)
def test_median(input, expected_out):

    output = input.median()
    assert output == expected_out
