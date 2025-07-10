import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the JSON file
df = pd.read_json('cleaned_applicant_data.json')

# Count unique program names
unique_programs = df['program'].nunique()

# Count total number of entries
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

# Cluster the PCA-reduced data into 50 clusters using KMeans
kmeans = KMeans(n_clusters=50, max_iter=100, n_init=5, random_state=42)
kmeans.fit(reduced)
labels = kmeans.labels_

print("KMeans clustering complete.")

# Add cluster labels to the original dataframe
df['cluster'] = labels

# Create a new DataFrame with program name, university, and cluster
# Replace 'university' with the actual column name if it's different in your data
result_df = df[['program', 'university', 'cluster']].copy()

# Show the first 100 rows
pd.set_option('display.max_rows', None)  # Show all rows
print(result_df.head(100))

# Plot the PCA-reduced data colored by cluster label
plt.figure(figsize=(10, 7))
scatter = plt.scatter(reduced[:, 0], reduced[:, 1], c=labels, cmap='tab20', s=30)
plt.title("KMeans Clustering of Programs")
plt.xlabel("KMeans Distance Direction 1")
plt.ylabel("KMeans Distance Direction 2")

#plt.show()
