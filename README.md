# Customer Segmentation Using RFM, K-Means Clustering & PCA

## Project Overview

This project focuses on customer segmentation using **RFM Analysis (Recency, Frequency, Monetary)** and **K-Means Clustering**. The goal is to identify different types of customers based on their purchasing behavior and spending patterns.
By analyzing customer transaction data, the model groups customers into meaningful segments such as Big Spenders, Loyal Regulars, New Customers, and Occasional / At-Risk Buyers. The project also uses **PCA (Principal Component Analysis)** to visualize customer clusters and understand how different customer groups are distributed.

## Objectives

- Analyze customer purchasing behavior using RFM analysis.
- Identify meaningful customer groups using K-Means clustering.
- Determine the optimal number of clusters using the Elbow Method and Silhouette Score.
- Visualize customer segments using PCA.
- Analyze customer distribution across different cities.
- Generate customer segmentation reports in JSON format.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Scikit-learn | Machine learning and clustering |
| K-Means | Customer segmentation |
| PCA | Dimensionality reduction |
| StandardScaler | Feature standardization |

## Project Workflow

### 1. Data Loading and Cleaning

The dataset is loaded from `online_retail.csv`.

The following cleaning operations are performed:

- Remove records without Customer ID.
- Remove transactions with zero or negative quantities.
- Remove records with zero or negative unit prices.
- Convert Customer ID into integer format.
- Extract city information from the Area column.
- Calculate total transaction value.

**Total Price = Quantity × Unit Price**

### 2. RFM Analysis

RFM analysis is used to understand customer purchasing behavior through three important metrics.

| Metric | Description |
|---|---|
| Recency | Number of days since the customer's last purchase |
| Frequency | Total number of unique orders placed by the customer |
| Monetary | Total amount spent by the customer |

These three metrics help identify customer behavior and purchasing patterns.

### 3. Data Transformation and Scaling

A logarithmic transformation (`log1p`) is applied to the RFM features to reduce the impact of highly skewed values.

After transformation, StandardScaler is used to standardize the features before applying K-Means clustering.

### 4. Finding the Optimal Number of Clusters

Two evaluation techniques are used:

- **Elbow Method:** Helps identify a suitable number of clusters by analyzing the reduction in inertia.
- **Silhouette Score:** Measures how well-separated the resulting clusters are.

The number of clusters can be adjusted based on the evaluation results.

![Elbow Method and Silhouette Score](Figure_1.png)

### 5. K-Means Clustering

K-Means clustering is applied to group customers based on their RFM characteristics.

The current implementation uses:

- Number of clusters: 4
- Random state: 42
- Initialization: 10

Each customer is assigned to one of the four clusters.

### 6. Customer Segmentation

Based on the average Recency, Frequency, and Monetary values, customers are assigned readable segment names.

| Customer Segment | Description |
|---|---|
| Big Spenders | Customers with the highest average spending |
| Loyal Regulars | Customers who purchase regularly |
| New Customers | Customers with relatively few orders |
| Occasional / At-Risk Buyers | Customers with longer periods since their last purchase |

### 7. PCA Visualization

Principal Component Analysis (PCA) reduces the three-dimensional RFM feature space into two dimensions.

This allows customer clusters to be visualized in a 2D scatter plot.

### 8. Additional Analysis

The project also generates:

- Average recency by customer segment.
- Average number of orders by customer segment.
- Average spending by customer segment.
- Customer distribution by city and segment.
- Top three cities for each customer segment.

## Dataset Information

**Dataset:** `online_retail.csv`

The project uses the following dataset columns:

- `InvoiceNo`
- `InvoiceDate`
- `CustomerID`
- `Quantity`
- `UnitPrice`
- `Area`

The dataset is treated as a Bangladesh retail dataset, with monetary values represented in Bangladeshi Taka (BDT).

## Results

After data cleaning and processing, the current execution produced the following results:

| Metric | Result |
|---|---:|
| Total Customers | 650 |
| Average Recency | 104.9 days |
| Average Frequency | 8.3 orders |
| Average Monetary Value | Tk 240,537.6 |
| Number of Clusters | 4 |

### Customer Purchasing Statistics

| Statistic | Recency | Frequency | Monetary |
|---|---:|---:|---:|
| Minimum | 1 | 1 | 739.2 |
| Maximum | 357 | 40 | 1,867,086.0 |
| Average | 104.9 | 8.3 | 240,537.6 |

## Business Applications

The customer segments can help a marketing team make better decisions.

- **Big Spenders:** Provide VIP membership, exclusive discounts, and premium offers.
- **Loyal Regulars:** Introduce loyalty points, rewards, and personalized promotions.
- **New Customers:** Provide welcome discounts and encourage repeat purchases.
- **Occasional / At-Risk Buyers:** Launch targeted campaigns and win-back offers.

## Installation and Usage

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/customer-segmentation.git
```

### 2. Navigate to the Project Folder

```bash
cd customer-segmentation
```

### 3. Install Required Libraries

```bash
pip install numpy pandas matplotlib scikit-learn
```

### 4. Add the Dataset

Place `online_retail.csv` inside the project directory.

### 5. Run the Project

```bash
python customer_segmentation.py
```

The program will display the clustering evaluation charts, PCA visualization, customer analysis charts, and final segmentation results.

It will also generate:

`customer_segments.json`

This JSON file contains customer-level segmentation results and a summary of each customer segment.

## Project Structure

```text
Customer-Segmentation/
│
├── customer_segmentation.py
├── online_retail.csv
├── Figure_1.png
├── customer_segments.json
└── README.md
```

## Future Improvements

- Experiment with different clustering algorithms such as DBSCAN and Hierarchical Clustering.
- Improve automatic customer segment classification.
- Develop an interactive dashboard using Streamlit.
- Introduce customer lifetime value (CLV) analysis.
- Improve customer targeting using predictive analytics.
