# Immo Eliza - Belgian Real Estate Market Analysis

A comprehensive exploratory data analysis (EDA) of the Belgian real estate market, analyzing pricing patterns, market segments, and geographic distributions across 23,000+ property listings.

## 📋 Table of Contents

- [🔍 Overview](#-overview)
- [🎯 Project Goals](#-project-goals)
- [📊 Dataset](#-dataset)
- [🔑 Key Findings](#-key-findings)
- [📈 Visualizations](#-visualizations)
- [📁 Project Structure](#-project-structure)
- [⚙️ Installation](#️-installation)
- [🚀 Usage](#-usage)
- [🛠️ Technologies](#️-technologies)
- [👥 Team](#-team)

## 🔍 Overview

This project performs in-depth analysis of Belgian real estate data to understand property pricing dynamics, identify market segments, and explore regional variations. The analysis combines property listings data with socio-economic indicators and geographic information to provide actionable insights into the Belgian housing market.

**Key Statistics:**
- 23,321 properties analyzed (after cleaning)
- 66 features per property
- Coverage across 580+ municipalities in Belgium
- 10 provinces (+ Brussels) analyzed

## 🎯 Project Goals

1. **Data Cleaning & Preparation:** Process raw property data for machine learning applications
2. **Exploratory Data Analysis:** Identify patterns, correlations, and market segments
3. **Geographic Analysis:** Map price distributions and regional variations
4. **Market Segmentation:** Distinguish luxury vs. residential property markets
5. **External Factors:** Analyze correlations with GDP and socio-economic indicators

## 📊 Dataset

### Raw Data Sources

- **Property Listings** ([raw_dataset_v4.csv](data/raw/raw_dataset_v4.csv)): 23,982 scraped property listings from Belgian real estate platforms
- **Median Income** ([median_income.csv](data/raw/median_income.csv)): Income data for 581 municipalities
- **Population Data** ([TF_SOC_POP_STRUCT_2025.csv](data/raw/TF_SOC_POP_STRUCT_2025.csv)): Socio-economic structure from Statbel (466,823 records)
- **Postal Codes** ([postal-codes-belgium.csv](data/raw/postal-codes-belgium.csv)): Mapping of 1,231 postal codes to municipalities
- **Geospatial Data**: Belgium 4-digit postal code shapefiles for mapping

### Cleaned Datasets

- [cleaned_dataset_v4.csv](data/cleaned/cleaned_dataset_v4.csv): 23,321 properties with 66 features
- [cleaned_dataset_v4_with_luxury_segment.csv](data/cleaned/cleaned_dataset_v4_with_luxury_segment.csv): 20,040 properties with luxury/residential classification

### Data Features (66 columns)

**Core Features:**
- `price`, `rooms`, `area`, `postal_code`, `locality`

**Property Characteristics:**
- `property_type` (House/Apartment), `property_subtype`, `state`, `build_year`

**Amenities:**
- `has_equipped_kitchen`, `has_garden`, `has_terrace`, `has_swimming_pool`, `garage`, `cellar`

**Energy & Sustainability:**
- `primary_energy_consumption`, `co2`, `heating_type`, `heat_pump`, `solar_panels`

**Legal & Planning:**
- `flooding_area_type`, `planning_permission_granted`, `preemption_right`

**Derived Features:**
- `price_per_m2`, `province_name`, `region_name`, `is_luxurious`

## 🔑 Key Findings

### 1. Market Segmentation: Luxury vs. Residential

**Critical Discovery:** Luxury properties (median price ~3x higher) must be analyzed separately from regular residential properties as they exhibit different market dynamics.

- **Luxury properties** drive most data skewness
- **Price per m²** remains relatively similar between segments
- **Distribution patterns** are distinctly different

### 2. Regional Price Patterns

**Highest Median Prices (by Province):**
- **Flemish Brabant**: €395,500 (13% luxury properties)
- **Brussels**: €385,000 (15% luxury properties)
- **East Flanders**: €369,000 (8% luxury properties)

**Lowest Median Prices:**
- **Hainaut**: €209,000 (8% luxury properties)
- **Liège**: €220,000 (6% luxury properties)

**Price per m² Leaders:**
- **Brussels**: €3,615/m²
- **West Flanders**: €2,908/m²
- **Hainaut** (lowest): €1,508/m²

### 3. Data Quality Insights

- **92% data retention** after cleaning (660 properties removed)
- **Type-specific features** require separate handling for houses vs. apartments
- **Outlier patterns** identified using IQR method

### 4. External Correlations

- **GDP/income** shows correlation with property prices
- **Brussels** acts as significant outlier in regional analyses
- **Geographic location** is a strong price predictor

### 5. Data Cleaning Decisions

**Removed Features (>80% missing):**
- Ultra-sparse amenities: parking_places_indoor, dining_rooms, wash_room, water_softener, rain_water_tank, air_conditioning, security_door
- Energy certifications: certification_gasoil_tank, low_energy, g_score, p_score
- Other: front_facade_orientation, garden_orientation, maintenance_cost, opportunity_for_professional

**Filtered Property Types:**
- Removed "Other" category (business surfaces, office spaces, development sites)

## 📈 Visualizations

### Interactive Maps (Available Online)

Explore the interactive visualizations:
- [Province-level Map](http://cavetales.eu.org/html/interactive_provinces_map_v3.html) (13MB)
- [Municipality-level Map](http://cavetales.eu.org/html/interactive_municipalitets_map_v3.html) (12MB)

### Generated Visualizations

**Static Maps** (PNG format in [reports/map_visualization_results/](reports/map_visualization_results/)):
- `map_median_price.png` - Geographic distribution of median property prices
- `map_price_by_m2.png` - Price per square meter by location
- `map_mean_area.png` - Average property size by location
- `map_number_of_records.png` - Data density/sample size by location
- `map_high_valued_properties.png` - Distribution of luxury properties
- `map_price_variance.png` - Price variability by location

**Statistical Plots:**
- Correlation heatmap (30x30 features)
- Missingness distribution charts
- Outlier percentage visualizations
- Property type comparison plots (Apartments vs Houses)
- Distribution histograms for price, area, and price_per_m²
- GDP vs house price scatter plots

## 📁 Project Structure

```
immo-eliza-gold-fishes-analysis/
├── analysis/
│   ├── analysis.ipynb              # Main analysis notebook (109 cells)
│   └── correlation_matrix.ipynb    # Correlation analysis
│
├── data/
│   ├── raw/                        # Original data sources
│   │   ├── raw_dataset_v4.csv
│   │   ├── median_income.csv
│   │   ├── TF_SOC_POP_STRUCT_2025.csv
│   │   └── postal-codes-belgium.csv
│   ├── cleaned/                    # Processed datasets
│   │   ├── cleaned_dataset_v4.csv
│   │   └── cleaned_dataset_v4_with_luxury_segment.csv
│   └── shapefiles/                 # Geographic data
│       ├── Belgium-4-Digit-Postcodes-2020.*
│       └── provinces.*
│
├── caveeagle_service_scripts/      # Utility scripts
│   ├── service_functions.py        # Province/region mapping functions
│   ├── analysis.py                 # Correlation matrix generation
│   ├── make_report.py              # Province/municipality aggregation
│   ├── join_datasets.py            # Dataset merging utilities
│   ├── join_shapefiles.py          # Shapefile processing
│   ├── simplify_shapefiles.py      # Shapefile optimization
│   └── map_visualization_scripts/  # Map generation notebooks
│       ├── interactive_maps_simple.ipynb
│       ├── interactive_maps_extended.ipynb
│       ├── interactive_provinces_map.ipynb
│       ├── static_map.ipynb
│       └── static_map_extend.ipynb
│
├── reports/
│   └── map_visualization_results/  # Generated outputs
│       ├── summary_by_provinces.csv
│       ├── summary_by_municip.csv
│       ├── *.png                   # Static maps (6 files)
│       └── *.html                  # Interactive maps (4 files)
│
└── README.md
```

## ⚙️ Installation

### Prerequisites

- Python 3.8+
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/immo-eliza-gold-fishes-analysis.git
cd immo-eliza-gold-fishes-analysis
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install pandas numpy matplotlib seaborn plotly geopandas folium scipy tabulate jupyter
```

## 🚀 Usage

### Running the Main Analysis

Open and run the main analysis notebook:
```bash
jupyter notebook analysis/analysis.ipynb
```

The notebook contains 109 cells covering:
- Data loading and cleaning
- Statistical analysis
- Market segmentation
- Geographic analysis
- Correlation studies
- Visualization generation

### Generating Maps

To regenerate the interactive maps:
```bash
jupyter notebook caveeagle_service_scripts/map_visualization_scripts/interactive_provinces_map.ipynb
```

### Using Utility Scripts

Generate province-level summaries:
```python
from caveeagle_service_scripts.make_report import generate_province_summary
summary = generate_province_summary('data/cleaned/cleaned_dataset_v4.csv')
```

Map postal codes to provinces:
```python
from caveeagle_service_scripts.service_functions import get_province_from_postal_code
province = get_province_from_postal_code(1000)  # Returns 'Brussels'
```

## 🛠️ Technologies

**Python Libraries:**
- **Data Analysis:** pandas, numpy
- **Visualization:** matplotlib, seaborn, plotly
- **Geospatial:** geopandas, folium
- **Statistics:** scipy
- **Utilities:** tabulate

**Data Sources:**
- Statbel (Belgian statistical office)
- Real estate scraping platforms
- OpenStreetMap (shapefiles)

## 👥 Team

**Gold Fishes Team** - BeCode Data Analysis Project

### Contributors
- [Jens Bogaert](https://github.com/BogJ674) 🐠
- [Amine Samoudi](https://github.com/AmineSam) 🐠
- [Wiktor Porczyński](https://github.com/wikporc) 🐠
- [Victor](https://github.com/caveeagle) 🐠
