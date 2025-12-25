import csv

def save_event(event):
    with open("events.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            event["timestamp"],
            event["event_type"],
            event["value"]
        ])
