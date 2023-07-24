```python
import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

# Load the encryption key from environment variables
ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY')

# Create a Fernet object
cipher_suite = Fernet(ENCRYPTION_KEY)

def encrypt_data(data):
    """
    Function to encrypt user data
    """
    encrypted_data = cipher_suite.encrypt(data)
    return encrypted_data

def decrypt_data(encrypted_data):
    """
    Function to decrypt user data
    """
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    return decrypted_data

def secure_data_transmission(data):
    """
    Function to secure data transmission
    """
    encrypted_data = encrypt_data(data)
    return encrypted_data

def comply_data_privacy(data):
    """
    Function to comply with data privacy regulations
    """
    encrypted_data = secure_data_transmission(data)
    return encrypted_data

def get_user_consent():
    """
    Function to get user consent for data processing
    """
    consent = input("Do you consent to the processing of your data? (yes/no): ")
    if consent.lower() == 'yes':
        return True
    else:
        return False
```