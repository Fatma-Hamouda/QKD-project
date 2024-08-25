# QKD Encryption and Decryption using BB84 and AES

## Project Overview

This project demonstrates quantum key distribution (QKD) using the BB84 protocol implemented with Cirq, and encryption/decryption using the Advanced Encryption Standard (AES). The BB84 protocol is a quantum cryptography technique that ensures secure communication by generating a shared secret key between two parties. This project utilizes this key for symmetric encryption and decryption with AES, ensuring both the secrecy and integrity of the transmitted data.

## Features

The project includes the following key components:

1. **Quantum Key Generation (BB84 Protocol with Cirq)**: 
   - Implements the BB84 protocol using Cirq to generate a secure quantum key for encryption and decryption.

2. **Key Padding**: 
   - Pads the quantum key to the desired length in bits to match the requirements for AES encryption.

3. **Key Conversion (Bits to Bytes)**: 
   - Converts the padded quantum key from bits to bytes, making it suitable for use with AES encryption and decryption algorithms.

4. **AES Encryption**:
   - Uses the quantum key to encrypt messages using the AES encryption algorithm, ensuring data confidentiality.

5. **AES Decryption**:
   - Decrypts messages using AES with the shared quantum key, ensuring that only authorized parties can read the data.

## Functions

The project is structured into five main functions:

1. **`generate_QKD_key()`**: 
   - Implements the BB84 protocol using Cirq to generate a shared quantum key between two parties.
   
2. **`pad_key_bits()`**: 
   - Pads the quantum key to the appropriate length in bits (128, 192, or 256 bits) required for AES encryption.

3. **`bits_to_bytes()`**: 
   - Converts the padded key from bits to bytes to meet the format required by AES.

4. **`encryption()`**: 
   - Encrypts the input data using AES and the shared quantum key, providing data confidentiality.

5. **`decryption()`**: 
   - Decrypts the AES-encrypted data using the same quantum key, restoring the original plaintext.

## Getting Started

### Prerequisites

- Python 3.x
- Required Python libraries:
  - `cirq` (for implementing the BB84 protocol)
  - `pycryptodome` (for AES encryption and decryption)
  - Any other libraries specific to the implementation

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/qkd-aes-encryption.git
   cd qkd-aes-encryption

