# EliteVideo Data Pipeline

This project demonstrates a complete data pipeline for a fictional video rental store, **EliteVideo**. The pipeline uses Excel as the data source, Python for ETL (Extract, Transform, Load) operations, and SQLite as the relational database. The pipeline is designed to simulate real-world data handling and reporting processes typical in a data analyst or junior data engineering role.

---

## Project Overview

**Objective**:  
To extract and clean transactional and reference data from multiple Excel worksheets, load them into a normalized SQLite database, and enable future data analysis and visualization.

---

## Tools & Technologies

- **Python**: Data cleaning and ETL scripting
- **Pandas**: Excel data manipulation
- **SQLite**: Lightweight relational database for storage and querying
- **Excel**: Raw data source (multi-tab workbook)
- **VS Code**: Development environment

---

## Schema Overview

The database is structured in a normalized relational schema, including:

- **Customer**
- **Movie**
- **Rental**
- **DetailRental** (junction table linking rentals to movies)
- **Staff**
- **Store**
- *(More depending on provided Excel tabs)*

All tables are created with appropriate primary keys and foreign key constraints to maintain data integrity.

---

## Pipeline Workflow

1. **Load Excel Workbook**
   - Source file contains multiple worksheets (e.g., `Customer`, `Movie`, `Rental`, `DetailRental`).
   - Each sheet is loaded into a pandas DataFrame.

2. **Data Cleaning**
   - Column headers are stripped of extra spaces and standardized to lowercase with underscores.
   - Null values are handled to ensure compatibility with SQLite.
   - Duplicates are removed.

3. **Database Creation**
   - A new SQLite database (`elitevideo.db`) is created if not already present.
   - Tables are created using `CREATE TABLE` statements with appropriate datatypes and constraints.

4. **Data Insertion**
   - Cleaned DataFrames are iterated through and inserted into the database using parameterized SQL queries.
