# test whether creating a DataFrame works.
from ie_pandas import DataFrame
import numpy as np
def test_get():
	pet0="cat"
	age0=1
	weight0=1.0
	sick0=True

	dictionary = {
    		"pet": np.array(["cat", "dog", "mouse"]),
    		"age": np.array([1, 2, 3]),
    		"weight": np.array([1.0, 2.0, 3.0]),
		"sick": np.array([True, True, False]),
		}

	df=DataFrame(dictionary)

	assert df["pet"][0]==pet0
	assert df["age"][0]==age0
	assert df["weight"][0]==weight0
	assert df["sick"][0]==sick0


