# **C**redito **E**miliano -  Fe**ature **S**election, **T**ransformation and **E**limination (CE - FeSTE)

This repo contains the 'FeSTE' python package which helps in the features management from the pre-filtering to the pre-processing and feature elimination.

# Installation

To install it:

1) **Optional**: create a new Python virtual environment (through bash terminal run: "py -m venv your_env_name" and then "source your_env_name/Scripts/activate )
2) Install the package:
    - User Mode: 
```pip install ce-feste```


# Structure

The .py package is stored in src and contains 3 sub-modules:
- **selection**: contains the feature preliminary selection functions
- **transform**: contains the feature pre-processing functions
- **elimination**: contains the feature elimination functions

# Filters

## Selection

- Univariate filters:
    - No constant features
    - Number of distinct value too low
    - Number of missing values too high
    - Too concentrate in the most frequent value
    - Unstable between sets
- Multivariate filters:
    - Spearman Correlation for numerical features
    - Cramer's V for categorical features
    - R2 for mixed features
    - VIF
- Explanatory filters:
    - Feature AUROC for classification 
    - Feature Correlation with target for regression
    
## Elimination
- Shap Recursive Feature Elimination with HyperParam Optimization

# Trasformation

- Only 2 classes added to select and rename columns in datasets. Useful for generating the production pipeline