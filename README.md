# **PhonePe Pulse - Digital Payments & User Insights Dashboard**
An interactive Streamlit dashboard built to explore and visualize PhonePe Pulse data (2018–2024), providing insights into transaction trends, app usage, insurance adoption, and regional user behavior across India.

# **Project Overview**
This project transforms JSON data from the PhonePe Pulse GitHub repo into a structured MySQL database and visualizes it through:

* 9 CSVs preprocessed from PhonePe Pulse JSON data.
* 8+ charts covering transactions, users, insurance, and geography.
* SQL-driven insights visualized using matplotlib and pandas.
* A deployed Streamlit dashboard with filters for state and year.

# **Tech Stack**
------------------------------------------------------------
|   **Component**    |           **Tools Used**             |
|--------------------|--------------------------------------|
| Programming        | Python 3.10                          |
| Visualization      | Matplotlib, Streamlit                |
| Data Handling      | pandas, NumPy                        |
| Source Data        | PhonePe Pulse (converted JSON → CSV) |
-------------------------------------------------------------

# ** Folder Structure **
```
phonepe-pulse-analysis/
├── app.py
├── aggregated_transaction.csv
├── aggregated_user.csv
├── aggregated_insurance.csv
├── map_transaction.csv
├── map_user.csv
├── map_insurance.csv
├── top_transaction.csv
├── top_user.csv
├── top_insurance.csv
├── Business Case Study.pdf
├── requirements.txt
└── colab/
    ├── phonepe.ipynb
    └── phonepe.pdf
```
# **Sample Visualizations**

1. Top 10 States by Transaction Volume :

2. Year-wise Growth of PhonePe :

3. Brand-wise Smartphone Usage :

4. Insurance-to-Transaction Ratio by State :

5. App Engagement vs User Base by Region :

