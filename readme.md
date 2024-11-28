# Distance-Based Price Prediction Model

## Overview
This project implements a simple linear regression model that predicts prices based on distance using gradient descent optimization.

🔍 **For a Detailed Explanation**: [Understanding Linear Regression with Gradient Descent](https://medium.com/@hocine.midoun/understanding-linear-regression-with-gradient-descent-a-practical-example-575fe1e50f03)

## Project Structure
- `predict.py`: Script for making price predictions on new data
- `train.py`: Contains model training and evaluation logic
- `utils.py`: Utility functions for data processing, normalization, and model management

## Prerequisites
- Python 3.x
- Required libraries:
  - matplotlib
  - csv
  - json

## Installation
1. Clone the repository
2. Install required dependencies:
   ```
   pip install matplotlib
   ```

## Model Workflow
1. **Data Preparation**: 
   - Input data should be in `files/data.csv`
   - CSV format: First column is distance (km), second column is price
   
2. **Training**:
   - Run `train.py` to:
     - Normalize input data
     - Train linear regression model
     - Evaluate model performance
     - Visualize results
     - Save model parameters

3. **Prediction**:
   - Run `predict.py`
   - Enter distance when prompted
   - Receives estimated price prediction

## Key Features
- Data normalization
- Gradient descent optimization
- Mean Squared Error (MSE) tracking
- Mean Absolute Percentage Error (MAPE) tracking
- Model parameter persistence

## Model Metrics
The model provides two key performance metrics:
- MSE (Mean Squared Error): Measures average squared difference between predicted and actual prices
- MAPE (Mean Absolute Percentage Error): Indicates percentage difference between predictions and actual values

## Example Usage
```bash
# Train the model
python train.py

# Make predictions
python predict.py
```

## Customization
- Adjust learning rate and epochs in `train.py`
- Modify data processing in `utils.py`

## More Information
For an in-depth explanation of the linear regression and gradient descent approach used in this project, check out the companion article:
👉 [Understanding Linear Regression with Gradient Descent](https://medium.com/@hocine.midoun/understanding-linear-regression-with-gradient-descent-a-practical-example-575fe1e50f03)
