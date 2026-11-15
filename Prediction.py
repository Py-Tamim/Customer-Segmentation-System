# ======================================= First Install the necessary Libraries =======================================

import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

df = pd.read_csv("online_retail.csv")                            # Load and clean data
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
print("Rows:", df.shape[0])
print("From:", df["InvoiceDate"].min())
print("To:  ", df["InvoiceDate"].max())

df = df.dropna(subset=["CustomerID"])
df = df[df["Quantity"] > 0]
df = df[df["UnitPrice"] > 0]
df["CustomerID"] = df["CustomerID"].astype(int)
df["City"] = df["Area"].str.split(",").str[-1].str.strip()
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]
print("Rows after cleaning:", len(df))

snapshot_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)  # Build the RFM table (one row per customer)             
rfm = df.groupby("CustomerID").agg(
    Recency=("InvoiceDate", lambda x: (snapshot_date - x.max()).days),
    Frequency=("InvoiceNo", "nunique"),
    Monetary=("TotalPrice", "sum"),
    City=("City", lambda x: x.mode()[0]),
)
print("\nCustomers:", len(rfm))
print(rfm[["Recency", "Frequency", "Monetary"]].describe().round(1))

rfm_log = np.log1p(rfm[["Recency", "Frequency", "Monetary"]])   # Log transform + scale
X = StandardScaler().fit_transform(rfm_log)

inertia = []                                                    # Elbow method + silhouette score
silhouette = []
k_values = range(2, 9)
for k in k_values:
    model = KMeans(n_clusters=k, n_init=10, random_state=42)
    model.fit(X)
    inertia.append(model.inertia_)
    silhouette.append(silhouette_score(X, model.labels_))
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(k_values, inertia, marker="o")
axes[0].set_title("Elbow Method")
axes[0].set_xlabel("Number of clusters (k)")
axes[0].set_ylabel("Inertia")
axes[1].plot(k_values, silhouette, marker="o", color="green")
axes[1].set_title("Silhouette Score")
axes[1].set_xlabel("Number of clusters (k)")
axes[1].set_ylabel("Score")
plt.tight_layout()
plt.show()

k = 4                                                       # Train KMeans
kmeans = KMeans(n_clusters=k, n_init=10, random_state=42)
rfm["Cluster"] = kmeans.fit_predict(X)

summary = rfm.groupby("Cluster").agg(                      # Describe each cluster
    Customers=("Recency", "count"),
    Avg_Recency_Days=("Recency", "mean"),
    Avg_Orders=("Frequency", "mean"),
    Avg_Spend_Tk=("Monetary", "mean"),
).round(1)

names = {}
left = list(summary.index)

big = summary.loc[left, "Avg_Spend_Tk"].idxmax()          # highest spending
names[big] = "Big Spenders"
left.remove(big)

occasional = summary.loc[left, "Avg_Recency_Days"].idxmax()   # inactive longest
names[occasional] = "Occasional / At-Risk Buyers"
left.remove(occasional)

new = summary.loc[left, "Avg_Orders"].idxmin()            # fewest orders
names[new] = "New Customers"
left.remove(new)

names[left[0]] = "Loyal Regulars"                         # the last one

rfm["Segment"] = rfm["Cluster"].map(names)
summary["Segment"] = summary.index.map(names)

print("\n===== Customer Segments =====")
print(summary.to_string())

# ------------------------------------------------------------
# 8. Draw clusters with PCA
# ------------------------------------------------------------
pca = PCA(n_components=2, random_state=42)
points = pca.fit_transform(X)

plt.figure(figsize=(9, 6))
for segment in rfm["Segment"].unique():
    mask = (rfm["Segment"] == segment).values
    plt.scatter(points[mask, 0], points[mask, 1], label=segment, alpha=0.7)

plt.title("Customer Segments (PCA view)")
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.legend()
plt.show()