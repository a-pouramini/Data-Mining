import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from scipy import stats

# =============================================
# Raw Data (commented as table for reference)
# =============================================
# | Hour | Machine_Speed | Reported_Temp | Notes                |
# |------|---------------|---------------|----------------------|
# | 1    | 100           | 72.1          | Valid                |
# | 2    | 105           | 73.5          | Valid                |
# | 3    | 110           | 74.8          | Valid                |
# | 4    | 108           | 142.3         | Outlier (sensor glitch) |
# | 5    | 112           | 75.2          | Valid                |
# | 6    | 115           | NULL          | Missing value        |
# | 7    | 120           | 77.0          | Valid                |
# | 8    | 125           | 78.5          | New validation point |
# =============================================

# Create DataFrame
data = {
    'Hour': [1, 2, 3, 4, 5, 6, 7, 8],
    'Machine_Speed': [100, 105, 110, 108, 112, 115, 120, 125],
    'Reported_Temp': [72.1, 73.5, 74.8, 142.3, 75.2, np.nan, 77.0, 78.5]
}
df = pd.DataFrame(data)

# Separate features (X) and target (y)
X = df[['Machine_Speed']]
y = df['Reported_Temp']

# =============================================
# Step 1: Initial Visualization
# =============================================
plt.figure(figsize=(12, 6))
plt.scatter(X, y, c='blue', label='Original Data', s=100, alpha=0.7)
plt.title('Temperature vs Machine Speed (Raw Data)')
plt.xlabel('Machine Speed (RPM)')
plt.ylabel('Reported Temperature (°F)')
plt.grid(True)
plt.legend()
plt.show()

# =============================================
# Step 2: Train Regression Model on Clean Data
# =============================================
# Identify initially clean data (non-null and reasonable values)
clean_mask = (~y.isna()) & (y < 100)  # Assuming temps < 100 are reasonable
X_clean = X[clean_mask]
y_clean = y[clean_mask]

# Train linear regression model
model = LinearRegression()
model.fit(X_clean, y_clean)

# Make predictions for all points
y_pred = model.predict(X)

# Calculate residuals
residuals = y - y_pred

# =============================================
# Step 3: Outlier Detection
# =============================================
# Calculate Z-scores of residuals (only for clean data)
residuals_clean = residuals[clean_mask]
z_scores = np.abs(stats.zscore(residuals_clean))

# Define outlier threshold (3 standard deviations)
outlier_threshold = 3
outlier_mask = (np.abs(residuals) > outlier_threshold * np.std(residuals_clean)) & ~y.isna()

print("=====================================")
print("Outlier Detection Results:")
print("=====================================")
print(f"Model Coefficients: {model.coef_[0]:.4f} (slope), {model.intercept_:.4f} (intercept)")
print(f"R-squared: {r2_score(y_clean, model.predict(X_clean)):.4f}")
print("\nPotential Outliers:")
print(df[outlier_mask])
print("=====================================")

# =============================================
# Step 4: Data Cleaning
# =============================================
# Create cleaned temperature column
df['Cleaned_Temp'] = y.copy()

# Replace outliers with predicted values
df.loc[outlier_mask, 'Cleaned_Temp'] = y_pred[outlier_mask]

# Impute missing values with predicted values
missing_mask = y.isna()
df.loc[missing_mask, 'Cleaned_Temp'] = y_pred[missing_mask]

# =============================================
# Step 5: Visualize Results
# =============================================
plt.figure(figsize=(14, 7))

# Plot original data
plt.scatter(X, y, c='blue', label='Original Data', s=100, alpha=0.5)

# Plot cleaned data
plt.scatter(X, df['Cleaned_Temp'], c='green', marker='s', label='Cleaned Data', s=100)

# Plot regression line
x_range = np.linspace(95, 130, 100).reshape(-1, 1)
y_range = model.predict(x_range)
plt.plot(x_range, y_range, 'r--', label='Regression Line')

# Highlight changes
for i in range(len(df)):
    if outlier_mask[i] or missing_mask[i]:
        plt.plot([X.iloc[i,0], X.iloc[i,0]], 
                [y.iloc[i], df['Cleaned_Temp'].iloc[i]], 
                'k--', alpha=0.3)

plt.title('Temperature Data Cleaning with Regression', fontsize=14)
plt.xlabel('Machine Speed (RPM)', fontsize=12)
plt.ylabel('Temperature (°F)', fontsize=12)
plt.legend(fontsize=12)
plt.grid(True)
plt.show()

# =============================================
# Step 6: Print Final Cleaned Table
# =============================================
print("\nFinal Cleaned Data Table:")
print("=====================================")
print(df[['Hour', 'Machine_Speed', 'Reported_Temp', 'Cleaned_Temp']])
print("=====================================")

# =============================================
# Step 7: Residual Analysis Plot
# =============================================
plt.figure(figsize=(12, 6))
plt.scatter(y_pred, residuals, c='blue', label='Residuals', s=100)
plt.axhline(y=0, color='black', linestyle='--')
plt.axhline(y=outlier_threshold * np.std(residuals_clean), color='red', linestyle=':', label='Outlier Threshold')
plt.axhline(y=-outlier_threshold * np.std(residuals_clean), color='red', linestyle=':')
plt.title('Residual Analysis', fontsize=14)
plt.xlabel('Predicted Values', fontsize=12)
plt.ylabel('Residuals', fontsize=12)
plt.legend(fontsize=12)
plt.grid(True)
plt.show()
