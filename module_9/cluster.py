import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

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

# Convert to COO format to print coordinates and values
coo = tfidf_matrix.tocoo()
print("Row | Col | Value")
for row, col, value in zip(coo.row, coo.col, coo.data):
    print(f"{row} {col} {value}")

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
