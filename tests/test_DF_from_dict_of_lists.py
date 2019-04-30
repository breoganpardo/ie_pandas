# Create df from a dict of lists
from ie_pandas import DataFrame
import numpy as np
import pytest


@pytest.mark.parametrize(
    "data,expected_df",
    [
        ({"c0": [1, 3, 5], "c1": [7, 6, 2], "c2": [2, -4, 7], "c3": [5, 3, 9]},np.array([[1, 7, 2, 5], [3, 6, -4, 3], [5, 2, 7, 9]])),
        
    ])

def test_create_DF_from_dict_of_list(data, expected_df):
    df = DataFrame(data)

    assert (df.data == expected_df).all()


@pytest.mark.parametrize(
    "data,expected_df",
    [
        ({"c0": np.array([1, 3, 5]), "c1": np.array([7, 6, 2]), "c2": np.array([2, -4, 7]), "c3": np.array([5, 3, 9])},np.array([[1, 7, 2, 5], [3, 6, -4, 3], [5, 2, 7, 9]]))
        
    ])
    

def test_create_DF_from_dict_of_nparray(data, expected_df):
    df = DataFrame(data)

    assert (df.data == expected_df).all()
 
       

  
@pytest.mark.parametrize(
    "data,expected_df",
    [
        (np.array([[1, 3, 5],[7, 6, 2],[2, -4, 7],[5, 3, 9]]),
         np.array([[1, 3, 5],[7, 6, 2],[2, -4, 7],[5, 3, 9]])
         )
        
    ])
    

def test_create_DF_from_nparray(data, expected_df):
    df = DataFrame(data)

    assert (df.data == expected_df).all()