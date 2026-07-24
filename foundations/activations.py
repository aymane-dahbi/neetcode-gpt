import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        calc =1 / (1 + np.exp(-z))
        return np.round(calc, 5)
        pass

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        L=[]
        for k in z:
            if k >= 0:
                L.append(k)
            else:
                L.append(0)
        return np.round(L,5)

