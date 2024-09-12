

 Overview

This project aims to perform customer segmentation for Walmart using historical sales data. By analyzing customer purchasing behavior, we can identify distinct customer groups and provide insights to improve marketing strategies, product placements, and overall customer experience.

 Objectives

- To segment Walmart customers into distinct groups based on their purchasing behavior and other related factors.
- To provide actionable insights and recommendations for targeted marketing strategies.

 Dataset

The dataset used for this project contains the following features:

- *Store*: The store number.
- *Date*: The week of sales.
- *Weekly_Sales*: Sales for the given store.
- *Holiday_Flag*: Indicator of whether the week is a special holiday (1 for Holiday week, 0 for Non-holiday week).
- *Temperature*: Temperature on the day of sale.
- *Fuel_Price*: Cost of fuel in the region.
- *CPI*: Consumer price index.
- *Unemployment*: Unemployment rate.

 Data Source

- The dataset is publicly available on [Kaggle](https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting/data).

Project Structure

The repository is organized as follows:


├── data
│   └── walmart_sales_data.csv  # The main dataset
├── notebooks
│   └── customer_segmentation.ipynb  # Jupyter Notebook containing the full code
├── outputs
│   └── walmart_customer_segments.csv  # Output file containing customer segments
├── README.md  # Project README file
└── requirements.txt  # Required libraries and dependencies

Usage

1. *Download the Dataset:*

   Download the dataset from the [Kaggle link](https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting/data) and save it to the data/ directory as walmart_sales_data.csv.

2. *Run the Analysis:*

   Open the Jupyter Notebook customer_segmentation.ipynb located in the notebooks/ folder and run each cell step-by-step to perform the segmentation analysis.

   Alternatively, you can run the script in any Python environment:

   bash
   python customer_segmentation.py
   

3. *View the Results:*

   The segmented customer data will be saved in the outputs/ folder as walmart_customer_segments.csv.

 Results

- *Clusters Identified*: The K-Means algorithm was applied, and the optimal number of clusters was determined using the Elbow Method.
- *Insights*: The project identified key customer segments based on purchasing behavior and other factors such as fuel price sensitivity and holiday impact.

 Business Impact

- *Targeted Marketing*: Personalized promotions for different customer groups.
- *Product Placement*: Optimize store layouts based on customer preferences.
- *Customer Retention*: Develop loyalty programs for high-value customers.

 Future Enhancements

- Incorporate more data features, such as customer demographics or online purchase data.
- Experiment with other clustering algorithms like Hierarchical Clustering or DBSCAN.
- Develop interactive dashboards using Tableau, Power BI, or Dash.

 Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions or improvements.


 Acknowledgements

- Special thanks to Walmart and Kaggle for providing the dataset.
- Inspiration from various data science communities and open-source contributors.


