import streamlit as st
import requests
import pandas as pd
import time

st.set_page_config(page_title="Triage Insight Dashboard", layout="wide")
st.title("🛡️ Customer Sentinel: Real-Time Triage")

# Fetch data from our FastAPI
try:
    response = requests.get("http://127.0.0.1:8000/analytics/dashboard")
    data = response.json()
except:
    data = {"total": 0, "high_priority": 0, "categories": {}, "recent_tickets": []}

# Top Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Tickets", data["total"])
col2.metric("High Priority", data["high_priority"])
col3.metric("System Status", "Online" if data["total"] >= 0 else "Offline")

# Charts
if data["categories"]:
    st.bar_chart(pd.Series(data["categories"]))

# Recent Tickets Table
if data["recent_tickets"]:
    st.subheader("Latest High Priority Summaries")
    st.table(pd.DataFrame(data["recent_tickets"]))

# Auto-refresh logic
time.sleep(5)
st.rerun()
