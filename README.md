# Customer Segmentation Using RFM, K-Means Clustering & PCA

## Project Overview

This project focuses on analyzing customer purchasing behavior and identifying different customer groups using **RFM Analysis (Recency, Frequency, Monetary)** and **K-Means Clustering**.

The main objective is to understand how customers interact with a retail business, how frequently they make purchases, and how much they spend. Based on these purchasing patterns, customers are grouped into meaningful segments such as Big Spenders, Loyal Regulars, New Customers, and Occasional / At-Risk Buyers.

The project also uses **PCA (Principal Component Analysis)** to reduce the dimensionality of customer data and visualize the resulting clusters in a 2D scatter plot.

By combining data analysis, machine learning, and visualization, this project demonstrates how customer segmentation can support data-driven marketing strategies and business decisions.

## Project Objectives

- Analyze customer purchasing behavior using RFM analysis.
- Identify meaningful customer segments using K-Means clustering.
- Determine the appropriate number of clusters using the Elbow Method and Silhouette Score.
- Apply data transformation and feature scaling to improve clustering performance.
- Visualize customer clusters using Principal Component Analysis (PCA).
- Analyze customer distribution across different cities.
- Identify the purchasing characteristics of each customer segment.
- Generate customer segmentation reports in JSON format.

## Technologies and Libraries Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Scikit-learn | Machine learning and data preprocessing |
| K-Means | Customer clustering |
| PCA | Dimensionality reduction and visualization |
| StandardScaler | Feature standardization |

## Project Workflow

### 1. Data Loading and Cleaning

The project uses an online retail transaction dataset named `online_retail.csv`.

Before performing customer analysis, the dataset goes through several cleaning operations:

- Remove records with missing Customer IDs.
- Remove transactions with zero or negative quantities.
- Remove transactions with zero or negative unit prices.
- Convert Customer ID into integer format.
- Extract city information from the Area column.
- Calculate the total value of each transaction.

**Total Price = Quantity × Unit Price**

These operations help remove invalid records and prepare the dataset for further analysis.

### 2. RFM Analysis

RFM analysis is used to evaluate customer purchasing behavior through three important metrics.

| Metric | Description |
|---|---|
| Recency | Number of days since the customer's last purchase |
| Frequency | Total number of unique orders placed by the customer |
| Monetary | Total amount spent by the customer |

These metrics provide a simple way to understand customer engagement, purchasing frequency, and spending behavior.

### 3. Data Transformation and Feature Scaling

Customer purchasing data can contain highly skewed values, particularly in the Monetary feature.

To reduce the impact of extreme values, a logarithmic transformation using `log1p()` is applied to the RFM features.

After transformation, `StandardScaler` is used to standardize the features so that Recency, Frequency, and Monetary contribute on a comparable scale during clustering.

### 4. Finding the Optimal Number of Clusters

Before applying K-Means, two evaluation techniques are used to determine a suitable number of clusters.

**Elbow Method**

The Elbow Method evaluates how the within-cluster sum of squares (inertia) changes as the number of clusters increases. It helps identify a point where adding more clusters provides diminishing improvements.

**Silhouette Score**

The Silhouette Score measures how well customers fit within their assigned clusters compared to other clusters. A higher score generally indicates better-separated and more cohesive clusters.

Both techniques are considered when selecting the number of clusters.

### 5. K-Means Clustering

K-Means is used to group customers based on their transformed and standardized RFM values.

Current model configuration:

- Number of clusters: 4
- Random state: 42
- Initialization: 10

Each customer is assigned to one of four clusters based on purchasing behavior.

### 6. Customer Segment Identification

After clustering, the average Recency, Frequency, and Monetary values of each cluster are analyzed to assign understandable customer segment names.

The four customer segments are:

| Customer Segment | Description |
|---|---|
| Big Spenders | Customers with relatively high total spending |
| Loyal Regulars | Customers who purchase frequently and demonstrate regular buying behavior |
| New Customers | Customers with relatively few orders and recent purchasing activity |
| Occasional / At-Risk Buyers | Customers with longer periods since their last purchase and less frequent activity |

These names make the machine learning results easier to interpret from a business perspective.

### 7. PCA Visualization

Principal Component Analysis (PCA) is applied to reduce the three-dimensional RFM feature space into two principal components.

The resulting two-dimensional representation is used to visualize customer clusters through a scatter plot.

This makes it easier to observe how customers are distributed and how different segments are separated from one another.

**Note:** PCA is used for visualization, while K-Means performs the actual customer clustering.

### 8. Additional Customer Analysis

Along with the main clustering results, the project performs additional analysis to understand customer behavior.

The analysis includes:

- Average recency by customer segment.
- Average number of orders by customer segment.
- Average spending by customer segment.
- Customer distribution by city and segment.
- Identification of the top three cities for each customer segment.
- Customer-level segmentation summaries.

### 9. JSON Report Generation

After completing the analysis, the program generates a JSON file named `customer_segments.json`.

The file contains customer-level segmentation information and summaries of the identified customer groups.

This makes the results easier to reuse in future applications, dashboards, or business analysis.

## Dataset Information

**Dataset:** `online_retail.csv`

The dataset contains retail transaction information with the following columns:

| Column | Description |
|---|---|
| InvoiceNo | Unique transaction or invoice number |
| InvoiceDate | Date and time of the transaction |
| CustomerID | Customer identification number |
| Quantity | Number of products purchased |
| UnitPrice | Price per product |
| Area | Customer location or city information |

**Currency:** Bangladeshi Taka (BDT)

The project treats the dataset as a Bangladesh retail dataset, with monetary values represented in BDT.

## Project Results

After data cleaning, preprocessing, and customer segmentation, the current execution produced the following results:

| Evaluation Metric | Result |
|---|---:|
| Total Customers | 650 |
| Average Recency | 104.9 days |
| Average Frequency | 8.3 orders |
| Average Monetary Value | Tk 240,537.6 |
| Number of Clusters | 4 |

### Customer Purchasing Statistics

| Statistic | Recency (Days) | Frequency (Orders) | Monetary (BDT) |
|---|---:|---:|---:|
| Minimum | 1 | 1 | 739.2 |
| Maximum | 357 | 40 | 1,867,086.0 |
| Average | 104.9 | 8.3 | 240,537.6 |

These results provide an overview of customer purchasing behavior and demonstrate how transaction data can be converted into meaningful customer segments.

## Business Applications

Customer segmentation can help marketing teams develop more targeted marketing strategies.

| Customer Segment | Suggested Marketing Strategy |
|---|---|
| Big Spenders | Offer VIP memberships, exclusive discounts, and premium services. |
| Loyal Regulars | Introduce loyalty points, rewards, and personalized promotions. |
| New Customers | Provide welcome discounts and encourage repeat purchases. |
| Occasional / At-Risk Buyers | Launch targeted campaigns, special offers, and win-back promotions. |

By understanding the characteristics of each group, businesses can improve customer engagement, allocate marketing resources more effectively, and develop better customer retention strategies.

## AI Assistance & Acknowledgement

I used AI tools as a learning and research assistant during the development of this project.

AI assistance helped me with:

- Exploring and refining the initial project idea.
- Finding and understanding suitable CSV datasets for customer segmentation.
- Comparing different machine learning approaches and selecting an appropriate clustering algorithm for the project.
- Understanding the concepts behind RFM analysis, K-Means clustering, and PCA.
- Exploring possible improvements and approaches to the project workflow.

The final project implementation, data preprocessing, model execution, result analysis, and understanding of the overall workflow were part of my own development and learning process.

I used AI as a supporting tool to improve my understanding and explore different approaches, rather than relying on it as a replacement for learning and implementation.

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

Place the `online_retail.csv` file inside the project directory.

### 5. Run the Project

```bash
python customer_segmentation.py
```

The program will execute the complete customer segmentation workflow and display:

- Clustering evaluation charts.
- PCA customer cluster visualization.
- Customer segment analysis charts.
- Customer distribution by city.
- Final customer segmentation results.

It will also generate:

`customer_segments.json`

This file contains customer-level segmentation results and summaries of each customer segment.

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

Some possible improvements for this project include:

- Experimenting with other clustering algorithms such as DBSCAN and Hierarchical Clustering.
- Improving automatic customer segment identification.
- Developing an interactive dashboard using Streamlit.
- Introducing Customer Lifetime Value (CLV) analysis.
- Applying predictive analytics to understand future customer purchasing behavior.
- Developing a recommendation system based on customer purchasing patterns.

## Conclusion

This project demonstrates how RFM analysis and unsupervised machine learning can be used together to understand customer purchasing behavior and identify meaningful customer segments.

By applying data preprocessing, feature scaling, K-Means clustering, and PCA visualization, raw transaction data can be transformed into useful business insights.

The project also provided practical experience with Python, data analysis, machine learning, clustering techniques, and data visualization.

**Developed as a Machine Learning and Data Analysis Portfolio Project.**
