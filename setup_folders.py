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

with open("requirements.txt", "w") as f:
    pass

with open("README.md", "w") as f:
    f.write("# HealthOps360 Analytics Platform\n\nProject to simulate hospital analytics using batch and real-time data engineering techniques.")
