# 🏦 Credit Risk Prediction

📌 Project Overview
The Credit Risk Prediction project is a machine learning application that predicts whether a loan applicant is likely to be a Low Credit Risk or High Credit Risk based on their financial and personal information.Built using Python, Scikit-learn, and Streamlit providing interactive web interface where user can enter applicant details and receive instant credit risk predictions.


📊 Features
- Interactive web application using Streamlit
- predicts applicants credit risk
- Accepts multiple applicant and loan-related inputs
- Display prediction result (Low Risk or High Risk)
- Integrated Preprocessing and prediction pipeline
- shows prediction confidence using probability
- Real-time credit risk prediction

🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib

🤖 Machine Learning Models

The following classification models were evaluated:

Logistic Regression
Decision Tree Classifier ✅ (Final Model)
KNeighbors Classifier

The Decision Tree Classifier achieved the best performance and accuracy (84%) and was selected for deployment.

| Model | Accuracy | Notes |
| --- | --- | --- |
| Logistic Regression | 78% | Baseline model |
| KNeighbors Classifier | 74% | Lower accuracy, sensitive to k |
| Decision Tree Classifier ✅ | **84%** | Best performance, final model |
