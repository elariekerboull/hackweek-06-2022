import cirq

# Pick a qubit.

qubit = cirq.GridQubit(0, 0)

#n = 8
#print(n//2)

print(cirq.X)
print(cirq.unitary(cirq.X))

print(cirq.Y)
print(cirq.unitary(cirq.Y))

print(cirq.Z)
print(cirq.unitary(cirq.Z))

print(cirq.S)
print(cirq.unitary(cirq.S))

print(cirq.H)
print(cirq.unitary(cirq.H))

print(cirq.CNOT)
print(cirq.unitary(cirq.CNOT))

print(cirq.CNOT**-1)
print(cirq.unitary(cirq.CNOT**-1))

print(cirq.SWAP)
print(cirq.unitary(cirq.SWAP))


# Create a circuit
circuit = cirq.Circuit(
    cirq.X(qubit)**0.5,  # Square root of NOT.
    cirq.measure(qubit, key='m')  # Measurement.
)
#print("Circuit:")
#print(circuit)

# Simulate the circuit several times.
#simulator = cirq.Simulator()
#result = simulator.run(circuit, repetitions=20)
#print("Results:")
#print(result)
