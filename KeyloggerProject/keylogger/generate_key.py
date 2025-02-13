from cryptography.fernet import Fernet

# Generate encryption key
key = Fernet.generate_key()

# Save the key to a file
with open("key.key", "wb") as key_file:
    key_file.write(key)

print("Encryption key has been generated and saved to key.key")
