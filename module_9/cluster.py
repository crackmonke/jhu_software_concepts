import pandas as pd
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the cleaned applicant data
with open('cleaned_applicant_data.json', 'r') as file:
    data = json.load(file)

# Convert to DataFrame
df = pd.DataFrame(data)

# Determine the number of unique program names
unique_programs = df['program'].unique()
num_unique_programs = len(unique_programs)

print(f"Number of unique program names: {num_unique_programs}")

# Show top 10 most frequent programs
program_counts = df['program'].value_counts()
print(program_counts.head(10))

# Create TF-IDF vectorizer and convert program names to sparse matrix
print("\nCreating TF-IDF vectorization of program names...")
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['program'])

print(f"TF-IDF matrix shape: {tfidf_matrix.shape}")

# Reduce dimensions to 2 components using PCA
print("\nReducing dimensions to 2 components...")
pca = PCA(n_components=2)
reduced_matrix = pca.fit_transform(tfidf_matrix.toarray())

print(f"Reduced matrix shape: {reduced_matrix.shape}")

# Elbow Method to determine optimal number of clusters
print("\nApplying Elbow Method to determine optimal number of clusters...")
inertias = []
k_range = range(1, 101)  # Test from 1 to 100 clusters

for k in k_range:
    kmeans_elbow = KMeans(n_clusters=k, max_iter=100, n_init=5, random_state=42)
    kmeans_elbow.fit(reduced_matrix)
    inertias.append(kmeans_elbow.inertia_)
    if k % 10 == 0:  # Print progress every 10 iterations
        print(f"Completed k={k}")

# Plot the elbow curve
plt.figure(figsize=(10, 6))
plt.plot(k_range, inertias, 'bo-', linewidth=2, markersize=4)
plt.xlabel('Vlue of k')
plt.ylabel('Inertia')
plt.title('Elbow Method using Inertia')
plt.grid(True, alpha=0.3)
plt.tight_layout()
#plt.show()

# Apply K-Means clustering
print("\nApplying K-Means clustering with 50 clusters...")
kmeans = KMeans(n_clusters=50, max_iter=100, n_init=5, random_state=42)
cluster_labels = kmeans.fit_predict(reduced_matrix)

print(f"Number of clusters: {len(set(cluster_labels))}")
print(f"Cluster labels shape: {cluster_labels.shape}")

# Create DataFrame with program, university, and cluster information
clustered_df = pd.DataFrame({
    'program': df['program'],
    'university': df['university'],
    'cluster': cluster_labels
})

# Display first 100 rows
print("\nFirst 100 rows of clustered data:")
print(clustered_df.head(100))

# Analyze GRE scores for Computer Science and Philosophy clusters
print("\nAnalyzing GRE scores for Computer Science and Philosophy clusters...")

# Find clusters containing Computer Science programs
cs_mask = df['program'] == 'Computer Science'
cs_clusters = set(cluster_labels[cs_mask])
print(f"Computer Science programs are in clusters: {cs_clusters}")

# Find clusters containing Philosophy programs  
phil_mask = df['program'] == 'Philosophy'
phil_clusters = set(cluster_labels[phil_mask])
print(f"Philosophy programs are in clusters: {phil_clusters}")

# Get GRE data for Computer Science cluster(s)
cs_cluster_mask = pd.Series(cluster_labels).isin(cs_clusters)
cs_gre_data = df[cs_cluster_mask][['gre_score', 'gre_v_score']].dropna()

# Get GRE data for Philosophy cluster(s)
phil_cluster_mask = pd.Series(cluster_labels).isin(phil_clusters)
phil_gre_data = df[phil_cluster_mask][['gre_score', 'gre_v_score']].dropna()

# Create comparison graphs for GRE scores
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# GRE Total Score comparison
ax1.boxplot([cs_gre_data['gre_score'].dropna(), phil_gre_data['gre_score'].dropna()], 
           labels=['Computer Science', 'Philosophy'])
ax1.set_title('GRE Total Score Comparison')
ax1.set_ylabel('GRE Total Score')
ax1.grid(True, alpha=0.3)

# GRE Verbal Score comparison
ax2.boxplot([cs_gre_data['gre_v_score'].dropna(), phil_gre_data['gre_v_score'].dropna()], 
           labels=['Computer Science', 'Philosophy'])
ax2.set_title('GRE Verbal Score Comparison')
ax2.set_ylabel('GRE Verbal Score')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print(f"GRE score comparison saved as 'clustered_dataFrame.png'")

# Plot the clustering results
plt.figure(figsize=(12, 8))
scatter = plt.scatter(reduced_matrix[:, 0], reduced_matrix[:, 1], 
                     c=cluster_labels, cmap='tab10', alpha=0.6, s=10)
plt.xlabel('KMeans Distance Direction 1')
plt.ylabel('KMeans Distance Direction 2')
plt.title('Kmeans Clustering of Programs')
plt.grid(True, alpha=0.3)
plt.tight_layout()
#plt.show()
