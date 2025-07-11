# Graduate Program Clustering Analysis

## Overview
This repository contains a machine learning analysis of graduate school application data using K-Means clustering and TF-IDF vectorization to group similar academic programs.

## File Description

### `kmeans.py`
A comprehensive Python script that performs clustering analysis on graduate school application data. The script implements the following workflow:

#### 1. Data Loading and Exploration
- Loads graduate application data from `cleaned_applicant_data.json`
- Analyzes unique program names (1,591 total programs)
- Displays the top 10 most frequent programs

#### 2. Text Vectorization
- Uses TF-IDF (Term Frequency-Inverse Document Frequency) vectorization to convert program names into numerical features
- Creates a sparse matrix representation of program name similarities

#### 3. Dimensionality Reduction
- Applies Principal Component Analysis (PCA) to reduce the high-dimensional TF-IDF matrix to 2 components
- Enables visualization and faster clustering computation

#### 4. Optimal Cluster Selection
- Implements the Elbow Method to determine the optimal number of clusters
- Tests cluster sizes from 1 to 100 and plots inertia values
- Saves the elbow curve as `elbow.png`

#### 5. K-Means Clustering
- Performs K-Means clustering with 50 clusters
- Parameters: max_iter=100, n_init=5, random_state=42
- Creates cluster assignments for all program applications

#### 6. Results Analysis
- Generates a DataFrame showing program names, universities, and cluster assignments
- Displays the first 100 rows for inspection

#### 7. GRE Score Analysis
- Compares GRE scores between Computer Science and Philosophy program clusters
- Creates side-by-side boxplots showing GRE Total and GRE Verbal scores for each field
- Visualizes score distributions to identify patterns between academic disciplines

#### 8. Visualization
- Creates a scatter plot of the clustered data in 2D PCA space
- Shows how programs are distributed across the reduced feature space
- Uses color coding to distinguish different clusters

## Dependencies
- pandas
- scikit-learn
- matplotlib
- json

## Usage
Run the script to perform the complete clustering analysis:
```bash
python kmeans.py
```

The script will output analysis results to the terminal and save visualization plots as PNG files.
