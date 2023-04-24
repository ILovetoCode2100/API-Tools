# Import required libraries
import requests
import json
import random
import time
from datetime import datetime
from threading import Thread, Lock

# API URL to send requests
API_URL = 'https://example.com'
MAX_CALLS = 900
REQUESTS_PER_MINUTE = 834
SECONDS_BETWEEN_REQUESTS = 60 / REQUESTS_PER_MINUTE
counter = 0
counter_lock = Lock()

def generate_fixed_json_body(counter_value):
    data = {
        'Request_Number: ': counter_value,
        'Timestamp: ': datetime.now().strftime("%H:%M:%S:%f")
    }
    return json.dumps(data)

# Add an optional parameter to specify the API method (default is 'POST')
def make_request(api_method='POST'):
    global counter
    with counter_lock:
        current_counter = counter
        counter += 1

    headers = {'Content-Type': 'application/json'}
    json_body = generate_fixed_json_body(current_counter)
    # Send request with the specified API method
    response = requests.request(api_method, API_URL, data=json_body, headers=headers)

    if response.status_code == 200:
        print(f'Success! Sent data: {json_body}')
    else:
        print(f'Failed to send data: {json_body}. Status code: {response.status_code}')

def send_requests_in_loop(api_method='POST'):
    while True:
        with counter_lock:
            if counter >= MAX_CALLS:
                break
        make_request(api_method)
        time.sleep(SECONDS_BETWEEN_REQUESTS)

if __name__ == '__main__':
    api_method = 'POST'  # Change this value to specify a different API method
    threads = [Thread(target=send_requests_in_loop, args=(api_method,)) for _ in range(10)]  # Adjust the number of threads as needed
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
