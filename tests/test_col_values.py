# importing necessary packages numpy and statistics
import numpy as np
import statistics

# import the created dataframe class
from ie_pandas import DataFrame

# simple test to get the column values
def test_get_col_values():

    dictionary = {
        "pet": np.array(["cat", "dog", "mouse"]),
        "age": np.array([1, 2, 3]),
        "weight": np.array([1.0, 2.0, 3.0]),
        "sick": np.array([True, True, False]),
    }

    df = DataFrame(dictionary)

    expected_output = dictionary.values()  

    output = df.col_values

    assert output == expected_output
