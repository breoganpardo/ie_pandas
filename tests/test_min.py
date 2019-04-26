import numpy as np
import ie_pandas as ie
import pytest


@pytest.mark.parametrize(
    "funct_input,expected",
    [
        (ie.DataFrame([[1, 2, 6], [3, 4, 9], [1, 4, 10], [7, 3, 4]]), [1, 2, 4]),
        (ie.DataFrame([[1, 2, 6], [3.0, 4, 9], [1, 4, 10.0], [7, 3, 4]]), [1, 2, 4]),
        (ie.DataFrame([[1, 2, 6], ["ABC", 4, 9], [1, 4, 10], [7, 3, 4]]), [2, 4]),
    ],
)
def test_min(funct_input, expected):
    funct_output = funct_input.min()
    assert expected == funct_output
