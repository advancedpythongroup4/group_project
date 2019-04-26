# Test Set
import numpy as np
from ie_pandas import DataFrame
def test_set():
    dictionary = {
        "pet": np.array(["cat", "dog", "mouse"]),
        "age": np.array([1, 2, 3]),
        "weight": np.array([1.0, 2.0, 3.0]),
        "sick": np.array([True, True, False]),
    }
    df=DataFrame(dictionary)
    
    df["pet"] = np.array(["frog", "lizard", "turtle"])


    pet0="frog"
    pet1="lizard"
    pet2="turtle"

    assert df[["pet"]][0][0]==pet0
    assert df[["pet"]][0][1]==pet1
    assert df[["pet"]][0][2]==pet2


