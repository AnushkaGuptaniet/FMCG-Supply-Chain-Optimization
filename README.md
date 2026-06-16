📦FMCG Supply Chain Optimization

Project Overview

This project focuses on **FMCG Supply Chain Optimization** by forecasting SKU-level product demand across distribution centers using **Data Analytics, K-Means Clustering, Logistic Regression, Random Forest, and an Interactive Streamlit Dashboard**.

The objective is to help supply chain managers optimize inventory levels, identify high-demand products, and improve warehouse operations through data-driven decision-making.

Problem Statement

Forecast SKU-level product demand across distribution centers using machine learning techniques to:

- Optimize inventory management
- Reduce stockouts and overstock situations
- Improve warehouse efficiency
- Enhance demand forecasting accuracy
- Support data-driven business decisions
  
Objectives

- Perform data cleaning and preprocessing
- Conduct Exploratory Data Analysis (EDA)
- Create demand categories (Low, Medium, High)
- Segment products using K-Means Clustering
- Build demand prediction models
- Develop an interactive Streamlit dashboard
- Generate business insights for supply chain optimization

Technologies Used

Programming Language
- Python

Libraries
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Plotly
- Streamlit
- Pickle

Machine Learning Algorithms
- K-Means Clustering
- Logistic Regression
- Random Forest Classifier

Development Environment
- Visual Studio Code (VS Code)

Dataset Description
The dataset contains FMCG warehouse and product information including:

| Feature | Description |
|----------|-------------|
| Ware_house_ID | Warehouse Identifier |
| WH_Manager_ID | Warehouse Manager Identifier |
| Location_type | Urban/Rural Location |
| WH_capacity_size | Warehouse Capacity |
| Zone | Warehouse Zone |
| SKU_ID | Product SKU Identifier |
| Product_Name | Product Name |
| Brand | Product Brand |
| Distribution_Center | Distribution Center |
| Inventory_Level | Available Inventory |
| Sales_Quantity | Product Sales Quantity |
| Price | Product Price |
| Promotion_Flag | Promotion Status |

Dataset Size:

- Rows: 25,000
- Columns: 33

Project Workflow
1. Data Cleaning

Performed:

- Missing Value Handling
- Duplicate Removal
- Date Conversion
- Data Validation

2. Exploratory Data Analysis (EDA)

Generated:

- Sales Distribution Analysis
- Inventory Distribution Analysis
- Promotion Impact Analysis
- Correlation Heatmap

3. Feature Engineering

Created:

- Year
- Month
- Day
- Demand_Category

Demand Categories:

- Low Demand
- Medium Demand
- High Demand

4. K-Means Clustering

Used features:

- Inventory_Level
- Sales_Quantity
- Price
- Promotion_Flag

Purpose:

- Product Segmentation
- Demand-Based Clustering

5. Logistic Regression

Purpose:

- Demand Category Prediction

Evaluation Metrics:

- Accuracy Score
- Confusion Matrix
- Classification Report

6. Random Forest Classifier

Purpose:

- Demand Forecasting

Benefits:

- Better Non-Linear Learning
- Feature Importance Analysis

7. Model Deployment

Trained model saved as:

Used in:

- Streamlit Dashboard
- Real-Time Demand Prediction

Dashboard Features
KPI Cards

- Total Records
- Average Sales
- Average Inventory
- Average Price

Interactive Visualizations
- Demand Category Distribution
- Promotion Impact Analysis
- Sales Quantity Analysis
- Inventory Analysis
- Product Insights

Demand Prediction System
User Inputs:
- Inventory Level
- Product Price
- Promotion Status

Output:
- Low Demand
- Medium Demand
- High Demand

Model Performance
Logistic Regression
| Metric | Value |
|----------|--------|
| Accuracy | 33.68% |

Random Forest
| Metric | Value |
|----------|--------|
| Accuracy | 33.82% |

Note:Initially, Logistic Regression achieved 100% accuracy due to data leakage (Sales_Quantity being used both in target creation and prediction). After removing leakage, realistic performance metrics were obtained.

Business Insights

- Demand categories are evenly distributed across the dataset.
- Product segmentation helps optimize inventory allocation.
- Promotional campaigns can influence sales patterns.
- Additional real-world features can significantly improve forecasting accuracy.

How to Run the Project
Clone Repository

```bash
git clone <repository-url>
cd FMCG_PROJECT




