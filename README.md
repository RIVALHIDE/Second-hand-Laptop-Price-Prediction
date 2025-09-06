# Second-hand-Laptop-Price-Prediction

This project focuses on building a Machine Learning model to predict laptop prices based on key hardware specifications. Using a dataset containing laptop attributes, a Random Forest Regressor model was trained to estimate the price of a laptop by considering factors such as:

* Processor Speed (GHz)

* RAM Size (GB)

* Storage Capacity (GB)

The model learns patterns between hardware configurations and their corresponding prices. Once trained, it was deployed into an interactive Streamlit web application, where users can input laptop specifications and receive an instant price estimation.

Dataset

The project uses the Laptop_price.csv dataset, which contains the following columns:

* Brand: The manufacturer of the laptop (e.g., Dell, HP, Asus).
* Processor_Speed: The speed of the processor in GHz.
* RAM_Size: The size of the RAM in GB.
* Storage_Capacity: The storage capacity in GB.
* Screen_Size: The screen diagonal size in inches.
* Weight: The weight of the laptop in kilograms.
* Price: The price of the laptop (target variable).

The model was trained using Processor_Speed, RAM_Size, and Storage_Capacity as the primary features.

link for Dataset :https://www.kaggle.com/datasets/mrsimple07/laptoppriceprediction

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

Setup and Installation

Follow these steps to get the project running on your local machine.

1. Clone the repository:

    git clone https://github.com/your-username/laptop-price-prediction.git
    cd laptop-price-prediction
   
2. Create and activate a virtual environment (recommended):

For Windows
python -m venv venv
.\venv\Scripts\activate

For macOS/Linux
python3 -m venv venv
source venv/bin/activate

3. Install the required dependencies:

Create a file named requirements.txt and add the following lines to it:

streamlit
pandas
scikit-learn
joblib
numpy
matplotlib

Then, run the following command in your terminal:
pip install -r requirements.txt

4. Run the Streamlit application:

   streamlit run app.py

 How to Use the App

1. Once the app is running, you will see a simple interface.
2. Enter the values for the laptop's specifications:

        Storage Capacity (GB)

        RAM Size (GB)

        Processor Speed (GHz)

3. Click the "Price Estimation" button.
4. The app will display the estimated price for the laptop with the given configuration.

Model Details

* Model: Random Forest Regressor
* Features: Storage_Capacity, RAM_Size, Processor_Speed
* Evaluation: The model achieved a Mean Absolute Error (MAE) of approximately ₹478.76 on the test set, indicating that the predictions are, on average, off by this amount from the actual price.

The complete exploratory data analysis, model training, and evaluation process can be found in the laptop_price_analysis.ipynb notebook.


   
