import pandas as pd
from db_connection import get_connection

conn = get_connection()

query = "SELECT * FROM customers"

df = pd.read_sql(query, conn)

print("\nTOTAL CUSTOMERS")
print(len(df))

print("\nCHURN RATE")
print(round(df["Exited"].mean() * 100, 2), "%")

print("\nCHURN BY GEOGRAPHY")
print(
    df.groupby("Geography")["Exited"]
      .mean()
      .sort_values(ascending=False)
)

print("\nCHURN BY GENDER")
print(
    df.groupby("Gender")["Exited"]
      .mean()
)

print("\nACTIVE VS INACTIVE")
print(
    df.groupby("IsActiveMember")["Exited"]
      .mean()
)

conn.close()