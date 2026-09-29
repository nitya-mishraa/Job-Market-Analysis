# Job-Market-Analysis

# 📊 Data Analyst Job Market Analysis — India (2026)

## 📌 Overview
An end-to-end data analysis project examining the current job market for Data Analyst roles in India. Data was scraped live from Naukri.com, cleaned and analyzed using Python and SQL, and visualized in an interactive Power BI dashboard.

## 🎯 Objective
To identify:
- Which cities have the highest demand for Data Analysts
- The most in-demand skills for freshers and experienced professionals
- Experience level distribution across job postings
- Actionable insights for freshers deciding which skills to prioritize

## 🛠️ Tools & Technologies
- **Python** — Selenium, BeautifulSoup, Pandas (web scraping & data cleaning)
- **SQLite** — Data storage and SQL analysis (JOINs, aggregations, CASE statements, HAVING clauses)
- **Power BI** — Interactive dashboard and data visualization

## 📁 Dataset
298 unique Data Analyst job postings scraped from Naukri.com, covering:
- Job Title
- Company Name
- Experience Required
- Location
- Required Skills

## 🔍 Key Insights
- 🏙️ **Bengaluru** leads with the highest number of Data Analyst openings (60 jobs, ~20% of total)
- 🧠 **Data Analysis, Data Analytics, Python, Power BI, and SQL** are the top 5 most in-demand skills
- 🎓 **72 jobs (24%)** are fresher-friendly with 0 years of experience required
- 📈 Average experience required for Power BI-related roles is approximately 2.7 years
- 📊 **Data Visualization** roles require the least average experience (1.8 years) — a great entry point for freshers

## 📷 Dashboard Preview
*(Add your Power BI dashboard screenshot here once uploaded — see instructions below)*

## 🧱 Project Workflow
1. **Data Collection** — Scraped live job listings from Naukri.com using Selenium (handles JavaScript-rendered content)
2. **Data Cleaning** — Removed duplicates, parsed experience ranges into numeric fields, standardized location names, normalized skill names using Python/Pandas
3. **SQL Analysis** — Loaded cleaned data into SQLite; wrote queries using JOINs, GROUP BY, CASE WHEN, and HAVING to extract insights
4. **Visualization** — Built an interactive Power BI dashboard with KPI cards, bar charts, maps, and donut charts

## 📂 Project Structure
job-market-analysis/
├── data_raw/ # Raw scraped data (CSV)
├── data_cleaned/ # Cleaned datasets (jobs + skills long-format)
├── sql_queries/ # SQLite database + SQL analysis queries
├── powerbi_dashboard/ # Power BI (.pbix) file + dashboard screenshot
├── scrape_jobs.py # Web scraping script (Selenium)
├── clean_data.py # Data cleaning & transformation script
├── create_database.py # SQLite database creation script
├── run_sql_query.py # SQL query execution script
└── README.md


## 🚀 How to Run This Project
1. Clone this repository:
   git clone https://github.com/nitya-mishraa/Job-Market-Analysis.git

2. Install required libraries:

pip install requests beautifulsoup4 pandas selenium webdriver-manager

3. Run the scripts in order:

python scrape_jobs.py
python clean_data.py
python create_database.py
python run_sql_query.py

4. Open `powerbi_dashboard/job_market_dashboard.pbix` in Power BI Desktop to explore the interactive dashboard

## 📌 Future Improvements
- Expand dataset to 1000+ listings for deeper statistical significance
- Add salary analysis (where data is available)
- Automate scraping on a weekly schedule to track trends over time
- Deploy dashboard using Power BI Service for public sharing

## 👤 Author
Made by Nitya Mishra — as part of building practical, real-world data analytics skills.

---
⭐ If you found this project helpful, feel free to star this repo!
