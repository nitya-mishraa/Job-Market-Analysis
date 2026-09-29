import pandas as pd
import sqlite3

# Load the cleaned CSV files
jobs_df = pd.read_csv("data_cleaned/jobs_cleaned.csv")
skills_df = pd.read_csv("data_cleaned/skills_long_format.csv")

# Create (or connect to) a SQLite database file
conn = sqlite3.connect("sql_queries/job_market.db")

# Write both dataframes as tables inside the database
jobs_df.to_sql("jobs", conn, if_exists="replace", index=False)
skills_df.to_sql("skills", conn, if_exists="replace", index=False)

print("Database created successfully at sql_queries/job_market.db")
print("Tables created: 'jobs' and 'skills'")

# Quick sanity check - run a simple query to confirm it worked
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM jobs")
job_count = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM skills")
skill_count = cursor.fetchone()[0]

print(f"\nSanity check:")
print(f"Jobs table has {job_count} rows")
print(f"Skills table has {skill_count} rows")

conn.close()