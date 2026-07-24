class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        def fpri(x):
            return 2*x
        x = init
        for k in range(iterations):
            x = x - learning_rate*fpri(x)
        return round(x,5)
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        pass
