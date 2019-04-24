# importing necessary packages numpy and statistics
import numpy as np
import statistics

# import the created dataframe class
from ie_pandas import DataFrame

# simple test to get the median of the values
def test_median1():

    dictionary = {
        "pet": np.array(["cat", "dog", "mouse"]),
        "age": np.array([1, 2, 3]),
        "weight": np.array([1.0, 2.0, 3.0]),
        "sick": np.array([True, True, False]),
    }

    df = DataFrame(dictionary)
    median_collector = []
    columns = []
    for key in dictionary:
        columns.append(key)
        median_collector.append(statistics.median(dictionary[key]))

    expected_output = median_collector

    output = df.median

    assert output == expected_output
