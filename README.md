# RiskPredict - AI-Driven Risk Management (Hackathon Project)

## Bank of Baroda Hackathon 2024

## Project Overview
RiskPredict is an AI-driven solution developed for a hackathon challenge, aimed at enhancing the risk management capabilities of banks. Leveraging Azure Machine Learning and Azure Databricks, it analyzes large datasets to identify potential risks and anomalies in real-time, offering predictive insights for market, credit, and operational risks, and generating actionable risk mitigation strategies while ensuring regulatory compliance.

## Problem Statement
Current risk management processes are manual, time-consuming, and error-prone, struggling to identify risks in real-time and lacking predictive capabilities.

## Proposed Solution
RiskPredict utilizes Azure Machine Learning for developing predictive models based on transaction data, customer data, and market data, with Azure Databricks handling large-scale data processing tasks.

## Benefits
- **Real-time Risk Identification**: Enables the bank to detect risks as they occur.
- **Predictive Insights**: Forecasts future risks, allowing for proactive risk management.
- **Actionable Strategies**: Generates strategies for risk mitigation.
- **Regulatory Compliance**: Ensures compliance with financial regulations.
- **Enhanced Customer Trust**: Builds trust through improved risk management.

## Implementation Plan
- **Data Collection and Analysis**: 2 weeks
- **Model Development and Testing**: 3 weeks
- **Integration**: 1 week

## Challenges & Risks
- **Data Privacy and Security**: Ensuring the protection of sensitive information.
- **System Integration**: Integrating with existing banking systems.
- **Model Accuracy**: Continuously refining the model for accurate predictions.

## Hackathon Progress

### Update - [16-06-2024]
- **Data Collection and Analysis**: Completed initial dataset collection, focusing on the banking sector and market indices, including stock prices and market indices. Preliminary analysis is underway to identify patterns and potential risk indicators.
- **Model Development**: Initiated the development of predictive models for market risk prediction using Azure Machine Learning.

### Update - [17-06-2024]
- **Exploratory Data Analysis (EDA)**: Conducted EDA on the collected dataset, including visualization of time series data for bank stocks and market indices, correlation analysis, and statistical summary. Adjustments were made to improve the clarity and readability of the visualizations.
- **Feature Engineering**: Began the process of feature engineering, planning to create lag features, rolling window features, and date-related features to enhance model accuracy.
- **Model Selection Discussion**: Started Brainstorming on selecting appropriate models for time series forecasting, considering linear regression for a baseline model and exploring more complex models like ARIMA and LSTM for better predictive performance.

### Update - [19-06-2024]
- **Advanced Feature Engineering**: Enhanced feature set with additional lag features, rolling statistics, and dropped rows with NaN values to ensure data integrity.
- **Extensive Hyperparameter Tuning**: Conducted randomized search for Gradient Boosting parameters to optimize model performance.
- **Model Performance**:
  - Best Gradient Boosting MSE after Randomized Search: 0.3598577296684397
  - Cross-Validation Scores for Gradient Boosting and Stacking Models:
    - Gradient Boosting Cross-Validation MSE Scores: [0.19158734, 0.41316652, 0.4267332, 0.33971528, 0.47925685, 0.33884471, 0.27667636, 0.30795477, 1.94825898, 0.62883489]
    - Average Gradient Boosting CV MSE: 0.5351028904061592
    - Stacking Model Cross-Validation MSE Scores: [97.53169183, 103.69966749, 133.27273096, 87.79037051, 141.28478177, 91.61037276, 84.96208976, 192.71618708, 188.80941417, 175.88209274]
    - Average Stacking Model CV MSE: 129.75593990660556
- **Feature Importance Analysis**:
  - Key Features: 
    - Adj Close: 0.71
    - Low: 0.15
    - Rolling Mean (3): 0.1
    - High: Between 0.05 and 0.1
    - Other features had negligible impact.

### Update - [24-06-2024]
- **Cluster Model Change**: Due to the quota being reached on the previous cluster, a new cluster was created on Azure Databricks to continue the work.
- **Model Development and Training**: Continued the development and training process on the new cluster.
  - **New Model Training Results**:
    - **Linear Regression**:
      - MSE: 262.16881015549114
      - R² Score: 0.9354914441872775
    - **Random Forest**:
      - MSE: 5.064867597481335
      - R² Score: 0.9987537522335231
    - **SVR**:
      - MSE: 977.362741002709
      - R² Score: 0.7595127395594654

  - **Model Performance Comparison**:
    - **Linear Regression**:
      - MSE: 262.16881015549114
      - R²: 0.9354914441872775
    - **Random Forest**:
      - MSE: 5.064867597481335
      - R²: 0.9987537522335231
    - **SVR**:
      - MSE: 977.362741002709
      - R²: 0.7595127395594654

  - **Random Forest Cross-Validation**:
    - **Cross-Validation Mean MSE**: 1249.0699581010008
    - **Cross-Validation Std MSE**: 1158.2127585329708

  - **After Hyperparameter Tuning**:
    - **Best Parameters**: {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 200}
    - **Tuned Random Forest**:
      - MSE: 4.954090030082464
      - R²: 0.9987810098652953
    - **Cross-Validation**:
      - **Mean MSE**: 8.588553513820877
      - **Std MSE**: 1.6117077861075733

  - **Residual Analysis**:
    - **Residuals vs. Predicted Values Plot**:
      - Residuals are mostly centered around zero, indicating a good fit.
      - A few outliers exist, warranting further analysis.
    - **Histogram of Residuals**:
      - Symmetric Distribution: Indicates an unbiased model with a good fit.
      - Residuals Close to Zero: Majority of predictions are accurate.
      - Tails in Distribution: Low frequency of outliers, potentially due to noise.

  - **Verification**:
    - **Verification MSE**: 4.954090030082464

### Update - [26-06-2024]
- **API Development**: Developed a Flask API to serve the model predictions.
  - **Flask App Code**:
    ```python
    from flask import Flask, request, jsonify
    import joblib
    import pandas as pd
    import numpy as np

    app = Flask(__name__)
    model = joblib.load('best_rf_model.pkl')

    @app.route('/predict', methods=['POST'])
    def predict():
        try:
            data = request.get_json(force=True)
            df = pd.DataFrame(data, index=[0])  # Create DataFrame with a single row index
            prediction = model.predict(df)
            return jsonify({'prediction': prediction.tolist()})
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8181)
    ```
- **API Testing**: Tested the API using a Jupyter notebook to send requests and receive predictions.
  - **API Testing Code**:
    ```python
    import requests
    import json

    url = 'https://riskpredictbob2024.azurewebsites.net/predict'
    data = {
        "Close_HDFCBANK": 2500,
        "Close_SBIN": 300,
        "Close_ICICIBANK": 600,
        "Close_AXISBANK": 800,
        "Close_BSE_SENSEX": 40000,
        "Close_NSEI": 12000
    }

    response = requests.post(url, json=data)
    print(response.json())
    ```
  - **API Response**:
    ```
    {'prediction': [61.12999949999995]}
    ```

- **Real-Time Data Fetching and Comparison**: 
  - Used `yfinance` to fetch real-time stock prices of various banks and market indices.
  - **Code**:
    ```python
    import requests
    import yfinance as yf

    # Function to fetch real-time stock price
    def get_real_time_stock_price(stock_symbol):
        stock = yf.Ticker(stock_symbol)
        hist = stock.history(period="1d")
        return hist['Close'].iloc[-1]

    # Fetch real-time data
    real_time_bankbaroda = get_real_time_stock_price("BANKBARODA.NS")
    real_time_data = {
        "Close_HDFCBANK": get_real_time_stock_price("HDFCBANK.NS"),
        "Close_SBIN": get_real_time_stock_price("SBIN.NS"),
        "Close_ICICIBANK": get_real_time_stock_price("ICICIBANK.NS"),
        "Close_AXISBANK": get_real_time_stock_price("AXISBANK.NS"),
        "Close_BSE_SENSEX": get_real_time_stock_price("^BSESN"),
        "Close_NSEI": get_real_time_stock_price("^NSEI")
    }

    # API request URL
    url = 'https://riskpredictbob2024.azurewebsites.net/predict'

    # Make the API request with real-time data
    response = requests.post(url, json=real_time_data)

    # Assuming the API response contains a list under the key 'prediction'
    # and you're interested in the first item of this list
    predicted_data = response.json().get('prediction', [None])[0]
    print(f"Predicted Close Price of BANKBARODA: {predicted_data}")

    # Print the real-time fetched data
    print(f"Real-time Close Price of BANKBARODA: {real_time_bankbaroda}")
    ```
  - **Output**:
    ```
    Predicted Close Price of BANKBARODA: 279.20549777999986
    Real-time Close Price of BANKBARODA: 281.3999938964844
    ```
  - The predicted close price of Bank of Baroda was very close to the actual real-time close price, indicating the model's effectiveness.


### Conclusion
Successfully built and validated a Random Forest model for predicting the closing prices of BANKBARODA stock. The model demonstrates excellent performance with a low MSE and high R². The cross-validation results further confirm its robustness. By saving and deploying the model, it can be used for real-time predictions.

### Update - [28-06-2024]
### Evaluate Model Performance
- **Real-Time Data Fetching and Prediction Comparison**: 
  - Used `yfinance` to fetch real-time stock prices of various banks and market indices.
  - **Code**:
    ```python
    import requests
    import yfinance as yf

    # Function to fetch real-time stock price
    def get_real_time_stock_price(stock_symbol):
        stock = yf.Ticker(stock_symbol)
        hist = stock.history(period="1d")
        return hist['Close'].iloc[-1]

    # Fetch real-time data
    real_time_bankbaroda = get_real_time_stock_price("BANKBARODA.NS")
    real_time_data = {
        "Close_HDFCBANK": get_real_time_stock_price("HDFCBANK.NS"),
        "Close_SBIN": get_real_time_stock_price("SBIN.NS"),
        "Close_ICICIBANK": get_real_time_stock_price("ICICIBANK.NS"),
        "Close_AXISBANK": get_real_time_stock_price("AXISBANK.NS"),
        "Close_BSE_SENSEX": get_real_time_stock_price("^BSESN"),
        "Close_NSEI": get_real_time_stock_price("^NSEI")
    }

    # API request URL
    url = 'https://riskpredictbob2024.azurewebsites.net/predict'

    # Make the API request with real-time data
    response = requests.post(url, json=real_time_data)

    # Assuming the API response contains a list under the key 'prediction'
    # and you're interested in the first item of this list
    predicted_data = response.json().get('prediction', [None])[0]
    print(f"Predicted Close Price of BANKBARODA: {predicted_data}")

    # Print the real-time fetched data
    print(f"Real-time Close Price of BANKBARODA: {real_time_bankbaroda}")

    # Calculate the absolute and percentage error
    abs_error = abs(predicted_data - real_time_bankbaroda)
    percent_error = (abs_error / real_time_bankbaroda) * 100

    print(f"Absolute Error: {abs_error}")
    print(f"Percentage Error: {percent_error:.2f}%")
    ```

  - **Results**:
    - Predicted Close Price: 285.25
    - Real-time Close Price: 275.40
    - **Metrics**:
      - Absolute Error: 9.85
      - Percentage Error: 3.58%
      - Directional Accuracy: Correct

## Today's Update - [01-07-2024]

### Fetching Real-Time Data and Storing in Azure Blob Storage

 I implemented a process to fetch real-time stock prices and store them in Azure Blob Storage using Azure Databricks.

#### Description:
    - Created a new Databricks notebook.
    - Installed necessary libraries: `yfinance`, `azure-storage-blob`, `sqlalchemy`, `pyodbc`.
    - Implemented a script to fetch real-time stock prices using the `yfinance` library.
    - Handled cases where data might be missing or symbols might be delisted.
    - Implemented a script to store the fetched data in Azure Blob Storage.
    - Ensured the data is stored with a timestamp in the file name for easy tracking.
    - Automated the data fetching and storage process using Databricks Jobs to update regularly with new data .


### Update [2024-07-04]

**Tasks Completed:**

1. **Automated Data Collection:**
   - Automated the process to collect real-time data using a scheduled job. The data is collected and stored in Azure Blob Storage with filenames like `realtime_data_20240701_063848.csv`.

2. **Data Integration:**
   - Integrated real-time data with the historical dataset to create an updated dataset for model training.

3. **Model Training:**
   - Used the updated dataset to train a Random Forest model.
   - Applied hyperparameter tuning using `RandomizedSearchCV` to optimize model performance.
   - Achieved optimal parameters: `{'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 50}`.

4. **Model Evaluation:**
   - Evaluated the model using Mean Squared Error (MSE) and R² score.
   - Results: `Mean Squared Error: 0.0`, `R^2 Score: 1.0`.

5. **Model Logging:**
   - Logged the model and results using MLflow for experiment tracking and reproducibility.

**Code and Notebook:**

- The notebook detailing today's work, including data integration, model training, and evaluation, is available [here](https://github.com/mritunjaypandey2k24/RiskPredict/blob/main/notebooks/Real%20TIme%20Data%20Collection%20and%20Storing%20to%20Blob.ipynb).





