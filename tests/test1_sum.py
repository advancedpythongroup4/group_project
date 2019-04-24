# importing necessary packages numpy and statistics
import numpy as np
import statistics

# import the created dataframe class
from ie_pandas import DataFrame

# simple test to get the column values
def test1_sum():

    dictionary = {
        "pet": np.array(["cat", "dog", "mouse"]),
        "age": np.array([1, 2, 3]),
        "weight": np.array([1.0, 2.0, 3.0]),
        "sick": np.array([True, True, False]),
    }

    df = DataFrame(dictionary)
    sum_collector = []
    columns = []
    for key in dictionary:
        columns.append(key)
        sum_collector.append(sum(dictionary[key]))
    print(columns)
    return sum_collector

    expected_output = sum_collector[]  

    output = df.sum

    assert output == expected_output
