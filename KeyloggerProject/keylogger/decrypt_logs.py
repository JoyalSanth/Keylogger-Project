from cryptography.fernet import Fernet

# Load the encryption key
with open("key.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)
LOG_FILE = "keylog_encrypted.txt"

def decrypt_logs():
    """Read and decrypt the keylog file."""
    with open(LOG_FILE, "rb") as f:
        encrypted_lines = f.readlines()

    for encrypted_data in encrypted_lines:
        decrypted_data = cipher.decrypt(encrypted_data).decode()
        print(decrypted_data, end="")  # Print decrypted keystrokes

decrypt_logs()
