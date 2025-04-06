import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Example dataset with outliers
data = [1, 10, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 110, 120, 150, 200, 250, 300]

# Compute quartiles
Q1 = np.percentile(data, 25)
Q2 = np.median(data)
Q3 = np.percentile(data, 75)
IQR = Q3 - Q1
print("IQR:", IQR)

# Compute outlier bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify outliers
outliers = [x for x in data if x < lower_bound or x > upper_bound]
print("Outliers:", outliers)

# Create the box plot
plt.figure(figsize=(6, 5))
sns.boxplot(data=data, width=0.3, color='lightblue', flierprops={'marker': 'o', 'color': 'red', 'markersize': 8})

# Annotate key statistics
plt.text(1.05, Q1, f'Q1: {Q1}', verticalalignment='center', fontsize=10, color='blue')
plt.text(1.05, Q2, f'Median: {Q2}', verticalalignment='center', fontsize=10, color='green')
plt.text(1.05, Q3, f'Q3: {Q3}', verticalalignment='center', fontsize=10, color='blue')
plt.text(1.05, min(data), f'Min: {min(data)}', verticalalignment='center', fontsize=10, color='black')
plt.text(1.05, max(data), f'Max: {max(data)}', verticalalignment='center', fontsize=10, color='black')

# Highlight outliers in red
for outlier in outliers:
    plt.scatter(1, outlier, color='red', zorder=3, s=100)  # Red dot
    plt.text(1.1, outlier, f'Outlier: {outlier}', verticalalignment='center', fontsize=10, color='red')

plt.xticks([])  # Hide x-axis labels
plt.ylabel("Values")
plt.title("Box Plot with Outliers Labeled")
plt.show()
