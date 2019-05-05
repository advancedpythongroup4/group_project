import numpy as np
import statistics

# import the created dataframe class
from ie_pandas import DataFrame


# simple test to get the maximum value
def test_max():

    dictionary = {
        "pet": np.array(["cat", "dog", "mouse"]),
        "age": np.array([1, 2, 3]),
        "weight": np.array([1.0, 2.0, 3.0]),
        "sick": np.array([True, True, False]),
    }

    df = DataFrame(dictionary)
    max_collector = []
    columns = []
    for key in dictionary:
        if dictionary[key].dtype == "float64" or 
            dictionary[key].dtype == "int32":
            columns.append(key)
            max_collector.append(max(dictionary[key]))

    expected_output = max_collector

    output = df.max()

    assert output == expected_output
