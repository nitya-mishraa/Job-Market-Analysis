-- Query 1: Which cities have the most Data Analyst job openings?
SELECT 
    primary_location, 
    COUNT(*) AS job_count
FROM jobs
GROUP BY primary_location
ORDER BY job_count DESC
LIMIT 10;

-- Query 2: Top 15 most in-demand skills overall
SELECT 
    skill, 
    COUNT(*) AS mention_count
FROM skills
GROUP BY skill
ORDER BY mention_count DESC
LIMIT 15;

-- Query 3: Top 5 skills specifically in Bengaluru (JOIN example)
SELECT 
    s.skill, 
    COUNT(*) AS mention_count
FROM skills s
JOIN jobs j ON s.job_index = j."Unnamed: 0"
WHERE j.primary_location = 'Bengaluru'
GROUP BY s.skill
ORDER BY mention_count DESC
LIMIT 5;