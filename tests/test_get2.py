
# test_get2
from ie_pandas import DataFrame
import numpy as np

# Define test to get more than one item
def test_get2():
	pet1 = "dog"
	age1 = 2

	dictionary = {
    		"pet": np.array(["cat", "dog", "mouse"]),
    		"age": np.array([1, 2, 3]),
    		"weight": np.array([1.0, 2.0, 3.0]),
		"sick": np.array([True, True, False]),
		}

	df=DataFrame(dictionary)

	assert df["Pet","age"][0][1] == pet1
	assert df["Pet","age"][1][1] == age1
