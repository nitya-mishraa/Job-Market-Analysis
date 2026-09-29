from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Setup browser
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

all_jobs = []

# We will scrape multiple pages (Naukri uses -2, -3, etc. in URL for pagination)
base_url = "https://www.naukri.com/data-analyst-jobs"
num_pages = 15

for page in range(1, num_pages + 1):
    if page == 1:
        url = base_url
    else:
        url = f"{base_url}-{page}"

    print(f"Scraping page {page}: {url}")
    
    try:
        driver.get(url)
        time.sleep(4)

        job_cards = driver.find_elements(By.CLASS_NAME, "cust-job-tuple")
        print(f"Found {len(job_cards)} jobs on page {page}")

        for card in job_cards:
            try:
                title = card.find_element(By.CLASS_NAME, "title").text
            except:
                title = None

            try:
                company = card.find_element(By.CLASS_NAME, "comp-name").text
            except:
                company = None

            try:
                experience = card.find_element(By.CLASS_NAME, "expwdth").text
            except:
                experience = None

            try:
                location = card.find_element(By.CLASS_NAME, "locWdth").text
            except:
                location = None

            try:
                skills_elements = card.find_elements(By.CLASS_NAME, "tag-li")
                skills = ", ".join([s.text for s in skills_elements])
            except:
                skills = None

            all_jobs.append({
                "title": title,
                "company": company,
                "experience": experience,
                "location": location,
                "skills": skills
            })
    except Exception as e:
        print(f"Error on page {page}: {e} - skipping this page")

    time.sleep(2)  # polite delay before next page

driver.quit()

# Save to CSV
df = pd.DataFrame(all_jobs)
df.to_csv("data_raw/naukri_data_analyst_jobs.csv", index=False)
print(f"Done! Saved {len(df)} jobs to data_raw/naukri_data_analyst_jobs.csv")