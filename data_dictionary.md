Target Variable (Dependent Variable)
default_probability -- Continuous -- 0.0 - 1.0 -- Probability that the farmer will default on their loan. Higher values indicate higher risk.

Input Features (Independent Variables)

1. Demographics & Experience
   1.1. age -- Continuous -- 18-80 years -- Age of the farmer
   1.2. farming_experience_years -- Continuous -- 0-50 years -- Number of years the farmer has been farming
   1.3. years_in_location -- Continuous -- 0-50 years -- How long the farmer has lived in their current location. Stability indicator.
2. Mobile Money & Financial Behavior
   2.1. months_as_mobile_user -- Continuous -- 0-120 months -- How long they've used mobile money services
   2.2. total_transaction_volume_6mo_usd -- Continuous -- 0-150,000 USD -- Total value of all mobile money transactions in past 6 months
   2.3. avg_account_balance_usd -- Continuous -- 0-5,000 USD -- Average mobile money account balance
   2.4. has_mobile_savings -- Binary -- 0 or 1 -- Whether they use mobile savings features (1=yes, 0=no)
   2.5. bill_payment_consistency -- Continuous -- 0.0 - 1.0 -- How consistently they pay bills on time (1.0 = always on time)
3. Credit History
   3.1. previous_loan_repaid -- Binary -- 0 or 1 -- Whether they repaid their previous loan (1=yes, 0=no)
   3.2. loan_default -- Binary -- 0 or 1 -- Whether they defaulted on a loan before (1=yes defaulted, 0=no default)
   3.3. has_trade_credit_history -- Binary -- 0 or 1 -- Whether they have history of buying inputs on credit (1=yes, 0=no)
4. Farm Characteristics
   4.1. farm_size_acres -- Continuous -- 0-500 acres -- Size of their farm in acres
   4.2. has_irrigation -- Binary -- 0 or 1 -- Whether farm has irrigation system (1=yes, 0=no)
   4.3. uses_improved_seeds -- Binary -- 0 or 1 -- Whether they use improved/certified seeds (1=yes, 0=no)
   4.4. previous_yield_bags -- Continuous -- 0-200 bags -- Number of bags harvested in previous season. Production indicator.
   4.5. has_off_farm_income -- Binary -- 0 or 1 -- Whether they have income from non-farming activities (1=yes, 0=no)
5. Environmental & Land Quality
   5.1. ndvi_current -- Continuous -- 0.0 - 1.0 -- Current vegetation health from satellite (NDVI index). Higher = healthier crops.
   5.2. ndvi_historical_avg -- Continuous -- 0.0 - 1.0 -- Average historical vegetation health. Indicates land quality.
   5.3. soil_moisture_index -- Continuous -- 0.0 - 1.0 -- Current soil moisture level. Higher = better water availability.
6. Social Capital & Support
   6.1. cooperative_member -- Binary -- 0 or 1 -- Member of farmer cooperative/group (1=yes, 0=no). Strong protective factor.
   6.2. has_buyer_contract -- Binary -- 0 or 1 -- Has guaranteed buyer contract for harvest (1=yes, 0=no). Reduces market risk.
   6.3. available_references -- Discrete -- 0-10 -- Number of people who can vouch for them
   6.4. has_crop_insurance -- Binary -- 0 or 1 -- Has crop insurance (1=yes, 0=no). Risk mitigation.
7. Infrastructure & Access
   7.1. distance_to_market_km -- Continuous -- 0-50 km -- Distance from farm to nearest market
   7.2. distance_to_input_dealer_km -- Continuous -- 0-50 km -- Distance to nearest agricultural input dealer
   7.3. road_quality_score -- Ordinal -- 1-4 -- Quality of road access (1=poor, 4=excellent)

Summary Statistics
Total features: 26 input features → 1 target variable
Variable type breakdown:

Binary variables: 10 features (38%)
Continuous probabilities/indices: 4 features (15%)
Continuous counts/measurements: 12 features (47%)

Strong protective factors (reduce default risk):

has_buyer_contract
cooperative_member
previous_loan_repaid
has_irrigation
bill_payment_consistency

Strong risk factors (increase default risk):

loan_default (previous default)
distance_to_market_km
Low bill_payment_consistency
No cooperative membership

Model: RidgeCV regression predicting continuous probability (0-1)
Performance: RMSE = 0.056 (predictions typically within ±5.6% of actual)
