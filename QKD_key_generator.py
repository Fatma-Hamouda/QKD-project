# Modules
import cirq
from random import choices
from random import randint

def generate_QKD_key():

  try:
    # Setup
    encode_gates = {0: cirq.I, 1: cirq.X}   # Dictionary for encoding gates
    basis_gates = {'Z': cirq.I, 'X': cirq.H}    # Dictionary for basis gates
    num_bits = randint(128, 257)    # Generate random number of bits for the key
    qubits = cirq.NamedQubit.range(num_bits, prefix = 'q')  # Create qubits for the quantum communication

    # Sender
    # Sender's actions
    sender_key = choices([0, 1], k = num_bits)    # Generate a random bit string as sender's key
    sender_bases = choices(['Z', 'X'], k = num_bits)    # Choose random bases for encoding
    sender_circuit = cirq.Circuit()   # Initialize sender's quantum circuit

    # Construct sender's quantum circuit
    for bit in range(num_bits):

      encode_value = sender_key[bit]
      encode_gate = encode_gates[encode_value]  # Choose encoding gate based on sender's key

      basis_value = sender_bases[bit]
      basis_gate = basis_gates[basis_value]  # Choose basis gate based on sender's basis choice

      qubit = qubits[bit]
      sender_circuit.append(encode_gate(qubit)) # Apply encoding gate
      sender_circuit.append(basis_gate(qubit))  # Apply encoding gate

    # Recevier
    # Receiver's actions
    recevier_bases = choices(['Z', 'X'], k = num_bits)  # Choose random bases for measurement
    recevier_circuit = cirq.Circuit()  # Initialize receiver's quantum circuit

    # Construct receiver's quantum circuit
    for bit in range(num_bits):

      basis_value = recevier_bases[bit]
      basis_gate = basis_gates[basis_value]  # Choose basis gate based on receiver's basis choice

      qubit = qubits[bit]
      recevier_circuit.append(basis_gate(qubit))  # Apply basis gate for measurement

    recevier_circuit.append(cirq.measure(qubits, key = 'recevier key'))   # Measure qubits and store results

    bb84_circuit = sender_circuit + recevier_circuit  # Combine sender's and receiver's circuits

    # Simulate quantum circuit
    sim = cirq.Simulator()
    results = sim.run(bb84_circuit)
    recevier_key = results.measurements['recevier key'][0] # Extract receiver's key

    # Compare keys and generate shared key
    final_sender_key = []
    final_recevier_key = []

    for bit in range(num_bits):

      if sender_bases[bit] == recevier_bases[bit]:
        final_sender_key.append(sender_key[bit])
        final_recevier_key.append(recevier_key[bit])

    # compare the first few bits in Alice's and Bob's key to ensure the protocol was successful.
    num_bits_to_compare = int(len(final_sender_key) * .5)
    if final_sender_key[0:num_bits_to_compare] == final_recevier_key[0:num_bits_to_compare]:
      final_sender_key = final_sender_key[num_bits_to_compare:]
      final_recevier_key = final_recevier_key[num_bits_to_compare:]
      shared_key = final_sender_key
      print('\n\nWe can use our keys!')
      print('\nThe shared Key: ', shared_key)


    else:
      print('\n\nEve was listening, we need to use a different channel!')

    return shared_key

  except Exception as e:
    print("An error occurred during key generation:", e)
