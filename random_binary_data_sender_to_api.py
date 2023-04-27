"""
# Random Binary Data Sender to API
This Python script generates a random binary file of a specified size (in MB) and sends it to an API URL using the HTTP method specified. The script uses the `requests` module to send the binary data to the API URL.

## Usage
To use the script, follow these steps:

1. Open the `random_binary_data_sender_to_api.py` file in a text editor.
2. Set the `API_URL` and `API_METHOD` variables to the URL and HTTP method of the API endpoint you want to send the binary data to.
3. Set the `file_size_mb` variable to the size of the binary file you want to generate, in megabytes.
4. Save the file.
5. Open a terminal window and navigate to the directory containing the `random_binary_data_sender_to_api.py` file.
6. Run the script by typing `python random_binary_data_sender_to_api.py` in the terminal and pressing Enter.
7. The script will generate a random binary file of the specified size, send it to the API URL using the HTTP method specified, and print the response from the API to the console.

Note: You will need the `requests` module installed to run this script. You can install it using `pip install requests`.

## License
This script is licensed under the MIT License. See the `LICENSE` file for more information.
"""

import requests
import os
import random

# API URL and METHOD
API_URL = "https://JitterbitITRIAL408019.jitterbit.eu/CloudNon-Production/apItoFile"
API_METHOD = "POST"

# Specify the file size in MB
file_size_mb = 20

# Convert MB to bytes
file_size_bytes = file_size_mb * 1024 * 1024

# Generate random binary data
binary_data = os.urandom(file_size_bytes)

# Create a temporary file to store the binary data
temp_file = f"tempfile_{random.randint(0, 100000000)}.bin"
with open(temp_file, "wb") as f:
    f.write(binary_data)

# Send the binary data to the API URL
with open(temp_file, "rb") as f:
    response = requests.request(method=API_METHOD, url=API_URL, data=f)

# Delete the temporary file
os.remove(temp_file)

# Check the response from the API
print(response.status_code)
print(response.content)
