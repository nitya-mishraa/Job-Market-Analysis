import pandas as pd
import re

# Load the raw scraped data
df = pd.read_csv("data_raw/naukri_data_analyst_jobs.csv")

print("Original shape:", df.shape)
print(df.head())# Remove exact duplicate rows (same title, company, experience, location, skills)
before = len(df)
df = df.drop_duplicates()
after = len(df)

print(f"Removed {before - after} exact duplicate rows")
print("Shape after removing duplicates:", df.shape)
# Reset index after removing duplicates, and create a clean job_id column
df = df.reset_index(drop=True)
df["job_id"] = df.index

print("Job IDs assigned. Sample:")
print(df[["job_id", "title", "company"]].head())

def parse_experience(exp_string):
    """
    Converts experience text like '0-5 Yrs' into two numbers: min and max.
    Handles edge cases like '0 Yrs' (single number) and missing values.
    """
    if pd.isna(exp_string):
        return None, None

    # Remove the word "Yrs" and extra spaces
    exp_string = exp_string.replace("Yrs", "").strip()

    # Check if it's a range like "0-5" or a single number like "0"
    if "-" in exp_string:
        parts = exp_string.split("-")
        min_exp = float(parts[0].strip())
        max_exp = float(parts[1].strip())
    else:
        min_exp = float(exp_string.strip())
        max_exp = min_exp

    return min_exp, max_exp

# Apply this function to every row in the experience column
df["min_experience"], df["max_experience"] = zip(*df["experience"].apply(parse_experience))

print(df[["experience", "min_experience", "max_experience"]].head(10))
print("\nMissing experience values:", df["min_experience"].isna().sum())

def clean_location(location_string):
    """
    Cleans location text:
    - Removes 'Hybrid - ' prefix
    - Removes bracketed area details like '(Bellandur)'
    - Takes only the first city if multiple cities are listed
    """
    if pd.isna(location_string):
        return None

    loc = location_string

    # Remove common prefixes
    loc = loc.replace("Hybrid - ", "").replace("Hybrid-", "")

    # If there are multiple cities separated by commas, take the first one
    loc = loc.split(",")[0]

    # Remove bracketed details like (Bellandur), (All Areas), etc.
    loc = re.sub(r"\(.*?\)", "", loc)

    # Remove extra whitespace
    loc = loc.strip()

    return loc

df["primary_location"] = df["location"].apply(clean_location)

print(df[["location", "primary_location"]].head(15))
print("\nUnique primary locations count:", df["primary_location"].nunique())
print("\nTop 10 locations by job count:")
print(df["primary_location"].value_counts().head(10))

# Create a separate dataframe where each skill gets its own row
# This is useful for counting which skills appear most often

skills_data = []
for index, row in df.iterrows():
    if pd.notna(row["skills"]):
        skill_list = [s.strip() for s in row["skills"].split(",")]
        for skill in skill_list:
            skills_data.append({
                "job_id": row["job_id"],
                "title": row["title"],
                "primary_location": row["primary_location"],
                "skill": skill
            })

skills_df = pd.DataFrame(skills_data)

print("Total skill mentions:", len(skills_df))
print("\nTop 20 most in-demand skills:")
print(skills_df["skill"].value_counts().head(20))

# Normalize skill names to avoid duplicates due to case differences
# e.g., "SQL", "sql" -> "Sql" all become the same
skills_df["skill"] = skills_df["skill"].str.strip().str.title()

print("Top 20 most in-demand skills (after normalization):")
print(skills_df["skill"].value_counts().head(20))

# Fix specific acronyms and known skill names to look professional
skill_name_fixes = {
    "Sql": "SQL",
    "Power Bi": "Power BI",
    "Bi": "BI",
    "Ai": "AI",
    "Etl": "ETL",
    "Kpi": "KPI",
    "Api": "API",
    "Gcp": "GCP",
    "Aws": "AWS",
    "Erp": "ERP",
    "Vba": "VBA",
    "Crm": "CRM",
    "Nlp": "NLP",
    "Sas": "SAS",
    "Mis": "MIS",
    "Ssrs": "SSRS",
    "Ssis": "SSIS",
    "Dax": "DAX"
}

skills_df["skill"] = skills_df["skill"].replace(skill_name_fixes)

print("Top 20 most in-demand skills (final, cleaned):")
print(skills_df["skill"].value_counts().head(20))

# Save the cleaned main jobs dataframe (with new experience & location columns)
df.to_csv("data_cleaned/jobs_cleaned.csv", index=False)
print("\nSaved: data_cleaned/jobs_cleaned.csv")

# Save the skills long-format dataframe (one skill per row)
skills_df.to_csv("data_cleaned/skills_long_format.csv", index=False)
print("Saved: data_cleaned/skills_long_format.csv")

print("\nFinal jobs dataset shape:", df.shape)
print("Final skills dataset shape:", skills_df.shape)