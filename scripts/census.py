"""
Census dataset preparation helper for the Ontario Gym Opportunity Dashboard.

This script documents the census-side workflow used in the project. It does not
call external APIs or overwrite source data. It reads the prepared CSV files in
../database and prints basic QA totals that can be used to verify the dashboard
inputs.
"""

from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
DATABASE_DIR = BASE_DIR / "database"


FILES = {
    "da_demographics": "dataset-a-da-demographics.csv",
    "zone_mapping": "dataset-a-market-zone-da-mapping.csv",
    "zone_demographics": "dataset-b-market-zone-demographics.csv",
    "decision_funnel": "master-analysis-decision-funnel.csv",
}


def load_csv(name: str) -> pd.DataFrame:
    path = DATABASE_DIR / FILES[name]
    if not path.exists():
        raise FileNotFoundError(f"Missing expected file: {path}")
    return pd.read_csv(path)


def main() -> None:
    print("Census / market-zone data QA")
    print("-" * 32)
    for label in FILES:
        df = load_csv(label)
        print(f"{label}: {len(df):,} rows, {len(df.columns):,} columns")

    zones = load_csv("zone_demographics")
    if {"Municipality", "Market_Zone"}.issubset(zones.columns):
        print("\nMarket zones by municipality:")
        print(zones.groupby("Municipality")["Market_Zone"].nunique().sort_index())


if __name__ == "__main__":
    main()
