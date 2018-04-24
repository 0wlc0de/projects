from math import pow
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# Mathematical Equations for Simple Linear Regression Model


def get_headers(dataframe):
    """
    Get the headers name of the dataframe
    :param dataframe:
    :return:
    """
    return dataframe.columns.values


# calculate the average of the data_set or samples
def mean(data_set):
    sum_all = sum(data_set)
    return sum_all/len(data_set)


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


# Root Mean Square Error
def cal_rmse(actual_readings, predicted_readings):
    """
    Calculating the root mean square error
    :param actual_readings:
    :param predicted_readings:
    :return:
    """
    square_error_total = 0.0
    total_readings = len(actual_readings)
    for i in range(0, total_readings):
        error = predicted_readings[i] - actual_readings[i]
        square_error_total += pow(error, 2)
    rmse = square_error_total / float(total_readings)
    return rmse



