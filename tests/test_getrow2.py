# test_getrow2
from ie_pandas import DataFrame
import numpy as np

# define test to get more than one row
def test_getrow():

    dictionary = {
        "pet": np.array(["cat", "dog", "mouse"]),
        "age": np.array([1, 2, 3]),
        "weight": np.array([1.0, 2.0, 3.0]),
        "sick": np.array([True, True, False]),
    }

    row0 = ["cat", 1, 1.0, True]
    row1 = ["dog", 2, 2.0, True]

    df = DataFrame(dictionary)

    assert df.get_row([0, 1])[0] == row0
    assert df.get_row([0, 1])[1] == row1
