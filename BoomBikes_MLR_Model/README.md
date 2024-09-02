
# Bike Sharing Demand Prediction Using Linear Regression

## Overview

This project addresses a business problem faced by **BoomBikes**, a bike-sharing company that experienced a significant decline in revenue during the COVID-19 pandemic. The company's goal is to understand the factors affecting bike demand as lockdown restrictions are lifted, enabling them to create a robust business plan.

## Problem Statement

BoomBikes is looking to:
- Identify which variables significantly impact the demand for shared bikes.
- Determine how well these variables can predict bike demand.

## Approach

To solve this problem, a linear regression model was developed using various features that might influence bike-sharing demand. The project includes the following steps:

1. **Data Importing and Cleaning**: 
    - Import necessary libraries and load the dataset.
    - Perform exploratory data analysis (EDA) to understand the dataset.
    
2. **Feature Selection**:
    - Use Recursive Feature Elimination (RFE) to identify the most significant features.
    - Check for multicollinearity among the selected features using the Variance Inflation Factor (VIF).

3. **Model Building**:
    - Split the data into training and testing sets.
    - Apply linear regression to the training set.
    - Evaluate the model's performance using R-squared and other metrics.

4. **Model Evaluation**:
    - Assess the model using various statistical measures.
    - Interpret the coefficients of the significant variables to provide insights to the company.

## Installation

To run this notebook, you'll need Python 3.x and the following libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels
```

## Usage

1. Clone this repository.
2. Open the `BoomBikes_Multi_LR.ipynb` notebook in Jupyter or any compatible environment.
3. Run the cells sequentially to execute the analysis.

## Results

The final model identifies key variables that predict bike demand effectively. These insights can help BoomBikes optimize their operations and marketing strategies.

## Contributing

If you wish to contribute to this project, please fork the repository and submit a pull request with detailed comments on the changes you’ve made.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or collaboration opportunities, please reach out to me on [LinkedIn](https://www.linkedin.com/in/rachit-jha/).
