# Convert a list of bits to bytes
def bits_to_bytes(bits):

  try:
    # Convert bits list to a string of '0's and '1's
    bits_str = ''.join(map(str, bits))

    # Convert the binary string to a byte string
    byte_string = int(bits_str, 2).to_bytes((len(bits) + 7) // 8, byteorder='big')
    return byte_string

  except Exception as e:
    print("An error occurred during conversion from bits to bytes:", e)
