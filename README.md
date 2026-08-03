# Ontario Gym Opportunity Dashboard

Prepared by **Pradeepta Kumar Saha**  
Student ID: **110194567**

Interactive regional-manager dashboard for evaluating gym expansion opportunities across selected Ontario market zones.

## Final dashboard links

- Vercel dashboard: https://ontario-gym-opportunity-dashboard.vercel.app/

## Repository name

The repository is named **8730-project** to match the project requirement.

## Repository structure

```text
8730-project/
|-- scripts/
|   |-- census.py
|   `-- gym.py
|-- database/
|   |-- dataset-a-da-demographics.csv
|   |-- dataset-a-market-zone-da-mapping.csv
|   |-- dataset-b-market-zone-demographics.csv
|   |-- dataset-c-final-gym-locations.csv
|   |-- dataset-d-market-zone-competition-summary.csv
|   |-- dataset-e-top-gym-websites.csv
|   |-- dataset-f-amenities-fees-links.csv
|   |-- dataset-g-pricing-pages.csv
|   |-- dataset-h-official-fee-research.csv
|   |-- dataset-i-monthly-fee-summary.csv
|   |-- dataset-j-brand-fees-amenities-manual.csv
|   `-- other supporting CSV audit files
|-- presentation/
|   `-- final-project-presentation.pptx
|-- index.html
|-- README.md
|-- technical-report.md
|-- ai-prompts.md
`-- dashboard.md
```

## Project purpose

The project screens gym expansion opportunities across 12 Ontario municipalities. It combines market-zone demographics, competitor gym supply, ratings/reviews, pricing, amenities, and opportunity scoring to help identify strong candidate zones for a new gym location.

## Main files

- `index.html` - standalone interactive dashboard.
- `database/` - CSV datasets used in the dashboard development process.
- `scripts/census.py` - census and market-zone data QA helper.
- `scripts/gym.py` - gym competitor, amenities, and pricing data QA helper.
- `technical-report.md` - written technical report.
- `ai-prompts.md` - AI-use statement and prompt disclosure.
- `dashboard.md` - guide to interpreting the dashboard.
- `presentation/final-project-presentation.pptx` - final presentation deck.

## Branch workflow

The repository includes feature-style branches to support the assignment requirement for a branch-based workflow:

- `data-preparation`
- `dashboard-development`
- `final-submission`
- `feature/census-data-processing`
- `feature/gym-dashboard-development`

## Academic note

This dashboard is designed for academic and screening analysis. Market-zone boundaries are project-defined approximations and should be validated with local real-estate, traffic, lease, parking, zoning, and operator data before any real business decision.
