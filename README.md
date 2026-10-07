# ⚙️ Predictive Maintenance Using Machine Learning

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Flask-black.svg)](https://flask.palletsprojects.com/)

An end-to-end Machine Learning web application designed to predict equipment and machine failures before they occur, reducing downtime and maintenance costs in industrial environments.

---

## 📌 Project Overview
This project implements classification models to predict machine failures using sensor readings from the **AI4I 2020 Predictive Maintenance Dataset**. 

<p align="center">
  <img src="assets/dashboard_preview.png" alt="Web App Dashboard Preview" width="850"/>
</p>

---

## 🚀 Key Features
- **Predictive Modeling**: Trained classification models to detect failure risks.
- **Interactive Web Interface**: Clean UI built with Flask for real-time predictions.
- **Robust Pipeline**: Automated feature scaling and preprocessing via Pickle (`.pkl`).

---

## 🛠️ Installation & Local Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/khalidllogic/predictive-maintenance-ml.git](https://github.com/khalidllogic/predictive-maintenance-ml.git)
cd predictive-maintenance-ml                                                 
pip install -r requirements.txt
python app.py