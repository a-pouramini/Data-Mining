import matplotlib.pyplot as plt

# Your manual data
data = [20, 30, 32, 35, 70, 44, 33, 80, 17, 19, 32, 88, 65, 55, 32, 24, 43, 32, 50, 89, 42, 35, 48, 90, 38]

# Create the histogram
plt.figure(figsize=(8, 6))
plt.hist(data, bins=20, color='blue', edgecolor='black', alpha=0.7)

# Add labels and title
plt.xlabel('Sales Data')
plt.ylabel('Frequency')
plt.title('Histogram of Sales Data')

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Show the plot
plt.show()
