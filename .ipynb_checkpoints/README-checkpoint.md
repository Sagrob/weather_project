# 🌍 Global Weather Repository — Data Science Analysis

> **PM Accelerator Data Science Assessment — Basic Track**

---

## 📌 PM Accelerator Mission

> *"Our mission is to accelerate the careers of product managers by providing world-class education, mentorship, and a supportive community — breaking down financial and geographic barriers to empower diverse talent to lead in the tech industry."*

---

## 📁 Project Structure

```
weather_basic/
├── notebooks/
│   └── 01_weather_basic.ipynb   # Main analysis notebook
├── data/
│   └── GlobalWeatherRepository.csv  # Download separately (see below)
├── outputs/
│   ├── figures/                 # Saved plots
│   └── models/                  # Saved model & metrics
├── environment.yml              # Conda environment
├── setup_check.py               # Environment verification script
└── README.md
```

---

## 📦 Dataset

**Source:** [Kaggle — Global Weather Repository](https://www.kaggle.com/datasets/nelgiriyewithana/global-weather-repository)

Download and place `GlobalWeatherRepository.csv` inside the `data/` folder.

```bash
kaggle datasets download -d nelgiriyewithana/global-weather-repository -p data/ --unzip
```

---

## ⚙️ Setup

```bash
# 1. Create environment
conda env create -f environment.yml

# 2. Activate
conda activate weather_ds

# 3. Check everything is working
python setup_check.py

# 4. Launch JupyterLab or Spyder
jupyter lab
```

---

## 🔬 Methodology

### 1. Data Cleaning & Preprocessing
- Identified and filled missing values using column medians
- Parsed `last_updated` into datetime; extracted year, month, day, season
- Capped outliers using the IQR method (1.5× fence) on temperature and precipitation
- Normalized numeric features with `StandardScaler`

### 2. Exploratory Data Analysis (EDA)
- Temperature distribution histogram and median by season
- Precipitation distribution and boxplot by season
- Correlation heatmap across the top 15 numeric features
- Monthly average temperature trend (line chart)
- Top 10 countries by average temperature (bar chart)

### 3. Forecasting Model
- Built a global daily mean temperature time series from `last_updated`
- Applied seasonal decomposition (additive, 30-day period)
- Trained a **Holt-Winters Exponential Smoothing** model (additive trend + seasonality)
- Evaluated on a **30-day hold-out** test set

**Metrics used:** MAE, RMSE, R²

---

## 📊 Outputs

| File | Description |
|---|---|
| `outputs/figures/temperature_distribution.png` | Histogram + seasonal medians |
| `outputs/figures/precipitation_distribution.png` | Histogram + seasonal boxplot |
| `outputs/figures/correlation_heatmap.png` | Feature correlation matrix |
| `outputs/figures/monthly_temperature.png` | Monthly average temperature trend |
| `outputs/figures/top_countries_temperature.png` | Top 10 countries by temperature |
| `outputs/figures/seasonal_decomposition.png` | Trend / seasonal / residual breakdown |
| `outputs/figures/forecast.png` | 30-day forecast vs actuals |
| `outputs/models/holt_winters_model.pkl` | Saved model |
| `outputs/models/metrics.csv` | MAE, RMSE, R² values |

---

*Submitted as part of the PM Accelerator Data Science Assessment.*
