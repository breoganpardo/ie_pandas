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
def test_index(input, expected_out):

    output = input.index
    assert output == expected_out
