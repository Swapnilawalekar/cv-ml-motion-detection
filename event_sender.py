import requests

def send_event(event):
    url = "http://localhost:5000/event"
    try:
        requests.post(url, json=event)
    except:
        print("Backend not running")
