import numpy as np
import statistics

# import the created dataframe class
from ie_pandas import DataFrame


# simple test to get the minimum value
def test_min():

    dictionary = {
        "pet": np.array(["cat", "dog", "mouse"]),
        "age": np.array([1, 2, 3]),
        "weight": np.array([1.0, 2.0, 3.0]),
        "sick": np.array([True, True, False]),
    }

    df = DataFrame(dictionary)
    min_collector = []
    columns = []
    for key in dictionary:
        if dictionary[key].dtype == "float64" or 
            dictionary[key].dtype == "int32":
            columns.append(key)
            min_collector.append(min(dictionary[key]))

    expected_output = min_collector

    output = df.min()

    assert output == expected_output
