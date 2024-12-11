#!/usr/bin/env python
# coding: utf-8

# # CSV FILES

# In[2]:


import pandas as pd
import random
from faker import Faker

faker = Faker()

num_students = 1000

students_data = {
    "Student Name": [faker.name() for _ in range(num_students)],
    "Student ID": [f"SID{1000 + i}" for i in range(num_students)],
    "Status": [random.choice([True, False]) for _ in range(num_students)]  # True = fees paid, False = not paid
}

students_df = pd.DataFrame(students_data)

students_df.to_csv("students.csv", index=False)

fees_data = {
    "Student ID": [student_id for student_id, paid in zip(students_df['Student ID'], students_df['Status']) if paid],
    "Payment Date": [f"2024-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}" for _ in range(len([x for x in students_df['Status'] if x]))]
}

fees_df = pd.DataFrame(fees_data)

fees_df.to_csv("fees.csv", index=False)

print("CSV files (students.csv and fees.csv) generated successfully.")


# # LINEAR CODE

# In[4]:


import pandas as pd
from collections import Counter
import time

students_df = pd.read_csv("students.csv")
fees_df = pd.read_csv("fees.csv")

start_time = time.time()

matched_dates = []
for _, student in students_df.iterrows():
    student_id = student["Student ID"]
    if student["Status"]:  
        fee_record = fees_df[fees_df["Student ID"] == student_id]
        if not fee_record.empty:
            matched_dates.append(fee_record["Payment Date"].values[0])

date_frequency = Counter(matched_dates)

date_frequency_df = pd.DataFrame(date_frequency.items(), columns=["Payment Date", "Frequency"])
date_frequency_df = date_frequency_df.sort_values(by="Frequency", ascending=False).reset_index(drop=True)

end_time = time.time()

print("Linear Processing Results:")
print(date_frequency_df)
print("Execution Time:", end_time - start_time, "seconds")


# # PARALLEL CODE

# In[10]:


import pandas as pd
from concurrent.futures import ThreadPoolExecutor

# Sample Data (adjust based on your actual data)
data = {
    "student_id": [1, 2, 3, 4, 5],
    "status": [True, False, True, True, False]
}

students_df = pd.DataFrame(data)

student_payment_dates = {
    1: "2024-01-01",
    2: "2024-01-02",
    3: "2024-01-03",
    4: "2024-01-04",
    5: "2024-01-05"
}

def process_student(student_id, status):
    if status:
        return student_payment_dates.get(student_id, None)
    return None

with ThreadPoolExecutor() as executor:
    matched_dates = list(executor.map(process_student, students_df["student_id"], students_df["status"]))

matched_dates = [date for date in matched_dates if date is not None]

print(matched_dates)

