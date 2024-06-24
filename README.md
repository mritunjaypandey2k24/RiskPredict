
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
- **Model Selection Discussion**: Started discussions on selecting appropriate models for time series forecasting, considering linear regression for a baseline model and exploring more complex models like ARIMA and LSTM for better predictive performance.

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
        app.run(debug=True)
    ```
- **API Testing**: Tested the API using a Jupyter notebook to send requests and receive predictions.
  - **API Testing Code**:
    ```python
    import requests
    import json

    url = 'http://127.0.0.1:5000/predict'
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

### New Model Training Results
- **Linear Regression**:
  - MSE: 262.16881015549114
  - R² Score: 0.9354914441872775
- **Random Forest**:
  - MSE: 5.064867597481335
  - R² Score: 0.9987537522335231
- **SVR**:
  - MSE: 977.362741002709
  - R² Score: 0.7595127395594654

### Model Performance Comparison
- **Linear Regression**:
  - MSE: 262.16881015549114
  - R²: 0.9354914441872775
- **Random Forest**:
  - MSE: 5.064867597481335
  - R²: 0.9987537522335231
- **SVR**:
  - MSE: 977.362741002709
  - R²: 0.7595127395594654

### Random Forest Cross-Validation
- **Cross-Validation Mean MSE**: 1249.0699581010008
- **Cross-Validation Std MSE**: 1158.2127585329708

### After Hyperparameter Tuning
- **Best Parameters**: {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 200}
- **Tuned Random Forest**:
  - MSE: 4.954090030082464
  - R²: 0.9987810098652953
- **Cross-Validation**:
  - **Mean MSE**: 8.588553513820877
  - **Std MSE**: 1.6117077861075733

### Residual Analysis
- **Residuals vs. Predicted Values Plot**:
  - Residuals are mostly centered around zero, indicating a good fit.
  - A few outliers exist, warranting further analysis.
- **Histogram of Residuals**:
  - Symmetric Distribution: Indicates an unbiased model with a good fit.
  - Residuals Close to Zero: Majority of predictions are accurate.
  - Tails in Distribution: Low frequency of outliers, potentially due to noise.

### Verification
- **Verification MSE**: 4.954090030082464

### Conclusion
Successfully built and validated a Random Forest model for predicting the closing prices of BANKBARODA stock. The model demonstrates excellent performance with a low MSE and high R². The cross-validation results further confirm its robustness. By saving and deploying the model, it can be used for real-time predictions.

### Next Steps
1. **Refine and Validate Model**
   - Confirm the forecast horizon of the model (e.g., one day ahead).
   - Perform additional validation to ensure model robustness and accuracy.

2. **Integration with Banking Systems**
   - Plan how the model's predictions will be integrated into existing banking systems.
   - Ensure secure and efficient data transfer between the prediction service and banking applications.

3. **Deployment**
   - Deploy the model and Flask API in a production environment using a robust server.
   - Monitor the performance of the deployed
