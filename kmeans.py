import numpy as np

# Function to initialize empty clusters
def initialize_cluster(clusters, k):
    clusters.clear()
    for i in range(k):
        clusters.append([])

# Function to calculate distance between points (works for 1D, 2D, and 3D)
def calculate_distance(point1, point2):
    return np.linalg.norm(np.array(point1) - np.array(point2))

# Function to find the closest cluster for each point
def find_cluster(point, centroids, clusters, k):
    dist = float('inf')
    temp_cluster = -1
    for i in range(k):
        d = calculate_distance(point, centroids[i])
        if d < dist:
            dist = d
            temp_cluster = i
    clusters[temp_cluster].append(point)

# Function to update centroids by calculating the mean of points in each cluster
def update_centroids(clusters, old_centroids, k):
    centroids = []
    for i in range(k):
        # Avoid division by zero in case a cluster has no points
        if len(clusters[i]) > 0:
            centroids.append(np.mean(clusters[i], axis=0))
        else:
            centroids.append(old_centroids[i])  # Keep the old centroid if no points
    return centroids

# Main K-means function
def k_means(points, centroids, max_iterations=100):
    k = len(centroids)
    clusters = []

    # Run the K-means algorithm for max_iterations or until convergence
    for _ in range(max_iterations):
        initialize_cluster(clusters, k)  # Initialize clusters to empty
        for point in points:
            find_cluster(point, centroids, clusters, k)  # Assign point to the closest cluster
        
        new_centroids = update_centroids(clusters, centroids, k)  # Update centroids
        
        # Check if centroids have changed
        if np.array_equal(new_centroids, centroids):
            break
        
        centroids = new_centroids  # Set new centroids as the current ones

    return clusters, centroids

# Example usage with 1D, 2D, and 3D points
points_1d = [5, 11, 19, 27, 23, 25, 6, 18, 2, 8, 10, 12, 31, 29, 4]  # 1D points
points_2d = [[5, 7], [11, 3], [19, 21], [27, 18], [23, 25], [25, 5], [6, 11], [18, 3], [2, 8], [8, 2], [10, 9], [12, 14], [31, 17], [29, 22], [4, 6]]  # 2D points
points_3d = [[5, 7, 9], [11, 3, 2], [19, 21, 15], [27, 18, 20], [23, 25, 28], [25, 5, 11], [6, 11, 14], [18, 3, 10], [2, 8, 6], [8, 2, 3], [10, 9, 12], [12, 14, 18], [31, 17, 25], [29, 22, 19], [4, 6, 8]]  # 3D points

centroids_1d = [0, 7, 20]  # Initial centroids for 1D
centroids_2d = [[0, 0], [7, 7], [20, 20]]  # Initial centroids for 2D
centroids_3d = [[0, 0, 0], [7, 7, 7], [20, 20, 20]]  # Initial centroids for 3D

# Running K-means for 1D, 2D, and 3D
clusters_1d, centroids_1d = k_means(points_1d, centroids_1d)
clusters_2d, centroids_2d = k_means(points_2d, centroids_2d)
clusters_3d, centroids_3d = k_means(points_3d, centroids_3d)

# Output results
print("1D Clusters:", clusters_1d)
print("1D Final Centroids:", centroids_1d)
print("2D Clusters:", clusters_2d)
print("2D Final Centroids:", centroids_2d)
print("3D Clusters:", clusters_3d)
print("3D Final Centroids:", centroids_3d)
