import numpy as np

# Generate 5 evenly spaced samples between 2.0 and 3.0, including the endpoint
samples = np.linspace(2.0, 3.0, num=5)
print(samples)

# Generate 5 evenly spaced samples between 2.0 and 3.0, excluding the endpoint
samples_excluded = np.linspace(2.0, 3.0, num=5, endpoint=False)
print(samples_excluded)

# Generate 5 evenly spaced samples between 2.0 and 3.0, and return the step size
samples_with_step, step = np.linspace(2.0, 3.0, num=5, retstep=True)
print(samples_with_step)
print("Step size:", step)