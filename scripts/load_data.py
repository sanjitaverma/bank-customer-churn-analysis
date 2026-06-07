import pandas as pd
from db_connection import get_connection

print("Reading CSV...")

df = pd.read_csv("data/Churn_Modelling.csv")

print("Rows found:", len(df))

conn = get_connection()

print("Connected to MySQL!")

cursor = conn.cursor()

query = """
INSERT INTO customers (
    RowNumber,
    CustomerId,
    Surname,
    CreditScore,
    Geography,
    Gender,
    Age,
    Tenure,
    Balance,
    NumOfProducts,
    HasCrCard,
    IsActiveMember,
    EstimatedSalary,
    Exited
)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

for _, row in df.iterrows():
    cursor.execute(query, tuple(row))

conn.commit()

print("Data Loaded Successfully!")

cursor.close()
conn.close()
