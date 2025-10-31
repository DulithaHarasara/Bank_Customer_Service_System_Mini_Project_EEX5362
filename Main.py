import pandas as pd

# Step 1: Create a list of dictionaries (each row is a dictionary)
data = [
    {"queue_id": "Q3001", "customer_id": "C1001", "arrival_time": "2025-05-10 09:15:00", "queue_type": "Cash", "wait_start": "09:15:00", "service_start": "09:20:00", "wait_time_min": 5},
    {"queue_id": "Q3002", "customer_id": "C1002", "arrival_time": "2025-05-10 09:18:00", "queue_type": "Inquiry", "wait_start": "09:18:00", "service_start": "09:23:00", "wait_time_min": 5},
    {"queue_id": "Q3003", "customer_id": "C1003", "arrival_time": "2025-05-10 09:22:00", "queue_type": "Cash", "wait_start": "09:22:00", "service_start": "09:27:00", "wait_time_min": 5},
    {"queue_id": "Q3004", "customer_id": "C1004", "arrival_time": "2025-05-10 09:30:00", "queue_type": "Loan", "wait_start": "09:30:00", "service_start": "10:15:00", "wait_time_min": 45},
    {"queue_id": "Q3005", "customer_id": "C1005", "arrival_time": "2025-05-10 09:45:00", "queue_type": "Cash", "wait_start": "09:45:00", "service_start": "09:50:00", "wait_time_min": 5},
    {"queue_id": "Q3006", "customer_id": "C1006", "arrival_time": "2025-05-10 10:00:00", "queue_type": "Cheque", "wait_start": "10:00:00", "service_start": "10:05:00", "wait_time_min": 5}
]

# Step 2: Convert to pandas DataFrame
df = pd.DataFrame(data)

# Step 3: Save to CSV file
file_name = "queue_data.csv"
df.to_csv(file_name, index=False)

print(f"✅ CSV file '{file_name}' created successfully!")
