# Test editing DF
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
            2,
        ),
        (
            ie.DataFrame(
                {
                    "c1": np.array(["a", "b", "c"]),
                    "c2": np.array([1, 3, 5]),
                    "c3": np.array([2, 7, 9]),
                }
            ),
            2,
        ),
        (
            ie.DataFrame(
                {
                    "c1": np.array(["a", 1, 2]),
                    "c2": np.array([1, 3, 5]),
                    "c3": np.array([2, 7, 9]),
                }
            ),
            2,
        ),
    ],
)
def test_edit_df(input, expected_out):
    df = input
    df[0, 1] = 2

    output = input[0, 1]

    assert output == expected_out