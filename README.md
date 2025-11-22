# 🚦 Smart City: Traffic Volume Forecasting

A Machine Learning powered application to predict real-time traffic volume based on weather conditions and time factors. This project is part of the Smart City initiatives to optimize urban mobility and reduce congestion.

🔗 **Live Demo:** _[https://smart-traffic-dashboard-fwawbwmutmovxmgocxzk38.streamlit.app/]_

---

##  Project Overview

**Track:** Smart Traffic (Track A)  
**Goal:** To assist city planners and commuters by forecasting traffic density using historical weather and temporal data.

This application uses a **Random Forest Regressor** trained on historical data to predict traffic volume. It is deployed as an interactive web dashboard where users can input current weather conditions to get instant traffic estimates.

---

##  Features

- **Real-time Prediction:** Estimate traffic volume (number of vehicles) instantly.  
- **Interactive Dashboard:** User-friendly interface built with Streamlit.  
- **Visual Indicators:** Color-coded alerts (Green/Yellow/Red) for traffic severity.  
- **Weather Integration:** Accounts for temperature, rain, and cloud coverage.

---

## 🛠️ Tech Stack

- **Language:** Python 3.9+  
- **Data Processing:** Pandas, NumPy  
- **Machine Learning:** Scikit-Learn (Random Forest)  
- **Web Framework:** Streamlit  
- **Deployment:** Streamlit Community Cloud  

---

##  Dataset

The model was trained on the **Metro Interstate Traffic Volume dataset** from the UCI Machine Learning Repository.

- **Source:** UCI Machine Learning Repository  
- **Records:** ~48,000 hourly observations including weather and holidays.  

---

##  Installation & Running Locally

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/smart-traffic-dashboard.git
cd smart-traffic-dashboard

```
### **1. Install Dependencies**
```bash
pip install -r requirements.txt

```
### **1. Run the app**
```bash
streamlit run app.py
```
### **1. Project structure**
```bash
📂 smart-traffic-dashboard
├── app.py                 # Main application code (Streamlit)
├── traffic_model.pkl      # Pre-trained Machine Learning model
├── requirements.txt       # List of Python dependencies
├── Traffic_Analysis.ipynb # Jupyter Notebook used for training (Colab)
└── README.md              # Project documentation
```
---

##  Model Performance

- **Algorithm:** Random Forest Regressor

- **R² Score:** ~0.94 (High accuracy)

- **Key Predictors:** Hour of day, Temperature, Cloud coverage

---


