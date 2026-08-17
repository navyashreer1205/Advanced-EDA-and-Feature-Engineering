# Advanced-EDA-and-Feature-Engineering
Advanced EDA &amp; Feature Engineering, is developed as part of the DecodeLabs Industrial Training Program and focuses on transforming a raw, unstructured e-commerce dataset into a clean, machine-learning-ready dataset through statistical analysis and data preprocessing.

## Overview

This project was developed as part of the **DecodeLabs Industrial Training Program** and focuses on transforming a raw e-commerce dataset into a clean, machine-learning-ready dataset using **Exploratory Data Analysis (EDA)** and **Feature Engineering**.

The project demonstrates the complete data preprocessing pipeline, including handling missing values, statistical data cleaning, outlier detection using the **Interquartile Range (IQR)** method, visualization, and creation of predictive features for future machine learning applications.

## Objectives

- Clean and preprocess raw data
- Handle missing values using statistical imputation
- Perform Exploratory Data Analysis (EDA)
- Detect and remove outliers using IQR
- Engineer meaningful predictive features
- Export a final machine-learning-ready dataset

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Visual Studio Code

## Project Structure

```text
Advanced-EDA-and-Feature-Engineering/
│
├── dataset/
│   └── final_feature_engineered_dataset.csv
│
├── output/
│   ├── product_distribution.png
│   ├── unit_price_histogram.png
│   └── unit_price_boxplot.png
│
├── src/
│   ├── main.py
│   └── eda.py
│
├── .gitignore
└── README.md
```

## Features Engineered

- **PricePerItem** – Calculates the price of each item.
- **HighValueOrder** – Identifies orders above ₹1000.
- **OrderMonth** – Extracts the purchase month from the order date.

## Outputs

- Cleaned dataset (`final_feature_engineered_dataset.csv`)
- Product distribution visualization
- Unit price histogram
- Boxplot for outlier analysis
- Python scripts for reproducible data preprocessing

## Author

**Navyashree R**
