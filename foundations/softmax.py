import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        L=[]
        softmax = 0
        x = np.max(z)
        sum = 0
        for k in z:
            sum = sum + np.exp(k-x)
        for i in z:
            softmax = np.exp(i-x)/sum
            L.append(softmax)
        return np.round(L,4)
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        pass
