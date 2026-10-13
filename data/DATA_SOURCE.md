# Dataset: Water Potability

**Title:** Water Quality and Potability  
**Author:** Aditya Kadiwal  
**Source:** Kaggle — https://www.kaggle.com/datasets/adityakadiwal/water-potability  
**Mirror used for download:** https://raw.githubusercontent.com/amankharwal/Website-data/master/water_potability.csv  
**License:** CC0 1.0 Universal (Public Domain Dedication)  
**Retrieved:** 2025  

## Description

The dataset contains water-quality measurements for 3,276 water bodies.
The target variable `Potability` indicates whether the water is safe for human consumption:
- `1` — Potable (safe)
- `0` — Not Potable (unsafe)

## Features

| Feature | Description | Unit |
|---|---|---|
| `ph` | pH value of water | — |
| `Hardness` | Capacity to precipitate soap | mg/L |
| `Solids` | Total dissolved solids | ppm |
| `Chloramines` | Amount of chloramines | ppm |
| `Sulfate` | Amount of dissolved sulfates | mg/L |
| `Conductivity` | Electrical conductivity | μS/cm |
| `Organic_carbon` | Amount of organic carbon | ppm |
| `Trihalomethanes` | Amount of trihalomethanes | μg/L |
| `Turbidity` | Measure of light-emitting property | NTU |
| `Potability` | Target: 1 = potable, 0 = not potable | binary |

## Known Limitations

- The dataset is synthetic/simulated for educational purposes.
- It should not be used as the sole basis for real-world water-safety decisions.
- Missing values are present in `ph`, `Sulfate`, and `Trihalomethanes`.

## Citation

Kadiwal, A. (2021). Water Quality. Kaggle. CC0: Public Domain.
https://www.kaggle.com/datasets/adityakadiwal/water-potability
