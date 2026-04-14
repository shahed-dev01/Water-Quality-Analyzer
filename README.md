# 💧 Water Quality Analyzer

[Water Quality Analyzer
](https://water-quality-analy.streamlit.app/)

## Overview
The Water Quality Analyzer is a Machine Learning web application designed to predict the potability of drinking water. By analyzing 9 distinct chemical and physical metrics, the model determines whether a water source is safe for human consumption.

This project was built to tackle real-world environmental and public health challenges using data-driven solutions.

## The Machine Learning Model
This application is powered by a **Random Forest Classifier**. 
* **Hyperparameter Tuning:** The model was optimized using `GridSearchCV` to find the ideal tree depth and splitting criteria, maximizing its ability to catch complex, non-linear chemical relationships.
* **Class Balancing:** The dataset was highly imbalanced. The model utilizes balanced class weights to heavily penalize False Negatives, ensuring the system prioritizes public safety by not over-classifying unsafe water as safe.

## Dataset
The model was trained on the [Drinking Water Potability](https://www.kaggle.com/datasets/adityakadiwal/water-potability) dataset from Kaggle.
**Features Analyzed:**
- pH Level
- Hardness
- Total Dissolved Solids
- Chloramines
- Sulfate
- Conductivity
- Organic Carbon
- Trihalomethanes
- Turbidity

## Tech Stack
* **Language:** Python
* **Machine Learning:** Scikit-Learn (`RandomForestClassifier`, `GridSearchCV`)
* **Data Manipulation:** Pandas, NumPy
* **Web Framework:** Streamlit
* **Deployment:** Streamlit Community Cloud

## How to Run Locally
If you want to run this application on your own machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/shahed-dev01/Water-Quality-Analyzer.git
