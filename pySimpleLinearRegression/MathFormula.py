"""
    SIMPLE LINEAR REGRESSION USING ORDERED SQUARED METHOD
"""

from math import pow
import matplotlib.pyplot as plt
# Mathematical Equations for Simple Linear Regression Model


# calculate the average of the data_set or samples
def mean(data_set):
    sum_all = sum(data_set)
    return sum_all/len(data_set)


# Simple Linear Regression equation
def predict_target_value(x, b0, b1):
    """
    Calculating the target (y) value using the input x and the coefficients b0, b1
    :param x:
    :param b0:
    :param b1:
    :return:
    """
    return b0 + b1 * x


def b1(x, y):
    mean_x = mean(array_x)
    mean_y = mean(array_y)
    summation = 0
    for i in range(0, len(x)):
        summation += (x[i] - mean_x)*(y[i] - mean_y)

    return summation / x_squared(x)


def x_squared(x):
    mean_x = mean(x)
    summation = 0.0
    for i in x:
        summation += pow(i - mean_x, 2)
    return summation


def b0(x, y, b1):
    b0 = mean(y) - (b1*mean(x))
    return b0


# Sample Data Sets
array_x = [1, 2, 3, 4, 5]
array_y = [2, 4, 5, 4, 5]

b1_ = b1(array_x, array_y)
b0_ = b0(array_x, array_y, b1(array_x, array_y))
slope = [predict_target_value(i, b0_, b1_) for i in array_x]


plt.scatter(array_x, array_y, color='red')
plt.plot(array_x, slope, color='blue')
plt.show()


# Other Equation for getting the covariance and variance
# Commented because we've implemented the short-cut method.
# Use these formulas if you want to calculate first the variance and the covariance
"""
#  1: Calculate the mean
#  2: Summation of every element in data_set minus mean and squared the answer
def variance(data_set):
    data_mean = mean(data_set)
    variance_ = 0.0
    for i in data_set:
        variance_ += pow(i - data_mean, 2)
    return variance_ / (len(data_set) - 1)


# 1: Calculate the mean of the data_set(X) and data_set(Y)
# 2: Summation => multiply the answer of (every element in data_set(X) minus mean of X) and
#                                        (every element of data_set(Y) minus mean of Y)
# 3: the answer of Summation divided by the length of the data_sets minus 1
def co_variance(x, y):
    mean_x = mean(x)
    mean_y = mean(y)
    cov = 0.0
    for i in range(0, len(x)):
        cov += (x[i] - mean_x)(y[i] - mean_y)
    return cov/(len(x)-1)


# 1: To get the Coefficient (b1) => divide the covariance of (X, Y) to the variance of (X)
# 2: To get the Constant (b0) => multiply the b1 (Constant) and the mean of X then minus the mean of Y
def calculate_b0_b1(X, y):
    b1 = co_variance(X, y) / float(variance(X))
    b0 = mean(y) - (b1 * mean(X))
    return b0, b1
"""
