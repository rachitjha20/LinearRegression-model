import matplotlib.pyplot as plt 
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error

import time



print("LIB IMPORTED")

diabetes = datasets.load_diabetes()

print("Dataset loaded")

print(dir(diabetes))

# ['DESCR', 'data', 'data_filename', 'data_module', 'feature_names', 'frame', 'target', 'target_filename']

diabetes_x = diabetes.data

diabetes_x_train = diabetes_x[:-30]
diabetes_x_test = diabetes_x[-30:]

diabetes_y_train = diabetes.target[:-30]
diabetes_y_test = diabetes.target[-30:]

model = linear_model.LinearRegression()

model.fit(diabetes_x_train, diabetes_y_train)

diabetes_x_predict = model.predict((diabetes_x_test))

print("Mean Squared Error : ", mean_squared_error(diabetes_y_test, diabetes_x_predict))

print("Weights : ", model.coef_)
print("Intercept : ", model.intercept_, end=" ")

# For Single element
# ['DESCR', 'data', 'data_filename', 'data_module', 'feature_names', 'frame', 'target', 'target_filename']
# Mean Squared Error 3035.060115291269
# Weights [941.43097333]
# Intercept 153.39713623331644

# plt.scatter(diabetes_x_test, diabetes_y_test)
# plt.plot(diabetes_x_test, diabetes_x_predict)
# plt.show()