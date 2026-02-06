from fastapi import FastAPI
# IMPORTANT: This import tells Python to look inside your new 'models' folder
from app.models import model_pipeline 
import pandas as pd

app = FastAPI(title="Intelligent Triage Engine")

# This will store our "analytics" in memory for the dashboard
processed_tickets = []

@app.post("/process_ticket")
async def process_ticket(ticket: dict):
    text = ticket.get("text", "")
    # Call the logic from the models folder
    result = model_pipeline.get_prediction(text)
    
    ticket_data = {
        "text": text,
        "category": result["category"],
        "priority": result["priority"],
        "summary": result["summary"]
    }
    processed_tickets.append(ticket_data)
    return ticket_data

@app.get("/analytics/dashboard")
async def get_analytics():
    try:
        # If no tickets exist yet, return empty stats safely
        if not processed_tickets:
            return {
                "total": 0, 
                "high_priority": 0, 
                "categories": {}, 
                "recent_tickets": []
            }
        
        # Convert our list of tickets to a DataFrame for analysis
        df = pd.DataFrame(processed_tickets)
        
        # Calculate stats
        total = len(df)
        high_priority = int(len(df[df['priority'] == 'High']))
        category_counts = df['category'].value_counts().to_dict()
        
        return {
            "total": total,
            "high_priority": high_priority,
            "categories": category_counts,
            "recent_tickets": processed_tickets[-5:] # Show last 5
        }
    except Exception as e:
        # This will show you exactly what is wrong in the terminal
        print(f"Error in analytics: {e}")
        return {"error": str(e)}