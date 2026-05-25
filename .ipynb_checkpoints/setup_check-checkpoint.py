#!/usr/bin/env python
"""
setup_check.py — Run this before opening the notebook.
"""
import importlib
from pathlib import Path

REQUIRED = ['numpy', 'pandas', 'matplotlib', 'seaborn', 'sklearn', 'statsmodels', 'joblib']

print('=' * 50)
print(' Weather DS — Environment Check')
print('=' * 50)

ok = True
for pkg in REQUIRED:
    try:
        mod = importlib.import_module(pkg)
        ver = getattr(mod, '__version__', '?')
        print(f'  ✅ {pkg:<18} {ver}')
    except ImportError:
        print(f'  ❌ {pkg:<18} NOT FOUND')
        ok = False

print()
data = Path(__file__).parent / 'data' / 'GlobalWeatherRepository.csv'
if data.exists():
    print(f'  ✅ Dataset found ({data.stat().st_size / 1_048_576:.1f} MB)')
else:
    print('  ⚠️  Dataset NOT found. Download it with:')
    print('     kaggle datasets download -d nelgiriyewithana/global-weather-repository -p data/ --unzip')
    ok = False

print()
print('  🚀 Ready!' if ok else '  ⚠️  Fix the issues above first.')
print('=' * 50)
