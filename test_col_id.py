# Test cols_id
import numpy as np
import ie_pandas as ie
import pytest


def test_cols_id():
    matrix = np.array([[1, 2, 3], [7, 3, 6], [7, 7, 9]])
    df = ie.DataFrame(matrix)

    output = df[:, 1]
    expected_out = np.array([2, 3, 7])

    assert (output == expected_out).all()
