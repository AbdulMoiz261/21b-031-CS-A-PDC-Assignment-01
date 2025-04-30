# Student Fee Tracker

A Python-based project to simulate student fee records using synthetic data, export them to CSV files, and analyze payment trends using both linear and parallel processing techniques.

## 📂 Features

- Generates `students.csv` with random student names, IDs, and fee status (paid/unpaid)
- Generates `fees.csv` for students who have paid, including random payment dates
- Performs analysis on payment dates to compute frequency of payments
- Includes:
  - **Linear processing** using Pandas and Counter
  - **Parallel processing** using ThreadPoolExecutor

## 🧪 Technologies Used

- Python 3
- [Faker](https://faker.readthedocs.io/) (for synthetic data generation)
- Pandas
- Collections
- ThreadPoolExecutor (for parallelism)
