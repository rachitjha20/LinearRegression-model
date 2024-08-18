
# E-commerce Customer Data Analysis

This project involves the analysis and prediction of customer spending behavior using an e-commerce dataset. The primary goal is to explore the relationships between various features and the yearly amount spent by customers.

## Project Structure

The notebook is organized as follows:

1. **Data Loading and Libraries**:
   - The necessary libraries, including `pandas`, `numpy`, `matplotlib`, `seaborn`, and `scikit-learn`, are imported.
   - The dataset is loaded and basic information about the data is displayed.

2. **Exploratory Data Analysis (EDA)**:
   - Descriptive statistics of the dataset are explored.
   - Data visualizations are used to understand the relationships between different variables.

3. **Feature Relationships**:
   - Joint plots are created to examine the relationship between features such as `Time on Website`, `Time on App`, and `Yearly Amount Spent`.
   - The relationship between the length of time customers spend on the website or app and their yearly spending is visualized.

4. **Modeling**:
   - The data is split into training and testing sets.
   - A linear regression model is trained on the dataset.
   - The model's performance is evaluated using metrics such as Mean Absolute Error (MAE) and Mean Squared Error (MSE).

5. **Results and Conclusion**:
   - The performance of the model is analyzed, and insights are drawn regarding customer behavior based on the model's predictions.

## How to Run

1. Clone the repository.
2. Ensure that you have the necessary dependencies installed.
   ```
   pip install -r requirements.txt
   ```
3. Open the `E-commerce.ipynb` notebook and run the cells sequentially.

## Dataset

The dataset used for this project is a hypothetical dataset that contains the following features:
- **Avg. Session Length**: Average session of in-store style advice sessions.
- **Time on App**: Average time spent on the app in minutes.
- **Time on Website**: Average time spent on the website in minutes.
- **Length of Membership**: Length of time the customer has been a member.
- **Yearly Amount Spent**: The target variable representing the yearly amount spent by the customer.

## Visualizations

Some key visualizations include:
- **Joint plots** to explore the relationships between different time metrics and customer spending.
- **Scatter plots** to visualize the data and model predictions.

## Conclusion

This analysis helps in understanding the key factors that influence customer spending in an e-commerce setting. The linear regression model provides a basic understanding of how different features contribute to the yearly amount spent by customers.

## Author

- Rachit Jha
