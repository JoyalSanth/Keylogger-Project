# 🔐 Encrypted Keylogger Project

## 📌 Overview
This is a simple **keylogger** that securely logs keystrokes and **encrypts** them using `cryptography`.

⚠️ **Warning:** This project is for educational purposes only. Do not use it for unethical activities.

---

## 🛠 Features
✅ Logs keystrokes and encrypts them  
✅ Decrypts logs for viewing  
✅ Clears logs when needed  
✅ Organized file structure  

---

## 🚀 Setup and Installation

### **1️⃣ Install Dependencies**
Run this command in your terminal:
```sh
pip install -r requirements.txt
```
2️⃣ Generate an Encryption Key (Run Once)
```sh
python keylogger/generate_key.py
```

3️⃣ Run the Keylogger
```sh
python keylogger/keylogger.py   (Press ESC to stop recording keystrokes.)
```

4️⃣ Decrypt and View Logs
```sh
python keylogger/decrypt_logs.py
```

5️⃣ Clear Logs
```sh
python keylogger/clear_logs.py
```
