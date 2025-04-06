import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import probplot

def qqplot(data):
    # Create a Q-Q plot against a normal distribution
    plt.figure(figsize=(8, 6))
    probplot(data, dist="norm", plot=plt)
    
    # Add quantiles to the plot
    q1 = np.percentile(data, 25)
    median = np.percentile(data, 50)
    q3 = np.percentile(data, 75)
    
    plt.axhline(y=q1, color='r', linestyle='--', label=f'Q1 (25th percentile) = {q1:.2f}')
    plt.axhline(y=median, color='g', linestyle='--', label=f'Median (50th percentile) = {median:.2f}')
    plt.axhline(y=q3, color='purple', linestyle='--', label=f'Q3 (75th percentile) = {q3:.2f}')
    
    plt.title('Q-Q Plot Against Normal Distribution')
    plt.legend()
    plt.grid(True)
    plt.show()

def qqplot_manual(data, second_data):

    # Sort both datasets
    data_sorted = np.sort(data)
    second_data_sorted = np.sort(second_data)

    # Calculate quantiles for both datasets
    quantiles_data = np.percentile(data_sorted, np.linspace(0, 100, len(data)))
    quantiles_second_data = np.percentile(second_data_sorted, np.linspace(0, 100, len(second_data)))

    # Create the Q-Q plot
    plt.figure(figsize=(8, 6))
    plt.scatter(quantiles_second_data, quantiles_data, color='b', label='Q-Q Plot')
    plt.plot([min(quantiles_second_data), max(quantiles_second_data)], 
             [min(quantiles_second_data), max(quantiles_second_data)], 
             color='r', linestyle='--', label='y = x')

    # Add quantiles to the plot
    q1_data = np.percentile(data, 25)
    median_data = np.percentile(data, 50)
    q3_data = np.percentile(data, 75)
    
    q1_second = np.percentile(second_data, 25)
    median_second = np.percentile(second_data, 50)
    q3_second = np.percentile(second_data, 75)
    
    plt.axhline(y=q1_data, color='orange', linestyle=':', label=f'Q1 (Your Data) = {q1_data:.2f}')
    plt.axhline(y=median_data, color='cyan', linestyle=':', label=f'Median (Your Data) = {median_data:.2f}')
    plt.axhline(y=q3_data, color='magenta', linestyle=':', label=f'Q3 (Your Data) = {q3_data:.2f}')
    
    plt.axvline(x=q1_second, color='orange', linestyle=':', label=f'Q1 (Second Data) = {q1_second:.2f}')
    plt.axvline(x=median_second, color='cyan', linestyle=':', label=f'Median (Second Data) = {median_second:.2f}')
    plt.axvline(x=q3_second, color='magenta', linestyle=':', label=f'Q3 (Second Data) = {q3_second:.2f}')

    plt.xlabel('Quantiles of Second Dataset')
    plt.ylabel('Quantiles of Your Data')
    plt.title('Q-Q Plot: Your Data vs Second Dataset')
    plt.legend()
    plt.grid(True)
    plt.show()

# Your manual data
data1 = [20, 30, 32, 35, 70, 44, 33, 80, 17, 19, 32, 88, 65, 55, 32, 24, 43, 32, 50, 89, 42, 35, 48, 90, 38]

print("Data1", np.sort(data1))
# Second dataset (e.g., a theoretical distribution or another empirical dataset)
mean = np.mean(data1)
std = np.std(data1)
data2 = np.random.normal(loc=mean, scale=std, size=len(data1))
data2 = np.round(data2,1)
print("Data2", np.sort(data2))

# Third dataset (normal distribution with mean=30, std=10)
mean = 30
std = 10
data3 = np.random.normal(loc=mean, scale=std, size=len(data1))

qqplot(data1)
qqplot_manual(data1, data2)
# qqplot_manual(data1, data3)

data4 = [10, 36, 42, 45, 70, 44, 43, 80, 27, 29, 42, 88, 65, 55, 42, 34, 53, 42, 55, 89, 52, 45, 48, 90, 48]
print("Data4", np.sort(data4))

qqplot_manual(data1, data4)
