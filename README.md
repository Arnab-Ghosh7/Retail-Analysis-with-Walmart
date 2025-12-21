#📊 Retail Analysis with Walmart
End-to-End Machine Learning Pipeline & Web Application

## 🛠️ Tools & Technologies Used
<p align="center"> <img src="https://img.shields.io/badge/Python-2.8k-blue?logo=python&logoColor=white" height="30"/> &nbsp;&nbsp; <img src="https://img.shields.io/badge/Pandas-1.2k-purple?logo=pandas&logoColor=white" height="30"/> &nbsp;&nbsp; <img src="https://img.shields.io/badge/NumPy-850-lightblue?logo=numpy&logoColor=white" height="30"/> &nbsp;&nbsp; <img src="https://img.shields.io/badge/scikit--learn-1.1k-orange?logo=scikitlearn&logoColor=white" height="30"/> </p> <p align="center"> <img src="https://img.shields.io/badge/Flask-600-black?logo=flask&logoColor=white" height="30"/> &nbsp;&nbsp; <img src="https://img.shields.io/badge/YAML-220-red?logo=yaml&logoColor=white" height="30"/> &nbsp;&nbsp; <img src="https://img.shields.io/badge/Joblib-180-green" height="30"/> &nbsp;&nbsp; <img src="https://img.shields.io/badge/Logging-150-grey" height="30"/> </p>
<p align="center">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" height="40"/>
  &nbsp;&nbsp;&nbsp;
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original.svg" height="40"/>
  &nbsp;&nbsp;&nbsp;
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/numpy/numpy-original.svg" height="40"/>
  &nbsp;&nbsp;&nbsp;
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/scikitlearn/scikitlearn-original.svg" height="40"/>
  &nbsp;&nbsp;&nbsp;
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/flask/flask-original.svg" height="40"/>
  &nbsp;&nbsp;&nbsp;
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/yaml/yaml-original.svg" height="40"/>
</p>


## 📌 Project Overview

This project is an end-to-end machine learning system designed to predict weekly sales for Walmart stores based on historical, economic, and environmental factors.

The project demonstrates how raw retail data can be transformed into actionable business insights using a structured ML pipeline and deployed as a Flask web application.

The goal is not just prediction, but to showcase real-world ML engineering practices such as:

- Modular pipeline design

- Configuration-driven development

- Model evaluation on unseen data

- Deployment-ready prediction interface

This project is portfolio-ready and suitable for interview discussion.

## 🎯 Problem Statement

Retail businesses like Walmart need accurate sales forecasts to:

- Optimize inventory

- Improve supply-chain planning

- Reduce operational cost

- Prepare for holidays and demand spikes

This project predicts Weekly Sales using features such as:

- Store number

- Holiday indicator

- Temperature

- Fuel price

- Consumer Price Index (CPI)

- Unemployment rate

## 🏗️ Project Architecture
<pre>
  Retail-Analysis-with-Walmart/
│
├── app.py                     # Flask web application
├── config/
│   └── config.yaml             # Configuration file
├── params.yaml                 # Model parameters
│
├── src/real_walmart/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   └── model_evaluation.py
│   │
│   ├── pipeline/
│   │   └── prediction.py
│   │
│   ├── entity/                 # Dataclass definitions
│   ├── config/                 # Configuration manager
│   ├── utils/                  # Common utilities
│   └── logger/                 # Logging system
│
├── artifacts/                  # Generated artifacts
│   ├── data_ingestion/
│   ├── data_transformation/
│   ├── model_trainer/
│   └── model_evaluation/
│
├── templates/
│   └── index.html              # Website UI
│
├── requirements.txt
└── README.md

</pre>


## ⚙️ Machine Learning Pipeline
🔹 1. Data Ingestion

- Downloads raw dataset (ZIP format)

- Extracts and stores it in a structured artifacts directory

🔹 2. Data Validation

- Checks required columns

- Ensures schema consistency

- Logs validation status

🔹 3. Data Transformation

- Cleans data

- Separates features & target

- Performs train–test split

- Saves transformed datasets

🔹 4. Model Training

- Trains a Random Forest Regressor

- Uses historical sales data

- Saves trained model as .pkl

🔹 5. Model Evaluation

- Evaluates model on unseen test data

Metrics used:

- RMSE

- MAE

- R² Score

- Stores evaluation results for analysis


## 🌐 Web Application (Flask)

A professional Flask web interface allows users to:

- Enter store & economic details

- Get real-time weekly sales prediction

- Use the trained ML model interactively

🔹 Input Features

- Store Number

- Holiday Flag

- Temperature

- Fuel Price

- CPI

- Unemployment Rate

🔹 Output

- Predicted Weekly Sales


## 🚀 How to Run the Project
<pre>
  1️⃣ Clone the Repository
git clone https://github.com/your-username/Retail-Analysis-with-Walmart.git
cd Retail-Analysis-with-Walmart

2️⃣ Create Environment & Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Web App
python app.py


Open in browser:

http://127.0.0.1:8080
</pre>

## 👤 Author

Arnab Ghosh
