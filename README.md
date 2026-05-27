# Global Weather Repository — Data Science Analysis

PM Accelerator Data Science Assessment
---

## PM Accelerator Mission

"Our mission is to accelerate the careers of product managers by providing world-class education, mentorship, and a supportive community — breaking down financial and geographic barriers to empower diverse talent to lead in the technology industry."

---

## Project Overview

This project analyzes the Global Weather Repository dataset from Kaggle, which contains daily weather information for cities around the world with over 40 features. The goal is to clean the data, uncover patterns through exploratory analysis, and build a forecasting model to predict future temperature trends.

---

## Project Structure

```
weather_project/
├── notebooks/
│   └── weather_analysis.ipynb   
├── data/
│   └── GlobalWeatherRepository.csv  
├── outputs/
│   ├── figures/                 
│   └── models/                  
└── README.md
```

---

## Dataset

Source: Kaggle — Global Weather Repository
https://www.kaggle.com/datasets/nelgiriyewithana/global-weather-repository

Download the CSV and place it inside the data/ folder before running the notebook.

---

## Setup

**1. Create and activate the conda environment:**

```bash
conda create -n weather_ds python=3.11 -y
conda activate weather_ds
```

**2. Install dependencies:**

```bash
conda install -c conda-forge jupyterlab numpy pandas matplotlib seaborn scikit-learn statsmodels joblib -y
```

**3. Launch JupyterLab:**

```bash
jupyter lab
```

**4. Open** `notebooks/weather_analysis.ipynb` and run all cells in order.

---

## Methodology

### 1. Data Cleaning and Preprocessing

- Parsed the `last_updated` column into datetime format and sorted the dataset chronologically
- Extracted temporal features: year, month, day, and season
- Filled missing values using column medians
- Capped outliers on temperature and precipitation using the IQR method (1.5x fence)
- Normalized all numeric features using StandardScaler

### 2. Exploratory Data Analysis

- Temperature distribution histogram and median temperature by season
- Precipitation distribution and boxplot by season
- Correlation heatmap across 10 key weather features
- Monthly average temperature trend across the full date range
- Top 10 countries by average temperature

### 3. Forecasting Model

- Built a global daily mean temperature time series from the `last_updated` feature
- Applied seasonal decomposition (additive model, 30-day period) to identify trend, seasonality, and residual components
- Trained a Holt-Winters Exponential Smoothing model with additive trend and seasonality
- Evaluated on a 30-day hold-out test set using MAE, RMSE, and R2

---

## Results

| Metric | Value |
|--------|-------|
| MAE    | 0.5316 °C |
| RMSE   | 0.6249 °C |
| R2     | -0.2568 |

The negative R2 score suggests the model struggles to capture the full variance 
of the global temperature series, likely because averaging temperatures across 
all countries worldwide flattens the seasonal signal. A per-country or 
per-region model would likely perform better.

---

## Output Files

| File | Description |
|------|-------------|
| outputs/figures/temperature_distribution.png | Temperature histogram and seasonal medians |
| outputs/figures/precipitation_distribution.png | Precipitation histogram and seasonal boxplot |
| outputs/figures/correlation_heatmap.png | Feature correlation matrix |
| outputs/figures/monthly_temperature.png | Monthly average temperature trend |
| outputs/figures/top_countries_temperature.png | Top 10 countries by average temperature |
| outputs/figures/time_series.png | Full daily temperature time series |
| outputs/figures/seasonal_decomposition.png | Trend, seasonal, and residual breakdown |
| outputs/figures/forecast.png | 30-day forecast vs actual values |
| outputs/models/holt_winters_model.pkl | Saved trained model |
| outputs/models/metrics.csv | MAE, RMSE, and R2 values |
| outputs/models/scaler.pkl | Saved StandardScaler |

---

## Environment

- OS: Arch Linux / KDE Plasma
- Python: 3.11
- Environment manager: Anaconda
- IDE: JupyterLab

---

Submitted as part of the PM Accelerator Data Science Assessment.
