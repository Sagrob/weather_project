import importlib
from pathlib import Path
 
REQUIRED = [
    'numpy',
    'pandas',
    'matplotlib',
    'seaborn',
    'sklearn',
    'statsmodels',
    'joblib',
]
 
print('=' * 50)
print(' Weather DS — Environment Check')
print('=' * 50)
 
all_ok = True
 
for pkg in REQUIRED:
    try:
        mod = importlib.import_module(pkg)
        ver = getattr(mod, '__version__', '?')
        print(f'  OK  {pkg:<18} {ver}')
    except ImportError:
        print(f'  MISSING  {pkg}')
        all_ok = False
 
print()
 
data = Path(__file__).parent / 'data' / 'GlobalWeatherRepository.csv'
if data.exists():
    size_mb = data.stat().st_size / 1_048_576
    print(f'  OK  Dataset found ({size_mb:.1f} MB)')
else:
    print('  MISSING  Dataset not found at data/GlobalWeatherRepository.csv')
    print()
    print('  Download it from:')
    print('  https://www.kaggle.com/datasets/nelgiriyewithana/global-weather-repository')
    print('  Then place the CSV inside the data/ folder.')
    all_ok = False
 
print()
if all_ok:
    print('  All checks passed. Open the notebook and run all cells.')
else:
    print('  Fix the issues above, then run this script again.')
print('=' * 50)