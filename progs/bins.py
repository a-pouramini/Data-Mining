import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sample data with noise and outliers
data = np.array([12, 15, 18, 120, 25, 28, 32, 35, 38, 200, 
                 42, 45, 48, 52, 55, 58, 62, 65, 68, 250, 
                 72, 75, 78, 82, 85, 88, 92, 95, 98, np.nan])

df = pd.DataFrame({'Raw_Values': data})

# Equal-width binning (4 bins)
df['Equal_Width_Bins'] = pd.cut(df['Raw_Values'], bins=4, 
                               labels=['Low', 'Medium', 'High', 'Very High'])

# Equal-frequency binning (4 bins)
df['Equal_Freq_Bins'] = pd.qcut(df['Raw_Values'], q=4, 
                               labels=['Q1', 'Q2', 'Q3', 'Q4'])

# Custom binning with outlier handling
bins = [0, 40, 80, 120, np.inf]
labels = ['0-40', '40-80', '80-120', 'Outliers']
df['Custom_Bins'] = pd.cut(df['Raw_Values'], bins=bins, labels=labels)

# Handle missing values with a separate bin
df['Custom_Bins'] = df['Custom_Bins'].cat.add_categories('Missing').fillna('Missing')

print("Original Data with Binning Results:")
print(df.dropna())  # Display first 10 non-null rows

# Visualization
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
df['Equal_Width_Bins'].value_counts().plot(kind='bar')
plt.title('Equal-Width Binning')

plt.subplot(1, 3, 2)
df['Equal_Freq_Bins'].value_counts().plot(kind='bar')
plt.title('Equal-Frequency Binning')

plt.subplot(1, 3, 3)
df['Custom_Bins'].value_counts().plot(kind='bar')
plt.title('Custom Binning with Outlier Handling')

plt.tight_layout()
plt.show()
