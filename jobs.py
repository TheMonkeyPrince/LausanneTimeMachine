import pandas as pd
import os
import glob

FIELD_JOB = "chef_vocation"
FOLDER_PATH = "recensements"




census = []

# Read all CSV files from the folder and store them in the list
for file in glob.glob(os.path.join(FOLDER_PATH, "*.csv")):
    df = pd.read_csv(file, sep=';')
    census.append(df)

# Extract unique job titles from all DataFrames
all_jobs = set()
for df in census:
    if "chef_vocation" in df.columns:
        all_jobs.update(df[FIELD_JOB].dropna().unique())

# Create a DataFrame with the unique job titles
jobs_df = pd.DataFrame({"jobs": list(all_jobs)})

# Save the jobs DataFrame to a CSV file
jobs_df.to_csv("jobs.csv", index=False)

print(f"Number of CSV files read: {len(census)}")
print(f"Number of unique jobs found: {len(all_jobs)}")
print("jobs.csv has been created successfully.")
