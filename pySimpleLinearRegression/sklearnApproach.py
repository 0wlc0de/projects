import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


data_set = pd.read_csv('C:\\Users\\User\\PycharmProjects\\projects\\'
                       'pySimpleLinearRegression\\Resources\\Salary_Data.csv')

# Separating the variables
independent_variable = data_set.iloc[:, :-1].values
dependent_variable = data_set.iloc[:, 1].values

# setting the train and test sets of X and Y
X_train, X_test, y_train, y_test = train_test_split(independent_variable, dependent_variable,
                                                    test_size=0.2, random_state=0)

# LinearRegression
Regressor = LinearRegression()
Regressor.fit(X_train, y_train)


y_pred = Regressor.predict(X_test)

plt.scatter(X_test, y_test, color="red")
plt.plot(X_train, Regressor.predict(X_train), color="blue")
plt.title("Simple Linear Regression with Scikit Learn")
plt.show()
