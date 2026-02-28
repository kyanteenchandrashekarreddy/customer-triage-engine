import streamlit as st
import requests

# 1. SET YOUR RENDER URL HERE
# Example: https://customer-triage-api.onrender.com
RENDER_URL = "https://customer-triage-engine.onrender.com"

st.title("Customer Support Triage Dashboard")

# 2. ADD INPUT AREA
with st.form("ticket_form"):
    user_message = st.text_area("Enter Customer Inquiry:", placeholder="e.g., I need a refund for my last order.")
    submit_button = st.form_submit_button("Process Ticket")

if submit_button and user_message:
    # Send the input to your Render Backend
    payload = {"text": user_message}
    response = requests.post(f"{RENDER_URL}/process_ticket", json=payload)
    
    if response.status_code == 200:
        result = response.json()
        st.success(f"Classified as: {result['category']} (Priority: {result['priority']})")
        st.info(f"AI Summary: {result['summary']}")
    else:
        st.error("Failed to connect to the AI backend.")

# 3. SHOW INSIGHTS/ANALYTICS
st.header("Customer Insights")
if st.button("Refresh Analytics"):
    # Fetch data from the /analytics/dashboard endpoint
    stats_response = requests.get(f"{RENDER_URL}/analytics/dashboard")
    
    if stats_response.status_code == 200:
        data = stats_response.json()
        
        # Display key metrics
        col1, col2 = st.columns(2)
        col1.metric("Total Tickets", data['total'])
        col2.metric("High Priority", data['high_priority'])
        
        # Show category breakdown
        st.bar_chart(data['categories'])
    else:
        st.warning("No data found. Try processing a few tickets first.")