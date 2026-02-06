# 🛡️ Customer Sentinel: Intelligent Triage Engine

A hybrid AI-powered ticketing system that uses **Scikit-Learn** for high-speed classification and **FastAPI** for a production-grade backend.

### 🏗️ Architecture
- **Backend:** FastAPI (Python)
- **ML Logic:** Scikit-Learn (TF-IDF + Random Forest)
- **Frontend:** Streamlit Dashboard
- **Structure:** Modular Architecture (Separated API, Models, and UI layers)

### 🚀 How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Start API: `python -m uvicorn app.api.main:app --reload`
3. Start Dashboard: `python -m streamlit run app/frontend/dashboard.py`
