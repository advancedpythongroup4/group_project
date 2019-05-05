# test_col_names
from ie_pandas import DataFrame
import numpy as np


def test_col_names():
    dictionary = {
        "pet": np.array(["cat", "dog", "mouse"]),
        "age": np.array([1, 2, 3]),
        "weight": np.array([1.0, 2.0, 3.0]),
        "sick": np.array([True, True, False]),
    }
    df = DataFrame(dictionary)
    df.col_names
