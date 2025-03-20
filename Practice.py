import base64

# Input string
input_string = "Hello, World!"

# Convert string to bytes
input_bytes = input_string.encode('utf-8')

# Encode to base64
encoded_string = base64.b64encode(input_bytes)

# Convert bytes back to string for display
encoded_string = encoded_string.decode('utf-8')

print(f"Encoded Base64 string: {encoded_string}")


#Noted