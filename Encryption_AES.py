# Modules
import binascii
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


# Encrypt with AES
def encryption(message, key_bytes):

  try:
    cipher = AES.new(key_bytes, AES.MODE_ECB)  # Create AES cipher object with the key

    # Convert the message to bytes and encrypt using AES
    message = message.encode()
    encrypted_message = cipher.encrypt(pad(message, AES.block_size))
    encrypted_message_hex = binascii.hexlify(encrypted_message)   # Convert the encrypted message to hexadecimal format for easy display

    cipher_text = encrypted_message_hex.decode()   # Decode from bytes to str for printing
    return cipher_text

  except Exception as e:
    print("An error occurred during encryption:", e)