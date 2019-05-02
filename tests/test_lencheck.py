#test_lencheck
from ie_pandas import DataFrame
import numpy as np
def test_lencheck():	
	dictionary = {
	"pet": np.array(["cat", "dog", "mouse","mouse"]),
	"age": np.array([1, 2, 3]),
	"weight": np.array([1.9000000000000000009, 2.0, 3.0]),
	"sick": np.array([True, True, False]),
	}
	df = DataFrame(dictionary)
