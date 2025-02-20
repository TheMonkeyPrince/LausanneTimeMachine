import pandas as pd
import os
import glob

FIELD_JOB = "chef_vocation"
FOLDER_PATH = "recensements"




census = []

# # Read all CSV files from the folder and store them in the list
# for file in glob.glob(os.path.join(FOLDER_PATH, "*.csv")):
#     df = pd.read_csv(file, sep=';')
#     census.append(df)

census.append(pd.read_csv("recensements/1810.csv", sep=';'))

# Extract unique job titles from all DataFrames
all_jobs = {}
for df in census:
    if FIELD_JOB in df.columns:
        # Split jobs separated by '|' and count occurrences
        job_series = df[FIELD_JOB].dropna().str.split('|').explode()
        job_counts = job_series.value_counts()
        
        for job, count in job_counts.items():
            job = job.strip()  # Remove leading/trailing whitespace
            if job in all_jobs:
                all_jobs[job] += count
            else:
                all_jobs[job] = count

# Create a DataFrame with the unique job titles and their counts
jobs_df = pd.DataFrame(list(all_jobs.items()), columns=['jobs', 'count'])

# Sort the DataFrame by count in descending order
jobs_df = jobs_df.sort_values('count', ascending=False).reset_index(drop=True)

# Save the jobs DataFrame to a CSV file
jobs_df.to_csv("jobs.csv", index=False)

print(f"Number of CSV files read: {len(census)}")
print(f"Number of unique jobs found: {len(jobs_df)}")
print("jobs.csv has been created successfully.")