import os

folders = [
    "data/raw",
    "src/ingestion",
    "src/transformation",
    "src/dq_checks",
    "src/orchestration",
    "warehouse/snowflake",
    "warehouse/redshift",
    "reports/power_bi",
    "docs",
    "tests"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    gitkeep_path = os.path.join(folder, ".gitkeep")
    with open(gitkeep_path, "w") as f:
        f.write("")
