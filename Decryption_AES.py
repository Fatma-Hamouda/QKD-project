# Modules
import binascii
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Decryption with AES
def decryption(cipher_text, key_bytes):

  try:
    decipher = AES.new(key_bytes, AES.MODE_ECB)  # Create AES cipher object with the key

    cipher_text = cipher_text.encode()  # Convert the ciphertext to bytes and decrypt using AES
    ciphertext_bytes = binascii.unhexlify(cipher_text)   # Convert the ciphertext from hexadecimal format to bytes

    plaintext_bytes = unpad(decipher.decrypt(ciphertext_bytes), AES.block_size)  # Decrypt the ciphertext and remove padding
    plain_text = plaintext_bytes.decode()   # Decode the plaintext from bytes to string for printing
    return(plain_text)

  except Exception as e:
    print("An error occurred during decryption:", e)