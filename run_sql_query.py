import sqlite3
import pandas as pd

conn = sqlite3.connect("sql_queries/job_market.db")

query = """
SELECT 
    s.skill, 
    COUNT(*) AS mention_count
FROM skills s
JOIN jobs j ON s.job_id = j.job_id
WHERE j.primary_location = 'Bengaluru'
GROUP BY s.skill
ORDER BY mention_count DESC
LIMIT 10;
"""
# Query: Average minimum experience required for jobs mentioning each top skill
query2 = """
SELECT 
    s.skill,
    ROUND(AVG(j.min_experience), 1) AS avg_min_experience,
    COUNT(*) AS job_count
FROM skills s
JOIN jobs j ON s.job_id = j.job_id
WHERE j.min_experience IS NOT NULL
GROUP BY s.skill
HAVING job_count >= 15
ORDER BY job_count DESC
LIMIT 10;
"""

result2 = pd.read_sql_query(query2, conn)
print("\nAverage experience required, by skill (only skills appearing 15+ times):")
print(result2)

# Query: Experience level distribution - how many jobs are truly "fresher friendly" (0 min experience)?
query3 = """
SELECT 
    CASE 
        WHEN min_experience = 0 THEN 'Fresher (0 yrs)'
        WHEN min_experience BETWEEN 1 AND 2 THEN '1-2 yrs'
        WHEN min_experience BETWEEN 3 AND 5 THEN '3-5 yrs'
        ELSE '5+ yrs'
    END AS experience_bucket,
    COUNT(*) AS job_count
FROM jobs
WHERE min_experience IS NOT NULL
GROUP BY experience_bucket
ORDER BY job_count DESC;
"""

result3 = pd.read_sql_query(query3, conn)
print("\nJob distribution by experience level:")
print(result3)
result = pd.read_sql_query(query, conn)
print("Top 10 skills in Bengaluru:")
print(result)

conn.close()