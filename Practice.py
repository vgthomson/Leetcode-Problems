# import base64

# # Input string
# input_string = "Hello, World!"

# # Convert string to bytes
# input_bytes = input_string.encode('utf-8')

# # Encode to base64
# encoded_string = base64.b64encode(input_bytes)

# # Convert bytes back to string for display
# encoded_string = encoded_string.decode('utf-8')

# print(f"Encoded Base64 string: {encoded_string}")


#Noted

def check_signed_32bit(value):
    # Signed 32-bit range: -2^31 to 2^31 - 1
    if -2**31 <= value <= 2**31 - 1:
        return True
    else:
        return False

# Example usage
value = 1534236469  # Maximum value for signed 32-bit integer
print(check_signed_32bit(value))  # Output: True


def reverse(self, x: int) -> int:
    x_str = str(x)
    
    if x < 0:
        x_str = x_str[1:] 
        x_str = '-' + x_str[::-1]  
    else:
        x_str = x_str[::-1]

    res = int(x_str)
    if ((res > (2**31 - 1)) or (res < -2**31)):
        return 0
    
    return res