#! usr/bin/env python3
# importing module base64
import base64 

  
code = input('Enter base64 code: ')
  
base64_string = code

base64_bytes = base64_string.encode("ascii") 

  

sample_string_bytes = base64.b64decode(base64_bytes) 

sample_string = sample_string_bytes.decode("ascii") 

  

print(f"Decoded string: {sample_string}") 
