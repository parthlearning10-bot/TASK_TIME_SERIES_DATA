Task: 
Time Series Demand Forecasting System
Build a system that forecasts future values from historical time-series data, evaluates itself against benchmarks, and monitors accuracy drift over time. Phased task  finish Phase 1 and then Phase 2
Dataset: US Births (daily, single series, strong weekly + yearly seasonality). Get it from the Monash Time Series Forecasting Repository at forecastingdata.org  find "US Births" in the dataset table and download it. It's in .tsf format; the loaders to read it into Python are in the repo's GitHub (linked on the same page).
Ground rules (whole task)

Send a short daily update on Slack EOD what you did, what's blocking you.
Research and debug independently through documentation before asking.
Do not copy GitHub projects or existing forecasting notebooks. Keep LLM use minimal  you must be able to explain every line you write.


Phase 1 Data & Baselines 

Load the US Births dataset and do EDA trend, seasonality, missing values, outliers.
Build a naive baseline: last-value and seasonal-naive. Every later model is compared against this.
Use walk-forward (rolling-origin) validation not a random split.
Report MAE, RMSE, MAPE for the baselines.

Deliverables:

EDA report
Baseline + walk-forward backtesting code
Results table (last-value vs seasonal-naive)



Phase 2  Models, Drift & Serving 

Build one statistical model (ARIMA/Prophet) and one ML model (for ex. XGBoost with lag features).
Evaluate with MAE, RMSE, MAPE, and a business-cost metric you define (over- vs under-forecast cost).
Beat the official Monash benchmark for US Births, or explain why you couldn't. The Monash benchmarks are in MASE, so compute MASE for that comparison; keep MAE/RMSE/MAPE for your own model-vs-model table.
Implement drift monitoring  detect whether forecast error worsens across the test period and explain the cause.
FastAPI /forecast endpoint  input: horizon; output: forecast + confidence interval + recent backtest error.
Add logging and exception handling.
Dockerize the full application.

Deliverables:

Working /forecast endpoint
Results table comparing baseline vs statistical vs ML model
Drift-monitoring report
Docker setup
1–2 page writeup defending your key decisions (model, validation window, lag/seasonality choices)


Timeline 15-20 Days

