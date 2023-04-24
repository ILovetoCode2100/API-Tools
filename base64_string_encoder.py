import base64

string_to_encode = "Hello, World!"  # replace with the string you want to encode

try:
    # convert the string to bytes
    bytes_to_encode = string_to_encode.encode('utf-8')
    
    # encode the bytes using Base64
    base64_bytes = base64.b64encode(bytes_to_encode)
    
    # convert the Base64 bytes to a string
    encoded_string = base64_bytes.decode('utf-8')

except UnicodeEncodeError as uee:
    print(f"Error: Unable to encode the string due to an encoding issue. Details: {uee}")
except UnicodeDecodeError as ude:
    print(f"Error: Unable to decode the Base64 bytes due to a decoding issue. Details: {ude}")
except Exception as e:
    print(f"Error: An unexpected error occurred. Details: {e}")
else:
    print(encoded_string)
