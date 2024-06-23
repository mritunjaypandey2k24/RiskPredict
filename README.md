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

### Update - [20-06-2024]
- **Model Tuning and Evaluation**:
  - Best Parameters for Random Forest: {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 100}
  - Tuned Random Forest Model Performance: MSE: 5.064867597481335, R²: 0.9987537522335231
- **Model Validation with Cross-Validation**:
  - Random Forest Cross-Validation Mean MSE: 8.588553513820877
  - Random Forest Cross-Validation Std MSE: 1.6117077861075733
- **Residual Analysis**:
  - Conducted residual analysis to ensure the model's predictions were unbiased and normally distributed.
  - Observed a roughly symmetric distribution of residuals centered around zero, indicating accurate model predictions with low frequency of large errors.

### Update - [21-06-2024]
- **Model Deployment**:
  - Prepared the model for deployment using Flask to create a web service for predictions.
  - Exported the trained Random Forest model (`best_rf_model.pkl`) from Databricks and configured the Flask application.
  - Ensured all dependencies and environment configurations were correctly set up in a local development environment using Visual Studio Code.
  - Flask Application Setup:
    - Created `app.py` to handle incoming prediction requests.
    - Set up the necessary routes and ensured the model could make predictions based on incoming data.
  - Verified the Flask application was running correctly and tested endpoint for predictions.

*Note: This section will be regularly updated with our daily progress throughout the hackathon.*
