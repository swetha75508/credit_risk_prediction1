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

- Logistic Regression
- KNeighbors Classifier
- Decision Tree Classifier ✅ (Final Model)

📊 Model Performance

| Model | Accuracy | Notes |
| --- | --- | --- |
| Logistic Regression | 77% | Baseline model |
| KNeighbors Classifier | 82% | Lower accuracy, sensitive to k |
| Decision Tree Classifier ✅ | **84%** | Best performance, final model |

The Decision Tree Classifier achieved the best performance and was selected for deployment.

📂 Project Structure

Credit_Risk_ML_Project/

│

├── app.py

├── credit_risk_model.pkl

├── requirements.txt

├── Credit_Risk_Dataset.csv

├── Credit Risk Prediction.ipynb

├── README.md

└── .gitignore


▶️ Run the Project
pip install -r requirements.txt
streamlit run app.py
