'''
README

This script sends multiple requests to a specified API URL in parallel using multithreading.
It's designed to be easily customizable to control the rate and the maximum number of requests sent.

Features:
- Customizable API endpoint
- Customizable request method (default is POST)
- Customizable maximum number of requests
- Customizable rate of requests per minute
- Multithreading support for parallel requests
- JSON payload generation with request number and timestamp

Usage:
1. Set the API_URL variable to the desired API endpoint.
2. Set the MAX_CALLS variable to the maximum number of requests you want to send.
3. Set the REQUESTS_PER_MINUTE variable to control the rate of requests sent per minute.
4. Optionally, change the default API method by setting the `api_method` variable in the `__main__` block.
5. Adjust the number of threads in the `threads` list comprehension to control the level of parallelism.

When the script is executed, it will start sending requests to the specified API_URL with the chosen method
and at the specified rate. The JSON payload of each request will contain the request number and a timestamp.
'''

# Import required libraries
import requests
import json
import random
import time
from datetime import datetime
from threading import Thread, Lock

# API URL to send requests
API_URL = 'https://example.com'
MAX_CALLS = 200
REQUESTS_PER_MINUTE = 200
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
