'''
README

This script decodes a Base64 encoded string to its original form. It includes error handling for common issues
that may arise during the decoding process, such as encoding and decoding issues, and invalid Base64 input.

Usage:
1. Replace the encoded_string variable with the Base64 encoded string you want to decode.
2. Run the script.

The script will attempt to decode the encoded string and print the decoded string if successful. If any errors occur
during the decoding process, an appropriate error message will be printed instead.

Note: If the encoded string is not a valid Base64 input, an error message will be printed with the details of the error.
'''

import base64

encoded_string = "SGVsbG8sIFdvcmxkIQ=="  # replace with the Base64 encoded string you want to decode

try:
    # convert the encoded string to Base64 bytes
    base64_bytes = encoded_string.encode('utf-8')
    
    # decode the Base64 bytes
    decoded_bytes = base64.b64decode(base64_bytes)
    
    # convert the decoded bytes to a string
    decoded_string = decoded_bytes.decode('utf-8')

except UnicodeEncodeError as uee:
    print(f"Error: Unable to encode the encoded string due to an encoding issue. Details: {uee}")
except UnicodeDecodeError as ude:
    print(f"Error: Unable to decode the decoded bytes due to a decoding issue. Details: {ude}")
except base64.binascii.Error as b64e:
    print(f"Error: Invalid Base64 input. Details: {b64e}")
except Exception as e:
    print(f"Error: An unexpected error occurred. Details: {e}")
else:
    print(decoded_string)
