# Agricultural Loan Default Prediction Model

Predicting loan default probability for smallholder farmers in Tanzania using machine learning.

## Project Overview

This project develops a credit risk assessment model to predict the probability that a farmer will default on their agricultural loan. The model uses 26 features including farming characteristics, mobile money behavior, environmental indicators, and social capital.

## Key Results

- **Best Model:** RidgeCV (Ridge Regression with Cross-Validation)
- **Performance:** RMSE = 0.056 (predictions within ±5.6% of actual probability)
- **Dataset:** 20,000 farmers with 26 input features
- **Prediction Range:** 0-1 (probability of default)

## Model Comparison

| Model                   | RMSE  | MSE    | Status       |
| ----------------------- | ----- | ------ | ------------ |
| RidgeCV                 | 0.056 | 0.0032 | **Selected** |
| ElasticNetCV            | 0.057 | 0.0032 | Comparable   |
| ElasticNet (GridSearch) | 0.066 | 0.004  | Not selected |

All three models showed similar scatter patterns, confirming that the 26 selected features are all contributing to predictions.

## Features Used

The model uses 26 input features across 6 categories:

**Demographics & Experience**

- Age, farming experience, years in location

**Mobile Money & Financial Behavior**

- Transaction volume, account balance, bill payment consistency

**Credit History**

- Previous loan repayment, default history, trade credit

**Farm Characteristics**

- Farm size, irrigation, improved seeds, yield history

**Environmental Indicators**

- NDVI (vegetation health), soil moisture

**Social Capital & Infrastructure**

- Cooperative membership, buyer contracts, distance to market

See [data_dictionary.md](data_dictionary.md) for complete feature descriptions.

## Project Structure

AGRI-CREDIT-ASSESSMENT-MODEL/
├── notebooks/
│ └──data.ipynb
| |**data_eda.ipynb
| |**ml_elasticnet.ipynb
| |\_\_ml_LR_model.ipynb
Complete analysis and modeling
├── models/
│ ├── ridgecv_model.joblib # Trained RidgeCV model
│ └── scaler.joblib # Fitted StandardScaler
├── results/
│ └── plots/ # Prediction visualizations
├── data_dictionary.md # Feature descriptions
├── README.md # This file
├── requirements.txt # Python dependencies
├── app.py # Streamlit interface (WIP)
└── predict.py # Prediction utilities (WIP)

## How to Use

### Installation

```bash
pip install -r requirements.txt

```

## Decision Thresholds

Based on model predictions:

< 40%: Low risk → Approve with standard terms
40-55%: Medium risk → Approve with monitoring or higher interest

> 55%: High risk → Reject or require collateral

## Key Findings

1. Strong protective factors: Having a buyer contract, cooperative membership, and previous loan repayment significantly reduce default risk
2. Major risk factors: Previous loan default, lack of social capital (no cooperative/contract), and poor payment consistency increase risk
3. All features contribute: ElasticNet's feature selection didn't improve performance, indicating all 26 features after correlation filtering (|r| > 0.05) are useful
4. Model stability: RidgeCV and ElasticNetCV produced nearly identical results (RMSE difference < 0.001), confirming robust feature selection

## Technologies Used

Python 3.x
pandas, numpy - Data manipulation
scikit-learn - Machine learning
matplotlib, seaborn - Visualization
joblib - Model serialization
