import numpy as np
import matplotlib.pyplot as plt

low =20
high=100
size=100 # number of data points

np.random.seed(42)  # For reproducibility
# Generate random sales data between 20 and 100
# Random sales data between 20 and 100, you can replace it with your own data
# data = np.random.uniform(low=20, high=100, size=100)  
# Generate random data based on Gamma distribution
#alpha, beta = 2, 2
#data = np.random.beta(alpha, beta, size) * (high - low) + low  # Scale to [20, 100]
data = [20, 30, 32, 35, 70, 44, 33, 80, 17, 19, 32, 88, 65, 55, 32, 24, 43, 32, 50, 89, 42, 35, 48, 90, 38]

data_sorted = np.sort(data)  # Sort the data in increasing order

# Number of observations
N = len(data_sorted)

# Calculate f_i values
i = np.arange(1, N + 1)
f_i = (i - 0.5) / N

# Create the quantile plot
plt.figure(figsize=(8, 6))
plt.plot(f_i, data_sorted, marker='o', linestyle='-', color='b')
plt.xlabel('f_i (Quantile)')
plt.ylabel('x_i (Sorted Sales Data)')
plt.title('Quantile Plot of Sales Data')
plt.grid(True)

# Highlight key quantiles (Q1, Median, Q3)
Q1 = np.percentile(data, 25)
median = np.percentile(data, 50)
Q3 = np.percentile(data, 75)

plt.axhline(y=Q1, color='r', linestyle='--', label='Q1 (25th percentile)')
plt.axhline(y=median, color='g', linestyle='--', label='Median (50th percentile)')
plt.axhline(y=Q3, color='purple', linestyle='--', label='Q3 (75th percentile)')

plt.legend()
plt.show()
