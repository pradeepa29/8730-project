"""
Gym competitor dataset preparation helper for the Ontario Gym Opportunity Dashboard.

This script documents the gym-side workflow used in the project. It reads the
prepared competitor, pricing, amenities, and audit datasets from ../database and
prints QA totals. No API keys or scraping credentials are stored in this repo.
"""

from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
DATABASE_DIR = BASE_DIR / "database"


FILES = {
    "gym_locations": "dataset-c-final-gym-locations.csv",
    "zone_competition": "dataset-d-market-zone-competition-summary.csv",
    "gym_websites": "dataset-e-top-gym-websites.csv",
    "amenities_links": "dataset-f-amenities-fees-links.csv",
    "pricing_pages": "dataset-g-pricing-pages.csv",
    "fee_research": "dataset-h-official-fee-research.csv",
    "monthly_fees": "dataset-i-monthly-fee-summary.csv",
    "manual_amenities": "dataset-j-brand-fees-amenities-manual.csv",
}


def load_csv(name: str) -> pd.DataFrame:
    path = DATABASE_DIR / FILES[name]
    if not path.exists():
        raise FileNotFoundError(f"Missing expected file: {path}")
    return pd.read_csv(path)


def main() -> None:
    print("Gym competitor data QA")
    print("-" * 24)
    for label in FILES:
        df = load_csv(label)
        print(f"{label}: {len(df):,} rows, {len(df.columns):,} columns")

    gyms = load_csv("gym_locations")
    if "Brand" in gyms.columns:
        print("\nTop brands by record count:")
        print(gyms["Brand"].value_counts().head(15))


if __name__ == "__main__":
    main()
