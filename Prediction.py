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
