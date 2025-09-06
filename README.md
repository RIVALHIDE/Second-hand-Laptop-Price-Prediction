# Second-hand-Laptop-Price-Prediction

This project focuses on building a Machine Learning model to predict laptop prices based on key hardware specifications. Using a dataset containing laptop attributes, a Random Forest Regressor model was trained to estimate the price of a laptop by considering factors such as:

* Processor Speed (GHz)

* RAM Size (GB)

* Storage Capacity (GB)

The model learns patterns between hardware configurations and their corresponding prices. Once trained, it was deployed into an interactive Streamlit web application, where users can input laptop specifications and receive an instant price estimation.

Key Features of the Project :

1. Data Analysis & Preprocessing

* Collected and cleaned laptop specification data.
* Selected essential features for training.
* Applied transformations and exploratory data analysis to understand price trends.

2. Model Building

* Implemented a Random Forest Regressor due to its robustness and ability to handle non-linear relationships.
* Performed hyperparameter tuning using GridSearchCV to optimize model accuracy.

3. Model Deployment

* Exported the trained model using Joblib.
* Developed an interactive Streamlit application (app.py).
* Users can input processor speed, RAM, and storage, and get an estimated laptop price instantly.

Objective :

The objective of this project is to provide a quick and reliable price estimation tool for laptops, which can be useful for:

* Buyers estimating a fair price before purchase.
* Sellers setting competitive pricing.
* Tech enthusiasts exploring how hardware affects pricing.

Technologies Used :

Python

* Pandas, NumPy for data handling
* Scikit-learn for machine learning
* Streamlit for web deployment
* Joblib for model persistence
