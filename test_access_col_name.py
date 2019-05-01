# Test Access_Col_Name
import numpy as np
import ie_pandas as ie
import pytest


def test_access_col_name_dict():
    dictionary1 = {
        "c1": np.array(["a", "b", "c"]),
        "c2": np.array([1, 3, 5]),
        "c3": np.array([2, 7, 9]),
    }
    df1 = ie.DataFrame(dictionary1)

    output1 = df1["c1"]
    expected_out1 = np.array(["a", "b", "c"])

    assert (output1 == expected_out1).all()


def test_access_col_name_list():
    df2 = ie.DataFrame([[1, 2, 3], [7, 3, 6], [7, 7, 9]])

    output2 = df2["0"]
    expected_out2 = np.array([1, 7, 7])
    assert (output2 == expected_out2).all()
