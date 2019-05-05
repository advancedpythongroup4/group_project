# importing necessary packages numpy and statistics
import numpy as np
import statistics

# import the created dataframe class
from ie_pandas import DataFrame

# simple test to get the number of rows
def test_get_number_of_rows():

    dictionary = {
        "pet": np.array(["cat", "dog", "mouse"]),
        "age": np.array([1, 2, 3]),
        "weight": np.array([1.0, 2.0, 3.0]),
        "sick": np.array([True, True, False]),
    }

    df = DataFrame(dictionary)

    expected_output = len(list(dictionary.keys())[0])

    output = df.nrows()

    assert output == expected_output
