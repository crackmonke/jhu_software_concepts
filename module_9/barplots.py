import pandas as pd
import matplotlib.pyplot as plt

# Load the clustered data (assuming the clustering script has already added the 'cluster' column)
df = pd.read_json('cleaned_applicant_data.json')

# If the cluster labels are not present, you may need to load them from a saved file or rerun the clustering code
if 'cluster' not in df.columns:
    raise ValueError("The DataFrame does not contain a 'cluster' column. Please run the clustering script first.")

# Find cluster numbers for Computer Science and Philosophy
cs_mask = df['program'].str.lower().str.contains('computer science')
ph_mask = df['program'].str.lower().str.contains('philosophy')

cs_clusters = df.loc[cs_mask, 'cluster'].unique()
ph_clusters = df.loc[ph_mask, 'cluster'].unique()

# Use the most common cluster for each
cs_cluster = df.loc[cs_mask, 'cluster'].mode().iloc[0] if len(cs_clusters) > 0 else None
ph_cluster = df.loc[ph_mask, 'cluster'].mode().iloc[0] if len(ph_clusters) > 0 else None

# Plot GRE V and GRE score ranges for Computer Science cluster
if cs_cluster is not None:
    cs_gre_v = df.loc[df['cluster'] == cs_cluster, 'GRE V']
    cs_gre = df.loc[df['cluster'] == cs_cluster, 'GRE']
    plt.figure(figsize=(8, 4))
    plt.bar(['GRE V min', 'GRE V max', 'GRE min', 'GRE max'],
            [cs_gre_v.min(), cs_gre_v.max(), cs_gre.min(), cs_gre.max()])
    plt.title(f'GRE Score Ranges for Computer Science Cluster #{cs_cluster}')
    plt.ylabel('Score')
    plt.show()
else:
    print("No Computer Science cluster found.")

# Plot GRE V and GRE score ranges for Philosophy cluster
if ph_cluster is not None:
    ph_gre_v = df.loc[df['cluster'] == ph_cluster, 'GRE V']
    ph_gre = df.loc[df['cluster'] == ph_cluster, 'GRE']
    plt.figure(figsize=(8, 4))
    plt.bar(['GRE V min', 'GRE V max', 'GRE min', 'GRE max'],
            [ph_gre_v.min(), ph_gre_v.max(), ph_gre.min(), ph_gre.max()])
    plt.title(f'GRE Score Ranges for Philosophy Cluster #{ph_cluster}')
    plt.ylabel('Score')
    plt.show()
else:
    print("No Philosophy cluster found.")
