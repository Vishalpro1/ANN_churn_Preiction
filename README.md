# ANN_churn_Preiction
Churn means when a customer stops using a company’s product or service.

Example (Banking):

A customer closes their bank account

A customer stops using bank services

Such customers are called churned customers.

Input Features (Independent Variables):
Feature	Description-----
1.CreditScore >	Customer’s credit score
2.Geography >	Country of the customer
3.Gender >	Male or Female
4.Age >	Customer age
5.Tenure >	Years with the bank
6.Balance >	Account balance
7.NumOfProducts >	Number of bank products used
8.HasCrCard >	Has credit card (1 = Yes, 0 = No)
9.IsActiveMember >	Active customer or not
10.EstimatedSalary >	Estimated yearly salary

Target Variable (Output):

Exited

1 → Customer churned

0 → Customer did not churn


Data Preprocessing

Before training the model, we cleaned and prepared the data.

Steps:

Removed unnecessary columns (like Customer ID, Name)

Converted categorical data (Gender, Geography) into numerical form

Handled missing values

Scaled numerical features using StandardScaler

Split data into:

Training set (80%)

Testing set (20%)

Activation Functions:

ReLU → Hidden layers

Sigmoid → Output layer (binary classification)


Model Compilation

The model was compiled using:

Optimizer: Adam

Loss Function: Binary Crossentropy

Metrics: Accuracy

This helps the model learn efficiently.


Technologies Used

Python

Pandas, NumPy

Scikit-learn

TensorFlow / Keras

Streamlit


Real-World Use Case

Banks can:

Offer discounts to risky customers

Improve customer support

Increase customer retention


