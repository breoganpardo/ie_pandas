import numpy as np
import ie_pandas as ie
import pytest


@pytest.mark.parametrize(
    "funct_input,expected",
    [
        (ie.DataFrame([[1, 2, 6], [3, 4, 9], [1, 4, 10], [7, 3, 4]]), [7, 4, 10]),
        (ie.DataFrame([[1, 2, 6], [3.0, 4, 9], [1, 4, 10.0], [7, 3, 4]]), [7, 4, 10.0]),
        (ie.DataFrame([[1, 2, 6], ["ABC", 4, 9], [1, 4, 10], [7, 3, 4]]), [4, 10]),
    ],
)
def test_max(funct_input, expected):
    funct_output = funct_input.max()
    assert expected == funct_output
