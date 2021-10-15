#! usr/bin/env python3
# base64 decoder
# importing module base64
import base64 

# user input
code = input('Enter base64 code: ')
 
# converting into base64
base64_string = code

base64_bytes = base64_string.encode("ascii") 

  
# coverting into bytes
sample_string_bytes = base64.b64decode(base64_bytes) 

sample_string = sample_string_bytes.decode("ascii") 

  
# printing result
print(f"Decoded string: {sample_string}") 
