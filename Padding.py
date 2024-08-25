# Pad key bits with zeros
def pad_key_bits(key_bits, length):

  try:
    # Check if the key_bits list is already at or exceeds the desired length
    if len(key_bits) >= length:
      return key_bits

    else:
      # Pad with zeros to reach the desired length
      padded_key_bits = key_bits + [0] * (length - len(key_bits))

    return padded_key_bits

  except Exception as e:
    print("An error occurred during key bit padding:", e)