# Fraud Detection and Financial Risk Analysis

## Data Source
Dataset: Credit Card Fraud Detection (Kaggle)  
284,807 transactions  
30 features + target variable (Class)  
Fraud rate ~0.17%

## Data Preparation
Raw CSV dataset converted to Parquet format for faster analytics.  
Exploratory Data Analysis performed to identify class imbalance and key statistics.  
Feature scaling applied using StandardScaler.

## Modeling
Baseline Logistic Regression classification model.  
Train/Test split 80/20 with stratification.  
Model AUC ≈ 0.96 indicating strong separation capability.

## Evaluation Metrics
Precision ≈ 0.83  
Recall ≈ 0.63  
Decision threshold optimized to 0.15 based on expected financial loss.

## Key Findings
1 Fraud transactions represent less than 0.2% of total volume.  
2 Logistic Regression provides strong predictive performance.  
3 Threshold optimization significantly reduces expected loss.  
4 Majority of transactions fall into Low risk segment.  
5 Critical risk segment is small but financially significant.

## Business Recommendations
1 Real-time monitoring of High and Critical risk segments.  
2 Threshold tuning based on financial cost of fraud vs false alarms.  
3 Deployment of Power BI dashboard for ongoing risk tracking.

## Tools Used
Python  
Scikit-learn  
SQL-ready dataset structure  
Power BI dashboard
