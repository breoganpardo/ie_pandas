from ie_pandas import DataFrame
import pytest
import numpy as np

#Test for sum() method
@pytest.mark.parametrize('data,expected_result1,expected_result2,expected_result3',[
        ({'c0': [1, 3, 5], 'c1': [7, 6, 2], 'c2': [2, -4, 7], 'c3': [5, 3, 9]} ,[9,15,5,17],[15,5,17],[8,3,12]),
        ({'c0': [1, 3, 5], 'c1': [7, 'b', 2], 'c2': [2, 4, 7], 'c3': [5, 'c', 9]},[9,13],[13],[11]),
        ({'c0': [1, 3, 5], 'c1': [7, True, 2], 'c2': [2, 4, 7], 'c3': [5, 'c', 9]},[9,10,13],[10,13],[3,11]),
        ({'c0': np.array([1, 3, 5]), 'c1': np.array([7, 6, 2]), 'c2': np.array([2, -4, 7]), 'c3': np.array([5, 3, 9])} ,[9,15,5,17],[15,5,17],[8,3,12]),
        ({'c0': np.array([1, 3, 5]), 'c1': np.array([7, 'b', 2]), 'c2': np.array([2, 4, 7]), 'c3': np.array([5, 'c', 9])} ,[9,13],[13],[11]),
        ({'c0': np.array([1, 3, 5]), 'c1': np.array([7, True, 2]), 'c2': np.array([2, 4, 7]), 'c3': np.array([5, 'c', 9])} ,[9,10,13],[10,13],[3,11]),
        ([[1,2,3,1], [4,5,6,1], [7,8,9,1]] ,[12,15,18,3],[15,18,3],[13,15,2])
        ])

def test_for_sum_method (data, expected_result1,expected_result2,expected_result3):
    input_DF= DataFrame(data)
    
    result1=input_DF.sum()
    result2=input_DF[:,1:4].sum()
    result3=input_DF[1:3,1:4].sum()
    
    assert expected_result1==result1
    assert expected_result2==result2
    assert expected_result3==result3
