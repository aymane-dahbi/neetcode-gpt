import numpy as np
from numpy.typing import NDArray

class Solution:

    def get_model_prediction(self, X: NDArray[np.float64], weights: NDArray[np.float64]) -> NDArray[np.float64]:
        return np.round(np.dot(X,weights),5)
        # X is (n, m), weights is (m,) -> return (n,) predictions
        # Round to 5 decimal places
        pass

    def get_error(self, model_prediction: NDArray[np.float64], ground_truth: NDArray[np.float64]) -> float:
        # Compute mean squared error between predictions and ground truth
        # Round to 5 decimal places
        sum = 0
        for k in range(len(model_prediction)):
            sum = sum + (model_prediction[k]-ground_truth[k])**2
        return np.round(sum[0]/len(model_prediction),5)
        pass
