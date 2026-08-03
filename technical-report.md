# Ontario Gym Location Analytics and Expansion Recommendation System

BSMM-8730 Data Acquisition and Management  
University of Windsor - Master of Management  
Project type: Data acquisition, database design, dashboard analytics, and business recommendation

## A. Background / Motivation

Fitness-club expansion is a local market decision. A municipality-level analysis can be useful for screening, but it is often too broad for choosing a gym site because customers usually evaluate convenience, travel time, nearby competitors, monthly price, and available amenities. For example, a city such as Windsor or London may contain several very different local markets. A gym placed in one part of the city may not serve the whole municipality equally.

This project responds to that problem by creating a decision-support dashboard for regional gym expansion across 12 Ontario municipalities. Instead of ranking only full municipalities, the project creates market zones such as Central London, Northwest Kitchener, and Northwest Windsor. This produces a more actionable level of geography for a regional manager.

## B. Problem Statement

The project asks:

> Which Ontario market zones should a regional fitness manager examine first when selecting the next gym location?

The objective is not to make a final lease decision. The objective is to create a screening tool that helps a manager narrow many possible locations into a smaller set of high-potential zones for deeper investigation.

The dashboard supports three business questions:

1. Which market zones show stronger demographic demand?
2. Which zones have fewer existing gym competitors or fewer budget competitors?
3. Which top zones appear most attractive after considering competitor price, amenities, ratings, and review volume?

## C. Dataset Description & Validation

The project uses four connected datasets:

| Dataset | Unit of analysis | Main role |
|---|---|---|
| Dataset B - Demographics | Market zone | Demand-side market profile |
| Dataset C - Gym locations | Gym location | Competitor supply and service profile |
| Dataset D - Market-zone summary | Market zone | Aggregated competition and opportunity scores |
| Fee and amenity analysis | Gym brand/location subset | Monthly fee, training, and amenity comparison |

The final working dataset contains 58 market zones and 190 gym competitor location records across 12 Ontario municipalities: Barrie, Greater Sudbury, Guelph, Hamilton, Kingston, Kitchener, London, Oshawa, St. Catharines, Thunder Bay, Waterloo, and Windsor.

Demographic variables include population, population density, median household income, average household income, renter share, apartment share, age 18-34 share, student-age proxy, labour force, employment, and unemployment. These variables are used to estimate the size and attractiveness of each local market zone.

Gym variables include gym name, brand, parent category, price tier, gym format, direct budget competitor flag, major-chain flag, address, latitude, longitude, market-zone assignment, personal training, group classes, tanning, hydromassage, sauna, Google rating, Google review count, source URL, source type, and verification status.

Validation was handled in three ways. First, row-level source fields and verification fields were retained so that users can see whether a record came from an official chain page, a geocoding output, or an open-source record. Second, major chain records were cross-checked more carefully than local independent records because they have higher influence on budget-gym competition. Third, Google rating and review fields were populated or checked using SerpApi Google Maps results where available. Open-source and quota-limited records are marked as screening-quality records that should be field-verified before final business use.

Important limitation: the market zones are analytical zones created for screening. They are not official municipal ward boundaries. This is acceptable for a managerial screening tool, but final site selection should validate each zone using local roads, retail corridors, traffic patterns, transit access, and real estate availability.

## D. Solution Design

The solution follows a simple data pipeline:

1. Acquire demographic, geographic, gym-location, rating, review, fee, and amenity data.
2. Clean and standardize municipality names, market-zone labels, addresses, brand categories, and service fields.
3. Assign gyms to market zones using municipality and nearest-zone logic.
4. Aggregate gym records into market-zone competition summaries.
5. Calculate a preliminary demand score and opportunity score.
6. Display results in an interactive dashboard for regional-manager decision making.

The database design separates the project into four core tables:

- `market_zone_demographics`
- `gym_locations`
- `market_zone_summary`
- `competitor_fee_analysis`

This design supports both dashboard filtering and SQL-based analysis. For example, a manager can query the highest opportunity zones, zones with no direct budget competitor, or competitor price gaps by market zone.

### Scoring methodology

The demand score is a preliminary normalized index built from variables that are relevant to gym demand. The logic emphasizes population size, population density, age 18-34 share, renter/apartment share, income, student-age proxy, and employment conditions. Higher scores indicate zones that appear stronger from a demand-side perspective.

The opportunity score combines demand with competitor supply. The core interpretation is:

> High demand plus lower gym supply plus limited direct budget competition equals stronger screening opportunity.

The opportunity score should be presented as a ranking aid, not a guaranteed profitability score. The model does not include lease costs, site visibility, traffic counts, parking, local zoning, or final catchment drive-time modelling.

## E. Results and Key Findings

The dashboard ranked the following zones highest by opportunity score:

| Rank | Zone | Municipality | Opportunity score | Interpretation |
|---:|---|---|---:|---|
| 1 | Central London | London | 74.7 | Highest overall screen; strong demand and low gym supply per population |
| 2 | Northwest Kitchener | Kitchener | 73.1 | Strong demand; no direct budget competitor in the current zone summary |
| 3 | Northwest Windsor | Windsor | 70.2 | Value-oriented rental market with strong budget-gym fit indicators |
| 4 | Northeast Barrie | Barrie | 58.4 | Moderate-to-strong option, but lower than the top three |
| 5 | East Waterloo | Waterloo | 58.1 | Very strong demand, but more visible gym supply |
| 6 | Southwest Oshawa | Oshawa | 56.0 | Potential gap but needs stronger review data |

The final recommendation is to prioritize the top three zones for deeper review:

1. Central London
2. Northwest Kitchener
3. Northwest Windsor

Central London is the strongest screening opportunity because it combines high demand with comparatively low gym supply per 10,000 residents and no direct budget competitor in the zone summary. Northwest Kitchener is attractive because its demand score is very strong and it appears to have a gap in direct budget-gym competition. Northwest Windsor is attractive because its demographic profile fits a value-oriented gym concept and current budget-chain pressure appears limited.

The dashboard also shows why a zone with gyms may still be attractive. The question is not only “Are there gyms?” but also “What type of gyms are they, what do they charge, what amenities do they offer, and is there still a budget-positioning gap?” Price and amenity comparisons help identify whether a new gym could compete on affordability, training availability, access, or service mix.

## F. Future Work

The next version should add:

- drive-time or walk-time catchment areas rather than approximate market-zone assignment only
- traffic counts and transit accessibility
- commercial real-estate availability and lease-rate data
- parking supply and visibility indicators
- more complete official monthly fee verification
- more complete Google review text analysis
- field validation for local independent gyms
- sensitivity testing for the score weights
- a formal database import script rather than only dashboard-ready CSV files

## AI Use Acknowledgement

Generative AI was used to support project planning, dataset design, dashboard design, wording, report drafting, presentation structuring, and quality-control checklists. AI was not used as an authoritative factual source. Factual claims should be supported by project datasets and cited sources. The project author remains responsible for reviewing the final analysis, validating records, and defending the recommendations.

## References

Fit4Less. (n.d.). Locations and membership information. https://www.fit4less.ca/

GoodLife Fitness. (n.d.). Memberships and club information. https://www.goodlifefitness.com/

OpenStreetMap contributors. (n.d.). OpenStreetMap. https://www.openstreetmap.org/

OpenStreetMap Foundation. (n.d.). Nominatim usage policy. https://operations.osmfoundation.org/policies/nominatim/

Planet Fitness. (n.d.). Gym memberships and locations. https://www.planetfitness.ca/

SerpApi. (n.d.). Google Maps API documentation. https://serpapi.com/google-maps-api

Statistics Canada. (2022). Census Profile, 2021 Census of Population. https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/index.cfm?Lang=E

Statistics Canada. (2022). Boundary files, 2021 Census. https://www12.statcan.gc.ca/census-recensement/2021/geo/sip-pis/boundary-limites/index2021-eng.cfm

