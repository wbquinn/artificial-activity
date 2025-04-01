import os
import subprocess
import random
from datetime import datetime, timedelta

def generate_github_activity(repo_path, activity_date, num_commits_per_day):
    """
    Generates artificial GitHub activity by creating commits on a specific day.

    Args:
        repo_path (str): Path to the local Git repository.
        activity_date (str): date for activity (YYYY-MM-DD).
        num_commits_per_day (int): Number of commits to make per day.
    """

    activity_date = datetime.strptime(activity_date, "%Y-%m-%d")

    for _ in range(num_commits_per_day):
        date_str = activity_date.strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"activity_{random.randint(1, 1000)}.txt"
        file_path = os.path.join(repo_path, file_name)

        # Create or modify the file
        with open(file_path, "w") as f:
            f.write(f"Commit on {date_str}")

        # Add, commit, and set the commit date
        subprocess.run(["git", "add", file_name], cwd=repo_path)
        subprocess.run(["git", "commit", "-m", f"Simulated activity on {date_str}"], cwd=repo_path, env={"GIT_AUTHOR_DATE": date_str, "GIT_COMMITTER_DATE": date_str})

        # delete the file after commiting, so that the repo does not get too large.
        subprocess.run(["git", "rm", file_name], cwd=repo_path)


    # Push the changes to GitHub
    # subprocess.run(["git", "push"], cwd=repo_path)

# Example usage:
repo_path = "/Users/brianquinn/workspace/artificial-activity" # Replace with your repository path
activity_date = "2023-01-01"
num_commits_per_day = 2

dates = [
    "2024-08-02",
"2024-08-03",
"2024-08-07",
"2024-08-08",
"2024-08-10",
"2024-08-11",
"2024-08-12",
"2024-08-13",
"2024-08-14",
"2024-08-17",
"2024-08-18",
"2024-08-21",
"2024-08-24",
"2024-08-25",
"2024-08-28",
"2024-08-31",
"2024-09-01",
"2024-09-04",
"2024-09-05",
"2024-09-06",
"2024-09-09",
"2024-09-10",
"2024-09-20",
"2024-09-21",
"2024-09-24",
"2024-09-25",
"2024-09-26",
"2024-10-02",
"2024-10-08",
"2024-10-18",
"2024-10-19",
"2024-10-23",
"2024-10-24",
"2024-10-28",
"2024-11-07",
"2024-11-08",
"2024-11-13",
"2024-11-16",
"2024-11-19",
"2024-11-23",
"2024-11-26",
"2024-11-29",
"2024-12-04",
"2024-12-05",
"2024-12-07",
"2024-12-20",
"2024-12-21",
"2024-12-24",
"2024-12-25",
"2024-12-26",
"2025-01-01",
"2025-01-07",
"2025-01-10",
"2025-01-11",
"2025-01-15",
"2025-01-16",
"2025-02-12",
"2025-02-13",
"2025-02-14",
"2025-02-17",
"2025-02-18",
"2025-02-22",
"2025-02-23",
"2025-03-01",
"2025-03-02",
"2025-03-06",
"2025-03-08",
"2025-03-09",
"2025-03-13",
"2025-03-15",
"2025-03-16",
"2025-03-20",
"2025-03-21",
"2025-03-24",
"2025-03-25",
"2025-03-26",
"2025-03-29"
]

for activity_date in dates: 
    generate_github_activity(repo_path, activity_date, num_commits_per_day)