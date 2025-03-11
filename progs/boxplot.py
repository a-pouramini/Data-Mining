import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Example dataset
data = np.array([23, 25, 25, 27, 30, 35, 35, 35, 40])

# Calculate quartiles and median
quartiles = np.percentile(data, [25, 50, 75])  # Q1, Q2 (median), Q3
min_val = np.min(data)
max_val = np.max(data)

# Print quantiles
print(f"Minimum: {min_val}")
print(f"Q1 (25th percentile): {quartiles[0]}")
print(f"Q2 (Median, 50th percentile): {quartiles[1]}")
print(f"Q3 (75th percentile): {quartiles[2]}")
print(f"Maximum: {max_val}")

# Create a box plot
plt.figure(figsize=(8, 6))
sns.boxplot(x=data, color="lightblue")

# Add labels and title
plt.title("Box Plot to Visualize Quantiles", fontsize=16)
plt.xlabel("Data", fontsize=14)

# Show the plot
plt.show()
