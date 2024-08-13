# National IQ Calculator

This repository contains a Streamlit application that estimates the national IQ and its standard deviation based on data from the Programme for International Student Assessment (PISA) 2022. This document explains the methodology behind these calculations.

## Overview

The application calculates a country's estimated national IQ and its standard deviation using the following inputs:
- **PISA Mean Score**: The country's average score in mathematics from the PISA assessments.
- **PISA Performance Gap**: The difference between the 90th and 10th percentile scores in the country's PISA mathematics results ([*See results for Brazil: go to Data Table tab*](https://gpseducation.oecd.org/CountryProfile?plotter=h5&primaryCountry=BRA&treshold=5&topic=PI)).
- **Global Reference Data**:
  - Global PISA Mean Score: 500
  - Global PISA Standard Deviation: 100
  - Global IQ Mean: 100
  - Global IQ Standard Deviation: 15

## Methodology

### 1. Calculating National IQ Standard Deviation

The national IQ standard deviation (`qi_sd_national`) is calculated by adjusting the global IQ standard deviation based on the ratio of the country's PISA standard deviation to the global PISA standard deviation.

`qi_sd_national = (pisa_sd / pisa_sd_global) * qi_sd_global`


Where:
- `pisa_sd`: The national standard deviation in PISA scores.
- `pisa_sd_global`: The global standard deviation in PISA scores (fixed at 100).
- `qi_sd_global`: The global IQ standard deviation (fixed at 15).

### 2. Calculating National IQ Mean

The national IQ mean (`qi_mean_national`) is calculated by mapping the difference between the national PISA mean and the global PISA mean onto the global IQ scale.

`qi_mean_national = ((pisa_mean - pisa_mean_global) / pisa_sd_global) * qi_sd_global + qi_mean_global`

Where:
- `pisa_mean`: The national mean in PISA scores.
- `pisa_mean_global`: The global mean in PISA scores (fixed at 500).
- `qi_mean_global`: The global IQ mean (fixed at 100).

### 3. Interpretation of Results

- **National IQ Mean**: This value represents the average IQ of individuals in the country as estimated from their PISA scores relative to the global PISA and IQ distributions.
- **National IQ Standard Deviation**: This value represents the variability of IQ scores within the country, adjusted according to the national variability in PISA scores.

## Example Calculation

Assume a country has the following PISA data:
- **PISA Mean Score**: 379
- **PISA Performance Gap**: 194 (difference between the 90th and 10th percentile)

Steps:
1. **Calculate National PISA Standard Deviation**:
    - National PISA SD = `194 / 2.56` ≈ 75.78
2. **Calculate National IQ SD**:
    - National IQ SD = `(75.78 / 100) * 15` ≈ 11.37
3. **Calculate National IQ Mean**:
    - National IQ Mean = `((379 - 500) / 100) * 15 + 100` ≈ 80.85

Thus, the estimated national IQ is 80.85 with a standard deviation of 11.37.

### Reason for Using 2.56

In statistics, the interval between the 10th percentile and the 90th percentile covers approximately 80% of the distribution of a variable. If we assume that the PISA scores follow a normal distribution, this difference (from the 90th to the 10th percentile) can be used to calculate the standard deviation of the distribution.

The difference between the 90th percentile and the 10th percentile spans about 1.28 standard deviations **below** the mean (10th percentile) to 1.28 standard deviations **above** the mean (90th percentile). Since the interval from the 90th to the 10th percentile covers 2.56 times the standard deviation of the distribution (1.28 + 1.28 = 2.56), we divide the "PISA Performance Gap" by 2.56 to estimate the national PISA standard deviation.

## Requirements

- **Python 3.x**
- **Streamlit**
- **Scipy**
- **Pandas**

Install the required packages using:

```bash
pip install -r requirements.txt
```

## Running the Application
To run the Streamlit application locally, execute:

```bash
streamlit run your_script_name.py
```

## Contact
For more info and suggestions, reach me at [Linkedin](linkedin.com/in/joaomj).
