#test_getrow
from ie_pandas import DataFrame
import numpy as np



def test_getrow():
    dictionary = {
    "pet": np.array(["cat", "dog", "mouse"]),
    "age": np.array([1, 2, 3]),
    "weight": np.array([1.0, 2.0, 3.0]),
    "sick": np.array([True, True, False]),
    }
    df=DataFrame(dictionary)

    pet0="cat"
    age0=1
    weight0=1.0
    sick0=True

    assert df.get_row(0)[0]==pet0
    assert df.get_row(0)[1]==age0
    assert df.get_row(0)[2]==weight0
    assert df.get_row(0)[3]==sick0
