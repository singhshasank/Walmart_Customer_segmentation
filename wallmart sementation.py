# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load the Walmart dataset
data = pd.read_csv('walmart_sales_data.csv')

# Display the first few rows of the data
print(data.head())

# Check for missing values
print(data.isnull().sum())

# Feature Selection
# Selecting relevant features for customer segmentation
data_selected = data[['Weekly_Sales', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']]

# Handle missing values if any
data_selected.fillna(data_selected.mean(), inplace=True)

# Feature Scaling
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data_selected)

# Finding the Optimal Number of Clusters using Elbow Method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=42)
    kmeans.fit(data_scaled)
    wcss.append(kmeans.inertia_)

# Plot the Elbow Method graph
plt.figure(figsize=(10, 5))
plt.plot(range(1, 11), wcss, marker='o', linestyle='--')
plt.title('Elbow Method for Optimal Number of Clusters')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# Applying K-Means Clustering
# Assuming the optimal number of clusters is 4 based on the Elbow Method
kmeans = KMeans(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=42)
clusters = kmeans.fit_predict(data_scaled)

# Adding cluster labels to the original data
data['Cluster'] = clusters

# Visualize the Clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Weekly_Sales', y='Temperature', hue='Cluster', data=data, palette='viridis', s=100)
plt.title('Customer Segments based on Weekly Sales and Temperature')
plt.xlabel('Weekly Sales')
plt.ylabel('Temperature')
plt.legend()
plt.show()

# Save the clustered data to a new CSV file
data.to_csv('walmart_customer_segments.csv', index=False)