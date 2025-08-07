# EliteVideo Data Pipeline

This project simulates a video rental store data pipeline using **Excel**, **Python**, and **SQLite**. It demonstrates how to extract, clean, and load structured data from multiple Excel sheets into a relational database for analysis.

---

## Tools Used

- **Python** for scripting (ETL)
- **Pandas** for data cleaning
- **SQLite** for storing structured data
- **Excel** as the data source

---

## What It Does

- Loads data from multiple Excel tabs (e.g., customers, rentals, movies)
- Cleans and standardizes column names
- Removes duplicates and handles missing values
- Creates a normalized SQLite database with primary/foreign key constraints
- Inserts cleaned data into appropriate tables

---

## Setup

1. Install dependencies:

   ```bash
   pip install pandas openpyxl
2. Run the ETL script
   
   ```bash
   python scripts/load_data.py
3. Open movies.db in SQLite or DBrowser.
