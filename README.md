# Customer Segmentation Using RFM, K-Means Clustering & PCA

A Python-based Machine Learning project that analyzes customer purchasing behavior and identifies meaningful customer groups using **RFM Analysis (Recency, Frequency, Monetary)** and **K-Means Clustering**.

The project uses historical retail transaction data to understand customer engagement, purchasing frequency, and spending patterns. Based on these characteristics, customers are grouped into four segments: Big Spenders, Loyal Regulars, New Customers, and Occasional / At-Risk Buyers.

Additionally, **Principal Component Analysis (PCA)** is applied to reduce the dimensionality of customer data and visualize the resulting clusters in a 2D scatter plot.

The main goal of this project is to demonstrate how data analysis and unsupervised machine learning can help businesses understand their customers and make better marketing decisions.

## 📌 Project Overview

Understanding customer purchasing behavior is important for businesses that want to improve customer retention, increase sales, and develop effective marketing strategies.

This project applies RFM analysis to evaluate customers based on three key purchasing metrics:

- **Recency:** How recently a customer made a purchase.
- **Frequency:** How frequently a customer places orders.
- **Monetary:** How much money a customer spends.

After calculating these metrics, the customer data is transformed, standardized, and processed using K-Means clustering to identify groups with similar purchasing behavior.

PCA is then used to visualize the identified customer groups and make the clustering results easier to understand.

## 🎯 Project Objectives

The main objectives of this project are:

- Analyze customer purchasing behavior using RFM analysis.
- Identify meaningful customer segments using K-Means clustering.
- Determine a suitable number of clusters using the Elbow Method and Silhouette Score.
- Apply logarithmic transformation and feature scaling to improve clustering performance.
- Visualize customer clusters using Principal Component Analysis.
- Analyze customer distribution across different cities.
- Compare purchasing characteristics across customer segments.
- Identify the top three cities for each customer segment.
- Generate customer-level segmentation reports in JSON format.
- Explore how customer segmentation can support targeted marketing strategies.

## ⚙️ Technologies and Libraries Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Scikit-learn | Machine learning and preprocessing |
| K-Means | Customer clustering |
| PCA | Dimensionality reduction and visualization |
| StandardScaler | Feature standardization |

## 🔄 Project Workflow

### 1. Data Loading and Cleaning

The project uses an online retail transaction dataset named `online_retail.csv`.

Before performing customer segmentation, the dataset goes through several preprocessing and cleaning operations.

The cleaning process includes:

- Removing records with missing Customer IDs.
- Removing transactions with zero or negative quantities.
- Removing transactions with zero or negative unit prices.
- Converting Customer ID into integer format.
- Extracting city information from the Area column.
- Calculating the total monetary value of each transaction.

The transaction value is calculated using the following formula:

\[
\text{Total Price} = \text{Quantity} \times \text{Unit Price}
\]

These operations help remove invalid transaction records and prepare the dataset for customer-level analysis.

### 2. RFM Analysis

RFM analysis is used to understand customer purchasing behavior through three important metrics.

| Metric | Description |
|---|---|
| Recency | Number of days since the customer's last purchase |
| Frequency | Total number of unique orders placed by the customer |
| Monetary | Total amount spent by the customer |

Each customer receives three RFM values based on their transaction history.

These values provide an overview of customer engagement, purchasing frequency, and spending behavior.

### 3. Data Transformation and Feature Scaling

Customer purchasing data often contains highly skewed values, especially in the Monetary feature.

To reduce the impact of extreme values, the project applies a logarithmic transformation using `log1p()` to the RFM features.

After transformation, `StandardScaler` is used to standardize the features.

This ensures that Recency, Frequency, and Monetary contribute on a comparable scale during the clustering process.

The preprocessing steps are:

1. Calculate customer-level RFM values.
2. Apply logarithmic transformation using `log1p()`.
3. Standardize the transformed features using `StandardScaler`.

### 4. Finding the Optimal Number of Clusters

Before applying K-Means, the project uses two evaluation techniques to identify a suitable number of customer clusters.

**Elbow Method**

The Elbow Method evaluates how the Within-Cluster Sum of Squares (WCSS), also known as inertia, changes as the number of clusters increases.

It helps identify the point where adding more clusters provides diminishing improvements in clustering performance.

**Silhouette Score**

The Silhouette Score measures how well customers fit within their assigned clusters compared to other clusters.

A higher score generally indicates better-separated and more cohesive clusters.

Both methods are considered when selecting the number of clusters for the final model.

### 5. K-Means Clustering

K-Means is used to group customers based on their transformed and standardized RFM values.

The algorithm groups customers with similar purchasing characteristics into the same cluster.

**Model Configuration:**

- Algorithm: `KMeans`
- Number of clusters: 4
- Random state: 42
- Initialization: 10

Each customer is assigned to one of four clusters based on their purchasing behavior.

### 6. Customer Segment Identification

After clustering, the average Recency, Frequency, and Monetary values of each cluster are analyzed to understand the purchasing characteristics of the customers.

Based on these characteristics, the four clusters are assigned business-friendly names.

| Customer Segment | Description |
|---|---|
| Big Spenders | Customers with relatively high total spending |
| Loyal Regulars | Customers who purchase frequently and demonstrate regular buying behavior |
| New Customers | Customers with relatively few orders and recent purchasing activity |
| Occasional / At-Risk Buyers | Customers with longer periods since their last purchase and less frequent activity |

These labels make the machine learning results easier to interpret from a business perspective.

### 7. PCA Visualization

Principal Component Analysis (PCA) is applied to reduce the three-dimensional RFM feature space into two principal components.

The resulting two-dimensional representation is used to visualize customer clusters through a scatter plot.

This helps identify:

- How customers are distributed across different clusters.
- How closely related customer groups are.
- How clearly the identified segments are separated.
- Whether different clusters contain similar or distinct purchasing patterns.

**Important:** PCA is used for dimensionality reduction and visualization. K-Means performs the actual customer clustering using the processed RFM features.

### 8. Additional Customer Analysis

Along with the main clustering results, the project performs additional analysis to better understand customer behavior.

The analysis includes:

- Average recency by customer segment.
- Average number of orders by customer segment.
- Average spending by customer segment.
- Customer distribution by city and segment.
- Identification of the top three cities for each customer segment.
- Customer-level segmentation summaries.

These additional analyses provide more detailed insights into the purchasing characteristics of each customer group.

### 9. JSON Report Generation

After completing the analysis, the program generates a JSON file named `customer_segments.json`.

The file contains customer-level segmentation information and summaries of the identified customer groups.

The generated report can be reused in future applications, dashboards, or additional business analysis without repeating the entire segmentation process.

## 📂 Dataset Information

**Dataset Name:** `online_retail.csv`

The dataset contains historical retail transaction information with the following columns:

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

## 📊 Project Results

After data cleaning, preprocessing, and customer segmentation, the current execution produced the following results:

### Overall Customer Statistics

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

These results provide an overview of customer purchasing behavior and demonstrate how historical transaction data can be converted into meaningful customer segments.

*Note: These are example results from the current execution. Actual results may vary depending on the dataset and preprocessing configuration.*

## 📈 Data Visualization

The project generates multiple visualizations to explore customer purchasing patterns and clustering results.

The visualizations include:

- Elbow Method graph for selecting the number of clusters.
- Silhouette Score comparison.
- PCA scatter plot showing customer clusters.
- Average recency by customer segment.
- Average frequency by customer segment.
- Average monetary value by customer segment.
- Customer distribution by city and segment.

These visualizations make it easier to understand the differences between customer groups and identify important purchasing patterns.

## 💼 Business Applications

Customer segmentation can help marketing teams develop more targeted campaigns and improve customer engagement.

Based on the identified customer groups, the following marketing strategies can be considered:

| Customer Segment | Suggested Marketing Strategy |
|---|---|
| Big Spenders | Offer VIP memberships, exclusive discounts, and premium services. |
| Loyal Regulars | Introduce loyalty points, rewards, and personalized promotions. |
| New Customers | Provide welcome discounts and encourage repeat purchases. |
| Occasional / At-Risk Buyers | Launch targeted campaigns, special offers, and win-back promotions. |

By understanding the characteristics of each customer group, businesses can:

- Improve customer retention.
- Develop personalized marketing campaigns.
- Identify high-value customers.
- Encourage repeat purchases.
- Allocate marketing resources more effectively.
- Improve overall customer engagement.

## 🤝 AI Assistance & Acknowledgement

During the development of this project, I used AI tools as a supporting resource for research, planning, and technical guidance.

AI assistance was mainly used for:

- Exploring and refining the initial customer segmentation project idea.
- Finding and understanding suitable CSV datasets for customer segmentation.
- Comparing different machine learning algorithms and identifying a suitable clustering approach for the project.
- Understanding RFM analysis, K-Means clustering, and PCA concepts.
- Exploring different preprocessing techniques and possible improvements to the project workflow.

I used AI as a learning and research assistant to explore different approaches and improve my understanding of the concepts involved.

The data preprocessing, implementation, model execution, visualization, and analysis were part of my project development and learning process. I also reviewed and evaluated the suggestions before applying them to the project.

## 📦 Installation and Usage

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/customer-segmentation.git
```

### 2. Navigate to the Project Directory

```bash
cd customer-segmentation
```

### 3. Install Required Libraries

```bash
pip install numpy pandas matplotlib scikit-learn
```

### 4. Prepare the Dataset

Place the `online_retail.csv` file inside the project directory.

### 5. Run the Program

```bash
python customer_segmentation.py
```

After execution, the program will perform the complete customer segmentation workflow and display:

- Clustering evaluation charts.
- PCA customer cluster visualization.
- Customer segment analysis charts.
- Customer distribution by city.
- Final customer segmentation results.

The program will also generate:

```text
customer_segments.json
```

This file contains customer-level segmentation results and summaries of the identified customer groups.

## 📁 Project Structure

```text
Customer-Segmentation/
│
├── customer_segmentation.py
├── online_retail.csv
├── Figure_1.png
├── customer_segments.json
├── README.md
└── requirements.txt
```

**File Description:**

- `customer_segmentation.py` – Main Python script containing data cleaning, RFM analysis, preprocessing, clustering, evaluation, and visualization.
- `online_retail.csv` – Retail transaction dataset used for customer analysis.
- `Figure_1.png` – Example visualization generated by the project.
- `customer_segments.json` – Generated customer segmentation report.
- `README.md` – Project documentation.
- `requirements.txt` – Required Python libraries.

## ⚠️ Limitations

The project provides a useful approach to customer segmentation, but there are some limitations:

- Customer segments depend on the quality and representativeness of the transaction dataset.
- RFM analysis considers purchasing history but does not directly capture customer preferences or product interests.
- K-Means requires selecting the number of clusters before training.
- Outliers and highly skewed purchasing behavior can influence clustering results.
- PCA simplifies the data for visualization, so some information may be lost in the two-dimensional representation.
- Customer segment names are assigned based on cluster characteristics and may require further business validation.
- The current system does not predict future customer purchases or customer lifetime value.

## 🚀 Future Improvements

Some possible improvements for this project include:

- Experimenting with other clustering algorithms such as DBSCAN and Hierarchical Clustering.
- Improving automatic customer segment identification.
- Developing an interactive dashboard using Streamlit.
- Introducing Customer Lifetime Value (CLV) analysis.
- Applying predictive analytics to estimate future customer purchasing behavior.
- Developing a recommendation system based on customer purchasing patterns.
- Including product-level purchasing behavior in customer segmentation.
- Evaluating cluster stability using different datasets and parameter configurations.

## 📝 Conclusion

This project demonstrates how RFM analysis and unsupervised machine learning can be combined to understand customer purchasing behavior and identify meaningful customer segments.

By applying data cleaning, feature transformation, standardization, K-Means clustering, and PCA visualization, raw retail transaction data can be transformed into useful business insights.

The project also provided practical experience in Python programming, data analysis, unsupervised machine learning, clustering techniques, and data visualization.

##*This project is intended for educational and research purposes. You may explore, modify, and extend it with appropriate attribution.**
