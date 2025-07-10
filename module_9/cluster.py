import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the JSON file
df = pd.read_json('cleaned_applicant_data.json')

# Count unique program names
unique_programs = df['program'].nunique()
num_entries = len(df)

print(f"Number of unique programs: {unique_programs}")
print(f"Number of entries: {num_entries}")

# Create a TF-IDF Vectorizer and transform the 'program' column
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['program'])

print("TF-IDF matrix created with shape:", tfidf_matrix.shape)
print("Number of stored elements (nnz):", tfidf_matrix.nnz)

# Reduce dimensionality to 2 components using PCA
pca = PCA(n_components=2)
tfidf_dense = tfidf_matrix.toarray()
reduced = pca.fit_transform(tfidf_dense)
print("PCA reduced matrix shape:", reduced.shape)

# Elbow Method to find optimal number of clusters
inertia_values = []
k_values = range(1, 101)  # Valid range: 1 to 100

print("Calculating inertia for different k values...")
for k in k_values:
    kmeans = KMeans(n_clusters=k, max_iter=100, n_init=5, random_state=42)
    kmeans.fit(reduced)
    inertia_values.append(kmeans.inertia_)

# Plot the Elbow Curve
plt.figure(figsize=(10, 6))
plt.plot(k_values, inertia_values, marker='o')
plt.title("Elbow Method using inertia")
plt.xlabel("Values of K")
plt.ylabel("Inertia")
plt.grid(True)
#plt.show()


optimal_k = 20

# Perform KMeans clustering with the chosen number of clusters
kmeans = KMeans(n_clusters=optimal_k, max_iter=100, n_init=5, random_state=42)
kmeans.fit(reduced)
labels = kmeans.labels_

print("KMeans clustering complete.")

# Add cluster labels to the original dataframe
df['cluster'] = labels

# Create a new DataFrame with selected columns
# Replace 'university' with the correct column name if it's different
result_df = df[['program', 'university', 'cluster']].copy()

# Expand display settings to show full output
pd.set_option('display.max_rows', None)

# Show the first 100 rows
print(result_df.head())


# Plot the PCA-reduced data with cluster colors
plt.figure(figsize=(10, 7))
plt.scatter(reduced[:, 0], reduced[:, 1], c=labels, cmap='tab20', s=30)
plt.title(f"KMeans Clustering of Programs (k={optimal_k})")
plt.xlabel("KMeans Distance Direction 1")
plt.ylabel("KMeans Distance Direction 2")
plt.grid(True)
#plt.show()

# Save the DataFrame with cluster assignments to a new JSON file
df.to_json('clustered_applicant_data.json', orient='records', lines=False)
print("Cluster assignments saved to clustered_applicant_data.json")