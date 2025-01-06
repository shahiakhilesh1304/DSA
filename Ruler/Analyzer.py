import math
import numpy as np
from sklearn.metrics import mean_squared_error
import time
from functools import wraps
import inspect



class BigOCalculator:
    def __init__(self):
        self.results = {}

    @staticmethod
    def calculate(input_sizes, times):
        complexities = {
            "O(1)": lambda n: [1 for _ in n],
            "O(log n)": lambda n: [math.log2(i) if i > 0 else 0 for i in n],
            "O(n)": lambda n: [i for i in n],
            "O(n log n)": lambda n: [i * math.log2(i) if i > 0 else 0 for i in n],
            "O(n^2)": lambda n: [i ** 2 for i in n],
            "O(2^n)": lambda n: [2 ** i for i in n],
        }

        errors = {}
        for complexity, func in complexities.items():
            estimated_times = func(input_sizes)
            scale = np.mean(times) / np.mean(estimated_times)
            scaled_estimated_times = [t * scale for t in estimated_times]
            errors[complexity] = mean_squared_error(times, scaled_estimated_times)

        best_fit = min(errors, key=errors.get)
        return best_fit

    def analyze_function(self, func, inputs):
        times = []
        input_sizes = []

        for input_data in inputs:
            start_time = time.time()
            func(*input_data)  # Pass unpacked arguments
            end_time = time.time()

            times.append(end_time - start_time)
            input_sizes.append(self._get_input_size(input_data[0]))  # Assuming the first argument determines size

        complexity = self.calculate(input_sizes, times)
        self.results[func.__name__] = complexity
        return complexity

    @staticmethod
    def _get_input_size(input_data):
        if isinstance(input_data, (list, tuple, str, set)):
            return len(input_data)
        elif isinstance(input_data, dict):
            return len(input_data.keys())
        else:
            raise ValueError("Unsupported input type for complexity analysis.")

    def get_results(self):
        return self.results



def analyze_complexity(inputs):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            num_params = len(inspect.signature(func).parameters)
            if num_params > 1:
                calculator = BigOCalculator()
                complexity = calculator.analyze_function(func, inputs)
            else:
                single_input_data = [(input,) for input in inputs]  
                calculator = BigOCalculator()
                complexity = calculator.analyze_function(func, single_input_data)

            print(f"Function {func.__name__} has a time complexity of {complexity}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

