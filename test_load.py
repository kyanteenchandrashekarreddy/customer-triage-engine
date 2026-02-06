import requests
import time
import random
import uuid
from concurrent.futures import ThreadPoolExecutor

API_URL = "http://127.0.0.1:8000/process_ticket"
NUM_REQUESTS = 100

def generate_random_ticket():
    text_samples = [
        "I need a refund immediately!",
        "The app is crashing.",
        "How do I change my password?",
        "Feature request: dark mode.",
        "Billing error on my account.",
        "Just saying hi."
    ]
    return {
        "ticket_id": str(uuid.uuid4()),
        "customer_text": random.choice(text_samples),
        "timestamp": "2023-10-27T10:00:00Z"
    }

def send_ticket(i):
    ticket = generate_random_ticket()
    try:
        start = time.time()
        response = requests.post(API_URL, json=ticket)
        duration = time.time() - start
        
        if response.status_code == 200:
            return f"Req {i}: Success ({duration:.3f}s) - {response.json()['priority']}"
        else:
            return f"Req {i}: Failed ({response.status_code})"
    except Exception as e:
        return f"Req {i}: Error {str(e)}"

def main():
    print(f"Starting load test with {NUM_REQUESTS} requests...")
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(send_ticket, range(NUM_REQUESTS)))
    
    success_count = sum(1 for r in results if "Success" in r)
    total_time = time.time() - start_time
    
    print("\n".join(results[:10])) # Print first 10
    print(f"...\nTotal Requests: {NUM_REQUESTS}")
    print(f"Successful: {success_count}")
    print(f"Total Time: {total_time:.2f}s")
    print(f"RPS: {NUM_REQUESTS/total_time:.2f}")

if __name__ == "__main__":
    main()
