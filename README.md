# House Price Predictor 🏠

Welcome to the **House Price Predictor** project! This repository contains a machine learning workflow that predicts house prices based on various features such as the number of bedrooms, bathrooms, living area, year built, and more. It includes data preprocessing, exploratory data analysis, a trained model, and a locally runnable web application built with Streamlit.

**Developed by**: Muhammed Rishal K

## 📝 Features

- **Pre-trained Random Forest Regressor Model**: Achieves high accuracy by robustly capturing non-linear relationships in housing data.
- **Interactive UI**: A sleek front-end built in Streamlit (`app.py`), allowing users to dynamically input house specifications and instantly see the estimated price.
- **Data Preprocessing Script**: Includes code (`ds_project.py`) to clean, filter, and encode categorical data (e.g., specific city/zipcode labeling).

## 🛠️ Tech Stack

- **Python**: Core programming language.
- **Pandas & NumPy**: For efficient data processing and numerical computations.
- **Scikit-Learn**: For training the Random Forest regression model.
- **Streamlit**: To create the user-friendly interactive web application interface.

## 🚀 Getting Started

### Prerequisites

You need Python 3.7+ installed. Make sure you install the necessary packages using:
```bash
pip install pandas numpy scikit-learn streamlit
```

### Running the App Locally

1. **Clone the repository**:
```bash
git clone https://github.com/riishaal/House_Price_Prediction.git
cd House_Price_Prediction
```

2. **(Optional) Re-train the Model**:
If you wish to re-train the model on your data, just run the original script and it will serialize a new `model.pkl` file locally.
```bash
python ds_project.py
```

3. **Launch the Streamlit interface**:
Run the following command to boot up the User Interface in your browser.
```bash
streamlit run app.py
```

## 📂 Project Structure

- `ds_project.py` - Core Python script that loads raw data, engineers features, trains the Random Forest model, and exports it to `model.pkl`.
- `app.py` - Streamlit application logic for the interface (loading the pickled model and serving predictions directly).
- `model.pkl` - Serialized, pre-trained Machine Learning model.
- `data.csv`, `data.dat`, `output.csv` - Datasets and outputs.
- `iris.ipynb` - Auxiliary exploratory analysis testing notebook.

## 📫 Author
**Muhammed Rishal K** - [GitHub Profile](https://github.com/riishaal)
