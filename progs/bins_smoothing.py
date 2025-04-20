import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate noisy data
np.random.seed(42)
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.2, 100)

# Create DataFrame
df = pd.DataFrame({'X': x, 'Y': y})

# Equal-width binning
df['X_bin'] = pd.cut(df['X'], bins=10)

# Calculate smoothed values
bin_means = df.groupby('X_bin')['Y'].mean()
df['Smoothed_Mean'] = df['X_bin'].map(bin_means)

bin_medians = df.groupby('X_bin')['Y'].median()
df['Smoothed_Median'] = df['X_bin'].map(bin_medians)

# Visualization
plt.figure(figsize=(12, 6))
plt.scatter(df['X'], df['Y'], label='Original Noisy Data', alpha=0.5)
plt.plot(df['X'], df['Smoothed_Mean'], 'r-', label='Bin Mean Smoothing', linewidth=2)
plt.plot(df['X'], df['Smoothed_Median'], 'g--', label='Bin Median Smoothing', linewidth=2)
plt.title('Data Smoothing Using Binning Methods')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.legend()
plt.grid(True)
plt.show()
