import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split


data_set = pd.read_csv('C:\\Users\\User\\PycharmProjects\\projects\\'
                       'MissingData\\Resources\\Data.csv')


# Splitting Independent Variables to Dependent
X = data_set.iloc[:, :-1].values
Y = data_set.iloc[:, 3].values

# Missing Values
imputation = Imputer(missing_values='NaN', strategy='mean', axis=0)
X[:, 1:3] = imputation.fit_transform(X[:, 1:3])

# Encoding Categorical Data
labelEncoder_X = LabelEncoder()

# Fit and Transform the X[:, 0] and store it to X[:, 0]
X[:, 0] = labelEncoder_X.fit_transform(X[:, 0])

# OneHotEncoder : categorical_feature = [the index of the encoded column]
onehotencoder = OneHotEncoder(categorical_features=[0])

# Fit and Transform the X[:, 0] to X matrix
X = onehotencoder.fit_transform(X).toarray()

# Encode the dependent Variable
labelEncoder_Y = LabelEncoder()

# Fit and Transform the Y vector and store it to Y
Y = labelEncoder_Y.fit_transform(Y)


# Train sets and Test Sets
train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size=0.2, random_state=0)


# Standard Scaling (feature Scaling)
sc_X = StandardScaler()
train_X = sc_X.fit_transform(train_X)
test_X = sc_X.transform(test_X)
