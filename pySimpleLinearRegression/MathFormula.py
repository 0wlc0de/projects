from math import pow
# Mathematical Equations for Simple Linear Regression Model


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


# Sample data_set
array = [10, 20, 30, 40, 50]

