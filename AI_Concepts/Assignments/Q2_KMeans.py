
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Step 1: Prepare Your Dataset
data = pd.read_csv('Mall_Customers.csv')
data_cleaned = data.drop(columns=['CustomerID'], errors='ignore')

# Step 2: Visualize Data Before Clustering
plt.figure(figsize=(8, 6))
plt.scatter(data_cleaned['Age'], data_cleaned['Annual Income (k$)'], label='Data Points')
plt.xlabel("Age")
plt.ylabel("Annual Income (k$)")
plt.title("Data Distribution Before Clustering")
plt.legend()
plt.grid()
plt.show()

# Step 3: Implement K-Means Clustering
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(data_cleaned.iloc[:, 1:])
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(8, 6))
plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.grid()
plt.show()

# Step 4: Visualize Data After Clustering
kmeans = KMeans(n_clusters=3, init='k-means++', random_state=42)
data_cleaned['Cluster'] = kmeans.fit_predict(data_cleaned.iloc[:, 1:])

plt.figure(figsize=(8, 6))
plt.scatter(data_cleaned['Age'], data_cleaned['Annual Income (k$)'], c=data_cleaned['Cluster'], cmap='viridis')
plt.xlabel("Age")
plt.ylabel("Annual Income (k$)")
plt.title("Data After K-Means Clustering")
plt.grid()
plt.show()

# Step 5: Interpret Your Results
print("Cluster Centroids:")
print(kmeans.cluster_centers_)
